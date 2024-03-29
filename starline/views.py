from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
import requests  # Не удалять нужен для Telegram bot

from .forms import FeedbackForm, FeedbackFormCon
from .models import Contacts, Product, Feedback, Action, OurWork, Company, Sale, Characteristic, Category

#  Добавить токен tele_bot_token и chat_id пользователя, которому будут приходить сообщения (chat_id у @userinfobot)
#  Пользователь, которому будут приходить сообщения должен добавить себе своего бота.
# Telegram bot GLOBAL SETTINGS
tele_bot_token = '5259906909:AAGwzQMWTVFTVuQha9NPOROQjzVGxYCVfys'
chat_id = 821421337


def index(request):
    contacts = Contacts.objects.all()
    products = Product.objects.count()
    """Телеграм бот из формы для заявки"""
    phone_form = FeedbackForm()
    if request.method == 'POST':
        phone_form = FeedbackForm(request.POST)
        if phone_form.is_valid():
            updated_values = {'published': False}
            phone_number = phone_form.cleaned_data['phone']
            name = phone_form.cleaned_data['name']
            message = phone_form.cleaned_data['message']
            Feedback.objects.update_or_create(phone=phone_number, name=name, message=message, defaults=updated_values)
            requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'*Новая заявка:* {phone_number}\n*Имя:* {name}\n*Сообщение:* {message}',
                      'parse_mode': 'markdown'}).json()
            return render(request, template_name='starline/index.html')

    """Телеграм бот из формы для консультации"""
    phone_con = FeedbackFormCon()
    if request.method == 'POST':
        phone_con = FeedbackFormCon(request.POST)
        if phone_con.is_valid():
            updated_values = {'published': False}
            phone_number = phone_con.cleaned_data['phone_c']
            Feedback.objects.update_or_create(phone=phone_number, defaults=updated_values)
            requests.post(
                url=f'https://api.telegram.org/bot{tele_bot_token}/sendMessage',
                data={'chat_id': chat_id,
                      'text': f'* Нужна консультация:* {phone_number}',
                      'parse_mode': 'markdown'}).json()
            return render(request, template_name='starline/index.html')
    context = {
        'products': products,
        'contacts': contacts,
        'phone_form': phone_form,
        'phone_con': phone_con,
    }
    return render(request, 'starline/index.html', context=context)


class ContactsView(ListView):
    """Контакты и информация"""
    model = Contacts
    template_name = 'starline/contact.html'
    context_object_name = 'contacts'


class AboutCompanyView(ListView):
    """О компании"""
    model = Company
    template_name = 'starline/about_company.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context


class ActionView(ListView):
    """Вывод акций на экран"""
    model = Action
    template_name = 'starline/action.html'
    context_object_name = 'action'

    def get_queryset(self):
        return Action.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        context['sale'] = Sale.objects.filter(published=True)
        return context


def listourwork(request):
    """наши работы"""
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'starline/portfolio_all.html', context)


class DetailOurWorkView(DetailView):
    """Детализация портфолио"""
    model = OurWork
    template_name = 'starline/portfolio_card.html'
    context_object_name = 'ourwork'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.count()
        context['contacts'] = Contacts.objects.all()
        return context


def all_product(request):
    """Вывод продуктов на экран"""
    contacts = Contacts.objects.all()
    context = {'contacts': contacts}
    return render(request, 'starline/catalog.html', context)


class DetailProductView(DetailView):
    """Детализация продукта"""
    model = Product
    template_name = 'starline/product_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        context['products'] = Product.objects.count()
        return context


def not_page(request):
    contacts = Contacts.objects.all()
    return render(request, '404/404.html', {'contacts': contacts})


def error(request, exception):
    contacts = Contacts.objects.all()
    return render(request, '404/404.html', {'contacts': contacts}, status=404)
