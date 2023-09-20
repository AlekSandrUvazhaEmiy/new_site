from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Advertisements(models.Model):

    title = models.CharField("Заголовок", max_length=128)

    #описание
    description = models.TextField('Описание')
    #цена 
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    #дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    #дата изменения
    updatet_at = models.DateTimeField(auto_now=True)
    #торг
    auction = models.BooleanField("Торг", help_text="отметьте если хотите торговаться")
    #картинка

    #адрес

    #отзывы о продавце

    #контакты продавца

    #похожие товары
    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html("<span style = 'color:green; font-weight:bold;> сегодня в {}</span", created_time)

        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})>"

    class Meta ():
        db_table = 'advertisements'