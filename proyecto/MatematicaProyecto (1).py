class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def crear_raiz(self, valor):
        if self.raiz is not None:
            print("Ya existe una raíz.")
        else:
            self.raiz = Nodo(valor)
            print(f"Raíz '{valor}' creada correctamente.")

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            print(f"Raíz '{valor}' creada correctamente.")
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor == nodo.valor:
            print("El valor ya existe, no se puede agregar.")
            return
        elif valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
                print(f"Hijo izquierdo '{valor}' agregado a '{nodo.valor}'.")
            else:
                self._insertar(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
                print(f"Hijo derecho '{valor}' agregado a '{nodo.valor}'.")
            else:
                self._insertar(nodo.derecho, valor)

    def mostrar_arbol(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            print("El árbol está vacío.")
            return
        # Mostrar primero el lado derecho, luego el nodo, y después el izquierdo
        if nodo.derecho:
            self.mostrar_arbol(nodo.derecho, nivel + 1)
        print("   " * nivel + f"- {nodo.valor}")
        if nodo.izquierdo:
            self.mostrar_arbol(nodo.izquierdo, nivel + 1)

    def preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierdo)
            self.preorden(nodo.derecho)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecho)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierdo)
            self.postorden(nodo.derecho)
            print(nodo.valor, end=" ")

    def altura(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    def es_binario(self, nodo):
        # Este árbol siempre será binario porque solo acepta dos hijos
        return True

# ---------------- MENÚ PRINCIPAL ----------------

def menu():
    arbol = Arbol()
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear nodo raíz")
        print("2. Agregar nodo")
        print("3. Mostrar árbol (texto)")
        print("4. Recorridos: Preorden, Inorden, Postorden")
        print("5. Altura del árbol")
        print("6. Es binario (sí o no)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            valor = input("Ingrese el valor de la raíz: ")
            arbol.crear_raiz(valor)

        elif opcion == "2":
            valor = input("Ingrese el valor del nuevo nodo: ")
            arbol.insertar(valor)

        elif opcion == "3":
            print("\nEstructura del árbol:")
            arbol.mostrar_arbol()

        elif opcion == "4":
            if arbol.raiz:
                print("Preorden:", end=" "); arbol.preorden(arbol.raiz); print()
                print("Inorden:", end=" "); arbol.inorden(arbol.raiz); print()
                print("Postorden:", end=" "); arbol.postorden(arbol.raiz); print()
            else:
                print("El árbol está vacío.")

        elif opcion == "5":
            if arbol.raiz:
                print("Altura del árbol:", arbol.altura(arbol.raiz))
            else:
                print("El árbol está vacío.")

        elif opcion == "6":
            print("El árbol es binario (cada nodo tiene como máximo 2 hijos).")

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu()