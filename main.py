from arbol_avl import AgendaTelefonicaAVL

agenda = AgendaTelefonicaAVL()
raiz = None


print("Ejercicio 1:")
lista1 = [("30", "11111111", "aaa.com"), ("20", "22222222", "bbb.com"), ("10", "33333333", "ccc.com"),
            ("25", "44444444", "ddd.com"), ("40", "55555555", "eee.com"), ("50", "66666666", "fff.com"),
            ("12", "77777777", "ggg.com"), ("7", "88888888", "hhh.com")]

for nombre, tel, correo in lista1:
    raiz = agenda.insertar(raiz, nombre, tel, correo)
    agenda.mostrar_inorden(raiz)
    print("            ")


print("\nEjercicio 2:")
raiz2 = None
lista2 = [("50", "11111111", "aaa.com"), ("60", "22222222", "bbb.com"), ("40", "33333333", "ccc.com"),
            ("45", "44444444", "ddd.com"), ("42", "55555555", "eee.com"), ("43", "66666666", "fff.com"),
            ("15", "77777777", "ggg.com"), ("1", "88888888", "hhh.com")]

for nombre, tel, correo in lista2:
    raiz2 = agenda.insertar(raiz2, nombre, tel, correo)
    agenda.mostrar_inorden(raiz2)
    print("            ")


print("\nEjercicio 3:")
raiz3 = None
lista3 = [("70", "11111111", "aaa.com"), ("60", "22222222", "bbb.com"), ("80", "33333333", "ccc.com"),
            ("90", "44444444", "ddd.com"), ("85", "55555555", "eee.com"), ("75", "66666666", "fff.com"),
            ("87", "77777777", "ggg.com"), ("3", "88888888", "hhh.com"), ("1", "99999999", "iii.com")]

for nombre, tel, correo in lista3:
    raiz3 = agenda.insertar(raiz3, nombre, tel, correo)
    agenda.mostrar_inorden(raiz3)
    print("            ")


print("\nEjercicio 4:")
busqueda = agenda.buscar(raiz3, "75")
if busqueda:
    print(f"Resultado de búsqueda:")
    print(f"Nombre: {busqueda.nombre}")
    print(f"Teléfono: {busqueda.telefono}")
    print(f"Correo: {busqueda.correo}")
else:
    print("Contacto no encontrado.")
