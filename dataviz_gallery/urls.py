from django.urls import path
from dataviz_gallery import views

urlpatterns = [
    # path("", views.plot_overview, name="plot_overview"),
    path("<str:pk>/", views.plot_detail, name="plot_detail"),
    path("", views.PlotListView.as_view(), name="plot_list_view")
]