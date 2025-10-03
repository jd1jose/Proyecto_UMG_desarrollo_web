from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('vacantes/', views.vacantes_list, name='vacantes'),
    path('vacantes/nueva/', views.vacante_create, name='vacante_create'),
    path('vacantes/<int:pk>/editar/', views.vacante_edit, name='vacante_edit'),
    path('vacantes/<int:pk>/eliminar/', views.vacante_delete, name='vacante_delete'),

    path('candidatos/', views.candidatos_list, name='candidatos'),
    path('candidatos/nuevo/', views.candidato_create, name='candidato_create'),
    path('candidatos/<int:pk>/editar/', views.candidato_edit, name='candidato_edit'),
    path('candidatos/<int:pk>/eliminar/', views.candidato_delete, name='candidato_delete'),

    path('informes/', views.informes_list, name='informe_riesgo'),
    path('informes/nuevo/', views.informe_create, name='informe_create'),

    path("usuarios/", views.usuarios_list, name="usuarios"),
    path("usuarios/nuevo/", views.usuario_create, name="usuario_create"),
    path("usuarios/<int:pk>/editar/", views.usuario_edit, name="usuario_edit"),
    path("usuarios/<int:pk>/toggle/", views.usuario_toggle, name="usuario_toggle"),


]
