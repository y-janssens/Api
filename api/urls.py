from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('', views.getRoutes, name="api"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('videos/', views.getVideos, name="videos"),
    path('videos/<str:pk>', views.getVideo, name="video"),
    path('video/add', views.addVideo, name="add_video"),
    path('categories/', views.getCategories, name="categories"),
    path('categories/<str:pk>', views.deleteCategory, name="delete_category"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)