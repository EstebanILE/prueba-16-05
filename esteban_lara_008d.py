
import time 
import os 
limpia_pantalla ="cls"
os.system(limpia_pantalla)
time.sleep(3)
entrar = 1
multa =1700 
camion_ = 765000
cantidad_camion = 0
dinero_total= 0
cilindro5 : 0
cilindros15 = 0
cilindros45 = 0
cantidad_k = 0
cantidad_kilos = 0
print("Bienvenido ")
while entrar ==1:
   

    nombre_cliente = input("ingrese su nombre: ")
    telefono_cliente = int(input("ingrese su numero: "))

    print("esta correcto el nombre: " + nombre_cliente)
    print(f"esta correcto el telefono:{telefono_cliente} ")
    print("1. Esta correcto")
    print("2. esta incorrecto")

    res = int(input("ingrese su respuesta (1-2):"))

    if res == 1:
        print("hola")
        os.system(limpia_pantalla)
        entrar += 1
        break
    elif res == 2:
        time.sleep(1)
        os.system(limpia_pantalla)

while entrar ==2:
    print("bienvenido al menu "+nombre_cliente)
    print("1.Comprar entrega de camiones estandar")
    print("2.comprar entrega carga especifica")
    print("3.imprimir boleta y cerrar pedido")
    res_2 =int(input("respuesta (1-3):"))
    



    if res_2 ==1:
        cantidad_camion +=int(input("¿cantidad de camiones estandar quiere?: "))
        print(f"cantidad de camiones es :{cantidad_camion}")
        time.sleep(3)
        os.system(limpia_pantalla)
    
    elif res_2 ==3:
        print("seperdio")
        os.system(limpia_pantalla)
        break
    while res_2 ==2:
        
        os.system(limpia_pantalla)
        print("decidio carga espesifica")
        print("1.desea cilindros de 5 kilos")
        print("2.desea cilindros de 15 kilos")
        print("3.desea cilindros de 45 kilos")
        print("4.esta listo mi pedido")
        res_3 =int(input("ingrese su respuesta (1-4): "))

        if res_3 == 1:
            print("decidio cilindros de 5 kilos")
            rescilindro5=int(input("ingrese la cantidad de cilindros de 5 kilos quiere:"))
            cilindro5 =(rescilindro5*5)
            time.sleep(2)
            os.system(limpia_pantalla)
        elif res_3 ==2:
            print("decidio cilindros de 15 kilos")
            rescilindro15=int(input("ingrese la cantidad de cilindros de 15 kilos quiere:"))
            cilindros15 =(rescilindro15*15)
            time.sleep(2)
            os.system(limpia_pantalla)
        elif res_3 ==3:
            print("decidio cilindros de 45 kilos")
            rescilindro45=int(input("ingrese la cantidad de cilindros de 45 kilos quiere:"))
            cilindros45 =(rescilindro45*45)
            time.sleep(2)
            os.system(limpia_pantalla)
        
        elif res_3 == 4:
            os.system(limpia_pantalla)
            break
        else:
            print("ingrese una opcion correcta")
            time.sleep(3)
            os.system(limpia_pantalla)
        

cantidad_kilos =(cilindro5+cilindros15+cilindros45)
    


while entrar ==4:
    print(f"cliente: {nombre_cliente}")
    print(f"telefono: {telefono_cliente}")
    print(f"cantidad de kilos:{cantidad_kilos}")
    print(f"camiones:{cantidad_camion}")
    print(f"valor total:{dinero_total}")
   





