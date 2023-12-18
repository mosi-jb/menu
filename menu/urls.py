"""
URL configuration for menu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('admin/user/',
         include(('user.urls.admin', 'menu.user'), namespace='users-admin')),
    path('admin/media/',
         include(('media.urls.admin', 'menu.media'), namespace='media-admin')),
    path('admin/product/',
         include(('product.urls.admin', 'menu.product'), namespace='product-admin')),
    path('admin/siteSetting/',
         include(('siteSetting.urls.admin', 'menu.siteSetting'), namespace='siteSetting-admin')),
]

front_urls = [
    path('front/media/',
         include(('media.urls.front', 'menu.media'), namespace='media-front')),
    path('front/product/',
         include(('product.urls.front', 'menu.product'), namespace='product-front')),
    path('front/siteSetting/',
         include(('siteSetting.urls.front', 'menu.siteSetting'), namespace='siteSetting-front'))
]

doc_patterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
                  path('akm/', admin.site.urls),
              ] + doc_patterns + admin_urls + front_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
