from tkinter import *

Nombre = ""
Edad = ""
Residencia = ""
Sueldo = ""
Antiguedad = ""

class Trabajador():
    def __init__(self,Nombre,Edad,Residencia,Sueldo,Antiguedad):
        self.nombre = Nombre
        self.edad = Edad
        self.residencia = Residencia
        self.sueldo = Sueldo
        self.antiguedad = Antiguedad

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
        raiz = Tk()

        miFrame = Frame(raiz, width=500, height=400)

        miFrame.pack()

        miNombre = StringVar()
        miEdad = IntVar()
        miResidencia = StringVar()
        miSueldo = IntVar()
        miAntiguedad = IntVar()

        miLabel = Label(miFrame, text="Nombre")
        miLabel.config(fg="blue",font=("Comic Sans MS", 20), anchor="w")
        miLabel.grid(row=0,column=0)

        miEntry = Entry(miFrame, textvariable=miNombre)
        miEntry.grid(row=0,column=1)
        miEntry.config(fg="blue", font=("Comic Sans MS", 20))


        miLabel = Label(miFrame, text="Edad")
        miLabel.config(fg="blue",font=("Comic Sans MS", 20), anchor="w")
        miLabel.grid(row=1,column=0)

        miEntry = Entry(miFrame, textvariable=miEdad)
        miEntry.grid(row=1,column=1)
        miEntry.config(fg="blue", font=("Comic Sans MS", 20))


        miLabel = Label(miFrame, text="Residencia")
        miLabel.config(fg="blue",font=("Comic Sans MS", 20), anchor="w")
        miLabel.grid(row=2,column=0)

        miEntry = Entry(miFrame, textvariable=miResidencia)
        miEntry.grid(row=2,column=1)
        miEntry.config(fg="blue", font=("Comic Sans MS", 20))


        miLabel = Label(miFrame, text="Sueldo")
        miLabel.config(fg="blue",font=("Comic Sans MS", 20), anchor="w")
        miLabel.grid(row=3,column=0)

        miEntry = Entry(miFrame, textvariable=miSueldo)
        miEntry.grid(row=3,column=1)
        miEntry.config(fg="blue", font=("Comic Sans MS", 20))


        miLabel = Label(miFrame, text="Antigüedad")
        miLabel.config(fg="blue",font=("Comic Sans MS", 20), anchor="w")
        miLabel.grid(row=4,column=0)

        miEntry = Entry(miFrame, textvariable=miAntiguedad)
        miEntry.grid(row=4,column=1)
        miEntry.config(fg="blue", font=("Comic Sans MS", 20))

        def borrado():
            miNombre.set("")
            miEdad.set(0)
            miResidencia.set("")
            miSueldo.set(0)
            miAntiguedad.set(0)

        miBoton = Button(miFrame, text="borrar",command=borrado)
        miBoton.grid(row=5,column=1)
        miBoton.config(fg="black", bg="red", font=("Comic Sans MS", 12), anchor="w")
        miBoton

        raiz.mainloop()

        Nombre = miNombre.get()
        Edad = str(miEdad.get())
        Residencia = miResidencia.get()
        Sueldo = str(miSueldo.get())
        Antiguedad = str(miAntiguedad.get())

        Mike = Trabajador(Nombre,Edad,Residencia,Sueldo,Antiguedad)
        Lista.append(Mike)

        ver = ""
        while True:
            raiz = Tk()

            miFrame = Frame(raiz, width=500, height=400)

            miFrame.pack()
            miVer = StringVar()

            miLabel = Label(miFrame,text="Desea introducir otro? (Y/N) ")
            miEntry = Entry(miFrame,textvariable=miVer)

            ver = miVer.get()
            if ((ver == "Y")|(ver == "y")):
                rep = 0
                break

            elif ((ver == "N")|(ver == "n")):
                rep = 1
                break

            else:
                print("Entrada no válida")

            raiz.mainloop()

    Reg = Registro(Lista)

    Reg.listado()

if __name__ == "__main__":
    main()