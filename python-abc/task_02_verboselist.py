#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """A special list class that displays a notification on the screen for each operation"""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extenden(self, item_list):
        length = len(item_list)
        super().extend(item_list)
        print("Extended the list with [{}] item".format(length))

    def remove(self, item):
        print("Remove [{}] from the list".format(item))
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print("Popped [{}] from the list".format(item))
        return super().pop(index)
