from django.urls import path
from django.contrib import admin

import app.views

admin.autodiscover()


urlpatterns = [
    path('', app.views.index, name='index'),
    path('db/', app.views.db, name='db'),
    path('emissions/', app.views.emissions, name='emissions'),
    path('emissions/<int:page>', app.views.emissions, name='emissions'),
    path('emissions/imo/', app.views.emission_detail, name='emission_detail'),
    path('emissions/imo/<int:imo>', app.views.emission_detail, name='emission_detail'),
    path('aggregation/', app.views.aggregation, name='aggregation'),
    path('visual/', app.views.visual, name='visual'),
    path('admin/', admin.site.urls),
]
