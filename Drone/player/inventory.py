__author__ = 'Travis Moy'

import functools
import string
from entity.entity import Entity


@functools.total_ordering
class IndexPair(object):
    def __init__(self, key, page):
        self.key = key
        self.page = page

    def __eq__(self, other):
        return self.key == other.key and self.page == other.page

    def __lt__(self, other):
        if self.page < other.page:
            return True
        elif self.page > other.page:
            return False
        else:
            return self.key < other.key

    def __repr__(self):
        return "({0}, p={1})".format(self.key, self.page)


class Inventory(object):

    def __init__(self, max_items, max_weight):
        self._letter_set = string.ascii_lowercase
        self.max_items = max_items
        self.max_weight = max_weight
        self.num_pages = max_items // len(self._letter_set)
        self._item_dict = {}
        self._init_dictionary()

    def add_item(self, item):
        try:
            key = (key for key, value in self._item_dict.items() if value is None).next()
        except StopIteration:
            return False
        self._item_dict[key] = item

    def remove_item(self, item):
        try:
            key = (key for key, value in self._item_dict.items() if value is item).next()
        except StopIteration:
            print "remove_item({0}) failed! Item was not in the map!".format(item)
            return False
        self._item_dict[key] = None

    def search_items_for(self, query):
        pass

    def get_keys_and_entities_on_page(self, page):
        pair_list = []
        keys = self._item_dict.keys()
        keys.sort()
        offset = page * len(self._letter_set)

        # This would be more elegant with a lesser_of(x, y) function.
        last = (page + 1) * len(self._letter_set)
        if self.max_items < last:
            last = self.max_items

        for i in range(offset, last):
            pair_list.append((keys[i].key, self._item_dict.get(keys[i])))

        return pair_list

    def get_item(self, key, page):
        return self._item_dict.get(IndexPair(key, page))

    def _init_dictionary(self):
        for i in range(0, self.max_items):
            if i > 0:
                page = i // len(self._letter_set)
            else:
                page = 0
            index = IndexPair(self._letter_set[i % len(self._letter_set)], page)
            self._item_dict[index] = None