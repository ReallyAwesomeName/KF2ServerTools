# Fully automate KF2 server map update process
# https://github.com/ReallyAwesomeName/KF2ServerInfo/blob/master/ServerInfo.md

# TODO: Actually make the ini edits
# TODO: Make into CLI script

import argparse
import os
from datetime import date


official_maps = [
    "KF-Airship",
    "KF-AshwoodAsylum",
    "KF-BarmwichTown",
    "KF-Biolapse",
    "KF-Bioticslab",
    "KF-BlackForest",
    "KF-BurningParis",
    "KF-CarillonHamlet",
    "KF-Catacombs",
    "KF-ContainmentStation",
    "KF-Crash",
    "KF-Desolation",
    "KF-DieSector",
    "KF-Dystopia2029",
    "KF-Elysium",
    "KF-EvacuationPoint",
    "KF-Farmhouse",
    "KF-HellmarkStation",
    "KF-HostileGrounds",
    "KF-InfernalRealm",
    "KF-KrampusLair",
    "KF-Lockdown",
    "KF-MonsterBall",
    "KF-Moonbase",
    "KF-Netherhold",
    "KF-Nightmare",
    "KF-Nuked",
    "KF-Outpost",
    "KF-PowerCore_Holdout",
    "KF-Prison",
    "KF-Rig",
    "KF-Sanitarium",
    "KF-Santasworkshop",
    "KF-ShoppingSpree",
    "KF-Spillway",
    "KF-SteamFortress",
    "KF-TheDescent",
    "KF-TragicKingdom",
    "KF-VolterManor",
    "KF-ZedLanding",
]

workshop_maps = [
    "KF-Anxiety",
    "KF-KF1-Aperture",
    "KF-Area52",
    "KF-AshwoodAsylum_Redux",
    "KF-Assault-CDEdit",
    "KF-KF1-Bedlam",
    "KF-BikiniAtoll",
    "KF-Blockfort-v2",
    "KF-BurningParis-CDEdit",
    "KF-CanvilleRM",
    "KF-CarillonHamletB1",
    "KF-PK-Cemetery_Halloween",
    "KF-City17-CDEdit",
    "KF-ClassicBioticsLab",
    "KF-Compound_Redux",
    "KF-ClubConfession",
    "KF-Crash_Original",
    "KF-CS_Italy-CDEdit",
    "KF-CS_Office-CDEdit",
    "KF-CytologyLab",
    "KF-DeepingWall",
    "KF-De_Dust",
    "KF-Dust2_Redux",
    "KF-De_Nuke-CDEdit",
    "KF-DesolationOriginal",
    "KF-PK-Enclave-Winter",
    "KF-Farm_Remastered",
    "KF-FrightYard_Redux",
    "KF-GardenHeights-CDEdit",
    "KF-HauntedMansion_V9",
    "KF-HellsCrypt",
    "KF-Hells_ReachV2",
    "KF-Hive",
    "KF-HotelZed",
    "KF-KameHouse",
    "KF-Kino_Der_Toten",
    "KF-Kokiri_Forest",
    "KF-KF1_Manor",
    "KF-Mario_64_Remastered",
    "KF-KF1-Medieval_Fortress",
    "KF-Miasma",
    "KF-MonsterBall-CDEdit",
    "KF-Museum-CDEdit",
    "KF-Nausea",
    "KF-Port",
    "KF-QuarantineBreach-CDEdit",
    "KF-Rig_zfix",
    "KF-SantasWorkshop-CDEdit",
    "KF-ShoppingSpree-CDEdit",
    "KF-The_End",
    "KF-ThrillsChills-CDEdit",
    "KF-KF1_West_London",
    "KF-ZedsDiner",
    "KF-Aftermath-CDEdit",
    "KF-Arid_Zedlands-CDEdit",
    "KF-BarmwichTown-CDEdit",
    "KF-CarillonHamlet-CDEdit",
    "KF-BarrioMuerte-CDEdit",
    "KF-Crash_Night",
    "KF-DE_Dust-CDEdit",
    "KF-Fairfield-CDEdit",
    "KF-HellmarkStation_Redux",
    "KF-IceCave-CDEdit",
    "KF-Inferno_Redux",
    "KF-Italy_Redux",
    "KF-BM-GonarchsLair",
    "KF-CandyLand",
    "KF-MirasLibrary_Redux",
    "KF-Meow_Remake-TAEdit",
    "KF-Slaughterhouse-CDEdit",
    "KF-SoBelow-CDEdit",
    "KF-SynthwaveThing-CDEdit",
    "KF-YuletideTown_Redux",
    "KF-CrystalCaverns",
]

lane_maps = [
    "KF-Corridor",
    "KF-Cross",
    "KF-Drone",
    "KF-Parallel",
    "KF-SubBalanced",
]

new_maps = [
]


# print sorted maplist for PCServer-KFGame.ini
# add [new_maps] to [workshop_maps]
workshop_maps += [workshop_maps.append(map) for map in new_maps if map not in workshop_maps]
print()
[print(f'"{x}"', end=",") for x in sorted(workshop_maps)]
print("\n\n")

# print KFMapSummary list
[print(f"[{x} KFMapSummary]\nMapName={x}\n") for x in sorted(new_maps)]
print("\n\n")





class map_object:
    def __init__(self) -> None:
        self.map_name = ""
        self.map_type = ""
        self.map_new = False
        self.workshop_id = 0
        self.KFMapSummary = ""
        

def update_map_db():
    """Update the db of current maps
    """
    pass

def find_new_maps():
    """Find the maps that were added
    """
    pass

def edit_KFEngine():
    """Make necessary edits to PCServer-KFEngine.ini
    """
    pass

def edit_KFGame():
    """Make necessary edits to PCServer-KFGame.ini
    """
    pass

def print_updated_map_list():
    """Print updated map list for ServerInfo.md
    """
    
    print("\n## **Map List**\n")
    # print new_maps
    print("### **Recent Additions**\n")
    print(f"```md\n-----Added on {date.today()}-----")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(new_maps), 1)]
    print("```\n")

    # print updated workshop_maps list
    print("### **Full Map List**\n")
    print("```md\n-----------WorkshopMaps-----------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(workshop_maps), 1)]
    print()

    # print lane_maps
    print("---------LaneMaps---------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(lane_maps), 1)]
    print()

    # print official_maps
    print("-----------OfficialMaps-----------")
    [print(f"{num}. {x}") for num, x in enumerate(sorted(official_maps), 1)]
    print()

    # print total number of maps
    total = len(workshop_maps) + len(lane_maps) + len(official_maps)
    print(f"\nTotal Maps: {total}")
    print("```\n")



def update_maps():
    """Find the maps that were added and make necessary updates to PCServer-KFEngine.ini
    and PCServer-KFGame.ini\nReturns updated map list for ServerInfo.md
    """
    pass


# CLI
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    
    # select action (plan to add more)
    subparsers = parser.add_subparsers(
        help="Desired action",
        dest="action",
    )
    
    # action: updatemaps
    newmap_parser = subparsers.add_parser(
        "updatemaps",
        help="Update server maps",
    )
    
    
    args = parser.parse_args()
    
    try:
        if args.action == "updatemaps":
            update_maps()
    except AttributeError:
        raise AttributeError
    


