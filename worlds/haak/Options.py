import typing
from Options import Option, Range, Choice, Toggle


class RandomizeGems(Toggle):
    """If the gem unlocks should be randomized"""
    display_name = "Gems"
    option_true = 1
    option_false = 0
    default = 1

class GemsInPool(Range):
    """How many Gems are in the pool"""
    display_name = "Gems in Pool"
    range_start = 0
    range_end = 40
    default = 4

class GemsRequired(Range):
    """What percentage of available gems (rounded down) is required to open the door"""
    display_name = "Gems Required"
    range_start = 0
    range_end = 100
    default = 75

class RequiredEndings(Range):
    """How many endings are required to be completed to win the game."""
    display_name = "Endings"
    range_start = 0
    range_end = 99
    default = 40

class RequireFailableJumps(Toggle):
    """This includes jumps in logic that are difficult and result in death if missed"""
    display_name = "RequireFailableJumps"
    option_true = 1
    option_false = 0
    default = 0

class RequireHardCombat(Toggle):
    """This adds ending 49 into logic without shield"""
    display_name = "RequireHardCombat"
    option_true = 1
    option_false = 0
    default = 0

class AddTreasureSword(Toggle):
    """This adds the sword in the treasure room into the sword progression"""
    display_name = "AddTreasureSword"
    option_true = 1
    option_false = 0
    default = 0

haak_options: typing.Dict[str, type(Option)] = {
    "endings": RequiredEndings,
    "randomizeGems": RandomizeGems,
    "gemsInPool": GemsInPool,
    "gemsRequired": GemsRequired,
    "hardjumps": RequireFailableJumps,
    "hardcombat": RequireHardCombat,
    "treasureSword": AddTreasureSword,
}
