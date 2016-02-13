import uuid
from pathlib import Path
import shutil

from sumatra.datastore.filesystem import FileSystemDataStore as SumatraFileSystemDataStore, DataFile
from sumatra.core import component


@component
class GAMSListingDataStore(SumatraFileSystemDataStore):
    """Data store for GAMS listings.

    The particularity with GAMS is that each output file will have the same name,
    namely the name of the input file with a *.lst suffix. GAMSListingDataStore
    aims at avoiding overwrites. For that it detects files from a GAMS run in the
    configured folder and moves them into a subfolder structure:
    ./gams-results/unique-folder-for-one-listing
    """

    LST_SUB_FOLDER = Path('gams-results')

    def find_new_data(self, timestamp):
        """Finds newly created/changed data items"""
        new_files_in_root = [Path(self.root) / path
                             for path in self._find_new_data_files(timestamp)]
        for new_file in new_files_in_root:
            assert new_file.suffix == '.lst'
        session_path = Path(self.root) / self.LST_SUB_FOLDER / str(uuid.uuid1())
        session_path.mkdir(parents=True)
        new_files_moved = [session_path / new_file.name for new_file in new_files_in_root]
        for src, dest in zip(new_files_in_root, new_files_moved):
            shutil.move(src.as_posix(), dest.as_posix())
        return [DataFile(path.as_posix(), self).generate_key() for path in new_files_moved]
