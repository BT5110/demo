from django import forms
from django.db import connections
from django.core.cache import cache

DAY_IN_SEC = 24 * 60 * 60


def get_choices(col: str):
    # Try to get choices from cache
    col_choices_key = f'{col}-CHOICES'
    if col_choices_key in cache:
        return cache[col_choices_key]

    # If choices are not in cache, query db, set cache and then return
    with connections['default'].cursor() as cursor:
        cursor.execute(f'SELECT DISTINCT {col} FROM co2emission_reduced')
        choices = [('', '---------')]
        for row in cursor.fetchall():
            choices.append((row[0], row[0]))

    cache.set(col_choices_key, choices, timeout=DAY_IN_SEC)
    return choices


class ImoForm(forms.Form):
    imo = forms.IntegerField(label='IMO Number', min_value=1111111, max_value=9999999)
    ship_name = forms.CharField(max_length=64)
    ship_type = forms.ChoiceField(choices=get_choices('ship_type'), required=False)
    # my_decimal_field = forms.DecimalField(max_digits=6, min_value=0, required=False)
    # my_date_field = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)
