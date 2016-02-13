import sumatra.records
import sumatra.web.views
from django.http import HttpResponse
from sumatra import commands

from forrest.record import extend_django_record_with_gams_metadata


class RecordDetailView(sumatra.web.views.RecordDetailView):
    """A class to add metadata from GAMS result file to record."""

    def get_object(self):
        record = super().get_object()
        return extend_django_record_with_gams_metadata(record)


class DataDetailView(sumatra.web.views.DataDetailView):
    """A class to add mimetype to GAMS result files ('*.lst')."""

    def get_object(self):
        datakey = super().get_object()
        if datakey.path.endswith('.lst'):
            datakey.metadata = datakey.metadata.replace('"mimetype": null', '"mimetype": "text/plain"')
        return datakey


class SettingsView(sumatra.web.views.SettingsView):
    """Fixes the columns of the RecordListView to be viewed."""

    def load_settings(self):
        settings = super().load_settings()
        settings['hidden_cols'] = [2, 3, 4, 7, 11]
        return settings


def run(request):
    """Running a default simulation with Sumatra.

    This will call ``smt run lo=3``.
    """
    print("Running a simulation. Now.")
    commands.run(["lo=3"])
    return HttpResponse('OK')
