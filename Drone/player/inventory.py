__author__ = 'Travis Moy'

import sys
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

    def __hash__(self):
        return self.page * 100 + ord(self.key)

    def __repr__(self):
        return "({0}, p={1})".format(self.key, self.page)


class Inventory(object):

    def __init__(self, max_items=0, max_weight=sys.maxint, contains=None):
        self._letter_set = string.ascii_lowercase
        if contains is not None:
            self.max_items = len(contains)
        else:
            self.max_items = max_items
        self.max_weight = max_weight
        self.num_pages = max_items // len(self._letter_set)
        self._item_dict = {}
        self._init_dictionary(contains)

    def is_full(self):
        try:
            (key for key, value in self._item_dict.items() if value is None).next()
            return False
        except StopIteration:
            return True

    def add_item(self, item):
        if item is None:
            return

        keys = self._item_dict.keys()
        keys.sort()
        for key in keys:
            if self._item_dict[key] is None:
                self._item_dict[key] = item
                print "Should have inserted {0} into {1}".format(item, key)
                return True

        return False

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
        pair = IndexPair(key, page)
        print pair
        print self._item_dict
        return self._item_dict.get(pair)

    def _init_dictionary(self, contains):
        for i in range(0, self.max_items):
            if i > 0:
                page = i // len(self._letter_set)
            else:
                page = 0
            index = IndexPair(self._letter_set[i % len(self._letter_set)], page)
            if contains is not None:
                self._item_dict[index] = contains[i]
            else:
                self._item_dict[index] = None