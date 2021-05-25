from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from src import views


urlpatterns = [
    path('', views.index_redirect, name='index'),
    path('safe/', views.safe, name='safe'),
    path('admin/', admin.site.urls),
    path('pizzas/v1/', include('pizza.urls')),
    path('users/v1/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
