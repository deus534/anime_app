import requests

def descargar_archivo(url, destino):
    # Realizamos la solicitud GET a la URL
    respuesta = requests.get(url, stream=True)
    
    # Comprobamos si la respuesta es exitosa (status code 200)
    if respuesta.status_code == 200:
        with open(destino, 'wb') as archivo:
            # Escribimos el contenido del archivo en bloques
            for bloque in respuesta.iter_content(1024):
                archivo.write(bloque)
        print(f"Archivo descargado con éxito en {destino}")
    else:
        print("Error al descargar el archivo, status code:", respuesta.status_code)

# Ejemplo de uso
url_de_descarga = input("introduce url: ")  # Reemplaza con la URL del archivo en 1Fichier
destino = 'archivo_descargado.zip'  # Nombre del archivo que quieres guardar

descargar_archivo(url_de_descarga, destino)
