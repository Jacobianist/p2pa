# p2pca

# 1. Up django server

``` Powershell
py -m venv venv # creating virtual environment venv
.\venv\Scripts\activate # activating environment
py -m pip install --upgrade pip
py -m pip install Django
mkdir src && cd .\src # source files folder
django-admin startproject ArbitrageProject . # creating Project
py manage.py startapp api # creating App
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver # local server up & check it localhttp://127.0.0.1:8000/
```

# 2. api
`/api/add` 
requests to:
- https://thesimpsonsquoteapi.glitch.me/quotes
- https://www.breakingbadapi.com/api/quote/random
and saves response random quotes into two tables,
but show only one(!)

`/api`
show last qoutes from both tables

`/admin`
adminpanel