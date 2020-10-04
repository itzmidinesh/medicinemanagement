"""medicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from expiry import views

urlpatterns = [
	path('', views.index_view, name="home"),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('medicine_list/', views.medicine_list, name="medicine_list"),
    path('my_medicine', views.my_medicine, name="my_medicine"),
    path('medicine_new', views.medicine_new, name="medicine_new"),
    path('<int:pk>/update', views.MedicineUpdateView.as_view(), name='medicine_update'),
    path('<int:pk>/delete', views.MedicineDeleteView.as_view(), name='medicine_delete'),
    path('admin/', admin.site.urls),
    path('profile/<slug:username>/', views.get_user_profile, name="user_profile"),
    
]