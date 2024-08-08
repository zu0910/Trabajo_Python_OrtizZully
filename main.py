import json
from os import system

with open("./productos.json", encoding="utf-8") as file:#con esto se abre el archivo de campusland.json que es donde esta toda la informacion
    productos=json.load(file)

with open("./ventas.json", encoding="utf-8") as files:
    sales=json.load(files)

with open("./compras.json", encoding="utf-8") as files:
    shop=json.load(files)

boleanito=True
while boleanito==True:
    print("""
    ////////////////////////////////////////////////////////////////////
    ------------------- WELCOME TO PANCAMP -----------------------------
        
        1. Registrar venta.
        2. Registrar compra.
        3. Generar informes.
        4. Salir.

    /////////////////////////////////////////////////////////////////////
    """)
    opc=int(input("Por favor digite la opcion que desees realizar: \n"))
    system("clear")
    if opc == 1:
        print("""
        /////////////////////////////////////////////////////////////////
        ------------- BIENVENIDO A LA SESIÓN DE VENTAS -----------------
            Por favor digite las siguientes datos para poder proceder
            a las ventas
        ----------------------------------------------------------------
        """)
        DateVenta= input("     Ingresa la fecha de la venta: \n")
        NameCli= input("     Ingresa el nombre del cliente: \n")
        DireCli= input("     Ingresa la dirección del cliente: \n")
        NameEmple=input("     Ingresa el nombre del empleado: \n")
        CargoEmple=input("     Ingresa el cargo del empleado: \n")
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
        NomSec=input("Ingrese el nombre de la categoria que desees comprar: \n")
        NomProd=input("Ingrese el nombre del producto: \n")
        PreProd=input("Ingrese el precio del producto: \n")
        CantProd=input("Ingrese la cantidad del producto: \n")
        system("clear")
        for i in productos[NomSec]:
            if i["nombre"]==NomProd:
                ventaProd={"nombre":i["nombre"], "Cantidad":CantProd, "Precio":i["precio"]}

        sales["venticas"].append({"Fecha":DateVenta, "NombreDelCliente": NameCli, "DirecciónDelCliente": DireCli, "NombreDelEmpleado":NameEmple, "CargoDelEmpleado": CargoEmple, "Producto":ventaProd})

        print("La venta del producto fue realizada con exito JEYYY XDDD")

        system("clear")
    elif opc==2:
        
        print("""
        /////////////////////////////////////////////////////////////////
        ------------- BIENVENIDO A LA SESIÓN DE COMPRAS -----------------
            Por favor digite las siguientes datos para poder proceder
            a las compras
        ----------------------------------------------------------------
        """)
        
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
        NomCate=input("Ingrese la categoria que desee comprar: \n")
        Nombre=input("Ingrese el nombre del producto: \n")
        Precio=int(input("Ingrese el precio del producto: \n"))
        Cantidad=int(input("Ingrese la cantidad del producto: \n"))
        system("clear")
        for i in productos[NomCate]:
            if i["nombre"]==Nombre:
                Compra= {"Nombre": i["nombre"], "Cantidad":Cantidad}

        shop["compritas"].append({"Fecha":DateCompra, "NombreDelProveedor": NamePro, "Contacto": ContPro, "NombreDelProducto":Nombre, "Precio":Precio, "Cantidad": Cantidad})

        print("La compra del producto fue realizada con exito JEYYY XDDD")
        system("clear")
    elif opc==3:
        print("""
        ////////////////////////////////////////////////////////
        ---------- BIENVENIDO A LA SESION DE INFORMES ---------
            
            1. Informes de ventas
            2. Informes de stock 
        """)
        num= int(input("Por favor digite la opción que desees ver: "))
        system("clear")
        if num == 1:
            print("------Informes de ventas---------")
            print("----------venticas---------------")

            for i in sales["venticas"]:
                print(" Fecha de la venta:",i["Fecha"], "\n Venta de producto:",i["Producto"]["nombre"]," \n Cantidad vendida:",i["Producto"]["Cantidad"], "\n Total",(i["Producto"]["Cantidad"]*i["Producto"]["Precio"]))
                 

        elif num == 2:
            print("------Informes de stock---------")
            print("----------compritas-------------")

            for i in shop["compritas"]:
                print("Fecha:", i["Fecha"], "\nNombreDelProveedor:", i["NombreDelProveedor"], "\nContacto:",i ["Contacto"], "\nNombreDelProducto:",i ["NombreDelProducto"], "\nCantidad comprada:",i["Cantidad"], "\nPrecio total:", i["Precio"]*i["Cantidad"])
            
    elif opc==4:
        print("Gracias por venir a PANCAMP")
        boleanito=False

     


Ventas=json.dumps(sales)
with open("./ventas.json","w") as files:
    files.write(Ventas)

Productos=json.dumps(productos)
with open("./productos.json","w") as files:
    files.write(Productos)

Compras=json.dumps(shop)
with open("./compras.json","w") as files:
    files.write(Compras)

#Desarrollado por Zully Fernanda Ortiz Avendaño