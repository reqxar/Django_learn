from django.db import models

class SubscribePrices(models.Model):
    subscribe_description = models.CharField(max_length=200, verbose_name='Описание подписки')
    subscribe_price = models.IntegerField(verbose_name='Цена подписки')

    def __str__(self) -> str:
        return self.subscribe_description

    class Meta:
        verbose_name = 'Подписку'
        verbose_name_plural = 'Подписки'    


class ServicePrices(models.Model):
    service_name = models.CharField(max_length=20, verbose_name='Название услуги')
    service_old_price = models.IntegerField(verbose_name='Старая цена')
    service_new_price = models.IntegerField(verbose_name='Новая цена')

    def __str__(self) -> str:
        return self.service_name

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'  
        
