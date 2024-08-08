import json


with open("./productos.json", encoding="utf-8") as file:#con esto se abre el archivo de campusland.json que es donde esta toda la informacion
    productos=json.load(file)

with open("./ventas.json", encoding="utf-8") as files:
    sales=json.load(files)

with open("./compras.json", encoding="utf-8") as files:
    shop=json.load(files)

Ventas=json.dumps(sales)
with open("./ventas.json","w") as files:
    files.write(Ventas)

Productos=json.dumps(productos)
with open("./productos.json","w") as files:
    files.write(Productos)

Compras=json.dumps(shop)
with open("./compras.json","w") as files:
    files.write(Compras)

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

if opc == 1:
    print("""
    /////////////////////////////////////////////////////////////////
    ------------- BIENVENIDO A LA SESIÓN DE VENTAS -----------------
          Por favor digite las siguientes datos para poder proceder
          a las ventas
    ----------------------------------------------------------------
    """)
    DateVenta= input("     Ingresa la fecha de la venta: \n")
    NameCli= str(input("     Ingresa el nombre del cliente: \n"))
    DireCli= str(input("     Ingresa la dirección del cliente: \n"))
    NameEmple=str(input("     Ingresa el nombre del empleado: \n"))
    CargoEmple=str(input("     Ingresa el cargo del empleado: \n"))
    
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
    NomProd=str(input("Ingrese el nombre del producto: \n"))
    PreProd=int(input("Ingrese el precio del producto: \n"))
    CantProd=int(input("Ingrese la cantidad del producto: \n"))

    for i in productos["nombre"]:
        if i["nombre"]==NomProd:
            ventaProd={"nombre":i["nombre"], "Cantidad":CantProd, "Precio":i["precio"]}

    sales["venticas"].append({"Fecha":DateVenta, "NombreDelCliente": NameCli, "DirecciónDelCliente": DireCli, "NombreDelEmpleado":NameEmple, "CargoDelEmpleado": CargoEmple, "Producto":ventaProd})

    print("La venta del producto fue realizada con exito JEYYY XDDD")


elif opc==2:
     
     print("""
    /////////////////////////////////////////////////////////////////
    ------------- BIENVENIDO A LA SESIÓN DE COMPRAS -----------------
          Por favor digite las siguientes datos para poder proceder
          a las compras
    ----------------------------------------------------------------
    """)
     
     DateCompra= input("     Ingresa la fecha de la compra: \n")
     NamePro= str(input("     Ingresa el nombre del proveedor: \n"))
     ContPro= int(input("     Ingresa el contacto del proveedor: \n"))

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
     Nombre=str(input("Ingrese el nombre del producto: \n"))
     Precio=int(input("Ingrese el precio del producto: \n"))
     Cantidad=int(input("Ingrese la cantidad del producto: \n"))

     for i in productos[Nombre]:
         if i["nombres"]==Nombre:
             Compra= {"Nombre": i["nombre"], "Cantidad":Cantidad}


     shop["compritas"].append({"Fecha":DateCompra, "NombreDelProveedor": Nombre, "Contacto": ContPro, "Precio":Precio, "Cantidad": Cantidad})

elif opc==3:
    print("""
    ////////////////////////////////////////////////////////
    ---------- BIENVENIDO A LA SESION DE INFORMES ---------
          
          1. Informes de ventas
          2. Informes de stock 
""")
    num= int(input("Por favor digite la opción que desees ver: "))

    if num == 1:
        print("------Informes de ventas---------")
        print("venticas")

    elif num == 2:
        print("------Informes de stock---------")
        print("compritas")

#Desarrollado por Zully Fernanda Ortiz Avendaño