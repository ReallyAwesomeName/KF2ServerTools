# Fully automate KF2 server map update process
# https://github.com/ReallyAwesomeName/KF2ServerTools

# TODO: Actually make the ini edits
# TODO: Make into CLI script

import argparse
import os
from datetime import date


class MapList:
    def __init__(self, new_maps, workshop_maps, lane_maps, official_maps) -> None:
        """
        Args:
            new_maps ([MapObject])
            workshop_maps ([MapObject])
            lane_maps ([MapObject])
            official_maps ([MapObject])
        """
        self.new_maps = new_maps
        self.workshop_maps = workshop_maps
        self.lane_maps = lane_maps
        self.official_maps = official_maps


class MapObject:
    def __init__(self) -> None:
        self.map_name = ""
        self.map_type = ""
        self.map_new = False
        self.workshop_id = 0
        self.map_summary = ""


def update_workshop_map_list(workshop_maps_to_update, new_maps_to_add):
    """Add [new_maps_to_add] to [workshop_maps_to_update]

    Args:
        workshop_maps_to_update (list): unupdated list of workshop maps
        new_maps_to_add (list): maps being added
    Returns:
        Updated list of workshop maps
    """

    # add [new_maps_to_add] to [workshop_maps_to_update]
    workshop_maps_to_update += [
        workshop_maps_to_update.append(map)
        for map in new_maps_to_add
        if map not in workshop_maps_to_update
    ]

    return workshop_maps_to_update  # now updated


def update_map_db():
    """Update the db of current maps"""
    pass


def find_new_maps():
    """Find the maps that were added"""
    # FIXME: DO THIS NEXT
    topdir = "T:\\Desktop\\workshop_backup_testing\\content\\232090"
    exten = ".kfm"

    for dirpath, dirnames, files in os.walk(topdir, topdown=False):
        for name in files:
            pass

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
