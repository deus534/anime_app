import requests
from bs4 import BeautifulSoup

def obtener_link_video(url_pagina):
    # Hacer una solicitud GET a la página
    response = requests.get(url_pagina)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Buscar el enlace del video (esto dependerá del sitio)
        video_tag = soup.find('video')  # Busca una etiqueta <video>
        if video_tag and 'src' in video_tag.attrs:
            return video_tag['src']

        # Alternativamente, busca enlaces <source> dentro de <video>
        source_tag = soup.find('source')
        if source_tag and 'src' in source_tag.attrs:
            return source_tag['src']

        # Otras plataformas pueden requerir más análisis
        print("No se encontró el enlace del video.")
    else:
        print(f"Error al acceder a la página: {response.status_code}")
    return None

# URL de la página HTML
url = "https://watchadsontape.com/e/ldr07aAZdJu7yR1/"
url = "https://www.youtube.com/watch?v=oq4LfEedlFU&ab_channel=BaityBait"
link_video = obtener_link_video(url)
print("Enlace del video:", link_video)

