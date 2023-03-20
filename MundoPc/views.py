from django.shortcuts import render
from .models import Procesador, Gpu, Disco, Ram



class Procesador:
    def __init__(self, nombre, ghz, nucleos, hilos, precio, posicion):
        self.nombre = nombre
        self.ghz = ghz
        self.nucleos = nucleos
        self.hilos = hilos
        self.precio = precio
        self.posicion = posicion

procesadores = [Procesador("Ryzen 5", 3.2, 6, 12, 15000, 1),
                Procesador("Ryzen 7", 3.5, 8, 16, 25000, 2),
                Procesador("Ryzen 9", 4, 10, 20, 35000, 3)]

class Gpu:
    def __init__(self, nombre, vram, pines, precio, posicion):
        self.nombre = nombre
        self.vram = vram
        self.pines = pines
        self.precio = precio
        self.posicion = posicion

gpus = [Gpu("RTX 2080", 8, 6, 50000, 1),
        Gpu("RTX 3080", 8, 8, 70000, 2),
        Gpu("RTX 4080", 16, 16, 130000, 3)]


class Disco:
    def __init__(self, nombre, capacidad, estado, precio, posicion):
        self.nombre = nombre
        self.capacidad = capacidad
        self.estado = estado.upper()
        self.precio = precio
        self.posicion = posicion

discos =[Disco("Samsung", 1, "SDD", 3000, 1),
        Disco("Samsung", 2, "SDD", 5000, 2),
        Disco("Seagate", 2, "HDD", 3400, 3)]


class Ram:
    def __init__(self, nombre, memoria, frecuencia, precio, posicion):
        self.nombre = nombre
        self.memoria = memoria
        self.frecuencia = frecuencia
        self.precio = precio
        self.posicion = posicion

rams = [Ram("Corsair", 16, 4333, 5000, 1),Ram("Viper", 16, 3200, 2800, 2)]





##--------------------------------------------------FUNCION------------------------------------------------
def index(request):
    compra_procesador = 0
    nombre_procesador = None
    compra_Gpu = 0
    nombre_Gpu = None
    compra_discos = 0
    nombre_discos = None
    compra_ram = 0
    nombre_ram = None

    if request.method == 'POST':
        seleccion_procesador = request.POST.get('seleccion_procesador', None)
        

        if seleccion_procesador == "1":
            compra_procesador = procesadores[0].precio
            nombre_procesador = procesadores[0].nombre
        elif seleccion_procesador == "2":
            compra_procesador = procesadores[1].precio
            nombre_procesador = procesadores[1].nombre
        elif seleccion_procesador == "3":
            compra_procesador = procesadores[2].precio
            nombre_procesador = procesadores[2].nombre
    
    
        seleccion_Gpu = request.POST.get('seleccion_Gpu', None)
        

        if seleccion_Gpu == "1":
            compra_Gpu = gpus[0].precio
            nombre_Gpu = gpus[0].nombre
        elif seleccion_Gpu == "2":
            compra_Gpu = gpus[1].precio
            nombre_Gpu = gpus[1].nombre
        elif seleccion_Gpu == "3":
            compra_Gpu = gpus[2].precio
            nombre_Gpu = gpus[2].nombre
    
    
        seleccion_discos = request.POST.get('seleccion_discos', None)
        

        if seleccion_discos == "1":
            compra_discos = discos[0].precio
            nombre_discos = discos[0].nombre
        elif seleccion_discos == "2":
            compra_discos = discos[1].precio
            nombre_discos = discos[1].nombre
        elif seleccion_discos == "3":
            compra_discos = discos[2].precio
            nombre_discos = discos[2].nombre
    
        seleccion_ram = request.POST.get('seleccion_ram', None)
        

        if seleccion_ram == "1":
            compra_ram = rams[0].precio
            nombre_ram = rams[0].nombre
        elif seleccion_ram == "2":
            compra_ram = rams[1].precio
            nombre_ram = rams[1].nombre

    precio_total= 0
    # Calculate the total price of the selected items
    precio_total = (compra_procesador + compra_Gpu + compra_discos + compra_ram)

    # Calculate the total price with 21% VAT
    precio_total_con_iva = precio_total * 1.21

    # Calculate the price with a 10% discount
    precio_con_descuento = precio_total_con_iva * 0.9

    # Calculate the monthly installments for a 12-month plan
    cuotas = round(precio_total_con_iva / 12)    




    context = {
            'procesadores': procesadores,
            'compra_procesador': compra_procesador,
            'nombre_procesador': nombre_procesador,
            'gpus': gpus,
            'compra_Gpu': compra_Gpu,
            'nombre_Gpu': nombre_Gpu,
            'discos': discos,
            'compra_discos': compra_discos,
            'nombre_discos': nombre_discos,
            'rams': rams,
            'compra_ram': compra_ram,
            'nombre_ram': nombre_ram,
            'precio_total': precio_total,
            'precio_total_con_iva': precio_total_con_iva,
            "cuotas":cuotas,
            "precio_con_descuento":precio_con_descuento

    

        }

    

    return render(request, 'index.html', context)


