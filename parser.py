import requests
from bs4 import BeautifulSoup as BS

def playbill(cinema):
    if cinema == "Empire_of_Dreams":
        id_cinema = "3008946"
    if cinema == "Petrel":
        id_cinema = "8320137"
    if cinema == "Rio":
        id_cinema = "8151399"

    kino = ''
    r = requests.get(f"https://nn.kinoafisha.info/cinema/{id_cinema}/schedule/?date=&order=movie")
    html = BS(r.content, 'html.parser')
    items = html.select(".schedule_showtimes > .showtimes_item > .showtimes_cell > .showtimesMovie_wrapper")
    for el in items:
        title = el.select(".showtimesMovie_info > span")
        kino += str(title[0].text) + str('\n')
    
    if kino == '': kino = 'Кажется нет расписания...'
    
    return kino
