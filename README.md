comenzi:
# pentru modificari
python manage.py makemigrations

# pentru accessarea serverului
python manage.py runserver
# si apasam pe likul din terminal la care apoi adaugam terminatia /admin sau backend/product/

# pentru iesirea din server
CTRL+C

# daca vreau sa adauga ceva din postman
introduc linkul http://127.0.0.1:8000/backend/product/

# apoi fac ce scrie in views
'''''''''''''''''''''''''''''''''''''''''''''''''''''
api_view(['POST'])
def add_product(request):
    # get params from request
    # insert params in database
    # return success / or not use http codes for this
'''''''''''''''''''''''''''''''''''''''''''''''''''''