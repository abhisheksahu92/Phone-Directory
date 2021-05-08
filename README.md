# Phone Directory
    It is a Contact Management Software designed to get information of caller and their call details. Using this software, you can easily insert, update and delete the data of a caller and their call details.

## There are two steps to follow:
1. Navigate to Phone-Directory directory.
2. Run pip install -r requirements.txt
3. Run python manage.py runserver
4. Open your web browser and enter http://127.0.0.1:8000/phone.
5. After sending the request you will recieve response.  

## OR

1. Navigate to Phone-Directory directory.
2. Download and install Docker and docker-compose using https://www.docker.com/products/docker-desktop.
3. Run docker compose up --build
4. Go to browser and enter http://127.0.0.1:8000/phone/.

### Commands lists:
1. python manage.py populate_phone
    #### This command will create 50 Person Details.   
2. python manage.py populate_populate_call_details
    #### This command will create 10 Person's call details.
4. python manage.py delete_phone
    #### This command will delete all the data.
5. python manage.py runserver
    #### this command will start the server.
  
