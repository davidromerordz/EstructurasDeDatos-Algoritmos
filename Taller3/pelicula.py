import csv
from datetime import datetime, date
import time
from algs4.quick import Quick
from algs4.merge import Merge
from algs4.selection import Selection
import stdrandom


class Pelicula:

    def __init__(self, imdb_title_id:str, title:str, original_title:str, year:int, 
    date_published:date, genre:str, duration:int, country:str, language:str, director:str, 
    writer:str, production_company:str, actors:str, description:str, avg_vote:float,
    votes:int, budget:str, usa_gross_income:str, worlwide_gross_income:str, 
    metascore:str, reviews_from_users:float, reviews_from_critics:str):

        self.imdb_title_id = imdb_title_id
        self.title = title
        self.original_title = original_title
        self.year = year
        self.date_published = date_published
        self.genre = genre
        self.duration = duration
        self.country = country
        self.language = language
        self.director = director
        self.writer = writer
        self.production_company = production_company
        self.actors = actors
        self.description = description
        self.avg_vote = avg_vote
        self.votes = votes
        self.budget = budget
        self.usa_gross_income = usa_gross_income
        self.worlwide_gross_income = worlwide_gross_income
        self.metascore = metascore
        self.reviews_from_users = reviews_from_users
        self.reviews_from_critics = reviews_from_critics

    def __str__(self):
        return f"{self.title}, {self.avg_vote}, {self.date_published}"

    def __eq__(self, otraPeli):
         return self.avg_vote == otraPeli.avg_vote

    # PUNTO 2: comparable *se colocó 'mayor que' para efectos prácticos*
    def __lt__(self, otraPeli):
        return self.avg_vote > otraPeli.avg_vote

    # PUNTO 4: nos devuelve el listado en orden descendiente (tarda aprox 90 segundos al utilizar MergeSort)
    def listarPorRating(pelis):
        comienzo = time.time()
        Merge.sort(pelis)
        final = time.time()

        print(f'El método ListarPorRating tarda: {final - comienzo} segundos en ordenar el arreglo.')

    # PUNTO 5: retorna el listado ordenado por titulo y fecha
    def comparator(pelis):
        pelis.sort(key=lambda x: (f'{x.title}', f'{x.date_published}'))

    # PUNTO 6
    def listarPorComparador(pelis:list, comparador:str):

        """
        COMPARADOR: \n
        Ecriba "promedio" si desea listar por avg_vote \n
        Ecriba "titulo" si desea listar por title \n
        Ecriba "fecha" si desea listar por date_published

        """

        if comparador == "promedio":
            return pelis.sort(key=lambda x: x.avg_vote)

        if comparador == "titulo":
            return pelis.sort(key=lambda x: x.title)
        
        if comparador == "fecha":
            return pelis.sort(key=lambda x: x.date_published)

    
    # PUNTO 7-8
    def medirTiempoALGcuadratico(pelis:list):

        stdrandom.shuffle(pelis)
        comienzo = time.time()
        Selection.sort(pelis)
        final = time.time()

        return f'El algoritmo de ordenación cuadrático tarda: {final - comienzo} segundos.'

    def medirTiempoALGlinAr(pelis:list):

        stdrandom.shuffle(pelis)
        comienzo = time.time()
        Quick.sort(pelis)
        final = time.time()

        print(f'El algoritmo de ordenación propio del lengiaje tarda: {final - comienzo} segundos.')

    def medirTiempoALGpython(pelis:list):

        stdrandom.shuffle(pelis)
        comienzo = time.time()
        pelis.sort()
        final = time.time()

        print(f'El algoritmo de ordenación propio del lengiaje tarda: {final - comienzo} segundos.')
   




def parseDate(f:str):
    if f.startswith('TV Movie '):
        return None
    if f.count('-')==2:
        return datetime.strptime(f, '%Y-%m-%d').date()
    if f.isdigit():
        return datetime.strptime(f, '%Y').date()
    return None



def read_csv(filename):
    pelis = []
    count = 0
    with open(filename, encoding='utf8') as fh:
        reader = csv.reader(fh, delimiter=',', quotechar='"')
        for rec in reader:
            count += 1
            if count==1:
                continue
            try:
                fecha_publicacion = parseDate(rec[4])
                pelicula = Pelicula(
                    rec[0],
                    rec[1],
                    rec[2],
                    int(rec[3]),
                    fecha_publicacion,
                    rec[5],
                    int(rec[6]),
                    rec[7],
                    rec[8],
                    rec[9],
                    rec[10],
                    rec[11],
                    rec[12],
                    rec[13],
                    float(rec[14]),
                    int(rec[15]),
                    rec[16],
                    rec[17],
                    rec[18],
                    rec[19],
                    rec[20],
                    rec[21]
                )
                pelis.append(pelicula)
            except:
                print('ERROR')
    return pelis