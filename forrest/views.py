import sumatra.records
import sumatra.web.views
from django.http import HttpResponse
from sumatra import commands

from forrest.record import extend_django_record_with_gams_metadata


class RecordDetailView(sumatra.web.views.RecordDetailView):

    def get_object(self):
        record = super().get_object()
        return extend_django_record_with_gams_metadata(record)


def run(request):
    """Running a default simulation with Sumatra.

    This will call ``smt run lo=3``.
    """
    print("Running a simulation. Now.")
    commands.run(["lo=3"])
    return HttpResponse('OK')
