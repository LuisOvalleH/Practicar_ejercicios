from node import Node

class List:
    def __init__(self):
        self.size = 0
        self.head: Node | None = None
        self.tail: Node | None = None

        self.__aux: Node | None = None

    def prepend(self, data: int):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def append(self, data: int):
        if self.is_empty():
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def search_by_value(self, data: int):
        current = self.head

        while current is not None:
            if current.data == data:
                return current
            else:
                current = current.next

        raise Exception('Elemento no encontrado')

    def search_by_index(self, index: int):
        current = self.head
        current_index = 0
        while current is not None:
            if current_index == index:
                return current
            else:
                current = current.next
                current_index += 1

        raise Exception('La posición no existe')

    def is_empty(self):
        return self.head is None and self.tail is None

    def transversal(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current)
            current = current.next

            if current is not None:
                result += '->'

        return result

    def insert_at(self, data: int, index: int):
        if index == 0:
            self.prepend(data)
        elif index == self.size:
            self.append(data)
        elif 0 < index < self.size:
            new_node = Node(data)
            previous = self.search_by_index(index - 1)
            new_node.next = previous.next
            previous.next = new_node
            self.size += 1
        else:
            raise Exception('La posición no existe')

    def shift(self) -> int:
        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return current.data
        else:
            current = self.head
            self.head = current.next
            current.next = None
            self.size -= 1

            return current.data

    def pop(self) -> int:
        if self.is_empty():
            raise Exception('Subdesbordamiento de lista')
        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size = 0

            return current.data
        else:
            current = self.tail
            previous = self.search_by_index(self.size - 2)
            self.tail = previous
            previous.next = None
            self.size -= 1

            return current.data

    def remove_at(self, index: int) -> int:
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif 0 < index < self.size - 1:
            current = self.search_by_index(index)
            previous = self.search_by_index(index - 1)
            previous.next = current.next
            current.next = None
            self.size -= 1

            return current.data
        else:
            raise Exception('La posición no existe')

    def get_index(self, ref: Node) -> int:
        current_position = 0
        current = self.head

        while current is not None:
            if current is ref:
                return current_position
            else:
                current = current.next
                current_position += 1

        raise Exception('El nodo no se encuentra')

    def remove_by_value(self, data: int) -> int:
        current = self.search_by_value(data)
        if current is self.head:
            return self.shift()
        elif current is self.tail:
            return self.pop()
        else:
            pos = self.get_index(current)
            previous = self.search_by_index(pos - 1)
            previous.next = current.next
            current.next = None
            self.size -= 1

            return current.data

    def _iter_(self):
        self.__aux = self.head

        return self

    def _next_(self):
        if self.__aux is None:
            raise StopIteration
        else:
            current = self.__aux
            self.__aux = self.__aux.next
            return current.data
