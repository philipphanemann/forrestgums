# forrestgums

## User Guide

### Project Configuration
	
	1. create simulation folder
	2. create trnsport.gms file
	3. command line: 
     $ forrest-init

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
