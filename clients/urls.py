from django.urls import path
from . import views


urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
    path('new/', views.client_create, name='client_create'),
    path('<int:pk>/edit/', views.client_update, name='client_update'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('<int:client_pk>/transactions/', views.transaction_list, name='transaction_list'),
    path('<int:client_pk>/transactions/new/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
]