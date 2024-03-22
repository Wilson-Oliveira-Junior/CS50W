from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("app/<str:feature>", views.app, name="app"),
    path("recipes/<int:recipe_id>", views.recipes, name="recipes"),
    path("new_item/", views.new_item, name="new_item"),
    path("new_ingredient/", views.new_ingredient, name="new_ingredient"),
    path("delete_ingredient/", views.delete_ingredient, name="delete_ingredient"),
    path("new_purchase/", views.new_purchase, name="new_purchase"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
