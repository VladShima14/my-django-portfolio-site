from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .forms import EmailForm, ContactForm
from .models import Post, SliderItem, Rewiew, Topic, Category, HomeItem
# Create your views here.


def phone_send(request):
    
    from_email = settings.EMAIL_HOST_USER   
    to_email = [from_email , '11@gmail.com ']
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            ae = "{},\n {},\n {}\n".format(message, phone, subject)
            
            try:
                send_mail(subject, ae, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ContactForm()
    
    
def homepage(request):
    homes = HomeItem.objects.all()
    
    context = {
        'homes': homes,
    }
    return render(request, 'agro/base.html', context)


def email_post(request):
    form = EmailForm()
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render(request, 'agro/news.html', {'form': form})


def category_page(request, id, category_slug=None):

    topic = get_object_or_404(Topic, id=id)
    
    category = None
    categories = Category.objects.filter(topic=topic)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    context = {

        'topic': topic,
        'category': category,
        'categories': categories,
    }
    return render(request, 'agro/section.html', context)



def product_page(request,category_slug=None, id=None):

    topic = get_object_or_404(Topic, id=id)

    category = None
    categories = Category.objects.filter(topic=topic)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'agro/item.html', {
        'topic': topic,
        'categ': category,
        'categories': categories,
    })


def news(request):

    queryset = Post.objects.all()
    
    from_email = settings.EMAIL_HOST_USER   
    to_email = [from_email , '11@gmail.com ']

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            mess = "Подписка на новости"
            
            ae = "{},\n {},\n {},\n {}".format(name, phone, email, mess)
            
            try:
                send_mail(name, ae, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = EmailForm()

    context = {
            "forms": form,
            "object_list": queryset,
               }
    return render(request, 'agro/news.html', context)


def post_detail(request, id=None):

    instance = get_object_or_404(Post, id=id)
    

    context = {

        "title": instance.title,
        "instance": instance,
    }
    return  render(request, 'agro/post_detail.html', context)


def post_rewiew(request):
    rewiewitem = Rewiew.objects.all()
    

    context = {
        "rewitem": rewiewitem,
    }
    return  render(request, "agro/feedback.html", context)

    

# def contacts(request):
#     items = SliderItem.objects.all()
#     context = {
#         'items': items,
#     }
#     return render(request, "agro/contacts.html", context)


class ContactsView(TemplateView):
    template_name = "agro/contacts.html"

    # def get_context_data(self, **kwargs):
    #     context = super(ContactsView, self).get_context_data(**kwargs)
    #     context['items'] = SliderItem.objects.all()
    #     return context


class CategoryView(TemplateView):
    template_name = "agro/production.html"
