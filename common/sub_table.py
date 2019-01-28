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

if __name__ == '__main__':
    pass
