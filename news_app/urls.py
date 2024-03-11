from django.urls import path
from .views import news_list, news_detail ,HomePageView, ContactPageView, Page404

urlpatterns = [
    path('', HomePageView, name="home_page"),
    path('news/', news_list, name="all_news_list"),
    path('news/<int:id>/', news_detail, name="news_detail_page"),
    path('contact-us/', ContactPageView.as_view(), name="contact_page"),
    path('404/', Page404, name="404-page"),
]