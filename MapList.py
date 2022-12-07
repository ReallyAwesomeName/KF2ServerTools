# MapList and MapObject classes
import os


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


class MapObject:
    def __init__(
        self, map_name="", map_type="", map_new=False, workshop_id=0, map_summary=""
    ) -> None:
        self.map_name = map_name
        self.map_type = map_type
        self.map_new = map_new
        self.workshop_id = workshop_id
        self.map_summary = map_summary
