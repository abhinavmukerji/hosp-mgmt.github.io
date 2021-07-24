from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hospital.urls')),
]

#by Abhinav Mukerji(EN18CS301006)