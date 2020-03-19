from django.db import models


# Create your models here.


class Province(models.Model):
    province_name = models.CharField(max_length=50, verbose_name=u'省份名称')

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = '省份'

    def __str__(self):
        return self.province_name


class City(models.Model):
    city_name = models.CharField(max_length=50, verbose_name=u'城市名称')
    province = models.ForeignKey('Province', on_delete=models.CASCADE, verbose_name=u'省份名称')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'

    def __str__(self):
        return self.city_name


class School(models.Model):
    school_name = models.CharField(max_length=50, verbose_name=u'学校名称')
    address = models.CharField(max_length=2000, verbose_name=u'学校地址')
    contect_person = models.CharField(max_length=200, verbose_name=u'联系老师')
    software_period = models.DateField(verbose_name=u'软件维保到期日')
    project_nature = models.BooleanField(default=False, verbose_name=u'运营项目')
    province = models.ForeignKey('Province', on_delete=models.CASCADE, verbose_name=u'省份名称')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name=u'城市名称')

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = '学校'

    def __str__(self):
        return self.school_name


class User(models.Model):
    user_name = models.CharField(max_length=50, verbose_name=u'用户名')
    nick_name = models.CharField(max_length=50, verbose_name=u'员工姓名')
    password = models.CharField(max_length=50, verbose_name=u'密码')
    headimgurl = models.CharField(max_length=200, verbose_name=u'头像')
    loginstate = models.BooleanField(default=False, verbose_name=u'授权状态(默认否)')
    role =models.CharField(max_length=50, verbose_name=u'角色')
    provinces = models.CharField(max_length=50, verbose_name=u'管理省份')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.nick_name


class TerminialType(models.Model):
    type_name = models.CharField(max_length=50, verbose_name=u'终端机型号')

    class Meta:
        verbose_name = '终端机型号'
        verbose_name_plural = '终端机型号'

    def __str__(self):
        return self.type_name


class Printer(models.Model):
    printer_name = models.CharField(max_length=50, verbose_name=u'打印机型号')

    class Meta:
        verbose_name = '打印机型号'
        verbose_name_plural = '打印机型号'

    def __str__(self):
        return self.printer_name


class Wiscard(models.Model):
    wiscard_name = models.CharField(max_length=50, verbose_name=u'一卡通型号')

    class Meta:
        verbose_name = '一卡通型号'
        verbose_name_plural = '一卡通型号'

    def __str__(self):
        return self.wiscard_name


class Terminial(models.Model):
    terminial_name = models.CharField(max_length=50, verbose_name=u'终端名')
    teamviewerid = models.CharField(max_length=50, verbose_name=u'TeamViewerID')
    anydeskid = models.CharField(max_length=50, verbose_name=u'AnyDeskID')
    hardware_period = models.DateField(verbose_name=u'硬件维保到期日')
    school = models.ForeignKey('School', on_delete=models.CASCADE, verbose_name=u'学校')
    contect_person = models.CharField(max_length=200, verbose_name=u'学校联系人')
    contect_person2 = models.CharField(max_length=200, verbose_name=u'硬件合作资源')
    terminial_type = models.ForeignKey('TerminialType', on_delete=models.CASCADE, verbose_name=u'终端机型号')
    printer = models.ForeignKey('Printer', on_delete=models.CASCADE, verbose_name=u'打印机型号')
    wiscard = models.ForeignKey('Wiscard', on_delete=models.CASCADE, verbose_name=u'一卡通型号')
    remarks = models.TextField(max_length=2000, verbose_name=u'备注')
    address = models.CharField(max_length=200, verbose_name=u'地址')

    class Meta:
        verbose_name = '终端'
        verbose_name_plural = '终端'

    def __str__(self):
        return self.terminial_name


class Order(models.Model):
    school = models.ForeignKey('School', on_delete=models.CASCADE, verbose_name=u'学校')
    terminial = models.ForeignKey('Terminial', on_delete=models.CASCADE, verbose_name=u'终端')
    job = models.CharField(max_length=2000, verbose_name=u'问题描述')
    create_date = models.DateField(verbose_name=u'创建日期')
    comleted_date = models.DateField(verbose_name=u'完成日期')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name=u'工程师')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name=u'状态')
    classification = models.ForeignKey('Classification', on_delete=models.CASCADE, verbose_name=u'工单分类')
    order_type = models.ForeignKey('OrderType', on_delete=models.CASCADE, verbose_name=u'问题分类')
    remarks = models.CharField(max_length=5000, verbose_name=u'处理方法')
    value1 = models.CharField(max_length=200, verbose_name=u'实际分值')
    value2 = models.CharField(max_length=200, verbose_name=u'最终分值')

    class Meta:
        verbose_name = '工单'
        verbose_name_plural = '工单'

    def __str__(self):
        return self.job


class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name=u'状态')

    class Meta:
        verbose_name = '状态'
        verbose_name_plural = '状态'

    def __str__(self):
        return self.status_name


class Classification(models.Model):
    classification = models.CharField(max_length=50, verbose_name=u'工单分类')

    class Meta:
        verbose_name = '工单分类'
        verbose_name_plural = '工单分类'

    def __str__(self):
        return self.classification


class OrderType(models.Model):
    order_type = models.CharField(max_length=50, verbose_name=u'问题分类')
    value = models.CharField(max_length=50, verbose_name=u'预估分值')
    classification = models.ForeignKey('Classification', on_delete=models.CASCADE, verbose_name=u'工单分类')

    class Meta:
        verbose_name = '问题分类'
        verbose_name_plural = '问题分类'

    def __str__(self):
        return self.order_type
