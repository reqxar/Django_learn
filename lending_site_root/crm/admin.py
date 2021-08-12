from django.contrib import admin
from .models import Order, OrderStatus, OrderComments


class Comment(admin.StackedInline):
    model = OrderComments
    fields = ('comment_text',)
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_name', 'order_phone', 'order_status', 'order_date')
    list_display_links = ('id', 'order_name',)
    search_fields = ('order_name', 'order_phone')
    list_filter = ('order_status',)
    list_editable = ('order_phone', 'order_status')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_name', 'order_phone', 'order_status' , 'order_date')
    readonly_fields = ('id', 'order_date')
    inlines = [Comment,]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)
admin.site.register(OrderComments)
