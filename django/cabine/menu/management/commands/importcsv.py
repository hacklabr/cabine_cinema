from django.core.management.base import NoArgsCommand
from optparse import make_option
from menu.models import *

class Command(NoArgsCommand):

    help = "Whatever you want to print here"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )
    
    def handle_noargs(self, **options):
        data = self.datadict()
        for index in data:
            iid=str(index)
            clip = data[iid]
            print "++ %s ++" % iid
            c = Clip(id=iid, name=clip["name"], orig_name=clip["orig_name"], sinopse=clip["sinopse"], classificacao=clip["classificacao"], count=0)
            c.save()
        
            for j in clip["director"].split(','):
                dire = j.strip()
                dire = self.query(Director, dire)
                c.director.add(dire)
                print "d\r"

            for j in clip["country"].split('/'):
                country = j.strip()
                country = self.query(Country, country)
                c.country.add(country)
                print "c\r"

            for j in clip["year"].split(','):
                year = j.strip()
                year = self.query(Year, year)
                c.year = year
                print "y\r"

            for j in clip["genre"].split('/'):
                genre = j.strip()
                genre = self.query(Genre, genre)
                c.genre.add(genre)
                print "g\r"

            for j in clip["star"].split(','):
                star = j.strip()
                substars = star.split(' e ')
                if len(substars) > 1:
                    for s in substars:
                        star = self.query(Star, s)
                        c.star.add(star)
                else:
                    star = self.query(Star, star)
                    c.star.add(star)
                print "s\r"

            c.save()

    def query(self,Obj, nome):
        try:
            return Obj.objects.get(name=nome)
        except:
            obj = Obj(name=nome)
            obj.save()
            return obj

    def datadict(self):
        data = open("../../doc/lista filmes cabine.csv","r").read().split("\n")
        data.pop(0)
        data_d = {}
        for i in data:
            try:
                data_d[i.split("|")[0]] = { "name": i.split("|")[1],
                                        "orig_name": i.split("|")[2],
                                        "director": i.split("|")[3],
                                        "country": i.split("|")[4],
                                        "year": i.split("|")[5],
                                        "genre": i.split("|")[6],
                                        "sinopse": i.split("|")[7],
                                        "star": i.split("|")[8],
                                        "classificacao": i.split("|")[9],
                                        }
            except:
                pass

        return data_d
