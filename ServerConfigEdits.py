# Fully automate KF2 server map update process
# https://github.com/ReallyAwesomeName/KF2ServerTools

# TODO: Actually make the ini edits
# TODO: Make into CLI script

import argparse
import os
from datetime import date
from MapList import MapList


def update_map_db(maplist: MapList):
    """Update the db of current maps"""
    
    pass


def edit_KFEngine():
    """Make necessary edits to PCServer-KFEngine.ini"""
    # Need to:
    #   Add entry to [OnlineSubsystemSteamworks.KFWorkshopSteamworks]
    #   ServerSubscribedWorkshopItems=1208883070 // 1 KF-Corridor
    pass


def edit_KFGame():
    """Make necessary edits to PCServer-KFGame.ini"""
    # Need to:
    #   Add [<mapname> KFMapSummary]
    #       MapName=<mapname>
    #   Add to Map Cycle

    # FIXME: MAKE THIS EDIT THE FILE

    # print KFMapSummary list
    [print(f"[{x} KFMapSummary]\nMapName={x}\n") for x in sorted(MapList.new_maps)]
    print("\n\n")

    # Add to Map List
    # print sorted maplist for PCServer-KFGame.ini
    print()
    [print(f'"{x}"', end=",") for x in sorted(MapList.workshop_maps)]
    print("\n\n")


def edit_server_info():
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


def map_update_driver():
    """Driver
    Find the maps that were added and perform necessary edits to
    PCServer-KFEngine.ini, PCServer-KFGame.ini and ServerInfo.md
    """
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

    args = parser.parse_args()

    try:
        if args.action == "mapupdate":
            map_update_driver()
    except AttributeError:
        raise AttributeError
