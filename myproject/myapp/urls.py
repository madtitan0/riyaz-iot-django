# myapp/urls.py
from django.urls import include, path

from myapp import admin
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.emg_data_view, name='emg_data'),
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Add this line
]


