#coding=utf-8
from django.contrib import admin
from tropic.models import speechTopic
from tropic.models import aboutNew
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from tropic.models import MyUser
from tropic .models import chickenSoup
from tropic .models import topicComment

from tropic .models import Activity
from tropic .models import blogPage
from tropic .models import Tag

from tropic .models import TodoTable
# from tropic .models import SignIn
# Register your models here.
class speechTopicAdmin(admin.ModelAdmin):
    list_display =['title','editor','creatTime']
    search_fields = ['title']
    list_filter = ['editor']
    
class aboutNewAdmin(admin.ModelAdmin):
    list_display=['logTime','content']
    search_fields = ['logTime']
    list_filter = ['content']
    
    


#出问题就搞这儿

class BlogAdmin(admin.ModelAdmin):
   list_display =['blogTitle','blogEditor','get_blogTag','blogTime']
   search_fields = ['blogTitle']
   list_filter = ['blogEditor']
   def get_blogTag(self, obj):
       alltag = ""
       for i in obj.blogTag.all():
          alltag=alltag+i.name+","
       return alltag


admin.site.register(Tag)
admin.site.register(blogPage,BlogAdmin)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'myuser'
 
# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MemberInline, )
 
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(chickenSoup)
admin.site.register(topicComment)
admin.site.register(speechTopic,speechTopicAdmin)  #这儿需要装载一下你们的数据结构的对象
admin.site.register(aboutNew,aboutNewAdmin)



# class detailActivityAdmin(admin.ModelAdmin):
#     list_display=['activityName','activityTime ']
#     search_fields = ['activityTime']
#     list_filter = ['activityTime']

class aboutTodoMission(admin.ModelAdmin):
    list_display=['missionContent','missionState','AsyncTime','username','missionDealine','missionDesc','idOnClient']
    search_fields = ['missionContent']
    list_filter = ['missionContent']


admin.site.register(Activity)
admin.site.register(TodoTable,aboutTodoMission)





# admin.site.register(SignIn)


