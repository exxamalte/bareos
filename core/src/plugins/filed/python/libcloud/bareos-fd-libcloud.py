#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2020-2020 Bareos GmbH & Co. KG
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of version three of the GNU Affero General Public
# License as published by the Free Software Foundation, which is
# listed in the file LICENSE.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# Original Author: Alexandre Bruyelles <git@jack.fr.eu.org>


# This module contains the wrapper functions called by the Bareos-FD, the
# functions call the corresponding methods from your plugin class
import BareosFdWrapper

# from BareosFdWrapper import parse_plugin_definition, handle_plugin_event, start_backup_file, end_backup_file, start_restore_file, end_restore_file, restore_object_data, plugin_io, create_file, check_file, handle_backup_file  # noqa
from BareosFdWrapper import *  # noqa

# This module contains the used plugin class
import BareosFdPluginLibcloud

from bareosfd import bRC_OK


def load_bareos_plugin(plugindef):
    """
    This function is called by the Bareos-FD to load the plugin
    We use it to instantiate the plugin class
    """
    # BareosFdWrapper.bareos_fd_plugin_object is the module attribute that
    # holds the plugin class object
    BareosFdWrapper.bareos_fd_plugin_object = (
        BareosFdPluginLibcloud.BareosFdPluginLibcloud(plugindef)
    )
    return bRC_OK


# the rest is done in the Plugin module
