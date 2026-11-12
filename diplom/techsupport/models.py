from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Problem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name="Пользователь")
    id_request = models.AutoField(primary_key=True, verbose_name="id")
    request_from_date = models.DateField(verbose_name="Дата обращения")
    name_of_problem = models.CharField(max_length=80, verbose_name="Наименование")
    description_of_problem = models.CharField(max_length=256, verbose_name="Описание")
    STATUS_CHOICES = (
        ('Открыта', 'Открыта'),
        ('В работе', 'В работе'),
        ('Выполнена', 'Выполнена'),
        ('Отклонена', 'Отклонена'),
        ('Ожидает', 'Ожидает'),
        ('На доработку', 'На доработку'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Открыта', blank=True, verbose_name="Статус")
    date_of_finish = models.DateField(null=True, blank=True, verbose_name="Дата завершения")

    def __str__(self):
        return f'{self.id_request} {self.request_from_date} {self.name_of_problem} {self.description_of_problem}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Note(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, verbose_name="Заявка")
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Работник")
    note_date = models.DateField(verbose_name="Дата записи")
    note_text = models.TextField(verbose_name="Текст записи")

    def __str__(self):
        return f'{self.problem} {self.worker} {self.note_date}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

class Feedback(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='feedback')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback')
    rating = models.IntegerField(default=5, verbose_name='Оценка')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Feedback for problem {self.problem.id_request} by {self.user.username}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

