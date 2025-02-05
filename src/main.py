from animeflv import AnimeFLV
import os

def limpiar_terminal():
   if os.name == 'nt':  # Windows
      os.system('cls')
   else:  # Linux/macOS
      os.system('clear')

def buscar_anime():
   with AnimeFLV() as api:
      elements = api.search(input("escribe serie: "))
      while( elements==[] ):
         elements = api.search(input("escribe serie: "))
      elem_sort = sorted(elements, key=lambda x: x.type)

      try:
         for i, elemen in enumerate(elem_sort):
            print(f"{i+1}: {elemen.type}=>{elemen.title}")
         selection = int(input("selecciona el anime: "))
         info = api.get_anime_info(elements[selection-1].id)
         info.episodes.reverse()

         print(f'+'*len(info.title), end='')
         print('++++++++++++++++++++')
         print(f'++++++++++{info.title}++++++++++')
         print(f'+'*len(info.title), end='')
         print('++++++++++++++++++++')

         for j, episode in enumerate( info.episodes):
            print(f"\t{j+1} | Episode - {episode.id}")

         index_episode = int(input("select episode: "))
         serie = elements[selection-1].id
         capitulo = info.episodes[index_episode-1].id
         results = api.get_links(serie, capitulo)
         servers_video = api.get_video_servers(serie, capitulo)

         print("----------LUGAR DE DESCARGA-----------")
         for result in results:
            print(f"{result.server}: {result.url}")
         print("---------LUGAR DE VISTA---------")
         for video in servers_video:
            for data in video:
               print(f"{data['title']}: {data['code']}")
      except Exception as e:
         print(e)

if __name__=="__main__":

   continuar = 1
   while( continuar==1 ):
      buscar_anime()
      print('Continuar')
      print('1: SI')
      print('2: NO')
      continuar = int( input('Seleccion: ') )
      limpiar_terminal()




