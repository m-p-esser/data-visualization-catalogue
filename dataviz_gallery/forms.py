from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
from crispy_forms.bootstrap import (
    FormActions,
    InlineRadios,
    InlineCheckboxes,
    Accordion,
    AccordionGroup
)
from django.utils.safestring import mark_safe
from .models import Plot


class PlotFilterForm(forms.Form):

    numerical = forms.IntegerField(
        label=mark_safe("<strong> Number of numerical variables</strong>"),
        min_value=0,
        max_value=10,
        required=False,
        help_text="Enter number between 0 and 10"
    )
    categorical = forms.IntegerField(
        label=mark_safe("<strong>Number of categorical variables</strong>"),
        min_value=0,
        max_value=10,
        required=False,
        help_text="Enter number between 0 and 10"
    )
    dimensionality = forms.MultipleChoiceField(
        label=mark_safe("<strong>Number of dimensions</strong>"),
        choices=[
            (str(o), str(o))
            for o in sorted(
                list(
                    Plot.objects.order_by()
                    .values_list("dimensionality", flat=True)
                    .distinct()
                )
            )
        ],
        widget=forms.RadioSelect(),
        required=False,
    )
    goals = forms.MultipleChoiceField(
        label=mark_safe("<strong>Visualization goals</strong>"),
        choices=[
            (str(o), str(o)) for o in list(Plot.objects.first().goals.keys()) if str(o) != ""],
        widget=forms.CheckboxSelectMultiple(),
    )
    facetted = forms.BooleanField(
        label="Facetted Plot",
        required=False)
    grouped = forms.BooleanField(
        label="Grouped Plot",
        required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup(
                    "Filter Menu",
                    # InlineRadios("dimensionality"),
                    # Row(
                    #     css_class="form-row pb-3"
                    # ),
                    InlineCheckboxes("goals"),
                    Row(css_class="form-row pb-5"),
                    Row(
                        Column("facetted", css_class="form-group col-md-6 mb-0"),
                        Column("grouped", css_class="form-group col-md-6 mb-0"),
                        css_class="form-row pb-3"
                    ),
                    Row(css_class="form-row pb-5"),
                    Row(
                        Column("numerical", css_class="form-group col-md-6 mb-0"),
                        Column("categorical", css_class="form-group col-md-6 mb-0"),
                        css_class="form-row pb-3"
                    ),
                    FormActions(Submit("submit", "Apply filter"), Reset("reset", "Reset filter")),
                )
            )
        )
