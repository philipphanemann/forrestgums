from unittest.mock import Mock

from sumatra.programs import Executable
from sumatra.versioncontrol import Repository
from sumatra.launch import LaunchMode
from sumatra.datastore import DataStore
from sumatra.records import Record
import pytest

from forrest.record import extend_sumatra_record_with_gams_metadata


@pytest.fixture
def sumatra_record():
    return Record(
        Mock(spec_set=Executable),
        Mock(spec_set=Repository),
        "trnsport.gms",
        999,
        Mock(spec_set=LaunchMode),
        Mock(spec_set=DataStore)
    )


def test_gams_metadata_is_added(sumatra_record):
    gams_record = extend_sumatra_record_with_gams_metadata(sumatra_record)
    assert hasattr(gams_record, 'gams')
