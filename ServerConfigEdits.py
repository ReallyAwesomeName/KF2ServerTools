# Fully automate KF2 server map update process
# https://github.com/ReallyAwesomeName/KF2ServerTools


import argparse
import os
from datetime import date
from shutil import copy
from MapList import MapList
import logging
from logging.handlers import RotatingFileHandler

# TODO: ADD LOGGING


def update_kfengine(maplist: MapList):
    """Make necessary edits to PCServer-KFEngine.ini"""
    # Need to:
    #   Add entry to [OnlineSubsystemSteamworks.KFWorkshopSteamworks]
    #   ServerSubscribedWorkshopItems=1208883070 // 1 KF-Corridor
    for new_map_index in range(len(maplist.new_maps)):
        map_id = getattr(maplist.new_maps[new_map_index], "workshop_id")
        map_name = getattr(maplist.new_maps[new_map_index], "map_name")
        map_steamworks_entry = f"ServerSubscribedWorkshopItems={map_id} // {map_name}"
        # TODO: copy file for backup then insert steamworks entry

    pass


def update_kfgame(maplist: MapList):
    """Make necessary edits to PCServer-KFGame.ini"""
    # Need to:
    #   Add [<mapname> KFMapSummary]
    #       MapName=<mapname>
    #   Add to Map Cycle
    # FIXME: MAKE THIS EDIT THE FILE
    # TODO: MAKE BACKUPS OF ALL EDITED FILES
    # TODO: SETUP LOGGING SOMEWHERE

    # get each map summary and add it to PCServer-KFGame.ini
    for new_map_index in range(len(maplist.new_maps)):
        map_summary_entry = getattr(maplist.new_maps[new_map_index], "map_summary")
        # TODO: FINISH THIS PART

    # print KFMapSummary list
    [print(f"[{x} KFMapSummary]\nMapName={x}\n") for x in sorted(MapList.new_maps)]
    print("\n\n")

    # Add to Map List
    # print sorted maplist for PCServer-KFGame.ini
    print()
    [print(f'"{x}"', end=",") for x in sorted(MapList.workshop_maps)]
    print("\n\n")


def update_map_db(maplist: MapList):
    """Update the db of current maps"""

    pass


def update_server_info(maplist: MapList):
    """Edit ServerInfo.md to reflect map list changes"""

    # FIXME: MAKE THIS EDIT THE FILE

    print("\n## **Map List**\n")
    # print new_maps
    print("### **Recent Additions**\n")
    print(f"```md\n-----Added on {date.today()}-----")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(MapList.new_maps), 1)]
    print("```\n")

    # print updated workshop_maps list
    print("### **Full Map List**\n")
    print("```md\n-----------WorkshopMaps-----------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(MapList.workshop_maps), 1)]
    print()

    # print lane_maps
    print("---------LaneMaps---------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(MapList.lane_maps), 1)]
    print()

    # print official_maps
    print("-----------OfficialMaps-----------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(MapList.official_maps), 1)]
    print()

    # print total number of maps
    total = (
        len(MapList.workshop_maps) + len(MapList.lane_maps) + len(MapList.official_maps)
    )

    print(f"\nTotal Maps: {total}")
    print("```\n")


def push_server_info():
    """Add, commit, push updated ServerInfo.md"""
    pass


def map_update_driver():
    """Driver
    Find the maps that were added and perform necessary edits to
    PCServer-KFEngine.ini, PCServer-KFGame.ini and ServerInfo.md
    """
    Server_Maps = MapList()
    Server_Maps.build_cur_map_list()
    Server_Maps.find_new_maps()
    Server_Maps.update_workshop_map_list()
    update_kfengine(Server_Maps)
    update_kfgame(Server_Maps)
    update_server_info(Server_Maps)
    update_map_db(Server_Maps)
    push_server_info()

    return


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

    args = parser.parse_args()

    try:
        if args.action == "mapupdate":
            map_update_driver()
    except AttributeError:
        raise AttributeError
