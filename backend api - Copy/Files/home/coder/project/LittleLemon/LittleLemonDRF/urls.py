from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path("", views.index, name="index"),
    path("menu/", views.MenuItemsView.as_view(), name="menu_list"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view(), name="menu_detail"),
    path("booking/", include(router.urls)),
]