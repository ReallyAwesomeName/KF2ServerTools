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
        # self.lane_maps = [] # don't need?
        self.official_maps = []

    def build_cur_map_list(self):
        """Build current (unupdated) map lists
        """
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
        return print(outmsg)

    def find_new_maps(self):
        """Find the maps to be added"""

        # FIXME: DO THIS NEXT

        topdir = "T:\\Desktop\\workshop_backup_testing\\content\\232090"
        exten = ".kfm"

        # FIXME: need this check?
        # if len(self) == 0:
        #     return print('checking for new maps on empty map list')

        for dirpath, dirnames, files in os.walk(topdir, topdown=False):
            for name in files:
                if name.endswith(exten):
                    if name not in self.workshop_maps:
                        # must be new
                        # make map_summary
                        this_map_summary = (
                            f"[{name[:-4]} KFMapSummary]\nMapName={name[:-4]}\n"
                        )
                        # get workshop_id from path
                        split_path = dirpath.split('\\')
                        this_workshop_id = split_path[split_path.index('content')+2]
                        
                        # create and add MapObject to MapList
                        this_map = MapObject(
                            map_name=name, map_new=True, workshop_id=this_workshop_id, map_summary=this_map_summary
                        )
                        self.new_maps.append(this_map)

        outmsg = f"\nNew maps found:\n{self.new_maps}\n"
        return print(outmsg)

    def update_workshop_map_list(self, workshop_maps_to_update, new_maps_to_add):
        """Add [new_maps_to_add] to [workshop_maps_to_update]

        Args:
            workshop_maps_to_update (list): unupdated list of workshop maps
            new_maps_to_add (list): maps being added
        Returns:
            Updated list of workshop maps
        """

        # FIXME: ??

        # add [new_maps_to_add] to [workshop_maps_to_update]
        workshop_maps_to_update += [
            workshop_maps_to_update.append(map)
            for map in new_maps_to_add
            if map not in workshop_maps_to_update
        ]

        return workshop_maps_to_update  # now updated


class MapObject:
    def __init__(self, map_name, map_type, map_new, workshop_id, map_summary) -> None:
        self.map_name = ""
        self.map_type = ""
        self.map_new = False
        self.workshop_id = 0
        self.map_summary = ""

