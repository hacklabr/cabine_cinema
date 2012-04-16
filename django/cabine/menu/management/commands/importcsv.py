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
        for i in data:
            iid=str(i)
            clip = data[iid]
            c = Clip(id=iid, name=clip["name"], orig_name=clip["orig_name"], sinopse=clip["sinopse"], classificacao=clip["classificacao"])
            c.save()

            for j in clip["director"].split(','):
                dire = j.strip()
                dire = self.query(Director, dire)
                c.director.add(dire)

            for j in clip["country"].split(','):
                dire = j.strip()
                dire = self.query(Country, dire)
                c.country = dire

            for j in clip["year"].split(','):
                dire = j.strip()
                dire = self.query(Year, dire)
                c.year = dire

            for j in clip["genre"].split(','):
                dire = j.strip()
                dire = self.query(Genre, dire)
                c.genre.add(dire)

            for j in clip["star"].split(','):
                dire = j.strip()
                dire = self.query(Star, dire)
                c.star.add(dire)

            c.save()

    def query(self,Obj, nome):
        try:
            return Obj.objects.get(name=nome)
        except:
            o = Obj(name=nome)
            o.save()
            return o

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
