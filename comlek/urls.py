"""comlek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from comlek  import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homeview, name="home"),
    url(r'^urunler/(?P<cattId>[\w-]+)/$', views.catView, name="products"),
    url(r'^urun/(?P<proId>[\w-]+)/$', views.proView, name="product"),
    url(r'^hakkimizda/', views.aboutview, name="aboutus"),
    url(r'^iletisim/', views.contactview, name="contact"),

    # url(r'^urun/(?P<productId>[\w-]+)/$', views.productView, name="product"),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


