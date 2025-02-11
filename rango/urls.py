from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rango import views
from django.urls import path, re_path

app_name = 'rango'  
LOGIN_URL = 'rango:login'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    re_path(r'^category/(?P<category_name_slug>[\w-]+)/add_page/$', views.add_page, name='add_page'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
