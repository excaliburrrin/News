from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from django.views.generic import TemplateView

from news_app.forms import ContactForm

from .models import News, Category
# from .forms import ContactForm
# from django.http import HttpResponse
# Create your views here.


def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list" : news_list
    }
    return render(request, "news/news_list.html")   

def news_detail(request, id):
    news = get_list_or_404(News,id=id, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)



def HomePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        "news": news,
        "category": categories
    }

    return render(request, "news/home.html",context)

# def ContactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#             form.save()
#             return HttpResponse("<h2> Thanks for contacting us")
#     context = {
#         "form": form
#     }


#     return render(request, "news/contact.html",context)

class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2> Thanks for contacting us")
        context = {
            "form": form
        }
        return render(request, "news/contact.html",context)


    # def get_context_data(self,request,*args, **kwargs):
    #     form = ContactForm()
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "news/contact.html",context)

    # def post(self, request, *args, **kwargs):
    #     form = ContactForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse("<h2> Thanks for contacting us")
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "news/contact.html",context)



def Page404(request):

   return render(request, "news/404.html")