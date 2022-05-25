from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainTemplateView.as_view(), name='main-view'),

    path('tasks/', include('tasks.urls')),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
