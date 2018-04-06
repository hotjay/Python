#-- coding:utf_8 --
# auther:校长
from django.urls import path
from polls import views
from django.views.generic import DetailView,ListView
from polls.models import Poll

# urlpatterns=[
#     path('',views.index,name='index'),
#     path('<int:poll_id>/',views.detail,name='detail'),
#     path('<int:poll_id>/result/',views.results,name='results'),
#     path('<int:poll_id>/vote/',views.vote,name='vote')
# ]


urlpatterns=[
    path('',
         ListView.as_view(
             queryset=Poll.objects.order_by('-pub_date')[:5],
             context_object_name='latest_poll_list',
             template_name='polls/index.html'),
         name='index'),
    path('<int:pk>/',
         DetailView.as_view(
             model=Poll,
             template_name='polls/detail.html'),
         name='detail'),
    path('<int:pk>/results/',
         DetailView.as_view(
             model=Poll,
             template_name='polls/results.html'),
         name='results'),
    path('<int:poll_id>/vote/',views.vote,name='vote'),
]