import sumatra.records
from sumatra.recordstore import django_store
import sumatra.web.views

from forrest.record import extend_sumatra_record_with_gams_metadata


class RecordDetailView(sumatra.web.views.RecordDetailView):

    def get_object(self):
        label = sumatra.web.views.unescape(self.kwargs["label"])
        return extend_sumatra_record_with_gams_metadata(
            django_store.models.Record.objects.get(label=label, project__id=self.kwargs["project"])
        )
