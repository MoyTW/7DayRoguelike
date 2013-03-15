__author__ = 'Travis Moy'

import functools
import math
import string


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
        else:
            return self.key < other.key

    def __repr__(self):
        return "({0}, p={1})".format(self.key, self.page)


class Inventory(object):

    def __init__(self, max_items, max_weight):
        self.max_items = max_items
        self.max_weight = max_weight
        self.item_dict = {}
        self._init_dictionary()

    def search_items_for(self, query):
        pass

    #def get_item(self, ):

    def _init_dictionary(self):
        for i in range(0, self.max_items):
            if i > 0:
                page = i / len(string.ascii_letters)
            else:
                page = 0
            index = IndexPair(string.ascii_letters[i % len(string.ascii_letters)], page)
            self.item_dict[index] = None