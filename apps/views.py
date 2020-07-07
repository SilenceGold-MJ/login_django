from django.shortcuts import render

# Create your views here.
import json
import os,time
import base64
from django.shortcuts import render, HttpResponse, redirect
from framework.API import API
from framework.logger import Logger
logger = Logger(logger="views").getlog()

# Create your views here.
address='http://127.0.0.1:8000'
# 1.登录
def login(request):
    print('----------------------------------->', )
    if request.method=="POST":
        username = request.POST.get("user")
        password = request.POST.get("pwd")
        data = API().login_api(username, password)
        logger.info('请求登录接口')
        logger.info(data)
        if data['result_code'] =='0000':
            logger.info('登录验证通过')
            #return render(request, 'index.html')

            return render(request,'tiaozhuan.html',{ "url":'http://127.0.0.1:8000/search.html'})
        else:
            logger.info('登录验证不通过')
            return render(request, "login.html")

    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('打开login.html')
    return render(request, "login.html")



# 3.个人页
def index(request):
    # print("GET", request.POST)
    # user = request.GET.get("username")
    # n = user
    # print(request.get_full_path())
    ret = request.GET.get('name')
    print(request.GET.get('name'))
    # return HttpResponse('ok')
    return render(request, "index.html", {"n": ret})

def register(request):
    path='/static/images/upload_image/'
    if request.method == 'POST':

        fname = request.FILES.get('head', '1')
        dic = {
            "name": (fname.name),
            "size": (fname.size),
            "base64_str": (fname.read()),
        }
        logger.info(dic)
        save_path = os.path.join(os.getcwd() + "/static/images/upload_image", dic["name"])
        destination = open(save_path, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in fname.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()


        if  "user" in request.POST and "pwd" in request.POST :
            logger.info(request.POST)
            # username = request.POST.get("user")
            # password = request.POST.get("pwd")

            dic={
            'username' : request.POST.get("user"),
            'pwd' : request.POST.get("pwd"),
            'realname' : request.POST.get("realname"),
            'nickname' : request.POST.get("nickname"),
            'gender' : request.POST.get("gender"),
            'email' : request.POST.get("email"),
            'mobile' : request.POST.get("mobile"),
            'deleted' : request.POST.get("deleted"),
            'head' : path+dic["name"],

            }




            data = API().Registered(dic)
            logger.info('请求接口')
            logger.info(data)
            if data['result_code'] == '0000':
                logger.info('验证通过')
                # return render(request, 'index.html')
                return render(request, '表格.html', {"dic": data})
            else:
                logger.info('验证不通过')
                # return render(request, "login.html")
                return render(request, '表格.html', {"dic": data})


    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('register.html')
    return render(request, "register.html")


def search(request):
    if request.method == 'POST':
        if  "user" in request.POST:
            logger.info(request.POST)
            username = request.POST.get("user")
            data = API().check_user(username)
            logger.info('请求接口')
            logger.info(data)

            if data['result_code'] == '0000':
                logger.info('验证通过')
                # return render(request, 'index.html')
                dicinfo = data['datalist'][0]

                dicinfo.update({'head': address + dicinfo['head']})
                return render(request, '搜索查看.html', {"dic": dicinfo})
            else:
                logger.info('验证不通过')
                # return render(request, "login.html")

                # return render(request, '表格.html', {"dic": data})
                return HttpResponse(str(data))

        elif 'alluser' in request.POST:
            logger.info(request.POST)
            # if request.method == "POST":
            username = request.POST.get("alluser")
            data = API().getalluser(username)
            logger.info('请求接口')
            logger.info(data)
            if data['result_code'] == '0000':
                logger.info('验证通过')
                # return render(request, 'index.html')
                return render(request, '表格.html', {"dic": data})
            else:
                logger.info('验证不通过')
                # return render(request, "login.html")
                return render(request, '表格.html', {"dic": data})

    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('打开sousuo.html')
    return render(request, "搜索.html")

def Updatainfo(request):
    path = '/static/images/upload_image/'
    if request.method == 'POST':
        fname = request.FILES.get('head', '1')
        logger.info(fname)

        dic={
        "name":(fname.name),
        "size":(fname.size),
        "bytes_pic":(fname.read()),

        }
        logger.info(dic)
        save_path = os.path.join(os.getcwd() +  "/static/images/upload_image", dic["name"])
        with open(save_path, 'wb') as f:
            f.write(dic['bytes_pic'])



        if  "nickname" in request.POST:
            logger.info(request.POST)
            dic={
            'username' : request.POST.get("user"),
            'pwd' : request.POST.get("pwd"),
            'realname' : request.POST.get("realname"),
            'nickname' : request.POST.get("nickname"),
            'gender' : request.POST.get("gender"),
            'email' : request.POST.get("email"),
            'mobile' : request.POST.get("mobile"),
            'deleted' : request.POST.get("deleted"),
            'head' :path+dic["name"],

            }


            logger.info(dic)
            data = API().updata_info( dic)
            logger.info('请求接口')
            logger.info(data)

            if data['result_code'] == '0000':
                logger.info('验证通过')
                # return render(request, 'index.html')

                return render(request, '表格.html', {"dic": data,'address':address})
            else:
                logger.info('验证不通过')
                # return render(request, "login.html")
                return render(request, '表格.html', {"dic": data})

    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('打开Updatainfo.html')
    return render(request, "Updatainfo.html")

def Seeinfo(request):
    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('打开查看.html')
    return render(request, "查看.html")

def imagelist(request):
    path=r'D:\Python\python3\web_django\login_django\static\images\wenwu'
    imagelist=os.listdir(path)
    # for i in os.listdir(path):
    #     imagepath=(path+"\\"+i).replace("\\","/")
    #
    #     imagelist.append(imagepath)
    #     logger.info(imagepath)

    return render(request, '查看图片.html', {"imagelist": imagelist})
def upload(request):

    if request.method == 'POST':
        fname = request.FILES.get('fafafa', '1')

        dic={
        "name":(fname.name),
        "size":(fname.size),
        "base64_str":(fname.read()),
        }
        logger.info(dic)
        save_path = os.path.join(os.getcwd() +  "/static/images/upload_image", dic["name"])
        destination = open(save_path, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in fname.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("上传完成!")


    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('上传.html')
    return render(request, "上传.html")

def post( request):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        obj = request.FILES.get('fafafa', '1')
        print((obj.name))
        f = open(os.path.join(BASE_DIR, 'media', 'image', obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        # return render(request, 'clashphone/test.html')
        return HttpResponse('OK')
