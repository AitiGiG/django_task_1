# 1. Команды для крада
python3 manage.py shell
from author.models import Author
from books.models import Books
# list:
    Authoor.objects.all() - получение всех данных
# retrieve:
    author1 = Author.objects.get(pk=1) получение данных по определённым критериям
# create:
    Author.objects.create(
       name =  'Gogol',
       age = '1998-03-03',
       alias = 'Stigman',
    )
# update:
    Author.objects.filter(pk=1).update(name='Pushkin', age= '1900-06-06', alias= 'now alias')
# delete:
    author1.delete()  
