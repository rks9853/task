
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('credit', views.credit, name = 'credit'),
    path('debit', views.debit, name = 'debit'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout_page    , name = 'logout'),
    path('delete/<int:pk>/', views.delete   , name = 'delete'),

    

]