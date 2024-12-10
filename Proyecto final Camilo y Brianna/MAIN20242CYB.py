#Integrantes: Brianna Lucia Dearbron Torres C.C.1218713579, Camilo Andres Romero Perez T.I.1102831402

from FUNCIONESPF20242CYB import *
import mysql.connector 
from pymongo import MongoClient

client= MongoClient('localhost', 27017)
db= client.Informatica1_PF

imagenesmedicas= db.imagenes
reportesmedicos= db.reportes

crear_db()
crear_tabla_de_users()
crear_tabla_de_pacientes()
crear_tabla_de_diagnosticos()
crear_datos_iniciales()
crear_reportes_iniciales()
crear_imagenes_iniciales()

while True:
    role=inicio_sesion()
    if not role:
        continue
    while True:
        print("\n" + "="*40)
        print("✨ BIENVENIDO AL MENÚ PRINCIPAL  ✨")
        print("="*40)
        
        if role == "Administrador":
                print("1️⃣ Gestión de Usuarios")
                print("2️⃣ Gestión de Pacientes y diagnosticos")
                print("3️⃣ Gestión de Imagenes, sus metadatos y gestion de reportes médicos")
                print("0️⃣ Salir")
                opcionA = input("Seleccione una opción: ")

                if opcionA=="1":
                    while True:
                        print("¿Que desea hacer en gestión de usuarios 🔧 ?")
                        print("1️⃣ Añadir Usuarios")
                        print("2️⃣ Eliminar Usuarios")
                        print("3️⃣ Modificar información de Usuarios")
                        print("4️⃣ Menu de busqueda de Usuarios")
                        print("0️⃣ Volver al menu anterior")
                        opcion1A= input("Seleccione una opción: ")

                        if opcion1A== "1":
                            agregar_usuario()
                        elif opcion1A=="2":
                            eliminar_usuario()
                        elif opcion1A=="3":
                            actualizar_usuario()
                        elif opcion1A=="4":
                            while True:
                                print("\n🔍✨ SUBMENÚ DE BÚSQUEDA ✨🔍")
                                print("1️⃣ Ver todos los usuarios")
                                print("2️⃣ Buscar usuario por ID")
                                print("0️⃣ Salir del submenú")
                                print("=" * 40)

                                opciona = input("Seleccione una opción: ")

                                if opciona == "1":
                                    print("\n👥 Lista de todos los usuarios:")
                                    mostrar_users() 
                                elif opciona == "2":
                                    buscar_usuario_por_id() 
                                elif opciona == "0":
                                    print("👋 Saliendo del submenú de búsqueda.")
                                    break
                                else:
                                    print("❌ Opción no válida. Intente nuevamente.")
                        elif opcion1A=="0":
                            print("👋 Saliendo...")
                            break
                        else: 
                            print("❌ Opción no válida. Intente nuevamente.")
                
                elif opcionA=="2":
                    while True:
                        print("¿Que desea hacer en gestión de pacientes y diagnosticos 🔧 ?")
                        print("1️⃣ Añadir datos de un paciente con su diagnostico")
                        print("2️⃣ Borrar por completo un paciente ")
                        print("3️⃣ Menu de busqueda de pacientes y diagnosticos")
                        print("4️⃣ Editar datos de un paciente con su diagnostico")
                        print("0️⃣ Volver al menu anterior")
                        opcion1aa= input("Seleccione una opción: ")

                        if opcion1aa=="1":
                            agregar_paciente_y_diagnostico()
                        elif opcion1aa=="2":
                            eliminar_paciente_y_diagnostico()
                            elimnar_imagenreporte(db)
                        elif opcion1aa=="3":
                            while True:
                                print("¿Que desea hacer en el menu de busqueda de pacientes y diagnosticos 🔧 ?")
                                print("1️⃣ Buscar paciente o diagnostico")
                                print("2️⃣ Ver todos los pacientes o diagnosticos")
                                print("0️⃣ Volver al menu anterior")
                                opcion2aa= input("Seleccione una opción: ")
                                if opcion2aa=="1":
                                    while True:
                                        print("¿Que desea hacer en 'Buscar paciente o diagnostico' 🔧 ?")
                                        print("1️⃣ Buscar paciente en especifico")
                                        print("2️⃣ Buscar diagnostico en especifico")
                                        print("3️⃣ buscar paciente en especifico y su diagnostico")
                                        print("0️⃣ Volver al menu anterior")
                                        opcion3aa= input("Seleccione una opción: ")

                                        if opcion3aa=="1":
                                            buscar_paciente_por_id()
                                        elif opcion3aa=="2":
                                            buscar_diagnostico_por_id()
                                        elif opcion3aa=="3":
                                            buscar_paciente_y_diagnostico_por_id()
                                        elif opcion3aa=="0":
                                            print("👋 Saliendo...")
                                            break
                                        else: 
                                            print("❌ Opción no válida. Intente nuevamente.")
                                elif opcion2aa=="2":
                                    while True:
                                        print("¿Que desea hacer en 'Ver todos los pacientes o diagnosticos' 🔧 ?")
                                        print("1️⃣ Ver todos los pacientes")
                                        print("2️⃣ Ver todos los diagnosticos")
                                        print("3️⃣ Ver todos los pacientes con su diagnostico")
                                        print("0️⃣ Volver al menu anterior")
                                        opcion3ad= input("Seleccione una opción: ")

                                        if opcion3ad=="1":
                                            mostrar_pacientes()
                                        elif opcion3ad=="2":
                                            mostrar_diagnosticos()
                                        elif opcion3ad=="3":
                                            ver_todos_pacientes_y_diagnosticos()
                                        elif opcion3ad=="0":
                                            print("👋 Saliendo...")
                                            break
                                        else: 
                                            print("❌ Opción no válida. Intente nuevamente.")
                                elif opcion2aa=="0":
                                    print("👋 Saliendo...")
                                    break
                                else: 
                                    print("❌ Opción no válida. Intente nuevamente.")
                        elif opcion1aa=="4":
                            while True:
                                print("¿Que desea hacer en Editar datos de un paciente con su diagnostico 🔧 ?")
                                print("1️⃣ Editar solo la informacion de un paciente")
                                print("2️⃣ Editar solo el diagnostico de un paciente en especifico")
                                print("3️⃣ Editar tanto la información de un paciente como su diagnostico")
                                print("0️⃣ Volver al menu anterior")
                                opcion2ad= input("Seleccione una opción: ")

                                if opcion2ad=="1":
                                    actualizar_paciente()
                                elif opcion2ad=="2":
                                    actualizar_diagnostico()
                                elif opcion2ad=="3":
                                    actualizar_paciente_y_diagnostico()
                                elif opcion2ad=="0":
                                    print("👋 Saliendo...")
                                    break
                                else: 
                                    print("❌ Opción no válida. Intente nuevamente.")
                        elif opcion1aa=="0":
                            print("👋 Saliendo...")
                            break
                        else: 
                            print("❌ Opción no válida. Intente nuevamente.")    

                elif opcionA=="3":
                    while True:
                        print("¿Que desea hacer en gestión imagenes y sus metadatos 🔧 ?")
                        print("1️⃣ Gestionar Imagenes y sus metadatos")
                        print("2️⃣ Gestionar Reportes médicos")
                        print("0️⃣ Volver al menu anterior")
                        opcion1i= input("Seleccione una opción: ")
                        if opcion1i== "1":
                            while True:
                                    print("\n🔧✨ GESTION DE IMAGENES Y SUS METADATOS ✨🔧")
                                    print("1️⃣ Cargar Imagen")
                                    print("2️⃣ Mover Imagen")
                                    print("3️⃣ Eliminar Imagen")
                                    print("4️⃣ Modificar Imagen")
                                    print("5️⃣ Submenu De Búsqueda")
                                    print("6️⃣ Gestionar Estado De Revisión Técnica")
                                    print("0️⃣ Volver al menu anterior")
                                    print("=" * 40)
                                    opci= input("Seleccione una opción: ")
                                    if opci == "1":
                                        ingresar_imagenes(db)
                                    elif opci== "2":
                                        mover_una_imagen(db)
                                    elif opci== "3":
                                        eliminar_imagen(db)
                                    elif opci =="4":
                                        editar_imagenes(db)
                                    elif opci =="5":
                                     while True:
                                        print("¿Que desea hacer en 'Submenu de búsqueda' 🔧 ?")
                                        print("1️⃣ Ver Todas las Imagenes")
                                        print("2️⃣ Buscar Imagen por ID")
                                        print("0️⃣ Volver al menu anterior")
                                        opci1= input("Seleccione una opción: ")
                                        if opci1== "1":
                                            ver_todas_las_imagenes(db)
                                        elif opci1=="2":
                                            buscar_imagen_por_id(db)
                                        elif opci1=="0":
                                            print("👋 Saliendo...")
                                            break
                                        else: 
                                                print("❌ Opción no válida. Intente nuevamente.")
                                    elif opci =="6":
                                     while True:
                                        print("¿Que desea hacer en 'Gestionar Estado de revisión técnica' 🔧 ?")
                                        print("1️⃣ Ver Todos los Estados de Revision Técnica")
                                        print("2️⃣ Ver Estado de Revision Técnica por ID")
                                        print("3️⃣ Modificar Estado de Revision Técnica")
                                        print("0️⃣ Volver al menu anterior")
                                        opci2= input("Seleccione una opción: ")
                                        if opci2== "1":
                                            ver_estados_tecnicos(db)
                                        elif opci2=="2":
                                            buscar_estadotécnico_de_img(db)
                                        elif opci2=="3":
                                            nuevo_estado_tecnico(db)
                                        elif opci2=="0":
                                            print("👋 Saliendo...")
                                            break
                                        else: 
                                                print("❌ Opción no válida. Intente nuevamente.") 
                                    elif opci =="0":
                                        print("👋 Saliendo...")
                                        break
                        elif opcion1i=="2":
                         while True:
                                    print("\n🔧✨ GESTION DE REPORTES MÉDICOS ✨🔧")
                                    print("1️⃣ Cargar Reporte médico")
                                    print("2️⃣ Eliminar Reporte Médico")
                                    print("3️⃣ Modificar Reporte Médico")
                                    print("4️⃣ Añadir Notas Técnicas")
                                    print("5️⃣ Submenu De Búsqueda")
                                    print("0️⃣ Volver al menu anterior")
                                    print("=" * 40)
                                    opci21= input("Seleccione una opción: ")  
                                    if opci21== "1":
                                        ingresar_reportes_medicos(db)
                                    elif opci21=="2":
                                        eliminar_reporte(db)
                                    elif opci21=="3":
                                        editar_reportes(db)
                                    elif opci21=="4":
                                        añadir_notas_tecnicas(db)
                                    elif opci21 =="5":
                                     while True:
                                        print("¿Que desea hacer en 'Submenu de búsqueda' 🔧 ?")
                                        print("1️⃣ Ver Todas los reportes médicos")
                                        print("2️⃣ Buscar reporte médico por ID")
                                        print("0️⃣ Volver al menu anterior")
                                        opci22= input("Seleccione una opción: ")
                                        if opci22=="1":
                                            ver_todos_los_reportes_medicos(db)
                                        if opci22=="2":
                                            buscar_reportes_por_id_paciente(db)
                                        elif opci22=="0":
                                            print("👋 Saliendo...")
                                            break
                                        else: 
                                                print("❌ Opción no válida. Intente nuevamente.") 
                                    elif opci21=="0":
                                        print("👋 Saliendo...")
                                        break
                                    else: 
                                        print("❌ Opción no válida. Intente nuevamente.")
                        elif opcion1i=="0":
                            print("👋 Saliendo...")
                            break
                elif opcion1A=="0":
                    print("👋 Saliendo...")
                    break
                
                else: 
                    print("❌ Opción no válida. Intente nuevamente.")

        if role == "Medico":
            print("1️⃣ Gestionar pacientes y diagnosticos")
            print("2️⃣ Gestionar reportes médicos")
            print("0️⃣ Salir")
            opcionM = input("Seleccione una opción: ")

            if opcionM =="1":
                while True:
                    print("¿Que desea hacer en gestión de pacientes y diagnnosticos 🔧 ?")
                    print("1️⃣ Submenú de busqueda")
                    print("2️⃣ Editar pacientes y diagnosticos")
                    print("0️⃣ Salir")
                    opcion1M = input("Seleccione una opción: ")

                    if opcion1M=="1":
                        while True:
                            print("\n🔍✨ SUBMENÚ DE BÚSQUEDA ✨🔍")
                        
                            print("¿Que desea hacer en el menu de busqueda de pacientes y diagnosticos 🔧 ?")
                            print("1️⃣ Buscar paciente o diagnostico")
                            print("2️⃣ Ver todos los pacientes o diagnosticos")
                            print("0️⃣ Volver al menu anterior")
                            opcion2m= input("Seleccione una opción: ")
                            if opcion2m=="1":
                                while True:
                                    print("¿Que desea hacer en 'Buscar paciente o diagnostico' 🔧 ?")
                                    print("1️⃣ Buscar paciente en especifico")
                                    print("2️⃣ Buscar diagnostico en especifico")
                                    print("3️⃣ buscar paciente en especifico y su diagnostico")
                                    print("0️⃣ Volver al menu anterior")
                                    opcion3m= input("Seleccione una opción: ")

                                    if opcion3m=="1":
                                        buscar_paciente_por_id()
                                    elif opcion3m=="2":
                                        buscar_diagnostico_por_id()
                                    elif opcion3m=="3":
                                        buscar_paciente_y_diagnostico_por_id()
                                    elif opcion3m=="0":
                                        print("👋 Saliendo...")
                                        break
                                    else: 
                                        print("❌ Opción no válida. Intente nuevamente.")
                            elif opcion2m=="2":
                                while True:
                                    print("¿Que desea hacer en 'Ver todos los pacientes o diagnosticos' 🔧 ?")
                                    print("1️⃣ Ver todos los pacientes")
                                    print("2️⃣ Ver todos los diagnosticos")
                                    print("3️⃣ Ver todos los pacientes con su diagnostico")
                                    print("0️⃣ Volver al menu anterior")
                                    opcion3mm= input("Seleccione una opción: ")

                                    if opcion3mm=="1":
                                        mostrar_pacientes()
                                    elif opcion3mm=="2":
                                        mostrar_diagnosticos()
                                    elif opcion3mm=="3":
                                        ver_todos_pacientes_y_diagnosticos()
                                    elif opcion3mm=="0":
                                        print("👋 Saliendo...")
                                        break
                                    else: 
                                        print("❌ Opción no válida. Intente nuevamente.")
                            elif opcion2m=="0":
                                print("👋 Saliendo...")
                                break
                            else: 
                                print("❌ Opción no válida. Intente nuevamente.")
                    elif opcion1M==2:
                        while True:
                            print("¿Que desea hacer en Editar datos de un paciente con su diagnostico 🔧 ?")
                            print("1️⃣ Editar solo la informacion de un paciente")
                            print("2️⃣ Editar solo el diagnostico de un paciente en especifico")
                            print("3️⃣ Editar tanto la información de un paciente como su diagnostico")
                            print("0️⃣ Volver al menu anterior")
                            opcion2me= input("Seleccione una opción: ")

                            if opcion2me=="1":
                                actualizar_paciente()
                            elif opcion2me=="2":
                                actualizar_diagnostico()
                            elif opcion2me=="3":
                                actualizar_paciente_y_diagnostico()
                            elif opcion2me=="0":
                                print("👋 Saliendo...")
                                break
                            else: 
                                print("❌ Opción no válida. Intente nuevamente.")
                    elif opcion1M=="0":
                            print("👋 Saliendo...")
                            break   
                    else: 
                                print("❌ Opción no válida. Intente nuevamente.")
            if opcionM=="2":
                while True:
                    print("¿Que desea hacer en gestión de reportes médicos 🔧 ?")
                    print("1️⃣ Crear reporte médico")
                    print("2️⃣ Modificar reporte médico")
                    print("3️⃣ Eliminar Reporte Médico")
                    print("4️⃣ Submenu de búsqueda")
                    print("0️⃣ Salir")
                    opcion11M = input("Seleccione una opción: ")
                    if opcion11M == "1":
                        ingresar_reportes_medicos(db)
                    elif opcion11M =="2":
                        editar_reportes(db)
                    elif opcion11M== "3":
                        eliminar_reporte(db)
                    elif opcion11M=="4":
                        while True:
                            print("\n🔍✨ SUBMENÚ DE BÚSQUEDA ✨🔍")
                        
                            print("¿Que desea hacer en el menu de busqueda de gestión de reportes médicos 🔧 ?")
                            print("1️⃣ Buscar reporte médico por ID")
                            print("2️⃣ Ver todos los reportes médicos")
                            print("0️⃣ Volver al menu anterior")
                            opcion12m= input("Seleccione una opción: ")
                            if opcion12m=="1":
                                buscar_reportes_por_id_paciente(db)
                            elif opcion12m=="2":
                                ver_todos_los_reportes_medicos(db)
                            elif opcion12m=="0":
                                print("👋 Saliendo...")
                                break
                            else: 
                                print("❌ Opción no válida. Intente nuevamente.")

                    elif opcion11M == "0":
                        print("👋 Saliendo...")
                        break 
                    else: 
                        print("❌ Opción no válida. Intente nuevamente.")
            elif opcion1M=="0":
                print("👋 Saliendo...")
                break
                
            else: 
                print("❌ Opción no válida. Intente nuevamente.")


        if role == "Técnico":
            print("1️⃣ Gestionar imágenes")
            print("2️⃣ Añadir Notas Técnicas")
            print("3️⃣ Gestionar Estado de revision técnica")
            print("0️⃣ Salir")
            opcionT = input("Seleccione una opción: ")   
            if opcionT== "1":
                 while True:
                    print("\n🔧✨ GESTION DE IMAGENES Y SUS METADATOS ✨🔧")
                    print("1️⃣ Cargar Imagen")
                    print("2️⃣ Mover Imagen")
                    print("3️⃣ Eliminar Imagen")
                    print("4️⃣ Modificar Imagen")
                    print("5️⃣ Submenu De Búsqueda")
                    print("0️⃣ Volver al menu anterior")
                    print("=" * 40)
                    opcit1= input("Seleccione una opción: ")

                    if opcit1=="1":
                        ingresar_imagenes(db)
                    elif opcit1 == "2":
                        mover_una_imagen(db)
                    elif opcit1 =="3":
                        eliminar_imagen(db)
                    elif opcit1== "4":
                        editar_imagenes(db)
                    elif opcit1=="5":
                        print("¿Que desea hacer en 'Submenu de búsqueda' 🔧 ?")
                        print("1️⃣ Ver Todas las Imagenes")
                        print("2️⃣ Buscar Imagen por ID")
                        print("0️⃣ Volver al menu anterior")
                        opcit5= input("Seleccione una opción: ")
                        if opcit5=="1":
                            ver_todas_las_imagenes(db)
                        elif opcit5=="2":
                            buscar_imagen_por_id(db)
                        elif opcit1 == "0":
                          print("👋 Saliendo...")
                          break 
                        else: 
                          print("❌ Opción no válida. Intente nuevamente.")
                    elif opcit1 == "0":
                        print("👋 Saliendo...")
                        break 
                    else: 
                        print("❌ Opción no válida. Intente nuevamente.")

            elif opcionT== "2":
                añadir_notas_tecnicas(db)
            elif opcionT== "3":
                 while True:
                        print("¿Que desea hacer en 'Gestionar Estado de revisión técnica' 🔧 ?")
                        print("1️⃣ Ver Todos los Estados de Revision Técnica")
                        print("2️⃣ Ver Estado de Revision Técnica por ID")
                        print("3️⃣ Modificar Estado de Revision Técnica")
                        print("0️⃣ Volver al menu anterior")
                        opci3t= input("Seleccione una opción: ")
                        if opci3t=="1":
                            ver_estados_tecnicos(db)
                        elif opci3t=="2":
                            buscar_estadotécnico_de_img(db)
                        elif opci3t=="3":
                            nuevo_estado_tecnico(db)
                        elif opci3t == "0":
                         print("👋 Saliendo...")
                         break 
                        else: 
                         print("❌ Opción no válida. Intente nuevamente.")

            elif opcionT== "0":
               print("👋 Saliendo...")
               break
            else: 
             print("❌ Opción no válida. Intente nuevamente.") 

                                    





                        







                


