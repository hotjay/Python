#-*-coding:utf-8-*-
"""
auther:张振华
version:1.0
Datetime:20180326
"""
import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
import re
from Excel import ExcleMsg
class MsgWin(QFrame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s=ExcleMsg()

    def initUI(self):
        self.setWindowTitle('财务科工资短信发送 auther：zzh version:1.0')
        self.setGeometry(200,200,200,200)
        self.lab1=QLabel('文件路径：')
        self.lineEdit=QLineEdit()
        self.lineEdit.setFixedHeight(30)
        self.btnOK=QPushButton('发送确认')
        self.btnCancle=QPushButton('退出')
        self.btnChoose=QPushButton('选择文件')

        grid = QGridLayout()#网格布局
        grid.setSpacing(30)
        grid.addWidget(self.lab1,0,0,2,0)
        grid.addWidget(self.lineEdit,0,1,2,10)

        grid.addWidget(self.btnChoose,3,0,5,2)
        grid.addWidget(self.btnOK,6,1,7,3)
        grid.addWidget(self.btnCancle,6,4,7,4)

        self.setLayout(grid)
        self.setAcceptDrops(True)

        self.btnCancle.clicked.connect(self.close)#按钮点击事件
        self.btnChoose.clicked.connect(self.btn_click_Choose)
        self.btnOK.clicked.connect(self.btn_click_Send)
        self.p=[]
        self.show()

    def btn_click_Send(self):
        try:
            self.p=self.s.msgSend(self.lineEdit.text())#获取函数返回值是一个列表
            tsmsg='成功发送：'+str(self.p[0])+'   '+'失败：'+str(self.p[1])#拼凑提示信息
            QMessageBox.information(self,'发送提示',tsmsg)
        except:
            QMessageBox.information(self,'错误提示','文件错误，请确认是Excel文件')

    def btn_click_Choose(self):
        absolute_path = QFileDialog.getOpenFileName(self,'open file','.','excel(*.xls;*.xlsx)') #过滤扩展名
        path2=absolute_path[0].replace('/', '\\\\')#替换路径中的/
        self.lineEdit.setText(path2)
        #print(path2)

    '''
    def enableBorder(self, enable):
        if enable:
            self.setStyleSheet("MainWidget{border:3px solid #426ab3}") #设置边框
        else:
            self.setStyleSheet('')
    '''
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():#获取URLS
            event.acceptProposedAction()#接收动作
            #self.enableBorder(True) #边框设置
        else:
            event.ignore() #忽略事件


    def dragMoveEvent(self, event): #移动事件
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.LinkAction) #设置接收可鼠标drop 事件：True
            event.accept() #接收事件
        else:
            event.ignore() #忽略事件


    def dragLeaveEvent(self, event): #拖拽文件离开窗口
        print('dragLeaveEvent...')
        #self.enableBorder(False)

    def dropEvent(self, event):#鼠标松开事件
        if event.mimeData().hasUrls():
            # 遍历输出拖动进来的所有文件路径
            for url in event.mimeData().urls(): #取出程序的地址
                #print(url)
                path = url.toLocalFile()#取程序地址
               # print(path)
            path1=path.replace('/','\\\\')
            #print(path1)
            self.lineEdit.setText(path1)
            event.acceptProposedAction() #接收动作
            #self.enableBorder(False)
            #print(self.lineEdit.text())
        else:
            event.ignore()  #忽略事件


def main():
    app=QApplication(sys.argv)
    msgform=MsgWin()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()