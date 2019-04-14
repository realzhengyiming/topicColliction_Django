#coding =utf-8
#from django.db import models
def decode(info):
      return info.decode('utf-8')
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#from __future__ import unicode_literals
# Create your models here.

class blogPage(models.Model):
    # instructions = RichTextField() # 将需要使用富文本编辑器的字段改为RichTextField
    blogTitle = models.CharField (max_length = 30,null=True,blank=True) #这个是博文的标题
    blogTime =models.DateTimeField(null=True)#创建的时间可以修改的对吧
    blogTag = models.ManyToManyField('Tag',verbose_name='标签集合',blank=True) #可以有多个标签，分类的那个后面再用，有区别吗
    blogEditor =models.ForeignKey(User,on_delete=models.CASCADE,) # #每个博文有一个作者
    blogContent = RichTextUploadingField(blank=True,null=True,verbose_name="博文内容") #这儿是博文的东西放的地方
    def __str__(self):  
        return self.blogTitle+"-"+str(self.blogTime)+"-"+"self.blogEditor.username"


#这两个表是一起创建的，原来如此，
class Tag(models.Model):  #这个才是标签的东西
    name = models.CharField(verbose_name="标签名",max_length=30)
    def __str__(self):
        return self.name


# class TodoTable(models.Model):  #这个才是标签的东西
#     missionContent = models.TextField()
#     missionDealine = models.TextField()
#     missionContent = models.TextField()



#     def __str__(self):
        # return self.name
class TodoTable(models.Model):
    missionContent = models.TextField()
    missionDesc = models.TextField()
    missionState = models.TextField()  #任务完成的状态
    AsyncTime = models.DateTimeField(auto_now = True)  #同步时间
    username = models.TextField()
    idOnClient = models.IntegerField()
    missionDealine = models.DateTimeField() #然后这儿先查询，查询的数据

    # updateVersion = models.IntegerField()  #传过来后只有当这个传过来的版本大于这边的版本号的时候才修改这边的情况，
      #安卓端每次更新数据的时候，版本号加1，默认的版本号是1，代表了修改了多少次
    def __str__(self):
        return (self.missionContent)


class speechTopic(models.Model):
    title = models.TextField()    #这个就是话题的题目
    creatTime = models.DateTimeField(auto_now = True)  
    background = models.TextField()    
    editor = models.TextField('your name',null= True)  
    editorImgae = models.TextField('dont change this box',default="/static/media/catright.png")
    #tag = models.CharField(25)
    
    def __str__(self):
        return self.title #就加了一个这个东西而已

        
class aboutNew(models.Model):
    logTime = models.DateTimeField(auto_now = True)#日志的时间，这个管理员的我来书写的
    content = models.TextField()#日志的内容放这里
    def __str__(self):
        return str(self.logTime)

   
#这儿是增加one to one 为用户增加字段

class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    phone = models.CharField (max_length = 20,null=True,blank=True)
    image = models.ImageField(upload_to = "photo", default=" photo/2cf8ca4e612042159b5dfffff196c86d.gif", null = True,blank=True)
    #username = user.User.get_username()  
    def __str__(self):
        return str(self.image)

#class Activity(models.Model):
 #   name = models.TextField()#活动的名字
    

#话题的评论的的东西，这个东西可以作为一个例子来做
class topicComment(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,) #把用户作为外键，这种方式有点麻烦，查询太多了，要指定到字段作为主键比较好
    comment = models.TextField() #这个就是评论的东西
    speechtopic = models.ForeignKey(speechTopic,on_delete=models.CASCADE,) #这个是话题的评论，取到话题的id
    imgurl = models.TextField(default="http://myest.club/static/media/city.png")  #这儿是头像的网址
    commenTime = models.DateTimeField(auto_now = True)
    def __str__(self):
        return (self.comment)
#from tropic.models import topicComment
#topicComment.objects.create(user=User.objects.get(id=1),comment="hellowrold 第一个沙发",owner=speechTopic.objects.get(id = 1))

#点赞的模型
class New_Likes(models.Model):
    content_type = models.ForeignKey(speechTopic,on_delete=models.CASCADE,) #属于话题的赞
    author = models.ForeignKey(User,on_delete=models.CASCADE,) #点赞用户
    pub_date = models.DateTimeField(auto_now_add=True) #点赞时间
    def __str__(self):
        return (self.content_type)


class chickenSoup(models.Model):
    soupContent = models.TextField(null=True)
    quotoFrom = models.TextField(default="from the internet......")
    def __str__(self):
        return (self.soupContent)
 
class Activity(models.Model):
    activityName =  models.CharField(max_length = 20,default= "常规训练")
    activityTime = models.DateTimeField(null=True)#创建的时间可以修改的对吧
    location = models.TextField(default="2b207")
    activityCotent = models.TextField()
    user = models.ManyToManyField(User)   #你真的理解多对多吗，可以为空吗。
    def __str__(self):
        return self.activityName+"-"+str(self.activityTime) #就加了一个这个东西而已
    
      
# class SignIn(models.Model): #这个是记录活动签到情况的
#     signTime = models.DateTimeField(auto_now_add=True) #签到时间，同一天
#     user =models.ForeignKey(User) #把用户作为外键，这种方式有点麻烦，查询太多了，要指定到字段作为主键比较好
#     signActivity = models.ManyToManyField(Activity) #和activity是多对多的关系
#     def __str__(self):
#         return str(self.user.username)#+"-"+str(self.signActivity.all()[0]) #把这个时候签到的多个活动同时展示起来。其实每次只签到一个活动
#         #果然事我自己对关系型数据库不太熟悉，明明事一个人可以签到多个活动，每个活动可以有很多个人同时签到
        
        
        
        
        