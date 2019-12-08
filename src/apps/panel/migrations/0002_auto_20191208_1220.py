# Generated by Django 3.0 on 2019-12-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claimtempmodel',
            name='slug',
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='assignee',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='city',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='date_out',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='до'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='date_with',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Назначена с'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='district',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='email',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='fio',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='floor',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='home_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='info',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='intercom',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Домофон'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='master',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='organization',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Организация'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='other_info',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='personal_bill',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Личный счет'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='priority',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='room_number',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Номер квартиры'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='street',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='claimtempmodel',
            name='type_chaim',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Тип'),
        ),
    ]
