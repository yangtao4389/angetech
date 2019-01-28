# from django.db import models
#
#
# # Create your models here.
# def getModel(db_table2):
#     '''
#     通过工厂模式来创建多个表
#     :param db_table:
#     :return:
#     '''
#     class MyClassMetaclass(models.base.ModelBase):
#         def __new__(cls, name, bases, attrs):
#             name += db_table2
#             return models.base.ModelBase.__new__(cls, name, bases, attrs)
#
#     class MyClass(models.Model):
#         __metaclass__ = MyClassMetaclass
#         c_transid = models.CharField(verbose_name="订单编号", unique=True, max_length=64, null=False, db_index=True)
#         c_userid = models.CharField(verbose_name="用户", db_index=True, max_length=50, null=True, blank=True, default="")
#         c_productId = models.CharField(verbose_name="产品id", max_length=50, null=True, )
#         c_contentId = models.CharField(verbose_name="内容id", max_length=50, null=True, )
#         t_cloudPayUrl = models.TextField(verbose_name="支付链接", max_length=256, null=True, )
#         t_return_url = models.TextField(verbose_name="订购失败跳转地址", max_length=256, null=True, )
#         t_currentUrl = models.TextField(verbose_name="订购成功跳转地址", max_length=256, null=True, )
#         i_paystatus = models.IntegerField(verbose_name="充值状态", null=True, default=0, help_text="0-等待,1-成功,-1-错误")
#         c_paymemo = models.CharField(verbose_name="充值状态说明", null=True, max_length=10, help_text="0-等待,1-成功,-1-错误")
#         c_payresult = models.CharField(verbose_name="充值错误code", null=True, max_length=50, )
#         update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True, null=True)
#         create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, db_index=True, null=True)
#         class Meta:
#             db_table = db_table2
#     return MyClass
#
# class ServiceOrderCondition(models.Model):
#     c_transid = models.CharField(verbose_name="订单编号", unique=True, max_length=64, null=False, db_index=True)
#     c_userid = models.CharField(verbose_name="用户", db_index=True, max_length=50, null=True, blank=True, default="")
#     c_productId = models.CharField(verbose_name="产品id", max_length=50, null=True, )
#     c_contentId = models.CharField(verbose_name="内容id", max_length=50, null=True, )
#     t_cloudPayUrl = models.TextField(verbose_name="支付链接", max_length=256, null=True, )
#     t_return_url = models.TextField(verbose_name="订购失败跳转地址", max_length=256, null=True, )
#     t_currentUrl = models.TextField(verbose_name="订购成功跳转地址", max_length=256, null=True, )
#     i_paystatus = models.IntegerField(verbose_name="充值状态", null=True, default=0, help_text="0-等待,1-成功,-1-错误")
#     c_paymemo = models.CharField(verbose_name="充值状态说明", null=True, max_length=10, help_text="0-等待,1-成功,-1-错误")
#     c_payresult = models.CharField(verbose_name="充值错误code", null=True, max_length=50, )
#     update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True, null=True)
#     create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, db_index=True, null=True)
#
#     class Meta:
#         db_table = "service_order_condition"
#         verbose_name_plural = "服务订购信息表"





# from django.db import models
# from django.db.models.base import ModelBase
#
# def create_model(db_table3):
#     class CustomMetaClass(ModelBase):
#         def __new__(cls, name, bases, attrs):
#             name += db_table3
#             return models.base.ModelBase.__new__(cls, name, bases, attrs)
#             # model = super(CustomMetaClass, cls).__new__(cls, name, bases, attrs)
#             # print(model)
#             # model._meta.db_table = db_table
#             # return model
#
#     class CustomModel(models.Model):
#         __metaclass__ = CustomMetaClass
#         # define your fileds here
#         c_transid = models.CharField(verbose_name="订单编号", unique=True, max_length=64, null=False, db_index=True)
#         c_userid = models.CharField(verbose_name="用户", db_index=True, max_length=50, null=True, blank=True, default="")
#         c_productId = models.CharField(verbose_name="产品id", max_length=50, null=True, )
#         c_contentId = models.CharField(verbose_name="内容id", max_length=50, null=True, )
#         t_cloudPayUrl = models.TextField(verbose_name="支付链接", max_length=256, null=True, )
#         t_return_url = models.TextField(verbose_name="订购失败跳转地址", max_length=256, null=True, )
#         t_currentUrl = models.TextField(verbose_name="订购成功跳转地址", max_length=256, null=True, )
#         i_paystatus = models.IntegerField(verbose_name="充值状态", null=True, default=0, help_text="0-等待,1-成功,-1-错误")
#         c_paymemo = models.CharField(verbose_name="充值状态说明", null=True, max_length=10, help_text="0-等待,1-成功,-1-错误")
#         c_payresult = models.CharField(verbose_name="充值错误code", null=True, max_length=50, )
#         update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, db_index=True, null=True)
#         create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, db_index=True, null=True)
#
#         # class Meta:
#         #     db_table = db_table
#
#     return CustomModel

from django.db import models

from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return "%s:%s" % (str(self.id), self.name)

    class Meta:
        # abstract = True
        db_table = "user"


def __create_user_model(db_table2):
    '''
    :param db_table2:表名
    :return:
    '''

    class MyClassMetaclass(models.base.ModelBase):
        def __new__(cls, name, bases, attrs):
            name += db_table2
            return models.base.ModelBase.__new__(cls, name, bases, attrs)

    class MyClass(models.Model):
        __metaclass__ = MyClassMetaclass
        id = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=20)
        age = models.IntegerField(default=0)

        class Meta:
            db_table = db_table2

    return MyClass

def get_user_db():
    '''
    return：数据库的名字，根据自己定义的数据库略作调整
    '''
    from django.db import connection
    return connection.settings_dict["NAME"]


def exe_sql(sql):
    from django.db import connection
    # connection = connections["default"]
    cr = connection.cursor()
    cr.execute(sql)
    try:
        connection.commit()
    except:
        pass
    return cr


import datetime,traceback
def get_diy_user_model():
    '''
    :return:会返回一个当前月份的一张表：user_2019_1
    '''
    dt = datetime.datetime.now()
    current_table_suffix = "_%s_%s" % (dt.year, dt.month)
    current_table = User._meta.db_table + current_table_suffix
    create_sql = """CREATE TABLE `%s` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    try:
        SQL = """
                      SELECT count(*) AS is_exist
                      FROM information_schema.tables
                          WHERE table_schema = '%s'
                          AND table_name = '%s'
              """ % (get_user_db(), current_table)
        cr = exe_sql(SQL)
        is_exist = cr.fetchall()[0][0]
        if not is_exist:
            exe_sql(create_sql % current_table)
        return __create_user_model(db_table2=current_table)
    except:
        print(traceback.print_exc())
        return User



