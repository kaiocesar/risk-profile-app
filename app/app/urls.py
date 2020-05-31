from django.contrib import admin
from django.urls import path
from risk_profile.views import RiskProfileViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'risk/create/',
        RiskProfileViewSet.as_view(
            {'post': 'create'}), name='create'),
]
