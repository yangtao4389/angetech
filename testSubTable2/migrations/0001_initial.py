# Generated by Django 2.0.4 on 2019-01-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceOrderCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_transid', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='订单编号')),
                ('c_userid', models.CharField(blank=True, db_index=True, default='', max_length=50, null=True, verbose_name='用户')),
                ('c_productId', models.CharField(max_length=50, null=True, verbose_name='产品id')),
                ('c_contentId', models.CharField(max_length=50, null=True, verbose_name='内容id')),
                ('t_cloudPayUrl', models.TextField(max_length=256, null=True, verbose_name='支付链接')),
                ('t_return_url', models.TextField(max_length=256, null=True, verbose_name='订购失败跳转地址')),
                ('t_currentUrl', models.TextField(max_length=256, null=True, verbose_name='订购成功跳转地址')),
                ('i_paystatus', models.IntegerField(default=0, help_text='0-等待,1-成功,-1-错误', null=True, verbose_name='充值状态')),
                ('c_paymemo', models.CharField(help_text='0-等待,1-成功,-1-错误', max_length=10, null=True, verbose_name='充值状态说明')),
                ('c_payresult', models.CharField(max_length=50, null=True, verbose_name='充值错误code')),
                ('update_time', models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '服务订购信息表',
                'db_table': 'service_order_condition',
            },
        ),
    ]