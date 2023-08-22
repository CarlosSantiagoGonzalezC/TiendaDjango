"""
URL configuration for GestionNegocio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from appTienda import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('inicio/', views.inicio),
#     path('', views.inicio),
#     path('vistaAgregarProducto/', views.vistaAgregarProducto),
#     path('agregarProducto/', views.agregarProducto),
#     path('listarProductos/', views.listarProductos),
#     path('vistaAgregarCategoria/', views.vistaAgregarCategoria),
#     path('listarCategorias/', views.listarCategorias),
#     path('agregarCategoria/', views.agregarCategoria),
#     path('consultarProducto/<int:id>/', views.consultarProducto),
#     path('actualizarProducto/', views.actualizarProducto),
#     path('eliminarProducto/<int:id>/', views.eliminarProducto)
# ]

# if settings.DEBUG:
#     urlpatterns += static(
#         settings.MEDIA_URL,
#         document_root = settings.MEDIA_ROOT
#     )


from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appTienda.urls')),
]