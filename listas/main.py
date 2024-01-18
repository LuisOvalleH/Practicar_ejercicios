from list import List
from student import Student

est1 = Student("carlos", "18", "1515922")
est2 = Student("maria", "19", "1252313")
lista = List()
lista.append(est1)
lista.append(est2)
while True:
    print("****MENU DE ESTUDIANTES****")
    print("1-Mostrar estudiantes")
    print("2-Buscar estudiante")
    print("3-Eliminar estudiante")
    print("4-Agregar estudiante")
    option = int(input("Ingrese una opcion de la lista:"))
    if option == 1:
        print("****LISTA DE ESTUDIANTES****")
        print(lista.transversal())

    if option == 2:
        carnet = input("Ingrese el carnet del estudiante:")
        print(lista.search_by_value(carnet))

    if option == 3:
        carnet = input("Ingrese el carnet del estudiante para borrarlo:")
        lista.remove_by_value(carnet)
        print("---Se elimino el estudiante---")
        print(lista.transversal())

    if option == 4:
        nombre = input("ingrese el nombre:")
        edad = input("Ingrese la edad:")
        carnet = input("Ingrese el carnet:")
        student = Student(nombre,edad,carnet)
        lista.append(student)
        print(lista.transversal())


