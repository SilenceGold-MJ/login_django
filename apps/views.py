from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from framework.API import API
from framework.logger import Logger
logger = Logger(logger="views").getlog()

# Create your views here.

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
    if request.method == 'POST':
        if  "user" in request.POST and "pwd" in request.POST :
            logger.info(request.POST)
            username = request.POST.get("user")
            password = request.POST.get("pwd")
            data = API().Registered(username,password)
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
                return render(request, '查询结果.html', {"dic": data})
            else:
                logger.info('验证不通过')
                # return render(request, "login.html")
                return render(request, '查询结果.html', {"dic": data})
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
                return render(request, '查询结果.html', {"dic": data})

    # 3.跳转页面
    # return HttpResponse('ok')
    logger.info('打开sousuo.html')
    return render(request, "搜索.html")

