from django.db import models
from django.contrib.auth.models import User, Group

class OfficeEquipment(models.Model):
    id_device = models.AutoField(primary_key=True, verbose_name="ID устройства")
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    STATUS_CHOICES1 = (
        ('Компьютеры', 'Компьютеры'),
        ('Телефоны', 'Телефоны'),
        ('Принтер', 'Принтер'),
        ('Сканер', 'Сканер'),
        ('Копировальные аппараты', 'Копировальные аппараты'),
        ('Факсимильные аппараты', 'Факсимильные аппараты'),
        ('Многофункциональные устройства (МФУ)', 'Многофункциональные устройства (МФУ)'),
        ('Серверы', 'Серверы'),
        ('Плоттеры', 'Плоттеры'),
        ('Шредеры', 'Шредеры'),
        ('Калькуляторы', 'Калькуляторы'),
        ('Ноутбуки', 'Ноутбуки'),
        ('Мониторы', 'Мониторы'),
        ('Клавиатуры', 'Клавиатуры'),
        ('Мыши', 'Мыши'),
        ('Сетевое оборудование (роутеры, свитчи, хабы)', 'Сетевое оборудование (роутеры, свитчи, хабы)'),
        ('Источники бесперебойного питания (ИБП)', 'Источники бесперебойного питания (ИБП)'),
        ('Кабели и разъемы', 'Кабели и разъемы'),
        ('Картриджи и тонеры', 'Картриджи и тонеры'),
        ('Бумага и другие расходные материалы', 'Бумага и другие расходные материалы'),
    )
    category = models.CharField(max_length=70, choices=STATUS_CHOICES1, verbose_name="Категория")
    STATUS_CHOICES = (
        ('В работе', 'В работе'),
        ('В ремонте', 'В ремонте'),
        ('В запасе', 'В запасе'),
        ('Списана', 'Списана'),
        ('Неизвестно', 'Неизвестно'),
        ('В утилизации', 'В утилизации'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Статус оборудования")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Отдел", to_field='name')
    delivery_date = models.DateField(verbose_name="Дата поставки")

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

class LicenseTimer(models.Model):
    os_timer = models.DateTimeField(verbose_name="Таймер ОС")
    antivirus_timer = models.DateTimeField(verbose_name="Таймер Антивируса")
    office_timer = models.DateTimeField(verbose_name="Таймер Офиса")

    def __str__(self):
        return f"ОС: {self.os_timer}, Антивирус: {self.antivirus_timer}, Офис: {self.office_timer}"

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

