"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf.urls.static import static
from home import views
from order import views as Orderviews
from user import views as UserViews

urlpatterns = [
	path('',include('home.urls')),
	path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),
    path('search/',views.search, name='search'),
    path('admin/', admin.site.urls),
    path('search_auto/', views.search_auto, name='search_auto'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('order/', include('order.urls')),
    path('shopcart/', Orderviews.shopcart, name='shopcart'),
    path('login/', UserViews.login_form, name='login_form'),
    path('signup/', UserViews.signup_form, name='signup_form'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('faq/', views.faq, name='faq'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),

    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)