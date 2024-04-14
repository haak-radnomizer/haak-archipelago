from BaseClasses import Location

haak_location_offset =                  135293100000
sanho_ruins_offset =      haak_location_offset+ 0000
neo_sano_offset =         haak_location_offset+ 1000
north_station_offset =    haak_location_offset+ 2000
subway_tunnel_offset =    haak_location_offset+ 3000
peoples_square_offset =   haak_location_offset+ 4000
whitestone_offset =       haak_location_offset+ 5000
brewery_offset =          haak_location_offset+ 6000
sillie_farm_offset =      haak_location_offset+ 7000
merlin_pit_offset =       haak_location_offset+ 8000
anthony_hill_offset =     haak_location_offset+ 9000
momoyama_offset =         haak_location_offset+10000
industry_zone_offset =    haak_location_offset+11000
subway_depot_offset =     haak_location_offset+12000
emperors_tower_offset =   haak_location_offset+13000

class HaakLocation(Location):
    game= "Haak"

    def __init__(self, player: int, name: str, address=None, parent=None):
        super(HaakLocation, self).__init__(player, name, address, parent)
        if address is None:
            self.event = True
            self.locked = True

location_table_sanho_ruins = {
    # Sanho Ruins
    "sanho_ruins_room_73_keycard": sanho_ruins_offset+1,
    "sanho_ruins_room_62_glove": sanho_ruins_offset+2,
    "sanho_ruins_room_60_disk": sanho_ruins_offset+3,
    "sanho_ruins_room_62_lifeshard": sanho_ruins_offset+4,
    "sanho_ruins_room_64_lifeshard": sanho_ruins_offset+5,
    "sanho_ruins_room_76_dye": sanho_ruins_offset+6,
    "sanho_ruins_room_61_newspaper": sanho_ruins_offset+7,
    "sanho_ruins_room_74_hookspeed": sanho_ruins_offset+8,
    "sanho_ruins_room_53_firstaid": sanho_ruins_offset+9,
    "sanho_ruins_room_58_keycard": sanho_ruins_offset+10,
    "sanho_ruins_room_58_disk": sanho_ruins_offset+11,
    "sanho_ruins_room_55_lifeshard": sanho_ruins_offset+12,
    "sanho_ruins_room_56_dash": sanho_ruins_offset+13,
    "sanho_ruins_room_71_tvantenna": sanho_ruins_offset+14,
    "sanho_ruins_room_47_newspaper": sanho_ruins_offset+15,
    "sanho_ruins_room_47_hooklength": sanho_ruins_offset+16,
    "sanho_ruins_room_66_metalsniffer": sanho_ruins_offset+17,
    "sanho_ruins_room_53_disk": sanho_ruins_offset+18,
    "sanho_ruins_room_69_lifeshard": sanho_ruins_offset+19,
    "sanho_ruins_room_69_attackboost": sanho_ruins_offset+20,
    "sanho_ruins_room_34_lifeshard": sanho_ruins_offset+21,
    "sanho_ruins_room_64_critrate": sanho_ruins_offset+22,
    "sanho_ruins_room_54_flyer": sanho_ruins_offset+23,
    "sanho_ruins_room_56_disk": sanho_ruins_offset+24,
}

location_table_neo_sanho = {
    "neo_sanho_room_16_lifeshard": neo_sano_offset,
    "neo_sanho_room_16_hooklength": neo_sano_offset+1,
    "neo_sanho_room_16_firstaid": neo_sano_offset+2,
    "neo_sanho_room_16_instantcharge": neo_sano_offset+3,
    "neo_sanho_room_16_hookspeed": neo_sano_offset+4,
    "neo_sanho_room_16_energyshard": neo_sano_offset+5,
    "neo_sanho_room_16_attackboost": neo_sano_offset+6,
    "neo_sanho_room_16_ultimatehook": neo_sano_offset+7,
    "neo_sanho_room_16_critrate": neo_sano_offset+8,
    "neo_sanho_room_16_attackboost": neo_sano_offset+9,
    "neo_sanho_room_16_photo": neo_sano_offset+10,
    "neo_sanho_room_23_disk": neo_sano_offset+11,
    "neo_sanho_room_5_book": neo_sano_offset+12,
    "neo_sanho_room_5_diary": neo_sano_offset+13,
    "neo_sanho_room_14_tape": neo_sano_offset+14,
    "neo_sanho_room_13_report": neo_sano_offset+15,
    "neo_sanho_room_5_powercord": neo_sano_offset+16,
    "neo_sanho_room_13_stereo": neo_sano_offset+17,
    "neo_sanho_room_12_disk": neo_sano_offset+18,
    "neo_sanho_room_22_picture": neo_sano_offset+19,
}


location_table_north_station = {
    "north_station_room_58_tvmotherboard": north_station_offset,
    "north_station_room_82_keycard": north_station_offset+1,
    "north_station_room_55_dye": north_station_offset+2,
    "north_station_room_48_lifeshard": north_station_offset+3,
    "north_station_room_63_disk": north_station_offset+4,
    "north_station_room_63_newspaper": north_station_offset+5,
    "north_station_room_67_disk": north_station_offset+6,
    "north_station_room_60_chargeattack": north_station_offset+7,
    "north_station_room_68_encryptednote": north_station_offset+8,
    "north_station_room_56_deflection": north_station_offset+9,
    "north_station_room_87_lifeshard": north_station_offset+10,
    "north_station_room_82_disk": north_station_offset+11,
    "north_station_room_89_disk": north_station_offset+12,
    "north_station_room_53_disk": north_station_offset+13,
    "north_station_room_67_intellectuals_spring": north_station_offset+14,
    "north_station_room_58_piercinghook": north_station_offset+15,
    "north_station_room_83_hunting_cert": north_station_offset+16,
    "north_station_room_86_disk": north_station_offset+17,
    "north_station_room_54_encryptednoted": north_station_offset+18,
    "north_station_room_54_hookspeed": north_station_offset+19,
    "north_station_room_52_critrate": north_station_offset+20,
    "north_station_room_51_hooklength": north_station_offset+21,
    "north_station_room_76_disk": north_station_offset+22,
    "north_station_room_84_firstaideffect": peoples_square_offset+28,
    "north_station_room_57_lifeshard": north_station_offset+29,
}


location_table_subway_tunnel = {
    "subway_tunnel_room_21_disk": subway_tunnel_offset,
    "subway_tunnel_room_25_energyshard": subway_tunnel_offset+1,
    "subway_tunnel_room_26_swordwaves": subway_tunnel_offset+2,
    "subway_tunnel_room_26_lifeshard": subway_tunnel_offset+3,
    "subway_tunnel_room_29_electrichook": subway_tunnel_offset+4,
    "subway_tunnel_room_33_disk": subway_tunnel_offset+5,
    "subway_tunnel_room_33_disk2": subway_tunnel_offset+6,
    "subway_tunnel_room_27_disk": subway_tunnel_offset+7,
    "subway_tunnel_room_17_newspaper": subway_tunnel_offset+8,
}

location_table_peoples_square = {
    "peoples_square_room_80_keycard": peoples_square_offset,
    "peoples_square_room_63_disk": peoples_square_offset+1,
    "peoples_square_room_69_lifeshard": peoples_square_offset+2,
    "peoples_square_room_55_disk": peoples_square_offset+3,
    "peoples_square_room_55_disk2": peoples_square_offset+4,
    "peoples_square_room_62_critrate": peoples_square_offset+5,
    "peoples_square_room_74_newspaper": peoples_square_offset+6,
    "peoples_square_room_70_divingthrust": peoples_square_offset+7,
    "peoples_square_room_79_dye": peoples_square_offset+8,
    "peoples_square_room_66_encryptednote": peoples_square_offset+9,
    "peoples_square_room_49_disk": peoples_square_offset+10,
    "peoples_square_room_49_disk2": peoples_square_offset+11,
    "peoples_square_room_49_lifeshard": peoples_square_offset+12,
    "peoples_square_room_56_lifeshard": peoples_square_offset+13,
    "peoples_square_room_68_disk": peoples_square_offset+14,
    "peoples_square_room_53_disk": peoples_square_offset+15,
    "peoples_square_room_60_boostedcharge": peoples_square_offset+16,
    "peoples_square_room_62_catfood": peoples_square_offset+17,
    "peoples_square_room_61_hookspeed": peoples_square_offset+18,
    "peoples_square_room_65_disk": peoples_square_offset+19,
    "peoples_square_room_68_disk": peoples_square_offset+21,
    "peoples_square_room_70_critrate": peoples_square_offset+22,
    "peoples_square_room_71_disk": peoples_square_offset+23,
    "peoples_square_room_69_picture": peoples_square_offset+24,
    "peoples_square_room_50_disk": peoples_square_offset+25,
    "peoples_square_room_57_lifeshard": peoples_square_offset+26,
    "peoples_square_room_59_lifeshard": peoples_square_offset+27,
    "fatty": None,
}

location_table_whitestone = {
    "whitestone_room_3_lifeshard": whitestone_offset,
    "whitestone_room_4_passcard": whitestone_offset+1,
    "whitestone_room_6_disk": whitestone_offset+2,
}

location_table_brewery = {
    "brewery_room_115_devlog": brewery_offset,
    "brewery_room_94_map": brewery_offset+1,
    "brewery_room_92_attackboost": brewery_offset+2,
    "brewery_room_80_rampage": brewery_offset+3,
    "brewery_room_91_disk": brewery_offset+4,
    "brewery_room_101_lifeshard": brewery_offset+5,
    "brewery_room_84_flyer": brewery_offset+6,
    "brewery_room_84_dye": brewery_offset+7,
    "brewery_room_87_hooklength": brewery_offset+8,
    "brewery_room_106_hookspeed": brewery_offset+9,
    "brewery_room_111_lifeshard": brewery_offset+10,
    "brewery_room_104_newspaper": brewery_offset+11,
    "brewery_room_82_note": brewery_offset+12,
    "brewery_room_35_powerdivingthrust": brewery_offset+13,
    "brewery_room_44_disk": brewery_offset+14,
    "brewery_room_107_disk": brewery_offset+15,
    "brewery_room_99_disk": brewery_offset+16,
    "brewery_room_82_dessertrecipe": brewery_offset+17,
}

location_table_sillie_farm = {
    "sillie_farm_room_92_gasmask": sillie_farm_offset,
    "sillie_farm_room_92_disk": sillie_farm_offset+1,
    "sillie_farm_room_92_disk2": sillie_farm_offset+2,
    "sillie_farm_room_84_disk": sillie_farm_offset+3,
    "sillie_farm_room_90_energyshard": sillie_farm_offset+4,
    "sillie_farm_room_9_newspaper": sillie_farm_offset+5,
}

location_table_merlin_pit = {
    "merlin_pit_room_36_thrustup": merlin_pit_offset,
    "merlin_pit_room_69_disk": merlin_pit_offset+1,
    "merlin_pit_room_123_lifeshard": merlin_pit_offset+2,
    "merlin_pit_room_140_disk": merlin_pit_offset+3,
    "merlin_pit_room_37_unlimitedslide": merlin_pit_offset+4,
    "merlin_pit_room_120_hooklength": merlin_pit_offset+5,
    "merlin_pit_room_115_hookspeed": merlin_pit_offset+6,
    "merlin_pit_room_115_disk": merlin_pit_offset+7,
    "merlin_pit_room_57_hooklength": merlin_pit_offset+8,
    "merlin_pit_room_144_lifeshard": merlin_pit_offset+9,
    "merlin_pit_room_124_disk": merlin_pit_offset+10,
    "merlin_pit_room_113_newspaper": merlin_pit_offset+11,
    "merlin_pit_room_110_critrate": merlin_pit_offset+12,
    "merlin_pit_room_110_disk": merlin_pit_offset+13,
    "merlin_pit_room_97_disk": merlin_pit_offset+14,
    "merlin_pit_vent1": None,
    "merlin_pit_vent2": None,
    "merlin_pit_vent3": None,
    "merlin_pit_vent4": None,
    "merlin_pit_vent5": None,
    "molegangleader": None,
}

location_table_anthony_hill = {
    "anthony_hill_room_107_disk": anthony_hill_offset,
    "anthony_hill_room_80_lifeshard": anthony_hill_offset+1,
    "anthony_hill_room_91_critrate": anthony_hill_offset+2,
    "anthony_hill_room_98_glide": anthony_hill_offset+3,
    "anthony_hill_room_50_secretmanual": anthony_hill_offset+4,
    "anthony_hill_room_133_report": anthony_hill_offset+5,
    "anthony_hill_room_59_fulldirectiondash": anthony_hill_offset+6,
    "anthony_hill_room_97_hookspeed": anthony_hill_offset+7,
    "anthony_hill_room_50_disk": anthony_hill_offset+8,
    "anthony_hill_room_80_secretmanual": anthony_hill_offset+9,
    "anthony_hill_room_60_secretmanual": anthony_hill_offset+10,
    "anthony_hill_room_86_flyer": anthony_hill_offset+11,
    "anthony_hill_room_119_laptop": anthony_hill_offset+12,
    "anthony_hill_room_57_study": anthony_hill_offset+13,
    "anthony_hill_room_76_energyshard": anthony_hill_offset+14,
    "anthony_hill_room_76_disk": anthony_hill_offset+15,
    "anthony_hill_room_132_disk": anthony_hill_offset+16,
    "anthony_hill_room_56_disk": anthony_hill_offset+17,
    "anthony_hill_vent6": None,
    "anthony_hill_vent7": None,
    "anthony_hill_vent8": None,
    "anthony_hill_vent9": None,
    "cleanvents": None,
}

# These are in the same room as anthony hills
location_table_momoyama = {
    # Currently missable
    # "momoyama_room_36_map": momoyama_offset,
    # "momoyama_room_52_book": momoyama_offset,
    "anthony_hill_room_64_dashslash": momoyama_offset,
    "samurai": None,
}

location_table_industry_zone = {
    "industry_zone_room_118_disk": industry_zone_offset,
    "industry_zone_room_123_newspaper": industry_zone_offset+1,
    "industry_zone_room_112_hacker": industry_zone_offset+2,
}

location_table_subway_depot = {
    "subway_depot_room_105_swordwaves": subway_depot_offset,
    "subway_depot_room_110_poster": subway_depot_offset+1,
    "subway_depot_room_92_hooklength": subway_depot_offset+2,
    "subway_depot_room_17_tape": subway_depot_offset+3,
}

location_table_emperors_tower = {
    "emperor_tower_room_155_manual": emperors_tower_offset,
    "emperor_tower_room_101_lifeshard": emperors_tower_offset+1,
    "emperor_tower_room_133_photo": emperors_tower_offset+2,
    "emperor_tower_room_140_newspaper": emperors_tower_offset+3,
    "emperor_tower_room_142_dashdamage": emperors_tower_offset+4,
    "emperor_tower_room_143_disk": emperors_tower_offset+5,
    "emperor_tower_room_154_tape": emperors_tower_offset+6,
    "emperor_tower_room_130_letter": emperors_tower_offset+7,
    "emperor_tower_room_127_report": emperors_tower_offset+8,
    "emperor_tower_room_127_critrate": emperors_tower_offset+9,
    "emperor_tower_room_146_dye": emperors_tower_offset+10,
    "emperor_tower_room_146_lifeshard": emperors_tower_offset+11,
    "emperor_tower_room_151_disk": emperors_tower_offset+12,
    "emperor_tower_room_149_devlog": emperors_tower_offset+13,
    "gael": None,
}

location_table = location_table_sanho_ruins | location_table_neo_sanho\
    | location_table_north_station | location_table_subway_tunnel | location_table_peoples_square\
    | location_table_whitestone | location_table_brewery | location_table_sillie_farm\
    | location_table_merlin_pit | location_table_anthony_hill | location_table_momoyama\
    | location_table_industry_zone | location_table_subway_depot | location_table_emperors_tower