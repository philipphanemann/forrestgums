import sumatra.records
from sumatra.recordstore import django_store
import sumatra.web.views

from forrest.record import extend_django_record_with_gams_metadata


class RecordDetailView(sumatra.web.views.RecordDetailView):

    def get_object(self):
        record = super().get_object()
        return extend_django_record_with_gams_metadata(record)
