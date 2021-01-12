from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    # path(r'about/', views.about, name='about'),
    # path(r'view_image/', views.view_image, name='view_image'),
    # path(r'category/', views.category, name='category'),
    # path(r'^search_results/', views.search_results, name='search_results'),


    
    path('about/', views.about, name='about'),
    path('view_image/', views.view_image, name='view_image'),
    # path('category/', views.category, name='category'),
    path('search_results/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)