from django.db import models
import datetime
from django.contrib import admin

def create_model(name, abstract_model_class, meta_options=None, admin_opts=None):
    """
    用于创建多个表
    :param name: 类的名称
    :param abstract_model_class: 继承自哪个abstract model
    :param meta_options : 用于更新meta的数据
    :param admin_opts:
    :return:
    """

    class Meta:
        pass

    if meta_options is not None:
        for key, value in meta_options.items():
            setattr(Meta, key, value)

    attrs = {
        '__module__': abstract_model_class.__module__,
        'Meta': Meta,
    }

    ModelClass = type(name, (abstract_model_class,), attrs)

    # 如果提供了admin参数，那么创建Admin类
    if admin_opts is not None:
        class Admin(admin.ModelAdmin):
            pass
        for key, value in admin_opts.items():
            setattr(Admin, key, value)
        admin.site.register(ModelClass, Admin)
    return ModelClass

shard_tables = {}
class UserShardMixin:
    @classmethod
    def shard(cls):
        # 返回当前用的表
        # 根据当前时间来看
        dt = datetime.datetime.now()
        year = dt.year
        month = dt.month
        current_table_suffix = "_%s_%s"%(year,month)
        current_table = shard_tables[current_table_suffix]
        print(current_table)
        return current_table
        # try:
        #
        # except:
        #
        #     return User

        #
        # node_id = str(id % SHARD_NUM)
        # print(shard_tables[node_id])
        # return shard_tables[node_id]

class User(models.Model, UserShardMixin):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s:%s" % (str(self.id), self.name)

    class Meta:
        # abstract = True
        db_table = "user"

    @property
    def list_field(self):
        return ['id', 'name', 'age', "active"]


# 动态生成table,说白了就是循环生成多个model
dt = datetime.datetime.now()
year = dt.year
month = dt.month
tb_years_12 = ["_%s_%s" % (year, index) for index in range(month, 13)]
print(tb_years_12)
for shard_id in tb_years_12:
    UserModel = create_model(
        User.__name__ + str(shard_id),
        User,
        meta_options={
            'verbose_name': User.__name__ + str(shard_id),
            'verbose_name_plural': User.__name__ + str(shard_id)
        },
        admin_opts={
            'list_display': User.list_field
        }
    )
    shard_tables[str(shard_id)] = UserModel

  # UserModel = create_model(
  #               User.__name__ + str(current_table_suffix),
  #               User,
  #               meta_options={
  #                   'verbose_name': User.__name__ + str(current_table_suffix),
  #                   'verbose_name_plural': User.__name__ + str(current_table_suffix)
  #               },
  #               # admin_opts={
  #               #     'list_display': ('id', 'name', 'age', 'active')
  #               # }
  #           )
  #           shard_tables[current_table_suffix] = UserModel
  #           os.system('python3 %s makemigrations'%MANAGE)
  #           os.system('python3 %s migrate'%MANAGE)
