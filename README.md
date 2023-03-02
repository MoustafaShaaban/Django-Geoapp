# backend

My Django Cookiecutter Template

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT


###  Project Goals

* Use Django admin site to import data from different sources (CSV, JSON, ...) into the database.

* Use the power of Folium to visualize data generated from Django Database on a Leaflet JS map.

* Visualize data using Folium's Simple Markers.

* Users can register for an account, login, and update their information (handled by Cookiecutter Django)

* Authenticated users can add, import, or export data using django forms.

### Project Preview

* [Youtube](https://www.youtube.com/watch?v=dqDSYeppbGI)

* [GIF](./geoapp.gif)



### To get started with this project

* Make sure that both Docker and docker-compose are installed in your system.

* Clone the repository: git clone https://github.com/MoustafaShaaban/Django-Geoapp.git

* Change directory to backend directory ``` cd backend ```

* Build the docker image to develop the project locally using docker-compose:

``` docker-compose -f local.yml build ```

* Create the database by running the following commands:

` docker-compose -f local.yml run --rm django python manage.py migrate `

* Create a super user:

` docker-compose -f local.yml run --rm django python manage.py createsuperuser `

* Now run the project:

``` docker-compose -f local.yml up ```


* Open the web browser and go to ` http://localhost:8000/ ` to see the results.


For more information about the available commands in this project check the Cookiecutter Django [Documentation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html#build-the-stack)





### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
