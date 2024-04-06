from BaseClasses import Entrance, Location, MultiWorld, Region
import typing
from .Locations import HaakLocation, location_table_sanho_ruins, location_table_neo_sanho, location_table_north_station, location_table_subway_tunnel,\
    location_table_peoples_square, location_table_whitestone, location_table_brewery, location_table_sillie_farm, location_table_merlin_pit,\
    location_table_anthony_hill, location_table_momoyama, location_table_industry_zone, location_table_subway_depot, location_table_emperors_tower,\
    location_table

class Room(typing.NamedTuple):
    name: str
    entrances: bool
    logic: bool

def create_region(multiworld: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, multiworld)
    if locations:
        for location in locations:
            loc_id = location_table.get(location, 0)
            location = HaakLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, f"{name} -> {exit}", ret))

    return ret

def create_regions(multiworld: MultiWorld, p: int):
    multiworld.regions += [
        create_region(multiworld, p, "Menu", None, ["Sanho Ruins"]),
        create_region(multiworld, p, "WorldMap", None, ["Neo Sanho", "North Station", "Whitestone", "Sillie Farm", "Merlin Pit", "Industry Zone", "Emperors Tower"]),
        create_region(multiworld, p, "Sanho Ruins", location_table_sanho_ruins, ["WorldMap"]),
        create_region(multiworld, p, "Neo Sanho", location_table_neo_sanho, ["Brewery"]),
        create_region(multiworld, p, "North Station", location_table_north_station, ["Subway Tunnel"]),
        create_region(multiworld, p, "Subway Tunnel", location_table_subway_tunnel, ["Peoples Square", "Subway Depot"]),
        create_region(multiworld, p, "Peoples Square", location_table_peoples_square),
        create_region(multiworld, p, "Whitestone", location_table_whitestone),
        create_region(multiworld, p, "Brewery", location_table_brewery),
        create_region(multiworld, p, "Sillie Farm", location_table_sillie_farm),
        create_region(multiworld, p, "Merlin Pit", location_table_merlin_pit, ["Anthony Hill"]),
        create_region(multiworld, p, "Anthony Hill", location_table_anthony_hill, ["Momoyama"]),
        create_region(multiworld, p, "Momoyama", location_table_momoyama),
        create_region(multiworld, p, "Industry Zone", location_table_industry_zone),
        create_region(multiworld, p, "Subway Depot", location_table_subway_depot),
        create_region(multiworld, p, "Emperors Tower", location_table_emperors_tower),
    ]

    # link up our regions
    multiworld.get_entrance("Menu -> Sanho Ruins", p).connect(multiworld.get_region("Sanho Ruins", p))

    multiworld.get_entrance("Sanho Ruins -> WorldMap", p).connect(multiworld.get_region("WorldMap", p))
    multiworld.get_entrance("Sanho Ruins -> WorldMap", p).access_rule = \
        lambda state: state.has_all(["Glove", "ProgressiveDash"], p) and state.has("KeyCard", p, 2)
    
    multiworld.get_entrance("WorldMap -> Neo Sanho", p).connect(multiworld.get_region("Neo Sanho", p))
    multiworld.get_entrance("WorldMap -> North Station", p).connect(multiworld.get_region("North Station", p))

    multiworld.get_entrance("North Station -> Subway Tunnel", p).connect(multiworld.get_region("Subway Tunnel", p))
    multiworld.get_entrance("North Station -> Subway Tunnel", p).access_rule = \
        lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p)
    
    multiworld.get_entrance("Subway Tunnel -> Peoples Square", p).connect(multiworld.get_region("Peoples Square", p))

    multiworld.get_entrance("WorldMap -> Whitestone", p).connect(multiworld.get_region("Whitestone", p))
    multiworld.get_entrance("WorldMap -> Whitestone", p).access_rule = \
        lambda state: state.has("FattyDefeated", p)
    
    multiworld.get_entrance("Neo Sanho -> Brewery", p).connect(multiworld.get_region("Brewery", p))
    multiworld.get_entrance("Neo Sanho -> Brewery", p).access_rule = \
        lambda state: state.has("FattyDefeated", p) and state.has("ProgressiveDivingThrust", p)
    
    multiworld.get_entrance("WorldMap -> Sillie Farm", p).connect(multiworld.get_region("Sillie Farm", p))
    multiworld.get_entrance("WorldMap -> Sillie Farm", p).access_rule = \
        lambda state: (state.has("Dessert Recipe", p) and state.can_reach(multiworld.get_region("Whitestone", p), None, p)) or state.has("ThrustUp", p)
    
    multiworld.get_entrance("WorldMap -> Merlin Pit", p).connect(multiworld.get_region("Merlin Pit", p))
    multiworld.get_entrance("WorldMap -> Merlin Pit", p).access_rule = \
        lambda state: state.has("Dessert Recipe", p) and state.can_reach(multiworld.get_region("Whitestone", p), None, p) and state.has("GasMask", p)
    
    multiworld.get_entrance("Merlin Pit -> Anthony Hill", p).connect(multiworld.get_region("Anthony Hill", p))
    multiworld.get_entrance("Merlin Pit -> Anthony Hill", p).access_rule = \
        lambda state: state.has("ThrustUp", p)
    
    multiworld.get_entrance("Anthony Hill -> Momoyama", p).connect(multiworld.get_region("Momoyama", p))
    multiworld.get_entrance("Anthony Hill -> Momoyama", p).access_rule = \
        lambda state: state.has_all(["Glide", "CleanVents"], p)
    
    multiworld.get_entrance("WorldMap -> Industry Zone", p).connect(multiworld.get_region("Industry Zone", p))
    multiworld.get_entrance("WorldMap -> Industry Zone", p).access_rule = \
        lambda state: state.has("East Passcard", p)
    
    multiworld.get_entrance("Subway Tunnel -> Subway Depot", p).connect(multiworld.get_region("Subway Depot", p))
    multiworld.get_entrance("Subway Tunnel -> Subway Depot", p).access_rule = \
        lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDash", p, 3) and state.has_all(["Glide", "ThrustUp", "DashSlash"], p)
    
    multiworld.get_entrance("WorldMap -> Emperors Tower", p).connect(multiworld.get_region("Emperors Tower", p))
    multiworld.get_entrance("WorldMap -> Emperors Tower", p).access_rule = \
        lambda state: state.has("East Passcard", p)
