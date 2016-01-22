from unittest.mock import Mock
from pathlib import Path
from collections import namedtuple

from sumatra.programs import Executable
from sumatra.versioncontrol import Repository
from sumatra.launch import LaunchMode
from sumatra.datastore import DataStore
from sumatra.records import Record
import pytest

from forrest.record import extend_sumatra_record_with_gams_metadata


Listing = namedtuple('Listing', ['path_to_file', 'solver'])


LISTING_PATH = Path(__file__).parent / 'resources'
GUROBI_LISTING = Listing(LISTING_PATH / 'run_gurobi.lst', 'gurobi')
CPLEX_LISTING = Listing(LISTING_PATH / 'run_cplex.lst', 'cplex')
BARON_LISTING = Listing(LISTING_PATH / 'run_baron.lst', 'baron')
CONOPT_LISTING = Listing(LISTING_PATH / 'run_conopt.lst', 'conopt')
XPRESS_LISTING = Listing(LISTING_PATH / 'run_xpress.lst', 'xpress')


@pytest.fixture(params=[GUROBI_LISTING, CPLEX_LISTING, BARON_LISTING, CONOPT_LISTING, XPRESS_LISTING])
def listing_and_sumatra_record(request):
    listing = request.param
    record = Record(
        Mock(spec_set=Executable),
        Mock(spec_set=Repository),
        "trnsport.gms",
        999,
        Mock(spec_set=LaunchMode),
        Mock(spec_set=DataStore),
        stdout_stderr=listing.path_to_file.read_text()
    )
    return listing, record


def test_detects_solver(listing_and_sumatra_record):
    listing = listing_and_sumatra_record[0]
    sumatra_record = listing_and_sumatra_record[1]
    gams_record = extend_sumatra_record_with_gams_metadata(sumatra_record)
    assert gams_record.solver.lower() == listing.solver
