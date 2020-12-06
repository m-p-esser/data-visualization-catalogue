from django.urls import path
from dataviz_gallery import views

urlpatterns = [
    path("", views.plot_index, name="plot_index"),
    path("<str:pk>/", views.plot_detail, name="plot_detail"),
]