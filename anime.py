from animeflv import AnimeFLV

with AnimeFLV() as api:
    
    elements = api.search(input("escribe serie: "))
    for elemen in elements:
        print(f"{elemen.title}")
# elements = api.search(input("escribe serie: "))
# for i, element in enumerate(elements):
#     print(f"{i} - {element.title}")