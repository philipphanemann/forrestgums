from pathlib import Path
from datetime import datetime

import pytest

from forrest.datastore import GAMSListingDataStore


def test_no_new_files(tmpdir):
    data_store = GAMSListingDataStore(root=str(tmpdir))
    assert len(data_store.find_new_data(datetime.now())) == 0


def test_detects_new_listings(tmpdir):
    data_store = GAMSListingDataStore(root=str(tmpdir))
    tmpdir.join('file1.lst').write("some results")
    tmpdir.join('file2.lst').write("some results")
    assert len(data_store.find_new_data(datetime.now())) == 2


def test_fails_with_file_not_being_a_listing(tmpdir):
    data_store = GAMSListingDataStore(root=str(tmpdir))
    tmpdir.join('file1.lst').write("some results")
    tmpdir.join('file2.gms').write("some more results")
    with pytest.raises(AssertionError):
        data_store.find_new_data(datetime.now())


def test_moves_file_after_being_found(tmpdir):
    data_store = GAMSListingDataStore(root=str(tmpdir))
    file = tmpdir.join('file.lst')
    file.write("some results")
    data_store.find_new_data(datetime.now())
    assert not file.exists()


def test_creates_sub_folder_for_listings(tmpdir):
    data_store = GAMSListingDataStore(root=str(tmpdir))
    tmpdir.join('file.lst').write("some results")
    data_store.find_new_data(datetime.now())
    assert (Path(str(tmpdir)) / GAMSListingDataStore.LST_SUB_FOLDER).exists()
