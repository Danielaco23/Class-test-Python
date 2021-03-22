class Persona():
    def __init__(self):
        self.nombre = input("Introduce el nombre: ")
        self.edad = str(input("Introduce la edad: "))
        self.residencia = input("Introduce la residencia: ")

class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = str(input("Introduce el sueldo: "))
        self.antiguedad = str(input("Introduce la antiguedad: "))

class Registro():
    def __init__(self,Lista):
        

        self.datos = []
        self.ListaNombres = []
        self.ListaEdad = []
        self.ListaResidencia = []
        self.ListaSueldo = []
        self.ListaAntiguedad = []

        for i in Lista:
            self.datos.append(i.nombre)
            self.datos.append(i.edad)
            self.datos.append(i.residencia)
            self.datos.append(i.sueldo)
            self.datos.append(i.antiguedad)

        self.longitud = len(self.datos)

        x = 0
        while x < self.longitud:
            self.ListaNombres.append(self.datos[x])
            self.ListaEdad.append(self.datos[x+1])
            self.ListaResidencia.append(self.datos[x+2])
            self.ListaSueldo.append(self.datos[x+3])
            self.ListaAntiguedad.append(self.datos[x+4])
            x = x + 5

        x = 0
        self.Temp = 0
        while x < len(self.ListaNombres):
            if self.Temp > len(self.ListaNombres[x]):
                True
            else:
                self.Temp = len(self.ListaNombres[x])
            x = x + 1
        x = 0
        while x < len(self.ListaEdad):
            if self.Temp > len(self.ListaEdad[x]):
                True
            else:
                self.Temp = len(self.ListaEdad[x])
            x = x + 1
        x = 0
        while x < len(self.ListaResidencia):
            if self.Temp > len(self.ListaResidencia[x]):
                True
            else:
                self.Temp = len(self.ListaResidencia[x])
            x = x + 1
        x = 0
        while x < len(self.ListaSueldo):
            if self.Temp > len(self.ListaSueldo[x]):
                True
            else:
                self.Temp = len(self.ListaSueldo[x])
            x = x + 1
        x = 0
        while x < len(self.ListaAntiguedad):
            if self.Temp > len(self.ListaAntiguedad[x]):
                True
            else:
                self.Temp = len(self.ListaAntiguedad[x])
            x = x + 1

    def listado(self):
        print("Nombre:".ljust(self.Temp+5," "),"Edad:".ljust(self.Temp+5," "),"Resisidencia:".ljust(self.Temp+10," "),"Sueldo:".ljust(self.Temp+5," "),"Antiguedad:")

        i = 0
        while (i < self.longitud):
            print(self.datos[i].ljust(self.Temp+5," "),self.datos[i+1].ljust(self.Temp+5," "),self.datos[i+2].ljust(self.Temp+10," "),end=" ")
            print(self.datos[i+3].ljust(self.Temp+5," "),self.datos[i+4])
            i = i + 5

def main():
    rep = 0
    Lista = []

    while rep == 0:

        Mike = Trabajador()
        Lista.append(Mike)

        ver = ""
        while True:
            ver = input("Desea introducir otro? (Y/N) ")

            if ((ver == "Y")|(ver == "y")):
                rep = 0
                break

            elif ((ver == "N")|(ver == "n")):
                rep = 1
                break

            else:
                print("Entrada no válida")

    Reg = Registro(Lista)

    Reg.listado()

if __name__ == "__main__":
    main()