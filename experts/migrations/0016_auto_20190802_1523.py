# Generated by Django 2.2.1 on 2019-08-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0015_auto_20190725_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertinfo',
            name='eemail',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='expertinfo',
            name='emobile',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='expertinfo',
            name='ename',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='expertinfo',
            name='eqq',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='expertinfo',
            name='eupdated_by',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='bank',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='银行账号'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='remark',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='workexp',
            name='company',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
