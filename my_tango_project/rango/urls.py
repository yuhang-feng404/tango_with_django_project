from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from django.urls import path
from rango import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.AddPageView.as_view(), name='add_page')path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
from django.urls import path
from rango import views

urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
]
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]path('restricted/', views.restricted, name='restricted'),
path('clear_session/', views.clear_session, name='clear_session'),
,