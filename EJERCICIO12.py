
#SOLUCION:

# PRIMERO DE SOLICITA AL USUARIO EL NOMBRE DEL ARCHIVO
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo (sufijo)
extension = nombre_archivo.split('.')[-1].lower() if '.' in nombre_archivo else None

# Definir los sufijos y sus tipos MIME correspondientes
sufijos_tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

# Obtener el tipo MIME correspondiente o 'application/octet-stream' si no coincide con ningún sufijo
tipo_mime = sufijos_tipos_mime.get(extension, 'application/octet-stream')

# Mostrar el tipo MIME
print(f"El tipo MIME para el archivo {nombre_archivo} es: {tipo_mime}")
