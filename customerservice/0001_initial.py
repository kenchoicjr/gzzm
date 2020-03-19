# Generated by Django 2.1.3 on 2019-01-13 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, verbose_name='城市名称')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_name', models.CharField(max_length=50, verbose_name='打印机型号')),
            ],
            options={
                'verbose_name': '打印机型号',
                'verbose_name_plural': '打印机型号',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=50, verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '省份',
                'verbose_name_plural': '省份',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=50, verbose_name='学校名称')),
                ('address', models.CharField(max_length=200, verbose_name='学校地址')),
                ('contect_person', models.CharField(max_length=200, verbose_name='联系老师')),
                ('software_period', models.DateField(verbose_name='软件维保到期日')),
                ('project_nature', models.BooleanField(default=False, verbose_name='运营项目')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.City', verbose_name='城市名称')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.Province', verbose_name='省份名称')),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
            },
        ),
        migrations.CreateModel(
            name='Terminial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terminial_name', models.CharField(max_length=50, verbose_name='终端名')),
                ('teamviewerid', models.CharField(max_length=50, verbose_name='TeamViewerID')),
                ('anydeskid', models.CharField(max_length=50, verbose_name='AnyDeskID')),
                ('hardware_period', models.DateField(verbose_name='硬件维保到期日')),
                ('contect_person', models.CharField(max_length=200, verbose_name='学校联系人')),
                ('contect_person2', models.CharField(max_length=200, verbose_name='硬件合作资源')),
                ('remarks', models.TextField(max_length=2000, verbose_name='备注')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.Printer', verbose_name='打印机型号')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.School', verbose_name='学校')),
            ],
            options={
                'verbose_name': '终端',
                'verbose_name_plural': '终端',
            },
        ),
        migrations.CreateModel(
            name='TerminialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, verbose_name='终端机型号')),
            ],
            options={
                'verbose_name': '终端机型号',
                'verbose_name_plural': '终端机型号',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='用户名')),
                ('nick_name', models.CharField(max_length=50, verbose_name='员工姓名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('headimgurl', models.CharField(max_length=200, verbose_name='头像')),
                ('loginstate', models.BooleanField(default=False, verbose_name='授权状态(默认否)')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Wiscard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiscard_name', models.CharField(max_length=50, verbose_name='一卡通型号')),
            ],
            options={
                'verbose_name': '一卡通型号',
                'verbose_name_plural': '一卡通型号',
            },
        ),
        migrations.AddField(
            model_name='terminial',
            name='terminial_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.TerminialType', verbose_name='终端机型号'),
        ),
        migrations.AddField(
            model_name='terminial',
            name='wiscard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.Wiscard', verbose_name='一卡通型号'),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerservice.Province', verbose_name='省份名称'),
        ),
    ]
