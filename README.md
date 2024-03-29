# Restaurant kitchen service project

Django project of managing processes in your own restaurant

> https://restaurant-kitchen-service-bqkn.onrender.com/

## Installing / Getting started

Python3 must be installed


```shell
git clone the-link-from-your-forked-repo
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
- Set the environment variable DJANGO_SECRET_KEY:

    `random-string`



- Use the following command to load prepared data from fixture to test and debug your code:

  `python manage.py loaddata data_for_loading.json`


- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`


### Production Login & Password
````
Login: `admin.user`
Password: `123qweasdzxc`
````
## Features

* Authentication functionality for Cook/User
* Managing processes of dish-creation
* Admin panel for adding cooks
* Search by name


## Demo
![Website interface](demo.png)
