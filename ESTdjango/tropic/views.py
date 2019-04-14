#coding=utf-8
from django.shortcuts import render

from datetime import datetime
from tropic.models import speechTopic
from tropic .models import MyUser
from tropic.models import aboutNew
from tropic.models import chickenSoup
from tropic.models import topicComment
from tropic .models import blogPage
from tropic .models import Activity
from tropic .models import TodoTable
# from tropic .models import SignIn

# from json_response import JsonResponse


from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import random,time

from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from django.http import HttpResponse
import simplejson 
from django.views.decorators.csrf import csrf_exempt

from django import forms    #导入表单
from django.contrib.auth.models import User   #导入django自带的user表


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密_码',widget=forms.PasswordInput())

# 这儿，
# Create your views here.
def test(request):
    allblogs = blogPage.objects.all()
    print(allblogs)
    return render(request,"test.html",{"blog_list":allblogs})   
    #if request.method =='POST':
     #   pass
    # if request.method =='GET':
    #     topic_id = request.GET.get('topic_id','') //属于谁的，提取出来
    #     username = request.GET.get('username','')
    #     topicComment =request.GET.get('content_value','')
    #   #return render(request,'test.html')   肯定不能直接这样返回一个页面的
    #   return HttpResponse 

    
def topic(request): 
    print("hello,here is the topic")
    return render(request,"topic.html")   
    #if request.method =='POST':
     #   pass
    # if request.method =='GET':
    #     topic_id = request.GET.get('topic_id','') //属于谁的，提取出来
    #     username = request.GET.get('username','')
    #     topicComment =request.GET.get('content_value','')
    #   #return render(request,'test.html')   肯定不能直接这样返回一个页面的
    #   return HttpResponse
    
def detail(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)  #包含用户名和密码
        if uf.is_valid():
            #获取表单数据
            username = uf.cleaned_data['username']  #cleaned_data类型是字典，里面是提交成功后的信息
            password = uf.cleaned_data['password']
            #添加到数据库
            # registAdd = User.objects.get_or_create(username=username,password=password)
            registAdd = User.objects.create_user(username=username, password=password)
            # print registAdd
            if registAdd == False:
                return render(request,'share1.html', {'registAdd': registAdd, 'username': username})
 
            else:
                # return HttpResponse('ok')
                return render(request,'share1.html', {'registAdd': registAdd}) 
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))
    return render(request,'detail.html', {'uf': uf})


# def detail(request):
    # allblogs = blogPage.objects.all()
    # print(allblogs)
    # return render(request,"detail.html")   
    #if request.method =='POST':
     #   pass
    # if request.method =='GET':
    #     topic_id = request.GET.get('topic_id','') //属于谁的，提取出来
    #     username = request.GET.get('username','')
    #     topicComment =request.GET.get('content_value','')
    #   #return render(request,'test.html')   肯定不能直接这样返回一个页面的
    #   return HttpResponse
    

@csrf_exempt
def login(request):
    a ={}  #a是一个字典，这个要声明的
    print (request.body)
    received_json_data = simplejson.loads(request.body)
    print ("这个就是传过来的所有的东西了吗") #这儿这个是一个字典
    print(received_json_data)
    requestCommend = received_json_data['request']
    print(requestCommend)
    if(requestCommend == "Login"):  
        print("进来辣")
        loginUsername = received_json_data['loginUsername']
        loginPassword = received_json_data['loginPassword']
        print(loginUsername)
        print(loginPassword)
        user = auth.authenticate(username=loginUsername,password = loginPassword)#后台的账号密码对得上的话就非空
        if user is not None:  #.
            
            auth.login(request,user) #非空那么就登陆，一句话就登陆完成
            request.session['user'] = loginUsername  #把用户名写入session中去,还可以设置保留的时长
            print ("对方已经登陆过了")
            print("登陆成功"+loginUsername)
            a["result"] = "post_success"        
            return HttpResponse(simplejson.dumps(a), content_type='application/json')
            
            #return HttpResponseRedirect('/')  #重定向啥也不做的样子
        else: 
            a["result"] = "false"        
            return HttpResponse(simplejson.dumps(a), content_type='application/json')
    else:
        pass




def android(request):  #这个是安卓的部分，可以暂时不用管
    loginUsername =request.POST.get('loginUsername')
    loginPassword =request.POST.get('loginPassword')
    # doWhatFlag = request.POST.get('doWhatFlag');  #这个标记是看看是登陆呢还是同步的操作
    print(loginPassword)

    a = {}  #这儿就是一个json 就是一个字典的意思啦 ，a在这儿是字典
      #a就是传进去的键值对
    # a["newcomment"] =newcomment
    user = auth.authenticate(username=loginUsername,password = loginPassword)#后台的账号密码对得上的话就非空
    if user is not None :  #.非空就返回头像和别的东西之类的。  and doWhatFlag == login
        user.myuser.image.url
        faceImage = "media/"+str(MyUser.objects.get(user= User.objects.get(username=loginUsername)).image)
        auth.login(request,user) #非空那么就登陆，一句话就登陆完成
        request.session['user'] = loginUsername  #把用户名写入session中去,还可以设置保留的时长
        a["result"] = "login_success"
        a["username"] = loginUsername
        a["faceImage"] = faceImage
        print ("对方已经登陆过了")
        print("登陆成功"+loginUsername)
        print(a)
        return HttpResponse(simplejson.dumps(a), content_type='application/json')
        # return JsonResponse({"result":"success"})
    if user is not None and doWhatFlag == ascyData: #这儿是同步的东西
        pass

        # return "登陆成功"+loginUsername
    # return "密码错误"
    a["result"] = "login_failed"
    a["username"] = "unknow"
    a["faceImage"] = "unknow"
    print(a)
    return HttpResponse(simplejson.dumps(a), content_type='application/json')

    

def androidAscy(request):
    loginUsername =request.POST.get('loginUsername')
    loginPassword =request.POST.get('loginPassword')
    DOWHAT = request.POST.get('DOWHAT')  #这个标记是看看是登陆呢还是同步的操作
    ascyData = request.POST.get('ascyData')  #提出传送过来的，一条记录
    print(loginPassword)
    a = {}  #这儿就是一个json 就是一个字典的意思啦 ，a在这儿是字典
      #a就是传进去的键值对
    return_json = {}  #同不用的返回去的所有的东西。
    # a["newcomment"] =newcomment
    user = auth.authenticate(username=loginUsername,password = loginPassword)#后台的账号密码对得上的话就非空
    if user is not None and DOWHAT == "ASCY" :  #.非空就返回头像和别的东西之类的。  
        user.myuser.image.url   #这儿是头像
        faceImage = "media/"+str(MyUser.objects.get(user= User.objects.get(username=loginUsername)).image)
        auth.login(request,user) #非空那么就登陆，一句话就登陆完成
        request.session['user'] = loginUsername  #把用户名写入session中去,还可以设置保留的时长
        a["result"] = "login_success"
        a["username"] = loginUsername
        a["faceImage"] = faceImage
        a["ascyState"] ="True"  #确认了同步状况

        for mission in TodoTable.objects.filter(username=loginUsername): #只返回是所登陆的用户的东西 
            return_json[str(mission.idOnClient)]={'todoContent':mission.missionContent,'missionDealine':mission.missionDealine,
            'idOnClient':mission.idOnClient,'missionState':mission.missionState,'missionDesc':mission.missionDesc
            }
        print(type(return_json))
        a['backupMission']= return_json #这个放过去，

        #这儿开始处理收到的json数据
        jsonData = request.POST.get('jsonData')  
        print (type(jsonData))
        print (jsonData)
        received_json_data = simplejson.loads(jsonData)  #转化成为字典
        for mission in received_json_data:
            deadline = mission["deadline"]
            missionDesc = mission["missionDesc"]
            state = mission["state"]
            todoContent = mission["todoContent"]
            missionAscy = mission["missionAscy"]
            idOnClient = mission["id"]  #提出传送过来的，一条记录

            
            try:  #还原操作的话，也是，回传列表，然后再每个单独查询，有重复的就删除掉，用最新的
                TodoTable.objects.get(idOnClient=idOnClient).delete()
                
            except Exception:
                pass

            print("任务id "+str(mission["id"]))  #先查询，如果有的话就修改合并
            print("截止日期 "+mission["deadline"])
            print("任务描述 "+mission["missionDesc"])
            print("任务完成状态 "+mission["state"])
            print("任务内容 "+mission["todoContent"])
            print("任务同步状态 "+mission["missionAscy"])  

            #然后就是把这些记录写入数据库
            newMissionData =TodoTable(missionContent=todoContent,missionDesc=missionDesc,missionState=state,username=loginUsername,missionDealine=deadline,idOnClient=idOnClient) #先创建后更新，
            newMissionData.save()  #同步到云端啦



        print (type(jsonData))
        print ("对方已经登陆过了")
        print("登陆成功"+loginUsername)
        print(a)
        return HttpResponse(simplejson.dumps(a), content_type='application/json')
        # return JsonResponse({"result":"success"})
    if user is not None and doWhatFlag == ascyData: #这儿是同步的东西
        pass
        # return "登陆成功"+loginUsername
    # return "密码错误"
    a["result"] = "login_failed"
    a["username"] = "unknow"
    a["faceImage"] = "unknow"
    print(a)
    return HttpResponse(simplejson.dumps(a), content_type='application/json')
        

def www(request):
    # allblogs = blogPage.objects.all()
    # print(allblogs)
    return render(request,"www.html")      


#from django.views.decorators.csrf import csrf_exempt
@csrf_exempt #这个是评论的东西
def terminal_svr(request):
    # a = int(request.POST.get('a'))
    # b = int(request.POST.get('b'))
    # return_json = {'result':a+b}   把用户的id查询后存起来
    print (request.body)
    received_json_data = simplejson.loads(request.body)
    print (received_json_data) #这儿这个是一个字典
    username = received_json_data['username']
    #userid = int(User.objects.get(username=username).id)
    imgurl =received_json_data['userimge']
    comment = received_json_data['comment']
    topic_id = received_json_data['topic_id']
    topicComment.objects.create(user=User.objects.get(username=username),comment=comment,imgurl=imgurl,speechtopic=speechTopic.objects.get(id=topic_id))
    
    allComment= topicComment.objects.filter(speechtopic_id = topic_id) #django外键的是用下划线的方式，查询外键的键值，一个id下有多个评论
    print(allComment)  #这是一个数组，这个东西怎么搞呢
    newcomment =''
    for i in allComment:
        string ='<div class="mdui-card-header"><div class="mdui-card-header-avatar"><img class="avatar" src="'+i.imgurl+'" width="40" height="40"></div><div class="mdui-card-header-title mdui-text-color-theme-accent"><a href="'+"http://www.zhengyiming.com"+'rel="external nofollow">'+i.user.username+'</a></div><div class="mdui-card-header-subtitle">'+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'</div></div><div class="mdui-card-content"><p>'+i.comment+'</p></div><div class="mdui-divider-inset-dark "></div>'
        newcomment = newcomment + string  # 把他们全部都串起来，从尾部接上去，已经排好顺序了
    #这人得把所有得合并成一个字符串，然后返回去，这么长得的东西嘛。。。。。然后前台直接就append出来就可以了
    a = {}  #这儿就是一个json 就是一个字典的意思啦 ，a在这儿是字典
    a["result"] = "post_success"  #a就是传进去的键值对
    a["newcomment"] =newcomment
    return HttpResponse(simplejson.dumps(a), content_type='application/json')


#晚点儿再把这儿这里分出去
@csrf_exempt
def randomTopic(request): 
    received_json_data = simplejson.loads(request.body)
    a = {}  # 这儿就是一个json 就是一个字典的意思啦 ，a在这儿是字典

    if(received_json_data['request']=="getATopic"):
        allObject= speechTopic.objects.all()   
        topicNumbers = len(allObject)
        oneTopic =allObject[random.randint(0,topicNumbers-1)] 
        string ='<div class="mdui-card-header"><div class="mdui-card-header-avatar"><img class="avatar" src="'+oneTopic.editorImgae+'" width="40" height="40"></div><div class="mdui-card-header-title mdui-text-color-theme-accent"><a href="'+"http://www.zhengyiming.com"+'rel="external nofollow">'+oneTopic.editor+'</a></div><div class="mdui-card-header-subtitle">'+str(oneTopic.creatTime)+'</div></div><div class="mdui-card-content"><p>'+'话题:'+oneTopic.title+'<br>'+'话题背景:'+oneTopic.background+'</p></div><div class="mdui-divider-inset-dark "></div>'
        print (oneTopic)
        a["result"] = "post_success"  #a就是传进去的键值对
        a["oneTopic"] =string
        # return HttpResponse(simplejson.dumps(a), content_type='application/json')
    else:
        a["result"] = "error"  #a就是传进去的键值对
        a["oneTopic"] ="你可能是盗链接的把，大哥"
        # return HttpResponse(simplejson.dumps(a), content_type='application/json')
    return HttpResponse(simplejson.dumps(a), content_type='application/json')

@csrf_exempt #还缺的东西就是写入数据库，把登陆的情况写进去，建立一个关系
def signactivity(request): 
    received_json_data = simplejson.loads(request.body)
    a = {}  # 写不写这个都没关系的
    if(received_json_data['SignName']!=""):
        a = {}  #写不写这个都没关系的 
        signName = received_json_data['SignName'] #签到的名字，还要签到的活动
        signActivity= received_json_data['signActivity'] 
        signUser = User.objects.get(username=signName)  #按名字查到了
        activity = Activity.objects.get(id = signActivity) #按活动的id查到了
        #添加之前先查询是否
        allUser = Activity.objects.get(id=signActivity).user.all()
        for i in allUser:  #遍历看看这个活动下的签到的用户有没有那个人就可以了
            if i ==signUser:
                a["result"] = "post_success"  #a就是传进去的键值对
                a["state"] ="check" #这儿是找
                print(a["state"] )

                return HttpResponse(simplejson.dumps(a), content_type='application/json')
            
        activity.user.add(signUser)# 已经添加了也不影响添加的，真好
        activity.save()  #增加了一个人以前签到了的意思
        print (activity) 
        obj = Activity.objects.filter(id=signActivity).first()  #然后加入一个尝试查询的，如果查询成功，则直接显示以签到就好了
        # 获取所有与当前数据关联的Class5数据
        
        print (obj.user.all())
        #print (signName + " "+signActivity)
        a["result"] = "post_success"  #a就是传进去的键值对
        a["state"] ="check"
    else:
        a["result"] = "error"  #a就是传进去的键值对
        a["oneTopic"] ="你可能是盗链接的把，大哥"
        # return HttpResponse(simplejson.dumps(a), content_type='application/json')
    return HttpResponse(simplejson.dumps(a), content_type='application/json')        


    
 #这个视图需要登陆才可以看到里面的东西的
# @login_required    
def backhome(request):
    str = ""
    if request.method =='GET':
        username = request.GET.get('username','')
        topic_id = request.GET.get('topic_id','')
        comment = request.GET.get('comment','')
        str = "username:"+username +" topic_id:"+ topic_id + "comment"+ comment
        return HttpResponse(str)
    return HttpResponse("hello world %s"%str)
    

#应该每个都是一个线程的，time。wait。不用，使用那种放置重复的就好了，话题也设置成key
def home(request): 

    #有第一条的时候才可以的啊
    oneActivity = Activity.objects.last()#只取出一个最新的活动过来
    allUser = oneActivity.user.all()  #查询一下有没有签到的
    stateNumber = len(allUser) #总签到人数 

    print (oneActivity)
    allSoup= chickenSoup.objects.all()
    total = len(allSoup)   #这儿是随机生成一个鸡汤的东西
    Soup =allSoup[random.randint(0,total-1)]
    #这儿是处理第一篇博文显示的地方，我想下要怎么显示。。。怎么处理多个博文的显示逻辑
    oneblogPage= blogPage.objects.last()
    #oneblogPage=""
    
    #print (Soup)
    allComment = topicComment.objects.all()
    allObject = speechTopic.objects.order_by("-creatTime")  #返回的是一个查找的列表
    paginator = Paginator(allObject,8)
    page = request.GET.get('page')
    try:#从这儿开始就是分页的那个功能的
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    if request.method =='POST':   #是post请求的话，#分别针对是登陆和非登陆这两个不同的请求做不同的反应
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password = password)#后台的账号密码对得上的话就非空
        if request.POST.get('title'):  #先判断是不是话题提交,如果提交的这个不是为空的话
            editor =  request.POST.get('editor','')
            title =  request.POST.get('title','')
            background =  request.POST.get('background','')
            newTopic = speechTopic(title=title,editor=editor,background=background) #先创建后更新，
            faceImage = "media/"+str(MyUser.objects.get(user= User.objects.get(username=editor)).image)
            newTopic.editorImgae=faceImage#找到一个后就都可以的啊
            newTopic.save()
            return HttpResponseRedirect('/')   #直接加一条这个语句就可以搞定这个，如果是首页的话，跳转到xx页面就是了
        if user is not None:  #.
            auth.login(request,user) #非空那么就登陆，一句话就登陆完成
            request.session['user'] = username  #把用户名写入session中去,还可以设置保留的时长
            print ("对方已经登陆过了")
            return HttpResponseRedirect('/')

        else: 
            username = "账号或者密码错误！"  #读取浏览器的session，提取出信息，密码错的话，也还是这样
            return render(request,'EST_HOME.html',{"username":username,'topic_list':contacts,'Soup':Soup})
    else: #这儿这个就是get的方式获得的话题提交的东西，post进来后的其他反应
        username = request.session.get('user','')  #读取浏览器的session，提取出信息
        
        #username = request.session['username']  
        print("这儿是get")
        print(username)
        
        state = "close"  #默认是close
        if username:#非空就返回这个session中去到的
            print("已经登陆过了")
            #签到的东西放在这儿
            # allUser = oneActivity.user.all()  #查询一下有没有签到的
            for i in allUser:
                if i ==User.objects.get(username= username): 
                    print(i)
                    state= "check"
                    print (state)
                    break
            return render(request,"EST_HOME.html",{"username":username,'topic_list':contacts,'Soup':Soup,'comments':allComment,'oneActivity':oneActivity,'state':state,'stateNumber':stateNumber,'signUsers':allUser,'content':oneblogPage})
        else:#空的话就返回提醒的字符
            username = "请点鱼登陆！"
            return render(request,"EST_HOME.html",{"username":username,'topic_list':contacts,'Soup':Soup,'comments':allComment,'oneActivity':oneActivity,'state':state,'stateNumber':stateNumber,'signUsers':allUser,'content':oneblogPage})

def page_not_found(request):
    return render_to_response("404.html")


def page_error(request):
    return render_to_response('500.html')


#@login_required  
def editpage(request):
    allObject = speechTopic.objects.order_by("-creatTime")  #返回的是一个列表
    paginator = Paginator(allObject,10)
    page = request.GET.get('page')
    #从这儿开始就是分页的那个功能的
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    if request.method =='POST':   #是post请求的话
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password = password)#这儿是登陆后台的验证
        if user is not None:  #如果登陆进去了.
            auth.login(request,user) #验证通过再登陆

            #如果登陆正确就要提取出头像，否则就用默认头像
            user_image = User.objects.get(username=username).myuser.image  #查到对应的名字的图标
            request.session['user'] = username  #把用户名写入session中去
            return render(request,'memberpage.html')
        #response = HttpResponseRedirect("/home/")
        else: 
            #username = request.session.get('user','')
            username = "账号或者密码错误！"  #读取浏览器的session，提取出信息，密码错的话，也还是这样
            return render(request,'memberpage.html',{"user":username,'topic_list':contacts})
    else:#这儿这个就是get的方式获得的话题提交的东西
        if request.GET.get('topic'):  #之后就是把get的东西提取出来啦
            editor =  request.POST.get('editor','')
            title =  request.POST.get('title','')
            background =  request.POST.get('background','')
            #写入数据库这条文章数据。
            return render(request,'memberpage.html',{'topic_list':contacts})


from django.contrib.auth import logout as auth_logout  #登出
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')#回去那儿就可以了


#用户界面，可以进行相关的操作
def userManagement(request):
    if request.method=="GET":
        personname =  request.POST.get('personname','')
        longitude =  request.POST.get('longitude','')
        latitude =  request.POST.get('latitude','')
        print("personname: "+personname+"longitude: "+longitude+"latitude: "+latitude)
        return render(request,'userManagement.html')
