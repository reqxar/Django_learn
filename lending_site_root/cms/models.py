from django.db import models

class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='slider_img/', verbose_name='Изображение')
    cms_title = models.CharField(max_length=200, verbose_name='Название слайда')
    cms_text = models.CharField(max_length=200, verbose_name='Текст слайда')

    def __str__(self) -> str:
        return self.cms_title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
