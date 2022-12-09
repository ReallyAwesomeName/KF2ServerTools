#
# KF2ServerTools.py
# Main driver code
#
# Author: Rin | Discord: Rin#0304
# https://github.com/ReallyAwesomeName/KF2ServerTools
#
# =========================================================================== #
#                                                                             #
#   KF2ServerTools - Tools for managing a Dedicated Killing Floor 2 Server    #
#   Copyright (C) 2022  Rin                                                   #
#                                                                             #
#   This file is a part of KF2ServerTools                                     #
#                                                                             #
#   KF2ServerTools is free software: you can redistribute it and/or modify    #
#   it under the terms of the GNU General Public License as published by      #
#   the Free Software Foundation, either version 3 of the License, or         #
#   (at your option) any later version.                                       #
#                                                                             #
#   KF2ServerTools is distributed in the hope that it will be useful,         #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU General Public License for more details.                              #
#                                                                             #
#   You should have received a copy of the GNU General Public License         #
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.    #
#                                                                             #
# =========================================================================== #


from maplist import MapList
import argparse
import logging
from logging.handlers import RotatingFileHandler


# TODO: ADD LOGGING AND BACKUPS


def map_update_driver():
    """Driver
    Find the maps that were added and perform necessary edits to
    PCServer-KFEngine.ini, PCServer-KFGame.ini and ServerInfo.md
    """
    Server_Maps = MapList()
    Server_Maps.build_cur_map_list()
    Server_Maps.find_new_maps()
    Server_Maps.update_workshop_map_list()
    Server_Maps.update_kfengine(Server_Maps)
    Server_Maps.update_kfgame(Server_Maps)
    Server_Maps.update_server_info(Server_Maps)
    Server_Maps.update_map_db(Server_Maps)
    Server_Maps.push_server_info()

    return


def cmd_helper_driver():
    pass


def dmg_driver():
    pass


def gui_driver():
    pass


# CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # select action (plan to add more)
    subparsers = parser.add_subparsers(
        help="Desired action",
        dest="action",
    )

    # action: mapupdate
    newmap_parser = subparsers.add_parser(
        "mapupdate",
        help="Update server maps",
    )

    # action: cmd
    cmd_parser = subparsers.add_parser(
        "cmd",
        help="Find and use commands",
    )

    dmg_parser = subparsers.add_parser(
        "dmg",
        help="Calculate weapon damage and breakpoints",
    )

    # action: gui
    gui_parser = subparsers.add_parser(
        "gui",
        help="Open the GUI",
    )

    args = parser.parse_args()

    try:
        if args.action == "mapupdate":
            map_update_driver()
        if args.action == "cmd":
            cmd_helper_driver()
        if args.action == "dmg":
            dmg_driver()
        if args.action == "gui":
            gui_driver()

    except AttributeError:
        raise AttributeError
