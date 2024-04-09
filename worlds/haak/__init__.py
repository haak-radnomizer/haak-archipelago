import string

from BaseClasses import Entrance, Item, ItemClassification, Location, MultiWorld, Region, Tutorial
from .Items import item_table, event_item_pairs, locked_item_pairs
from .Locations import location_table
from .Options import haak_options
from .Regions import create_regions
from .Rules import set_rules
from worlds.AutoWorld import WebWorld, World


class HaakWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Haak for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "haak_en.md",
        "haak/en",
        ["Droppel"]
    )]


class HaakWorld(World):
    """
    An Metroidvania set in a desolate world
    """

    option_definitions = haak_options
    game = "Haak"
    topology_present = False
    data_version = 0
    web = HaakWeb()
    required_client_version = (0, 4, 0)

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    def create_items(self):
        # Fill out our pool with our items from item_pool
        pool = []
        for name, data in item_table.items():
            if data.event: # Skip Events
                continue
            for i in range(data.count):
                item = HaakItem(name, self.player)
                pool.append(item)

        self.multiworld.itempool += pool

        # Locked Items
        for location, item in locked_item_pairs.items():
            item = HaakItem(item, self.player)
            self.multiworld.get_location(location, self.player).place_locked_item(item)

        # Events
        for event, item in event_item_pairs.items():
            event_item = HaakItem(item, self.player)
            self.multiworld.get_location(event, self.player).place_locked_item(event_item)

    def set_rules(self):
        set_rules(self.options, self.multiworld, self.player)

    def create_item(self, name: str) -> Item:
        return HaakItem(name, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> dict:
        slot_data = {}
        for option_name in haak_options:
            option = getattr(self.multiworld, option_name)[self.player]
            slot_data[option_name] = option.value
        return slot_data

    def get_filler_item_name(self) -> str:
        return "Nothing"


class HaakItem(Item):
    game = "Haak"

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(HaakItem, self).__init__(
            name,
            ItemClassification.progression if item_data.progression else ItemClassification.filler,
            item_data.code, player
        )
