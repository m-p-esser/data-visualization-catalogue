from django.urls import path
from dataviz_gallery import views

urlpatterns = [
    path("plot/<str:pk>", views.plot_detail, name="plot_detail"),
    path("goal/<goal>", views.GoalListView.as_view(), name="plot_goal"),
    path("shape/<shape>", views.ShapeListView.as_view(), name="plot_shape"),
    path("search/<q>", views.SearchListView.as_view(), name="plot_search"),
    path("goals", views.dataviz_goals, name="dataviz_goals"),
    path("", views.PlotListView.as_view(), name="plot_list_view")
]