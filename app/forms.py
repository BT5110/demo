from django import forms
from django.db import connections
from django.core.cache import cache

DAY_IN_SEC = 24 * 60 * 60
START_YEAR, END_YEAR = 2010, 2030


def get_choices(col: str):
    # Try to get choices from cache
    col_choices_key = f'{col}-CHOICES'
    if col_choices_key in cache:
        return cache[col_choices_key]

    # If choices are not in cache, query db, set cache and then return
    with connections['default'].cursor() as cursor:
        cursor.execute(f'SELECT DISTINCT {col} FROM co2emission')
        choices = [('', '---------')]
        for row in cursor.fetchall():
            choices.append((row[0], row[0]))

    cache.set(col_choices_key, choices, timeout=DAY_IN_SEC)
    return choices


class ImoForm(forms.Form):
    imo = forms.IntegerField(label='IMO Number', min_value=1111111, max_value=9999999)
    ship_name = forms.CharField(max_length=64)
    ship_type = forms.ChoiceField(choices=get_choices('ship_type'))
    reporting_year = forms.IntegerField(min_value=START_YEAR, max_value=END_YEAR)
    technical_efficiency_type = forms.ChoiceField(choices=get_choices('technical_efficiency_type'))
    technical_efficiency_number = forms.DecimalField(max_digits=5, min_value=0, required=False)
    port_of_registry = forms.CharField(max_length=64, required=False)
    home_port = forms.CharField(max_length=64, required=False)
    ice_class = forms.ChoiceField(choices=get_choices('ice_class'), required=False)
    doc_issue_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    doc_expiry_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
    co2_emissions_m_tonnes = forms.DecimalField(max_digits=8, min_value=0, required=False)
    annual_hours_at_sea = forms.DecimalField(max_digits=6, min_value=0, required=False)
    fuel_consumption_m_tonnes = forms.DecimalField(max_digits=8, min_value=0, required=False)
    fuel_consumption_per_dist = forms.DecimalField(max_digits=6, required=False, min_value=0)
    fuel_consumption_per_transport_work = forms.DecimalField(max_digits=6, required=False, min_value=0)
    co2_emissions_per_dist = forms.DecimalField(max_digits=6, required=False, min_value=0)
    co2_emissions_per_transport_work_mass = forms.DecimalField(max_digits=6, required=False, min_value=0)
    co2_emissions_per_transport_work_pax = forms.DecimalField(max_digits=6, required=False, min_value=0)
    co2_emissions_per_transport_work_freight = forms.DecimalField(max_digits=6, required=False, min_value=0)
