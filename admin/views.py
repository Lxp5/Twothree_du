from django.shortcuts import render

# Create your views here.

#g管理员登录
def login(request):
    print("这是登录界面")
    return render(request,"admin/login.html")

#后天管理首页
def index(request):
    print("这是首页")
    return render(request,"admin/index.html")