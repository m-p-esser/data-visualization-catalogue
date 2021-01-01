# from django.shortcuts import render
# from django.views.generic import ListView, CreateView, UpdateView, View
# from django.views.generic import FormView, TemplateView
# from .models import Plot
# from .forms import PlotFilterForm
# from django.db.models import Q


# def plot_detail(request, pk):
#     plot = Plot.objects.get(pk=pk)
#     context = {"plot": plot}
#     return render(request, "plots/plot_detail.html", context)


# def dataviz_goals(request):
#     return render(request, 'dataviz_goals.html')


# class PlotListView(ListView):
#     template_name = "index/plot_overview.html"

#     def get_queryset(self, **kwargs):
#         queryset = Plot.objects.all()

#         numerical_query = self.request.GET.get("numerical")
#         categorical_query = self.request.GET.get("categorical")
#         shape_query = self.request.GET.getlist("shapes")
#         goal_query = self.request.GET.getlist("goals")
#         facet_query = self.request.GET.get("facetted")
#         group_query = self.request.GET.get("grouped")

#         if numerical_query != "" and numerical_query is not None:
#             queryset = queryset.filter(numerical__exact=str(numerical_query))

#         if categorical_query != "" and categorical_query is not None:
#             queryset = queryset.filter(categorical__exact=categorical_query)

#         if categorical_query != "" and categorical_query is not None:
#             queryset = queryset.filter(categorical__exact=categorical_query)

#         if facet_query:
#             queryset = queryset.filter(facetted__exact=True)

#         if group_query:
#             queryset = queryset.filter(grouped__exact=True)

#         if len(goal_query) > 0:
#             for goal in goal_query:
#                 if goal == "" or goal is None:
#                     continue

#                 col = "goals"
#                 key = goal
#                 filter_expr = col + "__" + key
#                 queryset = queryset.filter(**{filter_expr: True})

#         if len(shape_query) > 0:
#             for shape in shape_query:
#                 if shape == "" or goal is None:
#                     continue

#                 col = "shapes"
#                 key = shape
#                 filter_expr = col + "__" + key
#                 queryset = queryset.filter(**{filter_expr: True})

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super(PlotListView, self).get_context_data(**kwargs)
#         queryset = self.get_queryset()
#         context["form"] = PlotFilterForm
#         context["plots"] = queryset
#         return context


# class GoalListView(ListView):
#     template_name = "index/plot_overview.html"

#     def get_queryset(self, **kwargs):
#         queryset = Plot.objects.all()

#         goal_query = self.kwargs.get("goal")
#         col = "goals"
#         key = goal_query.capitalize()
#         filter_expr = col + "__" + key
#         queryset = queryset.filter(**{filter_expr: True})

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super(GoalListView, self).get_context_data(**kwargs)
#         queryset = self.get_queryset()
#         context["form"] = PlotFilterForm
#         context["plots"] = queryset
#         return context


# class ShapeListView(ListView):
#     template_name = "index/plot_overview.html"

#     def get_queryset(self, **kwargs):
#         queryset = Plot.objects.all()

#         shape_query = self.kwargs.get("shape")
#         col = "shapes"
#         key = shape_query.capitalize()
#         filter_expr = col + "__" + key
#         queryset = queryset.filter(**{filter_expr: True})

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super(ShapeListView, self).get_context_data(**kwargs)
#         queryset = self.get_queryset()
#         context["form"] = PlotFilterForm
#         context["plots"] = queryset
#         return context


# class SearchListView(ListView):
#     template_name = "index/plot_overview.html"

#     def get_queryset(self, **kwargs):
#         queryset = Plot.objects.all()

#         search_query = self.kwargs.get("q")
#         queryset = Plot.objects.filter(
#             Q(parent_name__icontains=search_query)
#             | Q(variation_name__icontains=search_query)
#         )

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super(SearchListView, self).get_context_data(**kwargs)
#         queryset = self.get_queryset()
#         context["form"] = PlotFilterForm
#         context["plots"] = queryset
#         return context
