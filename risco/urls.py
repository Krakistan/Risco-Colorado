from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from risco import views as pagweb_views
from .forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', pagweb_views.registro, name='registro'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),
    path('iniciar-sesion/', auth_views.LoginView.as_view(
        template_name='risco/iniciar_sesion.html',
        authentication_form=CustomAuthenticationForm,
        redirect_authenticated_user=True,
    ), name='iniciar_sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(next_page='iniciar_sesion'), name='cerrar_sesion'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)