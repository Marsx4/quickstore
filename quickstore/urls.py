
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('login/', LoginView.as_view(template_name='login.htm'),name='site_login'),
    path('logout/', LogoutView.as_view(template_name='logout.htm'),name='site_logout'),
    path('register/', register,name='site_register'),

]
