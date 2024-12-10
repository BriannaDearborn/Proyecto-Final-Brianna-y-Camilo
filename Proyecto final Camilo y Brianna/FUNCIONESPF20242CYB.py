import mysql.connector
from pymongo import MongoClient

client= MongoClient('localhost', 27017)
db= client.Informatica1_PF

#CREAR COLECCIONES
imagenesmedicas= db.imagenes
reportesmedicos= db.reportes

# Validaciones auxiliares con manejo de excepciones integrado
def validar_alfabetico(valor, campo):
    """
    Valida que el valor contenga solo letras y espacios, y lo retorna.
    """
    try:
        if not all(c.isalpha() or c.isspace() for c in valor):
            raise ValueError(f"❌ El campo '{campo}' debe contener solo letras y espacios. Valor ingresado: '{valor}'")
        return valor.strip()
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
        raise

def validar_numerico(valor, campo):
    """
    Valida que el valor contenga solo números y lo retorna.
    """
    try:
        if not valor.isdigit():
            raise ValueError(f"❌ El campo '{campo}' debe contener solo números. Valor ingresado: '{valor}'")
        return valor
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
        raise

def validar_float(valor, campo):
    """
    Valida que el valor sea un número válido (entero o decimal) y lo retorna.
    """
    try:
        if not float(valor):
            raise ValueError (f"❌ El campo '{campo}' debe contener un número válido (entero o decimal). Valor ingresado: '{valor}'")
        return valor 
    except ValueError as e:
        mensaje_error = f"❌ El campo '{campo}' debe contener un número válido (entero o decimal). Valor ingresado: '{valor}'"
        print(f"❌ Error de validación: {e}")
        raise

def validar_edad(edad):
    """
    Valida que la edad esté en el rango de 0 a 120 años y la retorna.
    """
    try:
        if not edad.isdigit() or int(edad) < 0 or int(edad) > 120:
            raise ValueError(f"❌ La edad debe ser un número entre 0 y 120. Valor ingresado: '{edad}'")
        return int(edad)
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
        raise

def validar_genero(genero):
    """
    Valida que el género sea "Masculino" o "Femenino" y lo retorna.
    """
    try:
        opciones = ["Masculino", "Femenino"]
        if genero not in opciones:
            raise ValueError(f"❌ El género debe ser uno de los siguientes valores: {', '.join(opciones)}. Valor ingresado: '{genero}'")
        return genero
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
        raise

def validar_rol(rol):
    """
    Valida que el rol sea uno de los siguientes: "Administrador", "Medico" o "Tecnico".
    """
    try:
        roles_permitidos = ["Administrador", "Medico", "Tecnico"]
        if rol not in roles_permitidos:
            raise ValueError(f"❌ El rol debe ser uno de los siguientes valores: {', '.join(roles_permitidos)}. Valor ingresado: '{rol}'")
        return rol
    except ValueError as e:
        print(f"❌ Error de validación: {e}")
        raise


# Crear la base de datos
def crear_db():
    """
    Crea la base de datos 'Informatica1_PF' si no existe.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1')
    print(conexion.is_connected())
    cursor = conexion.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS Informatica1_PF"
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()

# Crear la tabla users
def crear_tabla_de_users():
    """
    Crea la tabla 'Users' en la base de datos si no existe.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        role ENUM('Administrador', 'Medico', 'Tecnico') NOT NULL)'''
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()

# Crear Tabla Pacientes
def crear_tabla_de_pacientes():
    """
    Crea la tabla 'Pacientes' en la base de datos si no existe.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS Pacientes (
        paciente_id INT NOT NULL,
        nombre VARCHAR(100) NOT NULL,
        edad INT NOT NULL,
        genero ENUM('Masculino', 'Femenino', 'Otro') NOT NULL,
        historial_diagnosticos TEXT)'''
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()

# Crear Tabla Diagnosticos
def crear_tabla_de_diagnosticos():
    """
    Crea la tabla 'Diagnosticos' en la base de datos si no existe.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS Diagnosticos (
        paciente_id INT NOT NULL,
        tipo_imagen ENUM('MRI', 'CT', 'Rayos X') NOT NULL,
        resultado_IA DECIMAL(5, 2),
        fecha_diagnostico DATE NOT NULL,
        fecha_toma_imagen DATE NOT NULL,
        estado_revision ENUM('Sí', 'No') NOT NULL)'''
    cursor.execute(sql)
    conexion.commit()
    cursor.close()
    conexion.close()
            
#Llenar de informacion las tablas con algunos datos inicales
def crear_datos_iniciales():
    """
    Ingresa usuarios en la tabla de usuarios, seis pacientes en la tabla de pacientes y los respectivos 6 diagnosticos en la tabla de diagnosticos.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()
    
    #users
    users = [
            ("Camilo Romero", "123456", "Administrador"), 
            ("Brianna Dearborn", "234567", "Medico"),       
            ("Yesid Ramirez", "345678", "Medico"),      
            ("Miguel Ochoa", "456789", "Tecnico"),     
            ("Sebastian Acosta", "567890", "Tecnico")]
    users_sql = "INSERT IGNORE INTO Users (username, password, role) VALUES (%s, %s, %s)"
    cursor.executemany(users_sql, users)
    
    #pacientes
    pacientes = [
            (1102, "Santiago Londoño", 45, "Masculino", "Diabetes"),
            (8562, "Policarpa Salabarrieta", 60, "Femenino", "Hipertensión"),
            (1984, "Anuel AA", 30, "Masculino", "Asma"),
            (2317, "Madelaine Petsch", 25, "Femenino", "Ninguno"),
            (5628, "Samuel Perez", 50, "Masculino", "Cáncer en remisión"),
            (6637, "Sofia Carson", 35, "Femenino", "Ninguno")]
    pacs_sql = "INSERT IGNORE INTO Pacientes (paciente_id, nombre, edad, genero, historial_diagnosticos) VALUES (%s, %s,%s, %s, %s)"
    cursor.executemany(pacs_sql, pacientes)
    
    #diagnosticos
    diagnosticos=[
            (1102, "MRI", 87.5, "2024-12-01","2024-11-28","Sí"),
            (8562, "CT", 45.3, "2024-11-15","2024-11-12", "No"),
            (1984, "Rayos X", 12.7, "2024-10-30","2024-10-27","Sí"),
            (2317, "MRI", 98.2, "2024-12-01","2024-11-28","Sí"),
            (5628, "CT", 65.4, "2024-09-21","2024-09-18","No"),
            (6637, "Rayos X", 72.1, "2024-11-30","2024-11-27","Sí")]
    dia_sql= "INSERT IGNORE INTO Diagnosticos (paciente_id, tipo_imagen, resultado_IA, fecha_diagnostico,fecha_toma_imagen, estado_revision) VALUES (%s, %s,%s, %s, %s,%s)"
    cursor.executemany(dia_sql, diagnosticos)
    
    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones CRUD para la tabla users
def agregar_usuario():
    """
    Agrega un nuevo usuario a la base de datos con un nombre de usuario, contraseña y rol.
    El rol puede ser Administrador, Médico o Técnico.
    """
    username = validar_alfabetico(input("Ingrese el nombre de usuario: "), "Username")
    password = input("Ingrese la contraseña (solo números): ")
    role = validar_rol(input("Ingrese el rol (Administrador, Medico, Tecnico): "))

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "INSERT INTO users (user_id, username, password, role) VALUES (NULL, %s, %s, %s)"
    cursor.execute(sql, (username, password, role))

    conexion.commit()
    print(f"✅ El usuario '{username}' fue agregado con éxito a la base de datos.")
    cursor.close()
    conexion.close()

def actualizar_usuario():
    """
    Actualiza los datos de un usuario en la base de datos, como el nombre de usuario, la contraseña y el rol.
    Se debe ingresar el ID del usuario a actualizar.
    """
    user_id = validar_numerico(input("Ingrese el ID del usuario a actualizar: "), "ID del usuario")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    resultado = cursor.fetchone()

    if resultado:
        nuevo_username = validar_alfabetico(input("Ingrese el nuevo username: "), "Nuevo Username")
        nueva_password = input("Ingrese la nueva contraseña: ")
        nuevo_role = validar_rol(input("Ingrese el nuevo rol (Administrador, Medico, Tecnico): "))

        sql_update = "UPDATE users SET username = %s, password= %s, role = %s WHERE user_id = %s"
        cursor.execute(sql_update, (nuevo_username, nueva_password, nuevo_role, user_id))

        conexion.commit()
        print(f"✅ Usuario con ID '{user_id}' actualizado con éxito.")
    else:
        print(f"⚠️ No se encontró un usuario con ID '{user_id}' en la base de datos.")
    
    cursor.close()
    conexion.close()

def eliminar_usuario():
    """
    Elimina un usuario de la base de datos a partir de su ID.
    """
    user_id = validar_numerico(input("Ingrese el ID del usuario a eliminar: "), "ID del usuario")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM users WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    resultado = cursor.fetchone()

    if resultado:
        sql= "DELETE FROM users WHERE user_id = %s"
        cursor.execute(sql, (user_id,))

        conexion.commit()
        print(f"✅ El usuario con ID '{user_id}' ha sido eliminado con éxito.")
    else:
        print(f"⚠️ No se encontró un usuario con ID '{user_id}' en la base de datos.")
    
    cursor.close()
    conexion.close()

def mostrar_users():
    """
    Muestra todos los usuarios registrados en la base de datos.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM users")
    resultados = cursor.fetchall()
    if resultados:
        for row in resultados:
            print(f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}, Role: {row[3]}")
    else:
        print("⚠️ No se encontraron users en la base de datos.")
    
    cursor.close()
    conexion.close()

def buscar_usuario_por_id():
    """
    Busca un usuario en la base de datos a partir de su ID.
    Si el usuario es encontrado, muestra sus datos.
    """
    user_id = validar_numerico(input("Ingrese el ID del usuario que desea buscar: "), "ID del usuario")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM Users WHERE user_id = %s"
    cursor.execute(sql, (user_id,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"✅ Usuario encontrado: \n"
              f"   ID: {resultado[0]}\n"
              f"   Username: {resultado[1]}\n"
              f"   Rol: {resultado[3]}")
    else:
        print(f"⚠️ No se encontró un usuario con ID {user_id}.")

    cursor.close()
    conexion.close()


# Funciones CRUD para la tabla Pacientes
def agregar_paciente():
    """
    Agrega un nuevo paciente a la base de datos con su ID, nombre, edad, género e historial de diagnósticos.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")
    nombre = validar_alfabetico(input("Ingrese el nombre del paciente: "), "Nombre")
    edad = validar_edad(input("Ingrese la edad del paciente: "))
    genero = validar_genero(input("Ingrese el género del paciente (Masculino/Femenino): "))
    historial = input("Ingrese el historial de diagnósticos del paciente (si tiene): ")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "INSERT INTO Pacientes (paciente_id, nombre, edad, genero, historial_diagnosticos) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (paciente_id, nombre, edad, genero, historial))

    conexion.commit()
    print(f"✅ Paciente '{nombre}' agregado con éxito.")
    cursor.close()
    conexion.close()

def actualizar_paciente():
    """
    Actualiza los datos de un paciente, como el nombre, la edad, el género y el historial de diagnósticos.
    Se debe ingresar el ID del paciente a actualizar.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente a actualizar: "), "ID del paciente")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql, (paciente_id,))
    resultado = cursor.fetchone()

    if resultado:
        nuevo_nombre = validar_alfabetico(input("Ingrese el nuevo nombre del paciente: "), "Nuevo Nombre")
        nueva_edad = validar_edad(input("Ingrese la nueva edad del paciente: "))
        nuevo_genero = validar_genero(input("Ingrese el nuevo género del paciente (Masculino/Femenino): "))
        nuevo_historial = input("Ingrese el nuevo historial de diagnósticos del paciente: ")

        sql= '''UPDATE Pacientes SET nombre = %s, edad = %s, genero = %s, historial_diagnosticos = %s WHERE paciente_id = %s'''
        cursor.execute(sql, (nuevo_nombre, nueva_edad, nuevo_genero, nuevo_historial, paciente_id))

        conexion.commit()
        print(f"✅ Paciente con ID '{paciente_id}' actualizado con éxito.")
    else:
        print(f"⚠️ No se encontró un paciente con ID '{paciente_id}' en la base de datos.")
    
    cursor.close()
    conexion.close()

def eliminar_paciente():
    """
    Elimina un paciente de la base de datos.
    Solicita el ID del paciente a eliminar, verifica si existe y, si es así, lo elimina.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente a eliminar: "), "ID del paciente")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql, (paciente_id,))
    resultado = cursor.fetchone()

    if resultado:
        sql_delete = "DELETE FROM Pacientes WHERE paciente_id = %s"
        cursor.execute(sql_delete, (paciente_id,))

        conexion.commit()
        print(f"✅ Paciente con ID '{paciente_id}' eliminado con éxito.")
    else:
        print(f"⚠️ No se encontró un paciente con ID '{paciente_id}' en la base de datos.")
    
    cursor.close()
    conexion.close()

def mostrar_pacientes():
    """
    Muestra todos los pacientes registrados en la base de datos.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Pacientes")
    resultados = cursor.fetchall()
    if resultados:
        for paciente in resultados:
            print(f"✅ Paciente: \n"
                  f"   ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Género: {paciente[3]}, "
                  f"Historial: {paciente[4]}")
    else:
        print("⚠️ No se encontraron pacientes en la base de datos.")
    
    cursor.close()
    conexion.close()

def buscar_paciente_por_id():
    """
    Busca un paciente por su ID en la base de datos.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente a buscar: "), "ID del paciente")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql, (paciente_id,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"✅ Paciente encontrado: ID: {resultado[0]}, Nombre: {resultado[1]}, Edad: {resultado[2]}, Género: {resultado[3]}, Historial: {resultado[4]}")
    else:
        print(f"⚠️ No se encontró un paciente con ID '{paciente_id}' en la base de datos.")
    
    cursor.close()
    conexion.close()

def agregar_paciente_y_diagnostico():
    """
    Agrega un nuevo paciente y su diagnóstico a la base de datos.
    Solicita la información del paciente (ID, nombre, edad, género, historial) y del diagnóstico (tipo de imagen, resultado de IA, fechas, estado de revisión).
    Inserta los datos en las tablas `Pacientes` y `Diagnosticos`.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")

    print("\n🔹 Información del paciente:")
    nombre = validar_alfabetico(input("Ingrese el nombre del paciente: "), "Nombre")
    edad = validar_edad(input("Ingrese la edad del paciente: "))
    genero = validar_genero(input("Ingrese el género del paciente (Masculino/Femenino): "))
    historial = input("Ingrese el historial de diagnósticos del paciente (si tiene): ")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql_paciente = "INSERT INTO Pacientes (paciente_id, nombre, edad, genero, historial_diagnosticos) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql_paciente, (paciente_id, nombre, edad, genero, historial))
    print(f"✅ Paciente '{nombre}' agregado con éxito.")

       
    print("\n🔹 Información del diagnóstico:")
    tipo_imagen = validar_alfabetico(input("Ingrese el tipo de imagen (MRI, CT, Rayos X): "), "Tipo de imagen")
    resultado_IA = validar_numerico(input("Ingrese el resultado de IA (en %): "), "Resultado de IA")
    fecha_diagnostico = input("Ingrese la fecha del diagnóstico (YYYY-MM-DD): ")
    fecha_toma_imagen = input("Ingrese la fecha de la toma de la imagen (YYYY-MM-DD): ")
    estado_revision = validar_alfabetico(input("Ingrese el estado de revisión (Sí/No): "), "Estado de revisión")

    sql_diagnostico = '''INSERT INTO Diagnosticos (paciente_id, tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision)
                             VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql_diagnostico, (paciente_id, tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision))
    print(f"✅ Diagnóstico para el paciente con ID '{paciente_id}' agregado con éxito.")

    conexion.commit()
    cursor.close()
    conexion.close()

# Funciones CRUD para la tabla Diagnosticos
def agregar_diagnostico():
    """
    Agrega un nuevo diagnóstico a un paciente específico en la base de datos.
    Solicita el ID del paciente y los detalles del diagnóstico (tipo de imagen, resultado de IA, fechas, estado de revisión).
    Inserta los datos en la tabla `Diagnosticos`.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")
    tipo_imagen = validar_alfabetico(input("Ingrese el tipo de imagen (MRI, CT, Rayos X): "), "Tipo de imagen")
    resultado_IA = validar_numerico(input("Ingrese el resultado de IA (en %): "), "Resultado de IA")
    fecha_diagnostico = input("Ingrese la fecha del diagnóstico (YYYY-MM-DD): ")
    fecha_toma_imagen = input("Ingrese la fecha de la toma de la imagen (YYYY-MM-DD): ")
    estado_revision = validar_alfabetico(input("Ingrese el estado de revisión (Sí/No): "), "Estado de revisión")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = '''INSERT INTO Diagnosticos (paciente_id, tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision)
             VALUES (%s, %s, %s, %s, %s, %s)'''
    
    cursor.execute(sql, (paciente_id, tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision))
    conexion.commit()
    print(f"✅ Diagnóstico para el paciente con ID '{paciente_id}' agregado con éxito.")
    cursor.close()
    conexion.close()

def actualizar_diagnostico():
    """
    Actualiza el diagnóstico de un paciente en la base de datos.
    Solicita el ID del paciente y los nuevos detalles del diagnóstico.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente para actualizar su diagnóstico: "), "ID del paciente")
    tipo_imagen = validar_alfabetico(input("Ingrese el nuevo tipo de imagen (MRI, CT, Rayos X): "), "Tipo de imagen")
    resultado_IA = validar_numerico(input("Ingrese el nuevo resultado de IA (en %): "), "Resultado de IA")
    fecha_diagnostico = input("Ingrese la nueva fecha del diagnóstico (YYYY-MM-DD): ")
    fecha_toma_imagen = input("Ingrese la nueva fecha de la toma de la imagen (YYYY-MM-DD): ")
    estado_revision = validar_alfabetico(input("Ingrese el nuevo estado de revisión (Sí/No): "), "Estado de revisión")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql = "SELECT * FROM Diagnosticos WHERE paciente_id = %s"
    cursor.execute(sql, (paciente_id,))
    resultado = cursor.fetchone()

    if resultado:
        sql_update = '''UPDATE Diagnosticos SET tipo_imagen = %s, resultado_IA = %s, fecha_diagnostico = %s,
                        fecha_toma_imagen = %s, estado_revision = %s WHERE paciente_id = %s'''
        cursor.execute(sql_update, (tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision, paciente_id))

        conexion.commit()
        print(f"✅ Diagnóstico para el paciente con ID '{paciente_id}' actualizado con éxito.")
    else:
        print(f"⚠️ No se encontró un diagnóstico para el paciente con ID '{paciente_id}'.")
    
    cursor.close()
    conexion.close()

def actualizar_paciente_y_diagnostico():
    """
    Actualiza la información del paciente y su diagnóstico en la base de datos, 
    incluyendo nombre, edad, historial y detalles del diagnóstico como tipo de imagen y resultados.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    # Actualizar información del paciente
    sql_paciente = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql_paciente, (paciente_id,))
    paciente = cursor.fetchone()

    if paciente:
        nuevo_nombre = validar_alfabetico(input("Ingrese el nuevo nombre del paciente: "), "Nuevo Nombre")
        nueva_edad = validar_edad(input("Ingrese la nueva edad del paciente: "))
        nuevo_genero = validar_genero(input("Ingrese el nuevo género del paciente (Masculino/Femenino): "))
        nuevo_historial = input("Ingrese el nuevo historial de diagnósticos del paciente: ")

        sql_update_paciente = '''UPDATE Pacientes SET nombre = %s, edad = %s, genero = %s, historial_diagnosticos = %s WHERE paciente_id = %s'''
        cursor.execute(sql_update_paciente, (nuevo_nombre, nueva_edad, nuevo_genero, nuevo_historial, paciente_id))
        print(f"✅ Paciente con ID '{paciente_id}' actualizado con éxito.")
    else:
        print(f"⚠️ No se encontró un paciente con ID '{paciente_id}' en la base de datos.")

    # Actualizar diagnóstico
    sql_diagnostico = "SELECT * FROM Diagnosticos WHERE paciente_id = %s"
    cursor.execute(sql_diagnostico, (paciente_id,))
    diagnostico = cursor.fetchone()

    if diagnostico:
        tipo_imagen = validar_alfabetico(input("Ingrese el nuevo tipo de imagen (MRI, CT, Rayos X): "), "Tipo de imagen")
        resultado_IA = validar_numerico(input("Ingrese el nuevo resultado de IA (en %): "), "Resultado de IA")
        fecha_diagnostico = input("Ingrese la nueva fecha del diagnóstico (YYYY-MM-DD): ")
        fecha_toma_imagen = input("Ingrese la nueva fecha de la toma de la imagen (YYYY-MM-DD): ")
        estado_revision = validar_alfabetico(input("Ingrese el nuevo estado de revisión (Sí/No): "), "Estado de revisión")

        sql_update_diagnostico = '''UPDATE Diagnosticos SET tipo_imagen = %s, resultado_IA = %s, fecha_diagnostico = %s,
                                    fecha_toma_imagen = %s, estado_revision = %s WHERE paciente_id = %s'''
        cursor.execute(sql_update_diagnostico, (tipo_imagen, resultado_IA, fecha_diagnostico, fecha_toma_imagen, estado_revision, paciente_id))
        print(f"✅ Diagnóstico para el paciente con ID '{paciente_id}' actualizado con éxito.")
    else:
        print(f"⚠️ No se encontró un diagnóstico para el paciente con ID '{paciente_id}'.")

    conexion.commit()
    cursor.close()
    conexion.close()


def mostrar_diagnosticos():
    """
    Muestra todos los diagnósticos registrados en la base de datos, con detalles de cada uno.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Diagnosticos")
    resultados = cursor.fetchall()
    if resultados:
        for i in resultados:
            print("   🔍 Diagnósticos:")
            print(f"Tipo de Imagen: {i[1]}, Resultado IA: {i[2]}%, Fecha Diagnóstico: {i[3]}, "
                  f"Fecha Toma Imagen: {i[4]}, Revisión: {i[5]}")
    else:
        print("⚠️ No se encontraron diagnósticos en la base de datos.")

def eliminar_diagnostico():
    """
    Elimina un diagnóstico de la base de datos después de solicitar confirmación al usuario.
    """
    diagnostico_id = validar_numerico(input("Ingrese el ID del diagnóstico a eliminar: "), "ID del diagnóstico")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    sql_verificar = "SELECT * FROM Diagnosticos WHERE diagnostico_id = %s"
    cursor.execute(sql_verificar, (diagnostico_id,))
    resultado = cursor.fetchone()

    if resultado:
    
        confirmacion = input(f"⚠️ ¿Está seguro de que desea eliminar el diagnóstico con ID {diagnostico_id}? (Sí/No): ").strip().lower()
        if confirmacion == "sí":
            sql_eliminar = "DELETE FROM Diagnosticos WHERE diagnostico_id = %s"
            cursor.execute(sql_eliminar, (diagnostico_id,))
            conexion.commit()
            print(f"✅ Diagnóstico con ID {diagnostico_id} eliminado exitosamente.")
        else:
            print("❌ Operación cancelada. No se eliminó el diagnóstico.")
    else:
        print(f"⚠️ No se encontró un diagnóstico con ID {diagnostico_id}.")

    cursor.close()
    conexion.close()

def eliminar_paciente_y_diagnostico():
    """
    Elimina un paciente y su diagnóstico de la base de datos tras confirmación del usuario.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del Paciente a eliminar: "), "ID del usuario")
    
    
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

   
    sql_pac = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql_pac, (paciente_id,))
    paciente = cursor.fetchone()

    if paciente:
        confirmacion_paciente = input(f"⚠️ ¿Está seguro de que desea eliminar al paciente con ID {paciente_id}? (Sí/No): ").strip().lower()
        if confirmacion_paciente == "sí":
            sql_eliminar_usuario = "DELETE FROM Pacientes WHERE paciente_id = %s"
            cursor.execute(sql_eliminar_usuario, (paciente_id,))
            conexion.commit()
            print(f"✅ Paciente con ID {paciente_id} eliminado exitosamente.")
        else:
            print("❌ Operación cancelada. No se eliminó el paciente.")
    else:
        print(f"⚠️ No se encontró un Paciente con ID {paciente_id}.")

    
    diagnostico_id = validar_numerico(input("Ingrese el ID del diagnóstico a eliminar: "), "ID del diagnóstico")
    sql_diagnostico = "SELECT * FROM Diagnosticos WHERE diagnostico_id = %s"
    cursor.execute(sql_diagnostico, (diagnostico_id,))
    diagnostico = cursor.fetchone()

    if diagnostico:
        confirmacion_diagnostico = input(f"⚠️ ¿Está seguro de que desea eliminar el diagnóstico con ID {diagnostico_id}? (Sí/No): ").strip().lower()
        if confirmacion_diagnostico == "sí":
            sql_eliminar_diagnostico = "DELETE FROM Diagnosticos WHERE diagnostico_id = %s"
            cursor.execute(sql_eliminar_diagnostico, (diagnostico_id,))
            conexion.commit()
            print(f"✅ Diagnóstico con ID {diagnostico_id} eliminado exitosamente.")
        else:
            print("❌ Operación cancelada. No se eliminó el diagnóstico.")
    else:
        print(f"⚠️ No se encontró un diagnóstico con ID {diagnostico_id}.")

    cursor.close()
    conexion.close()

def buscar_diagnostico_por_id():
    """
    Busca y muestra el diagnóstico de un paciente dado su ID.
    """
    paciente_id = int(input("Ingrese el ID del paciente para buscar su diagnóstico: "))
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()
    
    sql = "SELECT * FROM Diagnosticos WHERE paciente_id = %s"
    cursor.execute(sql, (paciente_id,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"Paciente ID: {resultado[0]}, Imagen: {resultado[1]}, Resultado IA: {resultado[2]}%, Fecha toma imagen: {resultado[3]}, Fecha diagnóstico: {resultado[4]}, Revisión: {resultado[5]}")
    else:
        print(f" ⚠️ No se encontró ningún diagnóstico para el paciente con ID {paciente_id}.")
    cursor.close()
    conexion.close()

def buscar_paciente_y_diagnostico_por_id():
    """
    Busca y muestra la información del paciente y sus diagnósticos dados su ID.
    """
    paciente_id = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")

    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    # Buscar paciente
    sql_paciente = "SELECT * FROM Pacientes WHERE paciente_id = %s"
    cursor.execute(sql_paciente, (paciente_id,))
    paciente = cursor.fetchone()

    if paciente:
        print(f"✅ Paciente encontrado: \n"
              f"   ID: {paciente[0]}\n"
              f"   Nombre: {paciente[1]}\n"
              f"   Edad: {paciente[2]}\n"
              f"   Género: {paciente[3]}\n"
              f"   Historial: {paciente[4]}")
        
        # Buscar diagnóstico del paciente
        sql_diagnostico = "SELECT * FROM Diagnosticos WHERE paciente_id = %s"
        cursor.execute(sql_diagnostico, (paciente_id,))
        diagnosticos = cursor.fetchall()

        if diagnosticos:
            print("\n🔍 Diagnósticos encontrados:")
            for diag in diagnosticos:
                print(f" Tipo de Imagen: {diag[1]}, Resultado IA: {diag[2]}%, Fecha Diagnóstico: {diag[3]}, "
                      f"Fecha Toma Imagen: {diag[4]}, Revisión: {diag[5]}")
        else:
            print("⚠️ No se encontraron diagnósticos para este paciente.")
    else:
        print(f"⚠️ No se encontró un paciente con ID {paciente_id}.")

    cursor.close()
    conexion.close()

def ver_todos_pacientes_y_diagnosticos():
    """
    Muestra la información de todos los pacientes y sus diagnósticos en la base de datos.
    """
    conexion = mysql.connector.connect(user='informatica1', password='info20242', host='127.0.0.1', database='Informatica1_PF')
    cursor = conexion.cursor()

    # Obtener todos los pacientes
    sql_pacientes = "SELECT * FROM Pacientes"
    cursor.execute(sql_pacientes)
    pacientes = cursor.fetchall()

    if pacientes:
        for paciente in pacientes:
            print(f"✅ Paciente: \n"
                  f"   ID: {paciente[0]}, Nombre: {paciente[1]}, Edad: {paciente[2]}, Género: {paciente[3]}, "
                  f"Historial: {paciente[4]}")

            # Obtener diagnósticos del paciente
            sql_diagnosticos = "SELECT * FROM Diagnosticos WHERE paciente_id = %s"
            cursor.execute(sql_diagnosticos, (paciente[0],))
            diagnosticos = cursor.fetchall()

            if diagnosticos:
                print("   🔍 Diagnósticos:")
                for diag in diagnosticos:
                    print(f"      Tipo de Imagen: {diag[1]}, Resultado IA: {diag[2]}%, Fecha Diagnóstico: {diag[3]}, "
                          f"Fecha Toma Imagen: {diag[4]}, Revisión: {diag[5]}")
            else:
                print("   ⚠️ No se encontraron diagnósticos para este paciente.")
            print("=" * 40)
    else:
        print("⚠️ No se encontraron pacientes en la base de datos.")

    cursor.close()
    conexion.close()



def inicio_sesion():
    """
    Solicita usuario y contraseña, valida las credenciales y retorna el rol del usuario.
    """
    print("\n💻 Inicio de Sesión 💻")
    username = input("👤 Usuario: ").strip()
    password = input("🔒 Contraseña: ").strip()

  
    conexion = mysql.connector.connect(
        user='informatica1',
        password='info20242',
        host='127.0.0.1',
        database='Informatica1_PF'
        )
    cursor = conexion.cursor()
    sql = "SELECT role FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    resultado = cursor.fetchone()

    if resultado:
        role = resultado[0]
        conexion.commit()
        print(f"✅ Bienvenido {role} 🎉")
        return role
    else:
        print("❌ Usuario o contraseña incorrectos.")
    
    
    cursor.close()
    conexion.close()

####################################################   FUNCIONES MONGODB  #####################################################
def ingresar_imagenes(db):
         """
         Permite ingresar una nueva imagen médica con los datos proporcionados por el usuario.
         """
         print("\n--- Ingresar una nueva imagen médica ---")
         id_imagen = input("Ingrese el ID de la imagen: ")
         id_paciente = validar_numerico(input("Ingrese el ID del paciente: "), "ID del paciente")
         fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
         tipo_imagen = validar_alfabetico(input("Ingrese el tipo de imagen (MRI, CT, Rayos X, etc.): "), "tipo de imagen")
         parte_cuerpo = validar_alfabetico(input("Ingrese la parte del cuerpo: "), "parte del cuerpo")
         preliminar= validar_float(input("Ingrese su resultado preliminar del análisis por IA en %: "), "resultado preliminar")
         image_path = input("Ingrese la ruta del archivo de imagen: ")
         estado_técnico= input("Ingrese el estado de revisión técnica: ")

         nueva_imagen = {
         "id_imagen": id_imagen,
         "id_paciente": id_paciente,
         "fecha": fecha,
         "tipo_imagen": tipo_imagen,
         "parte_cuerpo": parte_cuerpo,
         "Resultado preliminar del análisis por IA en %": preliminar ,
         "image_path": image_path,
         "estado_técnico": estado_técnico}

         imagenesmedicas.insert_one(nueva_imagen)
         print("\nImagen agregada correctamente.")


def mover_una_imagen(db):
    """
    Actualiza la ruta de una imagen médica existente según el ID ingresado.
    """
    img = input("Ingrese el ID de la imagen que desea buscar: ")

    imagen = imagenesmedicas.find_one({"id_imagen": img})
    if not imagen:
            print(f"❌ No se encontró ninguna imagen con ID '{img}'.")
            return
    if imagen:
        n_path= input("Ingrese el nuevo enlace al que desea mover la imagen: ")
        imagenesmedicas.update_one(
                    {"id_imagen": img},
                    {"$set": {"image_path": n_path}})
        print("La imagen se ha movido con éxito.")
     

def eliminar_imagen(db):
  """
  Elimina la imagen médica asociada al paciente cuyo ID es ingresado.
  """
  print("\n--- Eliminar Imagen Médica ---")
  id_paci = input("Ingrese el ID del paciente cuya imagen desea eliminar: ")

  imagen = imagenesmedicas.find_one({"id_paciente": id_paci})
  if imagen:
        imagenesmedicas.delete_one({"id_paciente": id_paci})
        print(f"✅ La imagen con ID '{id_paci}' ha sido eliminada exitosamente.")
  else:
        print(f"No se encontró una imagen con ID '{id_paci}.")


def elimnar_imagenreporte(db):
    """
    Elimina tanto la imagen médica como el reporte asociado a un paciente.
    """
    id_pacien = input("Ingrese el ID del paciente para confirmar que está seguro: ")
    imagen = imagenesmedicas.find_one({"id_paciente": id_pacien})
    if imagen:
        imagen_id = imagen.get('id_imagen')
        imagenesmedicas.delete_one({"id_imagen": imagen_id})
        print(f"Imagen asociada al paciente con ID {id_pacien} ha sido eliminada.")
    else:
        print(f"No se encontró una imagen asociada al paciente con ID {id_pacien}.")
    reporte = reportesmedicos.find_one({"id_paciente": id_pacien})
    if reporte:
        reporte_id = reporte.get('id_paciente')
        reportesmedicos.delete_one({"id_paciente": reporte_id})
        print(f"Reporte médico asociado al paciente con ID {id_pacien} ha sido eliminado.")
    else:
        print(f"No se encontró un reporte médico asociado al paciente con ID {id_pacien}.")


def editar_imagenes(db):
    """
    Permite editar los datos de una imagen médica existente.
    """
    id_imagen = input("Ingrese el ID de la imagen que desea editar: ")
    imagen = imagenesmedicas.find_one({"id_imagen": id_imagen})

    if not imagen:
        print(f"❌ No se encontró ninguna imagen con ID '{id_imagen}'.")
        return
    else:
        print("\n--- Ingresar los nuevos datos de la imagen ---")
        e_id_imagen = input("Ingrese el nuevo ID de la imagen: ")
        e_id_paciente = validar_numerico(input("Ingrese el nuevo ID del paciente: "), "id paciente")
        e_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD): ")
        e_tipo_imagen = validar_alfabetico(input("Ingrese el nuevo tipo de imagen (MRI, CT, Rayos X, etc.): "), "tipo de imagen")
        e_parte_cuerpo = validar_alfabetico(input("Ingrese la nueva parte del cuerpo: "), "parte del cuerpo")
        e_preliminar = validar_float(input("Ingrese el nuevo resultado preliminar del análisis por IA en %: "), "preliminar")
        e_image_path = input("Ingrese la nueva ruta del archivo de imagen: ")
        e_estado_técnico = input("Ingrese el nuevo estado de revisión técnica: ")

        imagen_editada = {
            "id_imagen": e_id_imagen,
            "id_paciente": e_id_paciente,
            "fecha": e_fecha,
            "tipo_imagen": e_tipo_imagen,
            "parte_cuerpo": e_parte_cuerpo,
            "Resultado preliminar del análisis por IA en %": e_preliminar,
            "image_path": e_image_path,
            "estado_técnico": e_estado_técnico,
        }
        imagenesmedicas.update_one(
            {"id_imagen": id_imagen},
            {"$set": imagen_editada}
        )

        print("✅ Imagen actualizada con éxito.")


def ver_todas_las_imagenes(db):
    """
    Muestra todas las imágenes médicas almacenadas en la base de datos, con sus respectivos detalles
    """
    imagenes = imagenesmedicas.find()
    print("\n--- Todas las Imágenes ---")
    for imagen in imagenes:
        print(f"\nID Imagen: {imagen.get('id_imagen')}")
        print(f"ID Paciente: {imagen.get('id_paciente')}")
        print(f"Fecha: {imagen.get('fecha')}")
        print(f"Tipo de Imagen: {imagen.get('tipo_imagen')}")
        print(f"Parte del Cuerpo: {imagen.get('parte_cuerpo')}")
        print(f"Resultado IA (%): {imagen.get('Resultado preliminar del análisis por IA en %')}")
        print(f"Ruta de la Imagen: {imagen.get('image_path')}")
        print(f"Estado técnico: {imagen.get('estado_técnico')}")


def buscar_imagen_por_id(db):
    """
    Permite buscar una imagen médica específica mediante su ID y mostrar los detalles correspondientes
    """
    id_imagen = input("Ingrese el ID de la imagen: ")
    imagen = imagenesmedicas.find_one({"id_imagen": id_imagen})
    if imagen:
        print(f"\nID Imagen: {imagen.get('id_imagen')}")
        print(f"ID Paciente: {imagen.get('id_paciente')}")
        print(f"Fecha: {imagen.get('fecha')}")
        print(f"Tipo de Imagen: {imagen.get('tipo_imagen')}")
        print(f"Parte del Cuerpo: {imagen.get('parte_cuerpo')}")
        print(f"Resultado IA (%): {imagen.get('Resultado preliminar del análisis por IA en %')}")
        print(f"Ruta de la Imagen: {imagen.get('image_path')}")
        print(f"Estado técnico: {imagen.get('estado_técnico')}")
    else:
        print(f"No se encontró una imagen con ID '{id_imagen}'.")


def ver_todos_los_reportes_medicos(db):
    """
    Muestra todos los reportes médicos almacenados
    """
    reportes = reportesmedicos.find()
    print("\n--- Todos los Reportes Médicos ---")
    for reporte in reportes:
        print(f"\nID Reporte: {reporte.get('id_reporte')}")
        print(f"ID Paciente: {reporte.get('id_paciente')}")
        print(f"Fecha del Reporte: {reporte.get('fecha')}")
        print(f"Tipo de Imagen: {reporte.get('tipo_imagen')}")
        print(f"Parte del Cuerpo: {reporte.get('parte_cuerpo')}")
        print(f"Ruta del Archivo de Imagen: {reporte.get('image_path')}")
        print(f"Estado Técnico: {reporte.get('estado_técnico')}")
        print("\n--- Análisis de IA ---")
        analisis_IA = reporte.get('analisis_IA', {})
        print(f"Condición Sugerida: {analisis_IA.get('condicion_sugerida')}")
        print(f"Resultado preliminar del análisis por IA en %: {analisis_IA.get('Resultado preliminar del análisis por IA en %')}")
        print(f"Notas de la IA: {analisis_IA.get('notas')}")
        print("\n--- Notas Técnicas ---")
        notas_tecnicas = reporte.get('notas_tecnicas', {})
        print(f"ID Técnica: {notas_tecnicas.get('id_tecnica')}")
        print(f"Fecha Nota Técnica: {notas_tecnicas.get('fecha_nota')}")
        print(f"Texto Nota Técnica: {notas_tecnicas.get('texto')}")


def buscar_reportes_por_id_paciente(db):
    """
    Permite buscar y mostrar todos los reportes médicos de un paciente específico usando su ID
    """
    id_paciente = input("Ingrese el ID del paciente: ")
    reportes = reportesmedicos.find({"id_paciente": id_paciente}) 
    print(f"\n--- Reportes Médicos del Paciente ID: {id_paciente} ---")
    reporte_encontrado = False
    for reporte in reportes:
        reporte_encontrado = True
        print(f"\nID Reporte: {reporte.get('id_imagen')}")
        print(f"Fecha del Reporte: {reporte.get('fecha')}")
        print(f"Tipo de Imagen: {reporte.get('tipo_imagen')}")
        print(f"Parte del Cuerpo: {reporte.get('parte_cuerpo')}")
        print(f"Ruta del Archivo de Imagen: {reporte.get('image_path')}")
        print(f"Estado Técnico: {reporte.get('estado_técnico')}")
        print("\n--- Análisis de IA ---")
        analisis_IA = reporte.get('analisis_IA', {})
        print(f"Condición Sugerida: {analisis_IA.get('condicion_sugerida')}")
        print(f"Resultado preliminar del análisis por IA en %: {analisis_IA.get('Resultado preliminar del análisis por IA en %')}")
        print(f"Notas de la IA: {analisis_IA.get('notas')}")
        print("\n--- Notas Técnicas ---")
        notas_tecnicas = reporte.get('notas_tecnicas', {})
        print(f"ID Técnica: {notas_tecnicas.get('id_tecnica')}")
        print(f"Fecha Nota Técnica: {notas_tecnicas.get('fecha_nota')}")
        print(f"Texto Nota Técnica: {notas_tecnicas.get('texto')}")
    if not reporte_encontrado:
        print(f"No se encontraron reportes médicos para el paciente con ID '{id_paciente}'.")


def ver_estados_tecnicos(db):
    """
    Muestra los estados técnicos de todas las imágenes médicas almacenadas en la base de datos.
    """
    imagenes = imagenesmedicas.find()  
    print("\n--- Estados Técnicos de Imágenes ---")
    imagen_encontrada = False  
    for imagen in imagenes:
        imagen_encontrada = True
        id_imagen = imagen.get('id_imagen')
        estado_técnico = imagen.get('estado_técnico') 
        print(f"\nID Imagen: {id_imagen}")
        print(f"Estado Técnico: {estado_técnico}")
    if not imagen_encontrada:
        print("No se encontraron imágenes en la base de datos.")


def buscar_estadotécnico_de_img(db):
    """
    Permite buscar el estado técnico de una imagen médica mediante su ID y mostrar el resultado.
    """
    img = input("Ingrese el ID de la imagen que desea buscar: ")

    imagen = imagenesmedicas.find_one({"id_imagen": img})
    
    if imagen:
        etec = imagen.get('estado_técnico')
        print(f"El estado de revisión técnica de la imagen es: {etec}")


def nuevo_estado_tecnico(db):
     """
     Permite actualizar el estado técnico de una imagen médica mediante su ID.
     """
     id_imagen = input("Ingrese el ID de la imagen que desea actualizar: ")
     a_estado_técnico = input("Ingrese el nuevo estado técnico: ")
     imagen = imagenesmedicas.find_one({"id_imagen": id_imagen})
     if imagen:
        
        imagenesmedicas.update_one(
            {"id_imagen": id_imagen}, 
            {"$set": {"estado_técnico": a_estado_técnico}} 
        )
        print("El estado técnico ha sido actualizado.")
     else:
        print(f"No se encontró una imagen con ID '{id_imagen}'.")


def añadir_notas_tecnicas(db):
    """
    Permite añadir notas técnicas a un reporte médico de un paciente específico 
    mediante el ID del paciente.
    """
    id_pa = input("Ingrese el ID del paciente al que desea agregar notas técnicas a su reporte médico: ")
    reporte = reportesmedicos.find_one({"id_paciente": id_pa})
    
    if not reporte:
        print(f"❌ No se encontró un reporte médico con ID '{id_pa}'.")
        return
    print("\n--- Ingresar Notas Técnicas ---")
    id_tecnica = input("Ingrese el nuevo ID de la técnica: ")
    fecha_nota = input("Ingrese la fecha de la nota técnica (YYYY-MM-DD): ")
    texto_nota = input("Ingrese el texto de la nota técnica: ")

    notas_tecnicas = {
        "id_tecnica": id_tecnica,
        "fecha_nota": fecha_nota,
        "texto": texto_nota
    }
    reportesmedicos.update_one(
        {"id_reporte": id_pa},
        {"$set": {"notas_tecnicas": notas_tecnicas}}
    )
    print("✅ Las notas técnicas han sido añadidas al reporte médico con éxito.")


def ingresar_reportes_medicos(db):
            """
            Permite ingresar un nuevo reporte médico con todos los detalles necesarios 
            como ID de imagen, ID de paciente, tipo de imagen, parte del cuerpo, análisis de IA 
            y notas técnicas.
            """
            print("\n--- Ingresar un nuevo reporte médico ---")
            id_imagen = input("Ingrese el ID de la imagen: ")
            id_paciente = validar_numerico(input("Ingrese el ID del paciente: "), "id del paciente")
            fecha = input("Ingrese la fecha del reporte (YYYY-MM-DD): ")
            tipo_imagen = validar_alfabetico(input("Ingrese el tipo de imagen (MRI, CT, Rayos X, etc.): "), "tipo de imagen")
            parte_cuerpo = validar_alfabetico(input("Ingrese la parte del cuerpo: "), "parte del cuerpo")
            image_path = input("Ingrese la ruta del archivo de imagen: ")
            estado_técnico= input("Ingrese el estado de revisión técnica: ")


            print("\n--- Ingresar nueva información sobre el análisis de IA ---")
            condicion_sugerida = validar_alfabetico(input("Ingrese la condición sugerida por la IA: "),"condicion sugerida")
            probabilidad = validar_numerico(input("Ingrese la probabilidad de la condición sugerida (%): "),"probabilidad")
            notas_ia = validar_alfabetico(input("Ingrese las notas del análisis de IA: "),"notas ia")

            print("\n--- Ingresar nueva información sobre notas técnicas ---")
            id_tecnica = input("Ingrese el ID de la técnica: ")
            fecha_notatecnica = input("Ingrese la fecha de la nota técnica (YYYY-MM-DD): ")
            texto_notatecnica = validar_alfabetico(input("Ingrese el texto de la nota técnica: "), "texto notas tecnicas")
            notas_tecnicas={
                        "id_tecnica": id_tecnica,
                        "fecha_nota": fecha_notatecnica,
                        "texto": texto_notatecnica}
            
            reporte_nuevo = {
                "id_imagen": id_imagen,
                "id_paciente": id_paciente,
                "fecha": fecha,
                "tipo_imagen": tipo_imagen,
                "parte_cuerpo": parte_cuerpo,
                "image_path": image_path,
                "estado_técnico": estado_técnico,
                "analisis_IA": {
                    "condicion_sugerida": condicion_sugerida,
                    "Resultado preliminar del análisis por IA en %": probabilidad,
                    "notas": notas_ia
                },
                "notas_tecnicas": notas_tecnicas
                }

            reportesmedicos.insert_one(reporte_nuevo)
            print("Reporte médico agregado correctamente.")


def editar_reportes(db):
    """
    Permite editar los reportes médicos de un paciente. Se puede elegir entre editar 
    los datos del reporte médico, la información del análisis de IA o las notas técnicas.
    El usuario debe ingresar el ID del paciente y seleccionar qué opción desea editar.
    """
    while True:
            id_paciente = validar_numerico(input("Ingrese el ID del paciente cuyo reporte desea editar: "), "ID del paciente")
            reporte = reportesmedicos.find_one({"id_paciente": id_paciente})
            
            if not reporte:
                print(f"No se encontró ningún reporte con ID del paciente '{id_paciente}'.")
                return
            
            print("\n--- Opciones para editar ---")
            print("1. Datos del reporte médico")
            print("2. Información del análisis IA")
            print("3. Notas técnicas")
            
            edit = validar_numerico(input("¿Qué opción desea editar?: "), "opción")
            
            if edit == "1":
                print("\n--- Ingresar los nuevos datos del reporte médico ---")
                r_id_imagen = input("Ingrese el nuevo ID de la imagen: ")
                r_fecha = input("Ingrese la nueva fecha del reporte (YYYY-MM-DD): ")
                r_tipo_imagen = validar_alfabetico(input("Ingrese el nuevo tipo de imagen (MRI, CT, Rayos X, etc.): "), "tipo de imagen")
                r_parte_cuerpo = validar_alfabetico(input("Ingrese la nueva parte del cuerpo: ")- "parte del cuerpo")
                r_image_path = input("Ingrese la nueva ruta del archivo de imagen: ")
                r_estado_tecnico = input("Ingrese el nuevo estado de revisión técnica: ")
                
                reportesmedicos.update_one(
                    {"id_paciente": id_paciente},
                    {"$set": {
                        "id_imagen": r_id_imagen,
                        "fecha": r_fecha,
                        "tipo_imagen": r_tipo_imagen,
                        "parte_cuerpo": r_parte_cuerpo,
                        "image_path": r_image_path,
                        "estado_técnico": r_estado_tecnico
                    }}
                )
                print("✅ Datos del reporte médico actualizados con éxito.")
            
            elif edit == "2":
                print("\n--- Ingrese la nueva información sobre el análisis de IA ---")
                r_condicion_sugerida = validar_alfabetico(input("Ingrese la nueva condición sugerida por la IA: "),"r condicion sugerida")
                r_probabilidad = validar_float(input("Ingrese la nueva probabilidad de la condición sugerida (%): "), "probabilidad")
                r_notas_ia = input("Ingrese las nuevas notas del análisis de IA: ")
                
                reportesmedicos.update_one(
                    {"id_paciente": id_paciente},
                    {"$set": {
                        "analisis_IA.condicion_sugerida": r_condicion_sugerida,
                        "Resultado preliminar del análisis por IA en %": r_probabilidad,
                        "analisis_IA.notas": r_notas_ia
                    }}
                )
                print("✅ Información del análisis IA actualizada con éxito.")
            
            elif edit == "3":
                print("\n--- Ingrese la nueva información sobre notas técnicas ---")
                r_id_tecnica = input("Ingrese el nuevo ID de la técnica: ")
                r_fecha_nota = input("Ingrese la nueva fecha de la nota técnica (YYYY-MM-DD): ")
                r_texto_nota = validar_alfabetico(input("Ingrese el nuevo texto de la nota técnica: "),"r texto nota")
                
                reportesmedicos.update_one(
                    {"id_paciente": id_paciente},
                    {"$set": {
                        "notas_tecnicas.id_tecnica": r_id_tecnica,
                        "notas_tecnicas.fecha_nota": r_fecha_nota,
                        "notas_tecnicas.texto": r_texto_nota
                    }}
                )
                print("✅ Notas técnicas actualizadas con éxito.")
            
            else:
                print("❌ Opción no válida. Intente nuevamente.")
                continue
            
            break
    

def eliminar_reporte(db):
    """
    Permite eliminar un reporte médico a partir del ID del paciente.
    """
    print("\n--- Eliminar Reporte Médico ---")
    id_rpaci = input("Ingrese el ID del paciente cuyo reporte médico desea eliminar: ")

    reporte = reportesmedicos.find_one({"id_paciente": id_rpaci})
    if reporte:
        reportesmedicos.delete_one({"id_paciente": id_rpaci})
        print(f"El reporte con ID {id_rpaci} ha sido eliminado exitosamente.")
    else:
        print(f"No se encontró un reporte con ID {id_rpaci}.")

########################### pacientes con imagenes pre creadas en mongo 

def crear_imagenes_iniciales():
    imagenesmedicas.insert_many([
        {
            "id_imagen": "img122",
            "id_paciente": "1102",
            "fecha": "2024-12-01",
            "tipo_imagen": "MRI",
            "parte_cuerpo": "Cerebro",
            "Resultado preliminar del análisis por IA en %": "87.5",
            "image_path": "imagenes/mri/2024/12/img122_mri_brain.jpg",
            "estado_técnico": "Optimización realizada para mejorar el contraste y la resolución anatómica en imágenes cerebrales."
            
        },
        {
            "id_imagen": "img113",
            "id_paciente": "8562",
            "fecha": "2024-11-15",
            "tipo_imagen": "CT",
            "parte_cuerpo": "Tórax",
            "Resultado preliminar del análisis por IA en %": "45.3",
            "image_path": "imagenes/ct/2024/11/img113_ct_torax.jpg",
            "estado_técnico": "Calibración finalizada para resaltar estructuras pulmonares y mediastino con alta precisión."
        },
        {
            "id_imagen": "img141",
            "id_paciente": "1984",
            "fecha": "2024-10-30",
            "tipo_imagen": "Rayos X",
            "parte_cuerpo": "Tórax",
            "Resultado preliminar del análisis por IA en %": "12.7",
            "image_path": "imagenes/rayosx/2024/10/img141_rayosx_torax.jpg",
            "estado_técnico": "Procesamiento técnico efectuado para una visualización óptima del sistema respiratorio."
        },
        {
            "id_imagen": "img216",
            "id_paciente": "2317",
            "fecha": "2024-12-01",
            "tipo_imagen": "MRI",
            "parte_cuerpo": "Corazón",
            "Resultado preliminar del análisis por IA en %": "98.2",
            "image_path": "imagenes/mri/2024/12/img216_mri_heart.jpg",
            "estado_ténico":  "Ajustes técnicos aplicados para realzar la calidad en cortes cardíacos y flujo sanguíneo."
        },
        {
            "id_imagen": "img383",
            "id_paciente": "5628",
            "fecha": "2024-09-21",
            "tipo_imagen": "CT",
            "parte_cuerpo": "Abdomen",
            "Resultado preliminar del análisis por IA en %": "65.4",
            "image_path": "imagenes/ct/2024/09/img383_ct_abdomen.jpg",
            "estado_técnico": "Revisión técnica completa para asegurar detalles claros en tejidos blandos abdominales."
        },
        {
            "id_imagen": "img297",
            "id_paciente": "6637",
            "fecha": "2024-11-30",
            "tipo_imagen": "Rayos X",
            "parte_cuerpo": "Fémur",
            "Resultado preliminar del análisis por IA en %": "72.1",
            "image_path": "imagenes/rayosx/2024/11/img297_rayosx_femur.jpg",
            "estado_técnico": "Imagen ajustada para obtener nitidez en estructuras óseas y tejidos circundantes."
        }
    ])


def crear_reportes_iniciales():
 reportesmedicos.insert_many([
    {
        "id_imagen": "img122",
        "id_paciente": "1102",
        "fecha": "2024-12-01",
        "tipo_imagen": "MRI",
        "parte_cuerpo": "Cerebro",
        "image_path": "imagenes/mri/2024/12/img122_mri_brain.jpg",
        "estado_técnico": "Optimización realizada para mejorar el contraste y la resolución anatómica en imágenes cerebrales.",
        "analisis_IA": {
            "condicion_sugerida": "Meningioma",
            "Resultado preliminar del análisis por IA en %": 87.5,
            "notas": "Masa bien definida sobre la capa externa del cerebro, ubicada en el área frontal. "
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech342",
                "fecha_nota": "2024-12-01",
                "texto": "Imagen capturada con paciente en decúbito supino con la cabeza fija en el soporte de la MRI"
            }
        ]
    },
    {
        "id_imagen": "img113",
        "id_paciente": "8562",
        "fecha": "2024-11-15",
        "tipo_imagen": "CT",
        "parte_cuerpo": "Tórax",
        "image_path": "imagenes/ct/2024/11/img113_ct_torax.jpg",
        "estado_técnico": "Calibración finalizada para resaltar estructuras pulmonares y mediastino con alta precisión.",
        "analisis_IA": {
            "condicion_sugerida": "Hipertensión",
            "Resultado preliminar del análisis por IA en %": 45.3,
            "notas": "Señales de engrosamiento en las paredes de la aorta, especialmente en la región torácica. "
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech442",
                "fecha_nota": "2024-11-15",
                "texto": "Imagen de alta calidad, no se observaron moviemientos del paciente"
            }
        ]
    },
    {
        "id_imagen": "img141",
        "id_paciente": "1984",
        "fecha": "2024-10-30",
        "tipo_imagen": "Rayos X",
        "parte_cuerpo": "Tórax",
        "image_path": "imagenes/rayosx/2024/10/img141_rayosx_torax.jpg",
        "estado_técnico": "Procesamiento técnico efectuado para una visualización óptima del sistema respiratorio.",
        "analisis_IA": {
            "condicion_sugerida": "Neumonía crónica",
            "Resultado preliminar del análisis por IA en %": 12.7,
            "notas": "Infiltrados homogéneos en el lóbulo inferior derecho del pulmón"
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech521",
                "fecha_nota": "2024-10-30",
                "texto": "Equipo de Rayos X calibrado correctamente antes de la captura, sin fallas técnicas"
            }
        ]
    },
    {
        "id_imagen": "img216",
        "id_paciente": "2317",
        "fecha": "2024-12-01",
        "tipo_imagen": "MRI",
        "parte_cuerpo": "Corazón",
        "image_path": "imagenes/mri/2024/12/img216_mri_heart.jpg",
        "estado_técnico":  "Ajustes técnicos aplicados para realzar la calidad en cortes cardíacos y flujo sanguíneo.",
        "analisis_IA": {
            "condicion_sugerida": "Arritmia supreventricular",
            "Resultado preliminar del análisis por IA en %": 98.2,
            "notas": "Cambios en la función del ventrículo izquierdo, con una leve dilatación y alteración en el patrón de contracción"
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech175",
                "fecha_nota": "2024-12-01",
                "texto": "Imagen capturada mediante resonancia magnética a 1.5T, secuencia T1 ponderada"
            }
        ]
    },
    {
        "id_imagen": "img383",
        "id_paciente": "5628",
        "fecha": "2024-09-21",
        "tipo_imagen": "CT",
        "parte_cuerpo": "Abdomen",
        "image_path": "imagenes/ct/2024/09/img122_ct_abdomen.jpg",
        "estado_técnico": "Revisión técnica completa para asegurar detalles claros en tejidos blandos abdominales.",
        "Estado de revision técnica": "aeiou",
        "analisis_IA": {
            "condicion_sugerida": "Enfermedad de Crohn",
            "Resultado preliminar del análisis por IA en %": 65.4,
            "notas": "Engrosamiento segmentario de las paredes intestinales, típicas de la Enfermedad de Crohn."
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech879",
                "fecha_nota": "2024-09-21",
                "texto": "Imagen de resolucion espacial de 1mm x 1mm, con grosor de corte de 3mm."
            }
        ]
    },
    {
        "id_imagen": "img297",
        "id_paciente": "6637",
        "fecha": "2024-11-30",
        "tipo_imagen": "Rayos X",
        "parte_cuerpo": "Fémur",
        "image_path": "imagenes/mri/2024/12/img122_rayosx_femur.jpg",
        "estado_técnico": "Imagen ajustada para obtener nitidez en estructuras óseas y tejidos circundantes.",
        "analisis_IA": {
            "condicion_sugerida": "Sarcoma de Ewing",
            "Resultado preliminar del análisis por IA en %": 72.1,
            "notas": "Áreas de destrucción ósea visibles, donde el tumor ha erosionado el tejido óseo."
        },
        "notas_tecnicas": [
            {
                "id_tecnica": "tech629",
                "fecha_nota": "2024-11-30",
                "texto": "Imagen capturada correctamente, sin artefactos visibles, sin movimientos del paciente."
            }
        ]
    }
    ])



