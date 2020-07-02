from django.contrib import admin
from django.urls import path
from core import views as core_views
from portafolio import views as portafolio_views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.Home, name='home'),
    path('about/', core_views.about, name='about'),
    path('contact/', core_views.contact, name='contacto'),
    path('portafolio/', portafolio_views.portfolio, name='portafolio'),
]


from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)