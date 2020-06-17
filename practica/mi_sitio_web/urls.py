"""mi_sitio_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from visitas_granada import views
from django.contrib import admin

from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import TemplateView # new
from rest_framework import routers
# from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'apivisitas', views.VisitaViewSet)
router.register(r'apicomentarios', views.ComentarioViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('', views.index, name='index'),
    path('<int:visita_id>/', views.detalle_visita, name='detail'),
    path('add_visita/', views.add_visita, name='add_visita'),
    path('post/ajax/visita/<int:visita_id>/', views.edit_visita, name='edit_visita'),
    path('delete/<int:visita_id>/', views.del_visita, name='del_visita'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    path('api-auth/', include('rest_framework.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns