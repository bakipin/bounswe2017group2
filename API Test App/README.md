# README

# Concert API
Concert API is the API for a small part of our Concert project. You can perfom CRUD operations on Concerts and Users.

## Setup
Assuming that you have pip, install django as follows:
pip install django
pip install djangorestframework
pip install pygments
After these installations 

Create a folder to copy the branch.
Clone the repository: git clone https://github.com/bounswe/bounswe2017group2.git ~/Desktop/ConcertAPI
Go into the folder: ConcertAPI
All the required, most recent files are there.

Move into the folder of the api: cd "ConcertAPI"
Yes we have 2 concerts API folders consecutively
Activate the environment: source env/bin/activate
Go into the ConcertAPI folder: cd ConcertAPI
Run the server: python manage.py runserver

## Endpoints
### Concert Endpoints
See the Concerts lists by going to the address "http://127.0.0.1:8000/concert/"

* Get All Concerts [GET]

* Get A Specific Concert [GET]
* Create New Concert [POST]
* Update A Concert [PUT]
* Delete A Concert [DELETE]

### User Endpoints
See the Users lists by going to the adress "http://127.0.0.1:8000/user/"

* Get All Users [GET]
* Get A Specific User [GET]
* Create New User [POST]
* Update A User [PUT]
* Delete A User [DELETE]

Post new concert by typing: "http --json POST http://127.0.0.1:8000/concert/ artist="Sezen Aksu", location = "Istanbul", date = "2017-10-10", minPrice = 100, maxPrice = 300"
Post new user by typing "http --json POST http://127.0.0.1:8000/user/" posting json file by writing "http://127.0.0.1:8000/users/ name="Ali", email = "aliveli@mail.com", password = "aosjd123", age = 23"