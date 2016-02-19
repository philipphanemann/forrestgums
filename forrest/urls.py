"""
Define URL dispatching for the Forrest web interface.
"""
# TODO should reuse url patterns from sumatra
from __future__ import unicode_literals

from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from sumatra.projects import Project
from sumatra.records import Record
from sumatra.web.views import (ProjectListView, ProjectDetailView,
                               DataListView, DiffView, ImageListView)
from forrest.views import RecordDetailView, DataDetailView, SettingsView, RecordListView

P = {
    'project': Project.valid_name_pattern,
    'label': Record.valid_name_pattern,
}

urlpatterns = patterns('',
                       (r'^$', ProjectListView.as_view()),
                       (r'^run/$', 'forrest.views.run'),
                       (r'^settings/$', SettingsView.as_view()),
                       (r'^%(project)s/$' % P, RecordListView.as_view()),
                       (r'^%(project)s/about/$' % P, ProjectDetailView.as_view()),
                       (r'^%(project)s/data/$' % P, DataListView.as_view()),
                       (r'^%(project)s/image/$' % P, ImageListView.as_view()),
                       (r'^%(project)s/image/thumbgrid$' % P, 'sumatra.web.views.image_thumbgrid'),
                       (r'^%(project)s/parameter$' % P, 'sumatra.web.views.parameter_list'),
                       (r'^%(project)s/delete/$' % P, 'sumatra.web.views.delete_records'),
                       (r'^%(project)s/compare/$' % P, 'sumatra.web.views.compare_records'),
                       (r'^%(project)s/%(label)s/$' % P, RecordDetailView.as_view()),
                       (r'^%(project)s/%(label)s/diff$' % P, DiffView.as_view()),
                       (r'^%(project)s/%(label)s/diff/(?P<package>[\w_]+)*$' % P, DiffView.as_view()),
                       (r'^%(project)s/%(label)s/script$' % P, 'sumatra.web.views.show_script'),
                       (r'^%(project)s/data/datafile$' % P, DataDetailView.as_view()),
                       (r'^data/(?P<datastore_id>\d+)$', 'sumatra.web.views.show_content'),
                       )

urlpatterns += staticfiles_urlpatterns()
