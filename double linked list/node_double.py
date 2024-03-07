from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar("T")


class NodeDouble(Generic[T]):
    def __init__(self, data: T):
        self.__data: T = data
        self.__next: NodeDouble | None = None
        self.__prev: NodeDouble | None = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: T):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @next.setter
    def next(self, new_next: NodeDouble[T]):
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev: NodeDouble[T]):
        self.__prev = new_prev
