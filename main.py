from animeflv import AnimeFLV

with AnimeFLV() as api:
    elements = api.search(input("escribe serie: "))
    try:
        for i, elemen in enumerate(elements):
            print(f"{i} - {elemen.title}")
        selection = int(input("selecciona el anime: "))
        info = api.get_anime_info(elements[selection].id)
        info.episodes.reverse()
        for j, episode in enumerate( info.episodes):
            print(f"{j} | Episode - {episode.id}")
        index_episode = int(input("select episode: "))
        serie = elements[selection].id
        capitulo = info.episodes[index_episode].id
        results = api.get_links(serie, capitulo)
        servers_video = api.get_video_servers(serie, capitulo)
        print("----------LUGAR DE DESCARGA-----------")
        for result in results:
            print(f"{result.server} - {result.url}")
        print("---------LUGAR DE VISTA---------")
        for video in servers_video:
            for data in video:
                print(f"{data['title']} - {data['code']}")
                # print(f"{data['title']}")
    except Exception as e:
        print(e)