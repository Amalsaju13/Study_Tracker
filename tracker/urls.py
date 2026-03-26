from django.urls import path
from . import views

urlpatterns = [

    path('', views.calendar_view, name='calendar'),

    path('add/', views.add_study, name='add_study'),

    path('entry/<int:id>/', views.study_detail, name='detail'),

    path('entry/<int:id>/edit/', views.edit_study, name='edit'),

    path('entry/<int:id>/delete/', views.delete_study, name='delete'),

    path('image/<int:id>/delete/', views.delete_image, name='delete_image'),
    path("add-images/<int:id>/", views.add_images, name="add_images"),

    path('dashboard/', views.dashboard, name='dashboard'),

    # auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
