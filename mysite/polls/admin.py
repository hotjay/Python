from django.contrib import admin
from polls.models import Poll
from polls.models import Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3
class PollAdmin(admin.ModelAdmin):
    fieldsets = [('aaa',                  {'fields':['pub_date']}),
                 ('Date information',   {'fields':['question'],'classes':
                  ['collapse']})]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date',]
    search_fields =['question',]
    date_hierarchy = 'pub_date'# 不可以用list
admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)