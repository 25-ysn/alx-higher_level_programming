#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == x else x for x in my_list]
