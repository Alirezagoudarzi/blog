from django.urls import path
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',HomeView.as_view(),name='basic'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
