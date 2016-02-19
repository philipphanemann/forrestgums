from unittest.mock import Mock
from pathlib import Path
from collections import namedtuple

from sumatra.datastore import DataStore
from sumatra.records import Record
import pytest

from forrest.record import extend_django_record_with_gams_metadata


Listing = namedtuple('Listing', ['path_to_file', 'solver', 'solver_version'])


LISTING_PATH = Path(__file__).parent / 'resources'
GUROBI_LISTING = Listing(LISTING_PATH / 'run_gurobi.lst', 'gurobi', '6.0.5')
CPLEX_LISTING = Listing(LISTING_PATH / 'run_cplex.lst', 'cplex', '12.6.2.0')
BARON_LISTING = Listing(LISTING_PATH / 'run_baron.lst', 'baron', '15.9.22')
CONOPT_LISTING = Listing(LISTING_PATH / 'run_conopt.lst', 'conopt', '3.17A')
XPRESS_LISTING = Listing(LISTING_PATH / 'run_xpress.lst', 'xpress', '28.01.05')


@pytest.fixture(params=[GUROBI_LISTING, CPLEX_LISTING, BARON_LISTING, CONOPT_LISTING, XPRESS_LISTING])
def listing_and_sumatra_record(request):
    listing = request.param
    output_data = Mock()
    output_data.content = listing.path_to_file.read_text().encode('utf-8')
    datastore = Mock(spec_set=DataStore)
    datastore.get_data_item.return_value = output_data
    record = Mock(spec=Record)
    record.datastore = datastore
    record.output_data = ['something']
    record.to_sumatra = Mock()
    record.to_sumatra.return_value = record
    return listing, record


def test_detects_solver(listing_and_sumatra_record):
    listing = listing_and_sumatra_record[0]
    sumatra_record = listing_and_sumatra_record[1]
    gams_record = extend_django_record_with_gams_metadata(sumatra_record)
    assert gams_record.solver.lower() == listing.solver


def test_detects_solver_version(listing_and_sumatra_record):
    listing = listing_and_sumatra_record[0]
    sumatra_record = listing_and_sumatra_record[1]
    gams_record = extend_django_record_with_gams_metadata(sumatra_record)
    assert gams_record.solver_version == listing.solver_version
