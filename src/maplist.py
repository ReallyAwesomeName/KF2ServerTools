#
# maplist.py
# MapList and MapObject classes
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


from datetime import date
import os


class MapObject:
    def __init__(self, map_name="", map_type="", map_new=False, workshop_id=0) -> None:
        self.map_name = map_name
        self.map_type = map_type
        self.map_new = map_new
        self.workshop_id = workshop_id
        # TODO: make sure no extention
        self.map_summary = f"[{self.map_name} KFMapSummary\nMapName={self.map_name}\n"


class MapList:
    """MapList contains lists of MapObjects\n
    [new_maps], [workshop_maps], [official_maps]
    """

    def __init__(self) -> None:
        """
        Args:
            new_maps ([MapObject])
            workshop_maps ([MapObject])
            lane_maps ([MapObject])
            official_maps ([MapObject])
        """
        self.new_maps = []
        self.workshop_maps = []
        self.official_maps = []

    def build_cur_map_list(self):
        """Build current (unupdated) map lists"""
        # read unupdated mapdb
        with open("mapdb.txt", "r") as f:
            curmaps = f.readlines()

        # build unupdated map list
        for map in curmaps:
            thismap = MapObject(map_name=map[3:], map_new=False)
            if map.startswith("wm."):
                thismap.map_type = "wm"
                self.workshop_maps.append(thismap)
            elif map.startswith("lm."):
                thismap.map_type = "lm"
                self.workshop_maps.append(thismap)
            elif map.startswith("om."):
                thismap.map_type = "om"
                self.official_maps.append(thismap)
        outmsg = f"\nBuilt current workshop_maps:\n{self.workshop_maps}\nBuilt current official_maps:\n{self.official_maps}\n"
        return

    def find_new_maps(self):
        """Find the maps to be added"""

        topdir = "T:\\Desktop\\workshop_backup_testing\\content\\232090"
        exten = ".kfm"

        # FIXME: need this check?
        # if len(self) == 0:
        #     return print('checking for new maps on empty map list')

        for dirpath, dirnames, files in os.walk(topdir, topdown=False):
            for name in files:
                if name.endswith(exten):
                    # FIXME: huh? Is this thing working?
                    # compare name to each workshop_maps.map_name
                    # assume new until it's found
                    this_map_new = True
                    for wm in self.workshop_maps:
                        if name in getattr(wm, "map_name"):
                            # map name found, NOT a new map
                            this_map_new = False
                            # break and check next name
                            break

                    if this_map_new:  # is still True
                        # checked name against all workshop_maps.map_name, no match found
                        # make new MapObject and add it to MapList.new_maps

                        # make map_summary
                        this_map_summary = (
                            f"[{name[:-4]} KFMapSummary]\nMapName={name[:-4]}\n"
                        )
                        # get workshop_id from path
                        split_path = dirpath.split("\\")
                        this_workshop_id = split_path[split_path.index("content") + 2]

                        # create and add MapObject to MapList
                        this_map = MapObject(
                            map_name=name,
                            map_new=True,
                            workshop_id=this_workshop_id,
                            map_summary=this_map_summary,
                        )
                        self.new_maps.append(this_map)

        outmsg = f"\nNew maps found:\n{self.new_maps}\n"
        return

    def update_workshop_map_list(self):
        """Adds self.new_maps to self.workshop_maps"""
        [self.workshop_maps.append(map) for map in self.new_maps]
        outmsg = "Added new_maps to workshop_maps"
        return

    def update_kfengine(self):
        """Make necessary edits to PCServer-KFEngine.ini"""
        # Need to:
        #   Add entry to [OnlineSubsystemSteamworks.KFWorkshopSteamworks]
        #   ServerSubscribedWorkshopItems=1208883070 // 1 KF-Corridor

        for new_map_index in range(len(self.new_maps)):
            new_map_id = getattr(self.new_maps[new_map_index], "workshop_id")
            new_map_name = getattr(self.new_maps[new_map_index], "map_name")
            map_steamworks_entry = (
                f"ServerSubscribedWorkshopItems={new_map_id} // {new_map_name}"
            )

            # TODO: copy file for backup then insert steamworks entry

        pass

    def update_kfgame(self):
        """Make necessary edits to PCServer-KFGame.ini"""
        # Need to:
        #   Add [<mapname> KFMapSummary]
        #       MapName=<mapname>
        #   Add to Map Cycle
        # FIXME: MAKE THIS EDIT THE FILE
        # TODO: MAKE BACKUPS OF ALL EDITED FILES
        # TODO: SETUP LOGGING SOMEWHERE

        # get each map summary and add it to PCServer-KFGame.ini
        for new_map_index in range(len(self.new_maps)):
            map_summary_entry = getattr(self.new_maps[new_map_index], "map_summary")
            # TODO: FINISH THIS PART

        # print KFMapSummary list
        [print(f"[{x} KFMapSummary]\nMapName={x}\n") for x in sorted(MapList.new_maps)]
        print("\n\n")

        # Add to Map List
        # print sorted maplist for PCServer-KFGame.ini
        print()
        [print(f'"{x}"', end=",") for x in sorted(MapList.workshop_maps)]
        print("\n\n")

    def update_map_db(self):
        """Update the db of current maps"""

        pass

    def update_server_info(self):
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
        total = len(MapList.workshop_maps) + len(MapList.official_maps)

        print(f"\nTotal Maps: {total}")
        print("```\n")

    def push_server_info():
        """Add, commit, push updated ServerInfo.md"""
        pass
