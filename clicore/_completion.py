# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

ARGCOMPLETE_ENV_NAME = '_ARGCOMPLETE'


class CLICompletion(object):

    def __init__(self, ctx=None):
        self.ctx = ctx
        self.ctx.cli_data['completer_active'] = ARGCOMPLETE_ENV_NAME in os.environ

    def get_completion_args(self, is_completion=False, comp_line=None):  # pylint: disable=no-self-use
        """ Get the args that will be used to tab completion if completion is active. """
        is_completion = is_completion or os.environ.get(ARGCOMPLETE_ENV_NAME)
        comp_line = comp_line or os.environ.get('COMP_LINE')
        # The first item is the exe name so ignore that.
        return comp_line.split()[1:] if is_completion and comp_line else None