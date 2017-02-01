entrada=input("Ingrese la distancia recorrida en km: ")
def tarifa(x):
    distancia=[x]
    banderazo=8.74
    km=1.84*4
    cantidad=0
    for x in distancia:
        cantidad=cantidad+banderazo+(x*km)
        print "Cantidad a pagar =","$",cantidad
salida=tarifa(entrada)
