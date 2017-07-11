from django.db import models

# Create your models here.

class Organization():
    id = models.IntegerField(verbose_name=u"序号")
    name = models.CharField(max_length=100, verbose_name=u"机构全称")
    address = models.CharField(max_length=100, verbose_name=u"机构地址")
    phtone = models.CharField(max_length=20, verbose_name=u"联系电话")
    websit = models.CharField(max_length=100, verbose_name=u"机构网址")
    product = models.TextField(verbose_name=u"产品/服务类型")
    customer = models.TextField(verbose_name=u"服务客户类型")
    detail = models.TextField(verbose_name=u"具体擅长哪类主题定制")
    charge = models.TextField(verbose_name=u"定制收费方式")
    destinnation = models.TextField(verbose_name=u"擅长目的地")
    count = models.IntegerField(verbose_name=u"全职定制师人数")
    brief = models.TextField(verbose_name=u"机构简介")

