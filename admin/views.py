from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
# Create your views here.
from admin import models
from utills import tools
#g管理员登录
def login(request):
    print(request.method)
    if request.method == "POST":
        # 接收传递过来的数据
        print("接收数据")
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        rem = request.POST.get('remember')
        print(user, pwd, rem)
        # 和数据库对接
        try:
            admininfo = models.User.objects.get(username=user)
            print(admininfo.id)
            print(admininfo)
            if pwd == admininfo.pwd:
                # 登录成功
                _data = tools.returndata(1, "登录成功")
                print(_data)

                # if rem != None:
                #     #把管理员存储在session中
                #     print('这个是id值',admininfo.id)
                #     request.session["user"]=admininfo.id
                ret = JsonResponse(_data)
                ret.set_cookie("uid", admininfo.id, max_age=7 * 24 * 60 * 60)
                return ret
            _data = tools.returndata(0, "密码错误")
            print(_data)
            return JsonResponse(_data)
        except Exception as e:
            _data = tools.returndata(0, "用户名不存在")
            print(_data)
            return JsonResponse(_data)

    return render(request,"admin/login.html")
#后天管理首页
def index(request):
    print("这是首页")
    return render(request,"admin/index.html")