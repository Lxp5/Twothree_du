from django.db import models
from datetime import datetime
from django.db.models import CharField,Aggregate
import datetime
# Create your models here.

# class Website:
#     """
#     网站初始化设置
#     """
class Admin_user(models.Model):
    """
    管理员表
    """
    admin_name = models.CharField(max_length=50, null=False)
    pwd = models.CharField(max_length=8,null=False)
    class Meta:
        # 数据库的表名称，默认app名称+下划线+类名
        db_table = "admin_user"

# class Pictures:
#     """
#     图片模块
#     """
#
# #首页
# class Server:
#     """
#     服务
#     """
#
# class Products:
#     """
#     产品分类模块：从产品展示页面的表中读取8条数据进行展示
#     """
#
# #关于我们
# class Certify:
#     """
#     资质证书
#     """
#
# #产品展示
# class Product_classify:
#     """
#     产品分类模块
#     """
#
# class Product_detail:
#     """
#     产品详情模块
#     """
#
# #工程案例
# #两表是一对多关系
# class Project_classify:
#     """
#     工程分类
#     """
# class Project_detail:
#     """
#     工程详情
#     """
# #技术文献
# class Technical_literature:
#     """
#     技术文献
#     """
#
# #服务支持
# class Data_download:
#     """
#     服务支持
#     """
#
# #联系我们
# class Talent_hire:
#     """
#     人才招聘
#     """
#
# class User_message:
#     """
#     客户留言
#    """