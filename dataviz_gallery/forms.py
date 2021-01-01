# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Div, HTML
# from crispy_forms.bootstrap import (
#     FormActions,
#     InlineRadios,
#     InlineCheckboxes,
#     Accordion,
#     AccordionGroup,
#     Container
# )
# from django.utils.safestring import mark_safe
# from .models import Plot


# class PlotFilterForm(forms.Form):

#     numerical = forms.IntegerField(
#         label=mark_safe("<strong>Numerical variables</strong>"),
#         min_value=0,
#         max_value=10,
#         required=False,
#         help_text="Enter number between 0 and 10",
#     )
#     categorical = forms.IntegerField(
#         label=mark_safe("<strong>Categorical variables</strong>"),
#         min_value=0,
#         max_value=10,
#         required=False,
#         help_text="Enter number between 0 and 10",
#     )
#     dimensionality = forms.MultipleChoiceField(
#         label=mark_safe("<strong>Number of dimensions</strong>"),
#         choices=[
#             (str(o), str(o))
#             for o in sorted(
#                 list(
#                     Plot.objects.order_by()
#                     .values_list("dimensionality", flat=True)
#                     .distinct()
#                 )
#             )
#         ],
#         widget=forms.RadioSelect(),
#         required=False,
#     )
#     goals = forms.MultipleChoiceField(
#         label=mark_safe("<strong>Visualization goals</strong>"),
#         choices=[
#             (str(o), str(o))
#             for o in list(Plot.objects.first().goals.keys())
#             if str(o) != ""
#         ],
#         widget=forms.CheckboxSelectMultiple(),
#         required=False
#     )
#     facetted = forms.BooleanField(label="Facetted Plot", required=False)
#     grouped = forms.BooleanField(label="Grouped Plot", required=False)

#     shapes = forms.MultipleChoiceField(
#         label=mark_safe("<strong>Shapes</strong>"),
#         choices=[
#             (str(o), str(o))
#             for o in list(Plot.objects.first().shapes.keys())
#             if str(o) != ""
#         ],
#         widget=forms.CheckboxSelectMultiple(),
#         required=False
#     )

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = "get"
#         self.helper.layout = Layout(
#             Accordion(
#                 Div(
#                     AccordionGroup(
#                         mark_safe(
#                             """
#                             <p class="text-info">
#                                 <span style="font-size: 2em">
#                                     <i class="fas fa-filter"></i>
#                                 </span>
#                                 Filter Menu
#                             </p>
#                             """
#                         ),
#                         Row(
#                             InlineCheckboxes("goals"), css_class="form-group col-md-10 pb-3 mb-0"
#                         ),
#                         Div(
#                             HTML("<p><b>Grouping</b></p>")
#                         ),
#                         Row(
#                             Column("facetted", css_class="form-group col-md-3 mb-0"),
#                             Column("grouped", css_class="form-group col-md-3 mb-0"),
#                             css_class="form-row pb-3",
#                         ),
#                         Row(
#                             Column("numerical", css_class="form-group col-md-4 mb-0"),
#                             Column("categorical", css_class="form-group col-md-4 mb-0"),
#                             css_class="form-row pb-3",
#                         ),
#                         Row(
#                             InlineCheckboxes("shapes"), css_class="form-group col-md-10 pb-3 mb-0"
#                         ),
#                         FormActions(
#                             Submit("submit", "Apply filter", css_class="btn btn-info"), Reset("reset", "Reset filter")
#                         ),
#                     ), css_class="text-secondary"
#                 )
#             )
#         )
