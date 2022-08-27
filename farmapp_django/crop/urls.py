from django.urls import path, include

from crop import views

urlpatterns = [
    path('crops/', views.CropsList.as_view()),
    path('crops/search/', views.search),
    path('crops/<slug:category_slug>/<slug:crop_slug>/', views.CropDetail.as_view()),
    path('crops/<slug:category_slug>/', views.CategoryDetail.as_view()),
]