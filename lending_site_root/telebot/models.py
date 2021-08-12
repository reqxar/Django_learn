from django.db import models

class botSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен бота')
    tg_chat = models.CharField(max_length=200, verbose_name='id Телеграм чата или человека')

    def __str__(self) -> str:
        return self.tg_token

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'    
