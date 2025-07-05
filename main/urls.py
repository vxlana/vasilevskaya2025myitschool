from django.urls import path
from . import views, api

app_name = "main"

urlpatterns = [
    path("", views.product_index, name="product_list"),
    path("api/clothing/", api.ClothingItemListApiView.as_view(), name='api_clothing'),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),

# ======================== для бота ========================================
    path("api/categories/", views.category_list_api, name='api_categories'),
    path("api/clothing/category/<int:category_id>/", views.clothing_items_by_category_api, name='api_clothing_by_category'),

]


