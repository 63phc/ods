from django.db import models


class ClaimTempModel(models.Model):
    title = models.CharField(verbose_name='Название', max_length=64, blank=True, null=True)

    date_with = models.CharField(verbose_name='Назначена с', max_length=64, blank=True, null=True)
    date_out = models.CharField(verbose_name='до', max_length=64, blank=True, null=True)
    type_chaim = models.CharField(verbose_name='Тип', max_length=64, blank=True, null=True)
    category = models.CharField(verbose_name='Категория', max_length=64, blank=True, null=True)
    priority = models.CharField(verbose_name='Приоритет', max_length=64, blank=True, null=True)
    organization = models.CharField(verbose_name='Организация', max_length=64, blank=True, null=True)
    master = models.CharField(verbose_name='Мастер', max_length=64, blank=True, null=True)
    assignee = models.CharField(verbose_name='Исполнитель', max_length=64, blank=True, null=True)
    info = models.CharField(verbose_name='Доп. информация', max_length=64, blank=True, null=True)

    # client
    phone = models.CharField(verbose_name='Телефон', max_length=64, blank=True, null=True)
    fio = models.CharField(verbose_name='ФИО', max_length=64, blank=True, null=True)
    email = models.CharField(verbose_name='Почта', max_length=64, blank=True, null=True)
    personal_bill = models.CharField(verbose_name='Личный счет', max_length=64, blank=True, null=True)

    city = models.CharField(verbose_name='Город', max_length=64, blank=True, null=True)
    district = models.CharField(verbose_name='Район', max_length=64, blank=True, null=True)
    street = models.CharField(verbose_name='Улица', max_length=64, blank=True, null=True)
    home_number = models.CharField(verbose_name='Номер дома', max_length=64, blank=True, null=True)
    room_number = models.CharField(verbose_name='Номер квартиры', max_length=64, blank=True, null=True)
    intercom = models.CharField(verbose_name='Домофон', max_length=64, blank=True, null=True)
    floor = models.CharField(verbose_name='Этаж', max_length=64, blank=True, null=True)
    other_info = models.CharField(verbose_name='Доп. информация', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title


