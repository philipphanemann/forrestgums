# forrestgums

## User Guide

### Project Configuration

	1. create simulation folder
	2. create trnsport.gms file
	3. command line:
	$ git init
	$ git add .
	$ git commit -m 'initial commit'
    $ smt init forrest --main=trnsport.gms --labelgenerator=uuid --datapath=.
    $ smt configure --add-plugin=forrest.executable
    $ smt configure --add-plugin=forrest.datastore
    $ smt configure --executable=gams
    $ smt configure --on-changed=store-diff

Use the GAMSListingDataStore instead of the normal FileSystemDataStore. For that replace
``sumatra.datastore.filesystem.FileSystemDataStore`` with ``forrest.datastore.GAMSListingDataStore``
in the ``.smt/project``.

Disallow command line parameters by setting `allow_command_line_parameters`
in `.smt/project` to `false`.

### Run a simulation

    $ smt run lo=3

### Start the web server

Start forrestgums in a Sumatra project folder:

    $ forrest

## Developer Guide

### Installation

Best install forrest in editable mode:

    $ pip install -e .

### Run the test suite

Run the test suite with py.test:

    $ py.test
