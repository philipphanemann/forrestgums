# forrestgums

## User Guide

### Project Configuration

    $ smt init forrest --main trnsport.gms
    $ smt configure --add-plugin=forrest.executable
    $ smt configure --executable=gams
    $ smt configure -d .

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
