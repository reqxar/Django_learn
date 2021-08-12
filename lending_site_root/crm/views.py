from django.shortcuts import render
from .models import Order
from cms.models import CmsSlider
from prices.models import SubscribePrices, ServicePrices
from .forms import OrderForm
from telebot.models import botSettings
from telegram_bot import sendMessage
from django.views.generic import ListView, CreateView

class HomePage(ListView):
    model = (CmsSlider)
    template_name = 'index.html'
    context_object_name = 'slides'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub1'] = SubscribePrices.objects.get(pk=1)
        context['sub2'] = SubscribePrices.objects.get(pk=2)
        context['sub3'] = SubscribePrices.objects.get(pk=3)
        context['table_service'] = ServicePrices.objects.all()
        context['form'] = OrderForm

        return context


def thanks(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        Order.objects.create(order_name=name, order_phone=phone)
        try:
            settings = botSettings.objects.get(pk=1)
            token = str(settings.tg_token)
            chat = str(f'-{settings.tg_chat}')
            sendMessage(token=token, chat_id=chat, name=name, phone=phone)
        except Exception:
            print('Настройки бота не найдены, настройте бота в админ панели или укажите корректный id')
        finally:
            pass

        return render(request, 'thanks.html', {'name':name, 'phone': phone})
    else:
        return render(request, 'thanks.html')
