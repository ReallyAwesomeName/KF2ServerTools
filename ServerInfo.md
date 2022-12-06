# **Info Regarding Our Server**

[Map List](#map-list)

## **Mods In Use**

- [Unofficial Killing Floor 2 Patch](https://steamcommunity.com/sharedfiles/filedetails/?id=2875147606)
- [Unofficial Killing Floor 2 Patch Options](https://steamcommunity.com/sharedfiles/filedetails/?id=2875577642)
- [Controlled Difficulty - Chokepoints Edition](https://steamcommunity.com/sharedfiles/filedetails/?id=2052571175)
- [Controlled Difficulty - Eternal Edition](https://steamcommunity.com/sharedfiles/filedetails/?id=1554427429)
- [CD Utils](https://steamcommunity.com/sharedfiles/filedetails/?id=1973922129)
- [PerkLevelManager](https://steamcommunity.com/sharedfiles/filedetails/?id=1862573749)

## **Client Side Configuration**

- [FriendlyHUD Full Options List](https://steamcommunity.com/sharedfiles/filedetails/?id=1827646464)

### *Most relevant FriendlyHUD settings:*

```md
Use these Console Commands OR edit the config file directly:
    My Documents\My Games\Killing Floor 2\Config\KFFriendlyHUD.ini
SetFHUDEnabled <bool> (default = true)
LoadFHUDPreset <string> (options: default, 1080_left, 1440_left, 1080_right, 1440_right, 1080_topright, 1440_topright)
LoadFHUDColorPreset <string> (options: default, gradient, classic, red, purple, blood, redregen)
SetFHUDHealthColor <byte R> <byte G> <byte B> <byte A = 192> (default = 0 192 0 192)
SetFHUDArmorColor <byte R> <byte G> <byte B> <byte A = 192> (default = 0 100 210 192)
SetFHUDBuffColor <byte R> <byte G> <byte B> <byte A = 192> (default = 255 255 255 192)
SetFHUDBuffLayout <string> (default = left)(options: none, left, right, top, bottom)
SetFHUDBuffCountMax <int> (default = 3)
SetFHUDBuffSize <float> (default = 8)
SetFHUDScale <float> (default = 1)
SetFHUDIgnoreSelf <bool> (default = true)

ResetFHUDConfig (Resets all settings to their defaults)
ResetFHUDLayout (Resets the layout settings to their defaults)
ResetFHUDColors (Resets the colors to their defaults)
ResetFHUDBar (Resets the bar settings to their defaults)
```

## **About Controlled Difficulty**

- [Beginner’s guide to CD](https://steamcommunity.com/sharedfiles/filedetails/?id=2513564310)
- [Controlled Difficulty Source](https://github.com/notblackout/kf2-controlled-difficulty)

### **Common CD Commands**

#### **Console Command**

```txt
SetBind <key> "<command>"
    ex: SetBind y "Say !cdot" will bind the Open Trader chat command to the y key
```

#### **Chat Commands**

```txt
!cdr (!cdready) – Tags you as ready, once everyone is ready, the trader countdown resumes
!cdur (!cdunready) - Un-ready
!cdot (!cdopentrader) – Opens trader remotely, saving you the hassle of travelling
!cdwho – Shows who is ready and who isn't. Also shows spectators
!cdinfo – Shows the basic CD settings currently set
!cdms – Shows you your stats (please don't be cringe and overuse it)
!cdstats damagetaken (larges, damagedealt, etc.) – Prints out specified game stat for all players
```

#### **Basic CD Settings**

```txt
MaxMonsters (mm) - How many zeds can be alive on the map at the same time
CohortSize (cs) - How many zeds spawn as a group at each SpawnPoll interval
SpawnPoll (sp) - How often (in seconds) the game attempts to spawn more zeds
SpawnCycle (sc) - Spawn presets to remove randomness. Every zed to be spawned is predetermined,
        the only randomness left with spawning is where they spawn (which lane they will go to)
```

#### **Full CD Settings**

```ini
[ControlledDifficulty_Eternal.CD_Survival]
CohortSize=0
MaxMonsters=0
SpawnMod=1.0000
SpawnPoll=1.0000
ZTSpawnMode=clockwork
DefaultAuthLevel=CDAUTH_READ
AuthorizedUsers=(SteamID="STEAM_0:0:47160255",Comment="Rin")
ZTSpawnSlowdown=1.5000
FriendlyFire=0.0000
DoshKill=0.9000
SelfInflictedDamageMod=0.5000
MovementSpeedMod=0.9500
ItemPickupsMod=0.1000
AmmoPickupsMod=0.2500
StartingDosh=250
RespawnDosh=250
AlbinoCrawlers=True
bLogControlledDifficulty=False
AlbinoAlphas=True
AlbinoGorefasts=True
DisableRobots=False
DisableRioters=False
DisableBloatPukeMines=False
DisableHuskFireballKnockDown=False
DisableCrawlerGas=False
Boss=unmodded
WaveType=unmodded
FleshpoundRageSpawns=False
HansMinionSpawnCycle=unmodded
PatriarchMinionSpawnCycle=unmodded
KingFleshpoundMinionSpawnCycle=unmodded
KingBloatMinionSpawnCycle=unmodded
MatriarchMinionSpawnCycle=unmodded
WaveSizeFakes=0
FakesMode=add_with_humans
TrashHPFakes=0
ScrakeHPFakes=0
QuarterPoundHPFakes=0
FleshpoundHPFakes=0
KingFleshpoundNoMinionsHPFakes=0
KingFleshpoundHPFakes=0
AbominationHPFakes=0
PatriarchHPFakes=0
HansHPFakes=0
MatriarchHPFakes=0
TrashHeadDamageMod=1.1000
TrashBodyDamageMod=1.0000
LargeHeadDamageMod=1.1000
LargeBodyDamageMod=1.0000
MaxHansMinionsToSpawn=18
MaxPatriarchMinionsToSpawn=10
MaxKingFleshpoundMinionsToSpawn=6
MaxKingBloatMinionsToSpawn=48
MaxMatriarchMinionsToSpawn=5
WaveSize=0
AutoPause=True
CountHeadshotsPerPellet=False
EnableReadySystem=True
TraderTime=12
WaveEndSummaries=True
WeaponTimeout=2147483647
ZedsTeleportCloser=False
LimitedPerkSwitch=False
DamageMessages=False
DisableTeamCollision=False
DropAllWeapons=False
ObjectiveMode=False
LargeKillMessages=False
DisableSpecialWaves=False
DisableZedReplacement=False
DisableEventZeds=False
StartWithTrader=False
TraderDash=True
FirstPersonLegs=False
InfiniteFlashlight=True
DisablePlayerCommandsResponse=False
bWaitForNetPlayers=True
bEnableMapObjectives=False
bEnableGameAnalytics=True
bRecordGameStatsFile=False
bLogScoring=False
bLogAIDefaults=False
bLogAICount=False
MinNetPlayers=1
EndOfGameDelay=10
GameModes=(FriendlyName="CDSurvival",ClassNameAndPath="ControlledDifficulty_Eternal.CD_Survival",bSoloPlaySupported=True,DifficultyLevels=4,Lengths=4,LocalizeID=0)
ZedReplacement=(ShouldReplace=CY,ReplaceWith=AL,ReplaceChance=1.0000)
SpecialWave=KFPNM,Wave=0,Count=0,AIRemaining=0
ServerExpirationForKillWhenEmpty=120.000000
RequiredMobileInputConfigs=(GroupName="DebugGroup",RequireZoneNames=("DebugStickMoveZone","DebugStickLookZone","DebugLookZone"),bIsAttractModeGroup=False)
bIsStandbyCheckingEnabled=False
MaxPlayers=6
GoalScore=0
MaxLives=0
TimeLimit=0
StandbyRxCheatTime=0.000000
StandbyTxCheatTime=0.000000
BadPingThreshold=0
PercentMissingForRxStandby=0.000000
PercentMissingForTxStandby=0.000000
PercentForBadPing=0.000000
JoinInProgressStandbyWaitTime=0.000000
DefaultGameType=KFGameContent.KFGameInfo_Survival
AnimTreePoolSize=0
SpawnCycle=unmodded
```

## **Map List**

### **Recent Additions**

```md
-----Added on 2022-12-05-----
1. KF-Aftermath-CDEdit
2. KF-Arid_Zedlands-CDEdit
3. KF-BM-GonarchsLair
4. KF-BarmwichTown-CDEdit
5. KF-BarrioMuerte-CDEdit
6. KF-CandyLand
7. KF-CarillonHamlet-CDEdit
8. KF-Crash_Night
9. KF-CrystalCaverns
10. KF-DE_Dust-CDEdit
11. KF-Fairfield-CDEdit
12. KF-HellmarkStation_Redux
13. KF-IceCave-CDEdit
14. KF-Inferno_Redux
15. KF-Italy_Redux
16. KF-Meow_Remake-TAEdit
17. KF-MirasLibrary_Redux
18. KF-Slaughterhouse-CDEdit
19. KF-SoBelow-CDEdit
20. KF-SynthwaveThing-CDEdit
21. KF-YuletideTown_Redux
```

### **Full Map List**

```md
-----------WorkshopMaps-----------
1. KF-Aftermath-CDEdit
2. KF-Anxiety
3. KF-Area52
4. KF-Arid_Zedlands-CDEdit
5. KF-AshwoodAsylum_Redux
6. KF-Assault-CDEdit
7. KF-BM-GonarchsLair
8. KF-BarmwichTown-CDEdit
9. KF-BarrioMuerte-CDEdit
10. KF-BikiniAtoll
11. KF-Blockfort-v2
12. KF-BurningParis-CDEdit
13. KF-CS_Italy-CDEdit
14. KF-CS_Office-CDEdit
15. KF-CandyLand
16. KF-CanvilleRM
17. KF-CarillonHamlet-CDEdit
18. KF-CarillonHamletB1
19. KF-City17-CDEdit
20. KF-ClassicBioticsLab
21. KF-ClubConfession
22. KF-Compound_Redux
23. KF-Crash_Night
24. KF-Crash_Original
25. KF-CrystalCaverns
26. KF-CytologyLab
27. KF-DE_Dust-CDEdit
28. KF-De_Dust
29. KF-De_Nuke-CDEdit
30. KF-DeepingWall
31. KF-DesolationOriginal
32. KF-Dust2_Redux
33. KF-Fairfield-CDEdit
34. KF-Farm_Remastered
35. KF-FrightYard_Redux
36. KF-GardenHeights-CDEdit
37. KF-HauntedMansion_V9
38. KF-HellmarkStation_Redux
39. KF-HellsCrypt
40. KF-Hells_ReachV2
41. KF-Hive
42. KF-HotelZed
43. KF-IceCave-CDEdit
44. KF-Inferno_Redux
45. KF-Italy_Redux
46. KF-KF1-Aperture
47. KF-KF1-Bedlam
48. KF-KF1-Medieval_Fortress
49. KF-KF1_Manor
50. KF-KF1_West_London
51. KF-KameHouse
52. KF-Kino_Der_Toten
53. KF-Kokiri_Forest
54. KF-Mario_64_Remastered
55. KF-Meow_Remake-TAEdit
56. KF-Miasma
57. KF-MirasLibrary_Redux
58. KF-MonsterBall-CDEdit
59. KF-Museum-CDEdit
60. KF-Nausea
61. KF-PK-Cemetery_Halloween
62. KF-PK-Enclave-Winter
63. KF-Port
64. KF-QuarantineBreach-CDEdit
65. KF-Rig_zfix
66. KF-SantasWorkshop-CDEdit
67. KF-ShoppingSpree-CDEdit
68. KF-Slaughterhouse-CDEdit
69. KF-SoBelow-CDEdit
70. KF-SynthwaveThing-CDEdit
71. KF-The_End
72. KF-ThrillsChills-CDEdit
73. KF-YuletideTown_Redux
74. KF-ZedsDiner

---------LaneMaps---------
1. KF-Corridor
2. KF-Cross
3. KF-Drone
4. KF-Parallel
5. KF-SubBalanced

-----------OfficialMaps-----------
1. KF-Airship
2. KF-AshwoodAsylum
3. KF-BarmwichTown
4. KF-Biolapse
5. KF-Bioticslab
6. KF-BlackForest
7. KF-BurningParis
8. KF-CarillonHamlet
9. KF-Catacombs
10. KF-ContainmentStation
11. KF-Crash
12. KF-Desolation
13. KF-DieSector
14. KF-Dystopia2029
15. KF-Elysium
16. KF-EvacuationPoint
17. KF-Farmhouse
18. KF-HellmarkStation
19. KF-HostileGrounds
20. KF-InfernalRealm
21. KF-KrampusLair
22. KF-Lockdown
23. KF-MonsterBall
24. KF-Moonbase
25. KF-Netherhold
26. KF-Nightmare
27. KF-Nuked
28. KF-Outpost
29. KF-PowerCore_Holdout
30. KF-Prison
31. KF-Rig
32. KF-Sanitarium
33. KF-Santasworkshop
34. KF-ShoppingSpree
35. KF-Spillway
36. KF-SteamFortress
37. KF-TheDescent
38. KF-TragicKingdom
39. KF-VolterManor
40. KF-ZedLanding


Total Maps: 119
```
