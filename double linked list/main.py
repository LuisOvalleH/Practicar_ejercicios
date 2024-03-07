from double_linked_list import DoublyLinkedList
lista  = DoublyLinkedList[int]()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.prepend(5)

print(lista.transversal())

print("Eliminamos nodo en la posicion 3",lista.delete_at(3))

print(lista.transversal())




