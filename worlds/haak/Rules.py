from BaseClasses import CollectionState, MultiWorld
from Options import PerGameCommonOptions
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import set_rule

def set_rules(options: PerGameCommonOptions, multiworld: MultiWorld, p: int):
    # sanho_ruins
    set_rule(multiworld.get_location("sanho_ruins_room_73_keycard", p),
             lambda state: True)
    set_rule(multiworld.get_location("sanho_ruins_room_62_glove", p),
             lambda state: state.has("KeyCard", p, 1))
    set_rule(multiworld.get_location("sanho_ruins_room_60_disk", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_62_lifeshard", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_64_lifeshard", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_76_dye", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_61_newspaper", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_74_hookspeed", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_53_firstaid", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_58_keycard", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_58_disk", p),
             lambda state: state.has("KeyCard", p, 1) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_55_lifeshard", p),
             lambda state: state.has("KeyCard", p, 2) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_56_dash", p),
             lambda state: state.has("KeyCard", p, 2) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_71_tvantenna", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ProgressiveDash"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_47_newspaper", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ProgressiveDash"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_47_hooklength", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ProgressiveDash"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_66_metalsniffer", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ProgressiveDivingThrust"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_53_disk", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ProgressiveDivingThrust", "Hacker", "ProgressiveDash", "Glide"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_69_lifeshard", p),
             lambda state: state.has("KeyCard", p, 2) and state.has("Glove", p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("sanho_ruins_room_69_attackboost", p),
             lambda state: state.has("KeyCard", p, 2) and state.has("Glove", p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("sanho_ruins_room_34_lifeshard", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ThrustUp", "ProgressiveDivingThrust", "ProgressiveChargeAttack"], p)
             and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("sanho_ruins_room_64_critrate", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ThrustUp"], p))
    set_rule(multiworld.get_location("sanho_ruins_room_54_flyer", p),
             lambda state: state.has("KeyCard", p, 2) and state.has("Glove", p))
    set_rule(multiworld.get_location("sanho_ruins_room_56_disk", p),
             lambda state: state.has("KeyCard", p, 2) and state.has_all(["Glove", "ThrustUp"], p))
    
    # neo sanho
    set_rule(multiworld.get_location("neo_sanho_room_16_lifeshard", p),
             lambda state: state.has("Disk", p, 2))
    set_rule(multiworld.get_location("neo_sanho_room_16_hooklength", p),
             lambda state: state.has("Disk", p, 4))
    set_rule(multiworld.get_location("neo_sanho_room_16_firstaid", p),
             lambda state: state.has("Disk", p, 8))
    set_rule(multiworld.get_location("neo_sanho_room_16_instantcharge", p),
             lambda state: state.has("Disk", p, 12))
    set_rule(multiworld.get_location("neo_sanho_room_16_hookspeed", p),
             lambda state: state.has("Disk", p, 18))
    set_rule(multiworld.get_location("neo_sanho_room_16_energyshard", p),
             lambda state: state.has("Disk", p, 23))
    set_rule(multiworld.get_location("neo_sanho_room_16_attackboost", p),
             lambda state: state.has("Disk", p, 28))
    set_rule(multiworld.get_location("neo_sanho_room_16_ultimatehook", p),
             lambda state: state.has("Disk", p, 34))
    set_rule(multiworld.get_location("neo_sanho_room_16_critrate", p),
             lambda state: state.has("Disk", p, 40))
    set_rule(multiworld.get_location("neo_sanho_room_16_attackboost", p),
             lambda state: state.has("Disk", p, 50))
    set_rule(multiworld.get_location("neo_sanho_room_16_photo", p),
             lambda state: state.has("Disk", p, 50) and state.has("ThrustUp", p))
    set_rule(multiworld.get_location("neo_sanho_room_23_disk", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("neo_sanho_room_22_picture", p),
             lambda state: state.has_all(["ThrustUp", "Glide"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("neo_sanho_room_5_book", p),
             lambda state: state.has("Hacker", p) or state.has_all(["ProgressiveDivingThrust", "ProgressiveSwordWaves"], p))
    set_rule(multiworld.get_location("neo_sanho_room_5_diary", p),
             lambda state: state.has("ProgressiveDash", p, 3) and state.has_all(["ProgressiveSwordWaves", "ThrustUp"], p) 
               and (state.has("Hacker", p) or state.has("ProgressiveDivingThrust", p)))
    set_rule(multiworld.get_location("neo_sanho_room_14_tape", p),
             lambda state: state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("neo_sanho_room_13_report", p),
             lambda state: state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("neo_sanho_room_5_powercord", p),
             lambda state: state.has("ProgressiveDash", p, 3) and state.has("ProgressiveChargeAttack", p))
    set_rule(multiworld.get_location("neo_sanho_room_13_stereo", p),
             lambda state: state.has("ProgressiveDash", p, 3) and state.has("ProgressiveSwordWaves", p))
    set_rule(multiworld.get_location("neo_sanho_room_12_disk", p),
             lambda state: state.has("ProgressiveDash", p, 4) and state.has_all(["ProgressiveSwordWaves", "PortableStereo", "Tape Yellow"], p))
    
    # north station
    set_rule(multiworld.get_location("north_station_room_58_tvmotherboard", p),
             lambda state: True)
    set_rule(multiworld.get_location("north_station_room_82_keycard", p),
             lambda state: True)
    set_rule(multiworld.get_location("north_station_room_55_dye", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_48_lifeshard", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_63_disk", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_63_newspaper", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_57_lifeshard", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_67_disk", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_60_chargeattack", p),
             lambda state: state.has("KeyCard", p, 3))
    set_rule(multiworld.get_location("north_station_room_68_encryptednote", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p))
    set_rule(multiworld.get_location("north_station_room_56_deflection", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p))
    set_rule(multiworld.get_location("north_station_room_87_lifeshard", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p))
    set_rule(multiworld.get_location("north_station_room_82_disk", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p))
    set_rule(multiworld.get_location("north_station_room_89_disk", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p))
    set_rule(multiworld.get_location("north_station_room_53_disk", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p))
    set_rule(multiworld.get_location("north_station_room_67_intellectuals_spring", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p) and state.has("Deflection", p))
    set_rule(multiworld.get_location("north_station_room_58_piercinghook", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection"], p))
    set_rule(multiworld.get_location("north_station_room_84_firstaideffect", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection", "ProgressiveDivingThrust"], p)
             and (state.has("Hacker", p) or state.has("ProgressiveSwordWaves", p, 2)))
    set_rule(multiworld.get_location("north_station_room_83_hunting_cert", p),
             lambda state: state.has("KeyCard", p, 3) and state.has("ProgressiveChargeAttack", p))
    set_rule(multiworld.get_location("north_station_room_86_disk", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection"], p))
    set_rule(multiworld.get_location("north_station_room_76_disk", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection"], p)
             and (state.has("Hacker", p) or state.has("ProgressiveSwordWaves", p, 2)))
    set_rule(multiworld.get_location("north_station_room_54_encryptednoted", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection"], p))
    set_rule(multiworld.get_location("north_station_room_54_hookspeed", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("north_station_room_52_critrate", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection", "ProgressiveDivingThrust", "ThrustUp"], p)
               and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("north_station_room_51_hooklength", p),
             lambda state: state.has("KeyCard", p, 3) and state.has_all(["ProgressiveChargeAttack", "Deflection", "ProgressiveDivingThrust", "ThrustUp"], p)
               and state.has("ProgressiveDash", p, 3))
    
    # Subway Tunnel
    set_rule(multiworld.get_location("subway_tunnel_room_21_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("subway_tunnel_room_27_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p)
             and (state.has("Hacker", p) or state.has("ProgressiveSwordWaves", p)))
    set_rule(multiworld.get_location("subway_tunnel_room_17_newspaper", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("subway_tunnel_room_25_energyshard", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("subway_tunnel_room_26_swordwaves", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("subway_tunnel_room_26_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveSwordWaves", p))
    set_rule(multiworld.get_location("subway_tunnel_room_29_electrichook", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("subway_tunnel_room_33_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDash", p, 3) and state.has_all(["Glide", "ThrustUp", "DashSlash"], p))
    set_rule(multiworld.get_location("subway_tunnel_room_33_disk2", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDash", p, 3) or state.has("ThrustUp", p))
    
    # People's Square
    set_rule(multiworld.get_location("peoples_square_room_80_keycard", p),
             lambda state: True)
    set_rule(multiworld.get_location("peoples_square_room_63_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_57_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_any(["ProgressiveSwordWaves", "Hacker"], p))
    set_rule(multiworld.get_location("peoples_square_room_69_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_55_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_55_disk2", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_62_critrate", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_74_newspaper", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_49_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_70_divingthrust", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_79_dye", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_59_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p) and state.has_any(["ProgressiveSwordWaves", "Hacker"], p))
    set_rule(multiworld.get_location("peoples_square_room_66_encryptednote", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_49_disk2", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_49_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_56_lifeshard", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_68_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_53_disk", p),
             lambda state: state.has("KeyCard", p, 4))
    set_rule(multiworld.get_location("peoples_square_room_60_boostedcharge", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_71_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp"], p))
    set_rule(multiworld.get_location("peoples_square_room_62_catfood", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("fatty", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_61_hookspeed", p),
             lambda state: state.has("KeyCard", p, 4) and state.has("ProgressiveDivingThrust", p))
    set_rule(multiworld.get_location("peoples_square_room_65_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp", "ProgressiveSwordWaves"], p))
    set_rule(multiworld.get_location("peoples_square_room_68_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp"], p))
    set_rule(multiworld.get_location("peoples_square_room_70_critrate", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp"], p))
    set_rule(multiworld.get_location("peoples_square_room_69_picture", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp", "DashSlash"], p))
    set_rule(multiworld.get_location("peoples_square_room_50_disk", p),
             lambda state: state.has("KeyCard", p, 4) and state.has_all(["ProgressiveDivingThrust", "ThrustUp"], p))
    
    # Whitestone
    set_rule(multiworld.get_location("whitestone_room_3_lifeshard", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("whitestone_room_4_passcard", p),
             lambda state: state.has("ThrustUp", p) and state.has_any(["ProgressiveDash", "DashSlash"], p))
    set_rule(multiworld.get_location("whitestone_room_6_disk", p),
             lambda state: state.has_all(["ThrustUp", "Hacker"], p) and state.has("EnergyShard", p, 3) and 
             (state.has("ProgressiveDash", p, 4) or (state.has("ProgressiveDash", p, 3) and state.has("ProgressiveSwordWaves", p))))

    # Brewery
    set_rule(multiworld.get_location("brewery_room_115_devlog", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_94_map", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_92_attackboost", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_80_rampage", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_91_disk", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_101_lifeshard", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_84_flyer", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_87_hooklength", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_84_dye", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_106_hookspeed", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_111_lifeshard", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_104_newspaper", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_107_disk", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_99_disk", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_82_dessertrecipe", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_82_note", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_35_powerdivingthrust", p),
             lambda state: True)
    set_rule(multiworld.get_location("brewery_room_44_disk", p),
             lambda state: True)
    
    # Sillie Farm
    set_rule(multiworld.get_location("sillie_farm_room_92_gasmask", p),
             lambda state: True)
    set_rule(multiworld.get_location("sillie_farm_room_92_disk", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("sillie_farm_room_92_disk2", p),
             lambda state: state.has("ThrustUp", p) and state.has("EnergyShard", p, 3) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("sillie_farm_room_9_newspaper", p),
             lambda state: state.has_all(["ThrustUp", "DashSlash"], p) and state.can_reach(multiworld.get_region("Anthony Hill", p), player=p))
    set_rule(multiworld.get_location("sillie_farm_room_84_disk", p),
             lambda state: state.has("ThrustUp", p) and state.has("EnergyShard", p, 3) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("sillie_farm_room_90_energyshard", p),
             lambda state: state.has("ThrustUp", p))
    
    # Merlin Pit
    set_rule(multiworld.get_location("merlin_pit_room_36_thrustup", p),
             lambda state: True)
    set_rule(multiworld.get_location("merlin_pit_room_69_disk", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("merlin_pit_room_123_lifeshard", p),
             lambda state: state.has("ThrustUp", p) and state.has("EnergyShard", p , 3))
    set_rule(multiworld.get_location("merlin_pit_room_140_disk", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("merlin_pit_room_37_unlimitedslide", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("merlin_pit_room_120_hooklength", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_115_disk", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_115_hookspeed", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_57_hooklength", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("merlin_pit_room_113_newspaper", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_110_critrate", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_110_disk", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_room_144_lifeshard", p),
             lambda state: state.has_all(["ThrustUp", "DashSlash", "ProgressiveDivingThrust"], p))
    set_rule(multiworld.get_location("merlin_pit_room_124_disk", p),
             lambda state: state.has_all(["DashSlash", "ProgressiveDivingThrust"], p))
    set_rule(multiworld.get_location("merlin_pit_room_97_disk", p),
             lambda state: state.has("MoleGangLeaderDefeated", p))
    set_rule(multiworld.get_location("merlin_pit_vent1", p),
             lambda state: True)
    set_rule(multiworld.get_location("merlin_pit_vent2", p),
             lambda state: True)
    set_rule(multiworld.get_location("merlin_pit_vent3", p),
             lambda state: state.has("ThrustUp", p))
    set_rule(multiworld.get_location("merlin_pit_vent4", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_vent4", p),
             lambda state: state.has("ThrustUp", p) and state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("merlin_pit_vent5", p),
             lambda state: state.has("MoleGangLeaderDefeated", p))
    set_rule(multiworld.get_location("molegangleader", p),
             lambda state: state.has_all(["ThrustUp", "AttackBoost"], p) and state.has("ProgressiveDash", p, 2) and state.has("LifeShard", p, 12))
    
    # Anthony Hill
    set_rule(multiworld.get_location("anthony_hill_vent6", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_vent7", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_vent8", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_vent9", p),
             lambda state: state.has("Glide", p))
    set_rule(multiworld.get_location("anthony_hill_room_107_disk", p),
             lambda state: state.has("ProgressiveDash", p, 2))
    set_rule(multiworld.get_location("anthony_hill_room_80_lifeshard", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_room_91_critrate", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_room_98_glide", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_room_50_secretmanual", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p))
    set_rule(multiworld.get_location("anthony_hill_room_80_secretmanual", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p) and (state.has("ProgressiveDash", p, 4) or state.has("DashSlash", p)))
    set_rule(multiworld.get_location("anthony_hill_room_60_secretmanual", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p) and (state.has("ProgressiveDash", p, 3)))
    set_rule(multiworld.get_location("anthony_hill_room_133_report", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p))
    set_rule(multiworld.get_location("anthony_hill_room_86_flyer", p),
             lambda state: state.has_all(["Glide", "CleanVents", "Hacker"], p))
    set_rule(multiworld.get_location("anthony_hill_room_57_study", p),
             lambda state: state.has_all(["Glide", "CleanVents", "Hacker"], p))
    set_rule(multiworld.get_location("anthony_hill_room_119_laptop", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p) and state.has_any(["DashSlash", "Hacker"], p))
    set_rule(multiworld.get_location("anthony_hill_room_76_energyshard", p),
             lambda state: state.has_all(["Glide", "CleanVents", "DashSlash"], p) and state.has("EnergyShard", p, 3))
    set_rule(multiworld.get_location("anthony_hill_room_76_disk", p),
             lambda state: state.has_all(["Glide", "CleanVents", "DashSlash"], p) and state.has("EnergyShard", p, 6))
    set_rule(multiworld.get_location("anthony_hill_room_56_disk", p),
             lambda state: state.has_all(["Glide", "CleanVents", "DashSlash"], p))
    set_rule(multiworld.get_location("anthony_hill_room_132_disk", p),
             lambda state: state.has_all(["Glide", "CleanVents", "DashSlash"], p))
    set_rule(multiworld.get_location("anthony_hill_room_59_fulldirectiondash", p),
             lambda state: state.has_all(["Glide", "CleanVents", "DashSlash"], p))
    set_rule(multiworld.get_location("anthony_hill_room_97_hookspeed", p),
             lambda state: state.has_all(["Glide", "CleanVents"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("anthony_hill_room_50_disk", p),
             lambda state: state.has_all(["Glide", "CleanVents", "ProgressiveSwordWaves"], p) and state.has("ProgressiveDash", p, 3))
    
    # Momoyama
   #  set_rule(multiworld.get_location("momoyama_room_36_map", p),
   #           lambda state: True)
   #  set_rule(multiworld.get_location("momoyama_room_52_book", p),
   #           lambda state: True)
    set_rule(multiworld.get_location("samurai", p),
             lambda state: True)
    set_rule(multiworld.get_location("anthony_hill_room_64_dashslash", p),
             lambda state: state.has("SamuraiDefeated", p))
    
    # Industry Zone
    set_rule(multiworld.get_location("industry_zone_room_118_disk", p),
             lambda state: state.has_all(["ProgressiveDash", "DashSlash", "ProgressiveSwordWaves"], p) and (state.has("ThrustUp", p) or state.has("ProgressiveDash", p, 3)))
    set_rule(multiworld.get_location("industry_zone_room_123_newspaper", p),
             lambda state: state.has_all(["ProgressiveDash", "DashSlash", "ProgressiveSwordWaves", "GasMask"], p)
                and (state.has("ThrustUp", p) or state.has("ProgressiveDash", p, 3)))
    set_rule(multiworld.get_location("industry_zone_room_112_hacker", p),
             lambda state: state.has_all(["ProgressiveDash", "DashSlash", "ProgressiveSwordWaves", "GasMask"], p)
                and (state.has("ThrustUp", p) or state.has("ProgressiveDash", p, 3)))
    
    # Subway Depot
    set_rule(multiworld.get_location("subway_depot_room_105_swordwaves", p),
             lambda state: state.has("Hacker", p))
    set_rule(multiworld.get_location("subway_depot_room_17_tape", p),
             lambda state: state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("subway_depot_room_92_hooklength", p),
             lambda state: state.has("Hacker", p) and state.has("ProgressiveSwordWaves", p, 2))
    set_rule(multiworld.get_location("subway_depot_room_110_poster", p),
             lambda state: state.has("Hacker", p) and state.has("ProgressiveSwordWaves", p, 2) and state.has("ProgressiveDash", p, 2))
    
    # Emperor Tower
    set_rule(multiworld.get_location("emperor_tower_room_155_manual", p),
             lambda state: state.has("DashSlash", p) and (state.has("ThrustUp", p) or state.has("ProgressiveDash", p, 3)))
    set_rule(multiworld.get_location("emperor_tower_room_130_letter", p),
             lambda state: state.has("DashSlash", p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_101_lifeshard", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_133_photo", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves", "Hacker", "DashSlash"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_140_newspaper", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves", "Hacker", "DashSlash", "ThrustUp"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_142_dashdamage", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves", "Hacker", "DashSlash", "ThrustUp"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_143_disk", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves", "Hacker", "DashSlash", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4)
               and state.has("EnergyShard", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_154_tape", p),
             lambda state: state.has_all(["Glide", "ProgressiveSwordWaves", "Hacker", "DashSlash", "ThrustUp"], p) and state.has("ProgressiveDash", p, 3))
    set_rule(multiworld.get_location("emperor_tower_room_127_report", p),
             lambda state: state.has_all(["DashSlash", "Hacker"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_127_critrate", p),
             lambda state: state.has_all(["DashSlash", "Hacker"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_146_dye", p),
             lambda state: state.has_all(["DashSlash", "Glide", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_146_lifeshard", p),
             lambda state: state.has_all(["DashSlash", "Glide", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_151_disk", p),
             lambda state: state.has_all(["DashSlash", "Glide", "Hacker", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("emperor_tower_room_149_devlog", p),
             lambda state: state.has_all(["DashSlash", "Glide", "Hacker", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4))
    set_rule(multiworld.get_location("gael", p),
             lambda state: state.has_all(["DashSlash", "Glide", "Hacker", "ThrustUp"], p) and state.has("ProgressiveDash", p, 4))
    
    multiworld.completion_condition[p] = lambda state: state.has("Victory", p)