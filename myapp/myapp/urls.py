from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cal_simple/', include('cal_simple.urls')),
    path('admin/', admin.site.urls),
]
