from django.db import models
from django.db.models.deletion import CASCADE, PROTECT


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Название статуса')

    def __str__(self) -> str:
        return self.status_name

    class Meta:
        verbose_name = 'Cтатус'
        verbose_name_plural = 'Статусы'  
        

class Order(models.Model):
    order_date = models.DateField(auto_now=True, verbose_name='Дата')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(OrderStatus, on_delete=PROTECT, null=True, verbose_name='Статус заказа')

    def __str__(self) -> str:
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderComments(models.Model):
    order = models.ForeignKey(Order, on_delete=CASCADE, verbose_name='Заказ')
    comment_text = models.TextField(verbose_name='Текст комментария')           

    def __str__(self) -> str:
        return self.comment_text

    class Meta:
        verbose_name = 'Комметарий'
        verbose_name_plural = 'Комментарии'
