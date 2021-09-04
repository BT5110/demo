from django.urls import path, include
from django.contrib import admin

import app.views

admin.autodiscover()


urlpatterns = [
    path('', app.views.index, name='index'),
    path('db/', app.views.db, name='db'),
    path('tpc-c/', app.views.tpc_c, name='tpc-c'),
    path('project/', app.views.project, name='project'),
    path('admin/', admin.site.urls),
]
