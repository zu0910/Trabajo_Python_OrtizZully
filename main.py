import json
from os import system # Import para limpir la pantalla de la consola 

with open("./productos.json", encoding="utf-8") as file:#con esto se abre el archivo de productos.json que es donde esta toda la información
    productos=json.load(file)

with open("./ventas.json", encoding="utf-8") as files:#con esto se abre el archivo de ventas.json donde esta vacio
    sales=json.load(files)

with open("./compras.json", encoding="utf-8") as files:#con esto se abre el archivo de compras.json donde esta vacio
    shop=json.load(files)
#boleanito va a ser verdadero
boleanito=True
while boleanito==True:#Mientras boleanito sea verdadero se hara
    #Se le mostrara un menu principal 
    print("""
    ////////////////////////////////////////////////////////////////////
    ------------------- WELCOME TO PANCAMP -----------------------------
        
        1. Registrar venta.
        2. Registrar compra.
        3. Generar informes.
        4. Salir.

    /////////////////////////////////////////////////////////////////////
    """)
    #El usuario tendra que digitar unas de la opciones anteriores
    opc=int(input("Por favor digite la opcion que desees realizar: \n"))
    system("clear")#Limpiar pantalla de la consola 
    #Si la opcion elegida es uno se hara
    if opc == 1:
        #se le mostrara la sesion de ventas
        print("""
        /////////////////////////////////////////////////////////////////
        ------------- BIENVENIDO A LA SESIÓN DE VENTAS -----------------
            Por favor digite las siguientes datos para poder proceder
            a las ventas
        ----------------------------------------------------------------
        """)
        #Crea variables vacios donde se guardara la informacion que el usuario digite en la consola 
        DateVenta= input("     Ingresa la fecha de la venta: \n")
        NameCli= input("     Ingresa el nombre del cliente: \n")
        DireCli= input("     Ingresa la dirección del cliente: \n")
        NameEmple=input("     Ingresa el nombre del empleado: \n")
        CargoEmple=input("     Ingresa el cargo del empleado: \n")
        system("clear")#limpiar consola 
        print("""
            ////////////////////////////////////////////////////////////////
            -------------------- PRODUCTOS PANCAMP -------------------------
            Mostrario de los productos disponibles, cada una con su 
            categoría.

                - Panaderia
        """)
        #Se le mosrara todos los productos del json donde sera por sesiones, para i que leera todos los productos de la panaderia e mostrara los nombres y precios asi con las otras categorias
        for i in productos["Panaderia"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Pasteleria
        """)
        for i in productos["Pasteleria"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Bebidas
        """)
        for i in productos["Bebidas"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Apartado de promociones
        """)
        for i in productos["Apartado de promociones"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
            Por favor ingresa los siguiente datos para proceder a la venta
            del producto
        """)
        #En las variales vacias se guardara los datos que el usuario ingrese en la consola 
        NomSec=input("Ingrese el nombre de la categoria que desees comprar: \n")
        NomProd=input("Ingrese el nombre del producto: \n")
        PreProd=input("Ingrese el precio del producto: \n")
        CantProd=input("Ingrese la cantidad del producto: \n")
        system("clear")
        #Para i que ingresara al json productos donde leera la categoria que el usuario ingreso
        for i in productos[NomSec]:
            #Si el nombre que el usuario ingreso es igual a los nombres que se encuentra guardada en el json se crea una variable donde guarde la otra informacion
            if i["nombre"]==NomProd:
                ventaProd={"nombre":i["nombre"], "Cantidad":CantProd, "Precio":i["precio"]}
        #El json que esta vacio se guardara la informacion que el usuario ingresp
        sales["venticas"].append({"Fecha":DateVenta, "NombreDelCliente": NameCli, "DirecciónDelCliente": DireCli, "NombreDelEmpleado":NameEmple, "CargoDelEmpleado": CargoEmple, "Producto":ventaProd})

        print("La venta del producto fue realizada con exito JEYYY XDDD")

        system("clear")
    #Si la opcion ingresada es dos se hara
    elif opc==2:
        #Se le mostrara el menu de la sesion de compras
        print("""
        /////////////////////////////////////////////////////////////////
        ------------- BIENVENIDO A LA SESIÓN DE COMPRAS -----------------
            Por favor digite las siguientes datos para poder proceder
            a las compras
        ----------------------------------------------------------------
        """)
        #En las variables vacias se guardara lo que el usuario ingreso en la consola 
        DateCompra= input("     Ingresa la fecha de la compra: \n")
        NamePro= input("     Ingresa el nombre del proveedor: \n")
        ContPro= input("     Ingresa el contacto del proveedor: \n")
        system("clear")
        print("""
            ////////////////////////////////////////////////////////////////
            -------------------- PRODUCTOS PANCAMP -------------------------
            Mostrario de los productos disponibles, cada una con su 
            categoría.

                - Panaderia
        """)
        
        for i in productos["Panaderia"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Pasteleria
        """)
        for i in productos["Pasteleria"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Bebidas
        """)
        for i in productos["Bebidas"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
                - Apartado de promociones
        """)
        for i in productos["Apartado de promociones"]:
            print("     Nombre: ", i["nombre"],  "   $",i["precio"])

        print("""
            -----------------------------------------------------------------
            Por favor ingresa los siguiente datos para proceder a la venta
            del producto
        """)
        #El usuario tendra que digitar estos datos p
        NomCate=input("Ingrese la categoria que desee comprar: \n")
        Nombre=input("Ingrese el nombre del producto: \n")
        Precio=int(input("Ingrese el precio del producto: \n"))
        Cantidad=int(input("Ingrese la cantidad del producto: \n"))
        system("clear")
        for i in productos[NomCate]:
            if i["nombre"]==Nombre:
                Compra= {"Nombre": i["nombre"], "Cantidad":Cantidad}
    #Se guardara en el json vacio de compra
        shop["compritas"].append({"Fecha":DateCompra, "NombreDelProveedor": NamePro, "Contacto": ContPro, "NombreDelProducto":Nombre, "Precio":Precio, "Cantidad": Cantidad})

        print("La compra del producto fue realizada con exito JEYYY XDDD")
        system("clear")
        # Si la opcion registrada es tres se hara
    elif opc==3:
        #Se le mostrara un menu donde el usuario podra digitar cual informe quiere ver
       
        print("""
        ////////////////////////////////////////////////////////
        ---------- BIENVENIDO A LA SESION DE INFORMES ---------
            
            1. Informes de ventas
            2. Informes de stock 
            
        """)
        num= int(input("Por favor digite la opción que desees ver: "))
        system("clear")
        #si la opcion elegida es uno se hara 
        if num == 1:
            print("------Informes de ventas---------")
            print("----------venticas---------------")
            #Se mostrara los datos que esta guardaro en el json de ventas
            for i in sales["venticas"]:
                print(" Fecha de la venta:",i["Fecha"], "\n Venta de producto:",i["Producto"]["nombre"]," \n Cantidad vendida:",i["Producto"]["Cantidad"], "\n Total",(i["Producto"]["Cantidad"]*i["Producto"]["Precio"]))
                
        #Si la opcion elegida es dos se hara
        elif num == 2:
            print("------Informes de stock---------")
            print("----------compritas-------------")
            #se le mostrara los datos que estan guardados en compras
            for i in shop["compritas"]:
                print("Fecha:", i["Fecha"], "\nNombreDelProveedor:", i["NombreDelProveedor"], "\nContacto:",i ["Contacto"], "\nNombreDelProducto:",i ["NombreDelProducto"], "\nCantidad comprada:",i["Cantidad"], "\nPrecio total:", i["Precio"]*i["Cantidad"])

    

    #Si la opcion elegida es cuatro finalizara programa 
    elif opc==4:
        print("Gracias por venir a PANCAMP")
        boleanito=False

     


Ventas=json.dumps(sales) #Guardara los datos que ingrese el usuario en ventas.json
with open("./ventas.json","w") as files:
    files.write(Ventas)

Productos=json.dumps(productos)#Guardara los datos que ingrese el usuario en productos.json
with open("./productos.json","w") as files:
    files.write(Productos)

Compras=json.dumps(shop)#Guardara los datos que ingrese el usuario en vemtas.json
with open("./compras.json","w") as files:
    files.write(Compras)

#Desarrollado por Zully Fernanda Ortiz Avendaño