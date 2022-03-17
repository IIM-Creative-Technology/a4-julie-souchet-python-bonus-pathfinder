from typing import TypeVar, List, Tuple

T = TypeVar("T")
Item = Tuple[int, T]  # priority (lower is better, and data)


def get_sort_key(item: Item):
    return item[0]


class PriorityQueue(List[Item]):
    def append(self, item: Item) -> None:
        if self.__contains__(item):
            self.remove(item)
        super().append(item)
        self.sort(key=get_sort_key)

    def is_in_with_lower_prio(self, item: Item):
        """Returns true if the given item is already
        in queue, but with a lower priority value"""
        for priority, data in self:
            if data == item[1] and priority < item[0]:
                return True
        return False
