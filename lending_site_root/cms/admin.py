from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CmsSlider


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cms_title', 'get_img')
    list_display_links = ('id', 'cms_title', 'get_img')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'cms_title', 'cms_text', 'get_img')
    readonly_fields = ('id', 'get_img')

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.cms_img.url}" width="50px"')

    get_img.short_description = 'Картинка'    

admin.site.register(CmsSlider, SliderAdmin)
