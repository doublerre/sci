from django.urls import path
# from centroinvestigacion import views, views_enfoque
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
    path('registrar', views.RegistrarView.as_view(), name='registrar'),


]
