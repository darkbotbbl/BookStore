"""BookStore URL configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # user authentication - django auth 
    path('accounts/', include('allauth.urls')),

    # local
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
]
