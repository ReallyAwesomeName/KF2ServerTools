#
# zed.py
# Zed classes
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


class Zed:
    def __init__(self, num_players, difficulty) -> None:
        self.num_players = num_players
        self.difficulty = difficulty


###### Trash Zeds ######
class Trash(Zed):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Cyst(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class AlphaClot(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)
        self.health = num_players * difficulty


# NOTE: Inheritance
class Rioter(AlphaClot):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Slasher(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Crawler(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Gorefast(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


# NOTE: Inheritance
class Gorefiend(Gorefast):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Stalker(Trash):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


###### E.D.A.R Variants ######
class Robot():
    def __init__(self) -> None:
        pass
    

###### Medium Zeds ######
class Medium(Zed):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Bloat(Medium):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Husk(Medium):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Siren(Medium):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


###### Large Zeds ######
class Large(Zed):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Scrake(Large):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


class Fleshpound(Large):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)


# NOTE: Inheritance
class QuarterPound(Fleshpound):
    def __init__(self, num_players, difficulty) -> None:
        super().__init__(num_players, difficulty)
