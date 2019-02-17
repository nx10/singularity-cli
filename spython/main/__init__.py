
# Copyright (C) 2017-2019 Vanessa Sochat.

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.


def get_client(quiet=False, debug=False):
    '''
       get the client and perform imports not on init, in case there are any
       initialization or import errors. 

       Parameters
       ==========
       quiet: if True, suppress most output about the client
       debug: turn on debugging mode

    '''
    from .base import Client

    Client.quiet = quiet
    Client.debug = debug

    # Do imports here, can be customized
    from .apps import apps
    from .build import build
    from .execute import execute 
    from .help import help
    from .inspect import inspect
    from .instances import ( instances, stopall ) # global instance commands
    from .run import run
    from .pull import pull

    # Actions
    Client.apps = apps
    Client.build = build
    Client.execute = execute
    Client.help = help
    Client.inspect = inspect
    Client.instances = instances
    Client.run = run
    Client.pull = pull

    # Command Groups, Images
    from spython.image.cmd import generate_image_commands  # deprecated
    Client.image = generate_image_commands()

    # Commands Groups, Instances
    from spython.instance.cmd import generate_instance_commands  # instance level commands
    Client.instance = generate_instance_commands()
    Client.instance_stopall = stopall

    # Initialize
    cli = Client()

    # Pass on verbosity
    cli.image.debug = cli.debug
    cli.image.quiet = cli.quiet
    cli.instance.debug = cli.debug
    cli.instance.quiet = cli.quiet

    return cli

Client = get_client()
