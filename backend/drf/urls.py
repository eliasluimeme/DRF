from django.urls import path, re_path
from django.contrib import admin
from core import views as core_views
from auth2 import views
from rest_framework import routers


# router = routers.DefaultRouter()

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', core_views.ContactAPIView.as_view()),
    path('signup/', views.signup),
    re_path('signin/', views.signin),
    re_path('test_token/', views.test_token),
]