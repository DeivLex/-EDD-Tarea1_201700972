import sys
#Clase nodo simple con puntero
class Nodo(object) :
    def __init__(self,elemento) :
        #atributo que tendra el nodo
        self.__elemento=elemento
        self.pSig = None
    def getElemento(self) :
        return self.__elemento
#Clase lista simple
class ListaSimple(object) :
    def __init__(self) :
        self.__primero = None
        self.__ultimo = None

    def getVacio(self) :
        if self.__primero == None:
            return True
    def InsertarAlInicio(self,elemento) :
        nuevo = Nodo(elemento)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            nuevo.pSig = self.__primero
            self.__primero = nuevo
    def InsertarAlFinal(self,elemento) :
        nuevo = Nodo(elemento)
        if self.getVacio()==True:
            self.__primero = self.__ultimo = nuevo
        else:
            self.__ultimo.pSig = nuevo
            self.__ultimo = nuevo
    def eliminarPrimero(self):
        if self.getVacio()==True:
            print("Lista vacia, no se puede eliminar")
        elif self.__primero == self.__ultimo:
            self.__primero = None
            self.__ultimo = None
            print("Elemento eliminado, la lista esta vacia")
        else:
            temp = self.__primero
            self.__primero = self.__primero.pSig
            temp = None
            print("Elemento eliminado")
    def eliminarUltimo(self):
        if self.getVacio() == True:
            print("Lista vacia, no se puede eliminar")
        elif self.__primero == self.__ultimo:
            self.__primero = None
            self.__ultimo = None
            print("Elemento eliminado, la lista esta vacia")
        else:
            validar = True
            temp = self.__primero
            while(validar):
                if temp.pSig == self.__ultimo:
                    temp2 = self.__ultimo
                    self.__ultimo = temp
                    temp2 = None
                    validar = False
                    print("Elemento eliminado")
                else:
                    temp = temp.pSig

    # Método para eleminar nodos
    def EliminarNodo(self,item):
        actual = self.__primero
        previo = None
        encontrado = False
        while not encontrado:
            if actual.getElemento() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.pSig

        if previo == None:
            self.__primero = actual.pSig
        else:
            previo.pSig = actual.pSig
    # Método para modificar nodos
    def ModificarNodo(self,d,item):
    #a nodo actual se le asigna el primer nodo.
        nodoActual = self.__primero
            #Mientras exista el nodo actual.
        while nodoActual:
                #Si el dato de nodo actual es igual a d, devuelve d
            if nodoActual.getElemento() == d:
                nodoActual = item
                return nodoActual
            else:
                    #Si no, el nodo actual apunta al proximo nodo.
                nodoActual = nodoActual.pSig
            #Si no se encuentra devuelve None.
        return None
        

    def getNodoPrimero(self):
        if self.getVacio() ==True:
            return ("Lista vacia")
        else:
            return self.__primero
    def getNodoUltimo(self):
        if self.getVacio() ==True:
            return ("Lista vacia")
        else:
            return self.__ultimo
    def ImprimirLista(self):
        if self.getVacio()==True:
            print("Lista vacia")
        else:
            validar = True
            temp = self.__primero
            while(validar):
                print(temp.getElemento())
                if temp == self.__ultimo:
                    validar = False
                else:
                    temp = temp.pSig


if __name__ == "__main__":
    listas = ListaSimple()
    while(True):
        print("-----Menu-----\n"+
            "1. Insertar inicio\n"+
            "2. Insertar final\n"+
            "3. Modificar\n"+
            "4. Imprimir\n"+
            "5. Eliminar por dato\n"+
            "6. Eliminar ultimo\n"+
            "7. Salir\n")
        num = input("Ingrese la opcion: ")
        if num == "1":
            dato = input("Ingresar dato: ")
            listas.InsertarAlInicio(dato)
        elif num == "2":
            dato = input("Ingresar dato: ")
            listas.InsertarAlFinal(dato)
        elif num == "3":
            dato = input("Ingresar dato a modificar: ")
            dato1 = input("Ingresar nuevo dato: ")
            listas.ModificarNodo(dato,dato1)
        elif num == "4":
            listas.ImprimirLista()
        elif num == "5":
            dato = input("Ingresar dato a eliminar: ")
            listas.EliminarNodo(dato)
        elif num == "6":
            listas.eliminarUltimo()
            print("Se elimino el ultimo dato")
        elif num == "7":
            sys.exit()
        else:
            print("Numero ingresado es invalido")
