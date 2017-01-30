from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.homepage, name='HomePage'),
    url(r'^news/$', views.news, name="news"),
    url(r'^news/(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^rewiews/$', views.post_rewiew, name="rewiews"),
    url(r'^contacts/$', views.ContactsView.as_view(), name="contacts"),
    #views.contacts_view.as_view() for base template
    url(r'^categories/(?P<id>\d+)/$', views.category_page, name='CategoryPage'),
    url(r'^categories/$', views.CategoryView.as_view(), name='CategoryList'),
    url(r'^phone-send/$', views.phone_send, name='phone_send'),
    url(r'^categories/(?P<id>\d+)/(?P<category_slug>[-\w]+)/$', views.product_page, name='ProductPage'),
]