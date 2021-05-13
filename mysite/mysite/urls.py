"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Phải xử lý các url sau
# /admin
# /api
# /api/races
# /api/races/add
# /api/racers
# /api/racers/add
# /api/bets
# /api/bets/add

# Bài 1, tìm cách làm API cho race



urlpatterns = [

#    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('api/', include('api.urls')), # Kéo chú urls của api vào 
]
