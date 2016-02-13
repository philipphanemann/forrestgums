#!/usr/bin/env python
"""
Web interface to Forrest.
"""
# TODO try to hook into Sumatra smtweb

import sys
import os
try:
    import thread
except ImportError: # Python 3. TODO: move to higher level ``threading`` module
    import _thread as thread
import webbrowser
from django.core import management
from sumatra.projects import load_project
from sumatra.recordstore.django_store import DjangoRecordStore, db_config
from sumatra.web import __file__ as sumatra_web
from argparse import ArgumentParser
from textwrap import dedent
import time


def delayed_new_tab(url, delay):
    """
    Open a new browser tab with a time delay, to give the server enough
    time to start up.
    """

    time.sleep(delay)
    # maybe optional with python setup develop ?
    webbrowser.open_new_tab(url)


def start_web_server(arguments=None):
    """Launch the Forrest web interface"""
    description = dedent("""\
        Launch the Forrest web interface. There must be a Sumatra
        project in the working directory and the record store for that project
        will be used.""")
    parser = ArgumentParser(description=description)
    parser.add_argument('-a', '--allips', default=False, action="store_true",
                        help="run server on all IPs, not just localhost")
    parser.add_argument('-p', '--port', default="8000",
                        help="run server on this port number")
    parser.add_argument('-n', '--no-browser', default=False, action="store_true",
                        help="do not open browser")
    parser.add_argument('-r', '--read_only', default=False, action="store_true",
                        help="set read-only mode")
    args = parser.parse_args(arguments)

    project = load_project()
    if not isinstance(project.record_store, DjangoRecordStore):
        # should make the web interface independent of the record store, if possible
        print("This project cannot be accessed using the web interface (record store is not of type DjangoRecordStore).")
        sys.exit(1)
    del project

    smt_root_dir = os.path.dirname(sumatra_web)
    db_config.update_settings(
        INSTALLED_APPS=db_config._settings["INSTALLED_APPS"] + ['forrest'] + ['sumatra.web'],
        ROOT_URLCONF='forrest.urls',
        STATIC_URL='/static/',
        TEMPLATE_DIRS=(os.path.join(os.getcwd(), ".smt", "templates"),
                       os.path.join(os.path.dirname(__file__), "templates"),
                       os.path.join(smt_root_dir, "templates"),),
        MIDDLEWARE_CLASSES=tuple(),
        READ_ONLY=args.read_only
    )

    db_config.configure()

    if not args.no_browser:
        thread.start_new_thread(delayed_new_tab, ("http://127.0.0.1:%s" % args.port, 3))

    if args.allips:
        address = '0.0.0.0'
    else:
        address = '127.0.0.1'
    address += ':' + args.port
    management.call_command('runserver', address, use_reloader=False)
