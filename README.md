# Working with FastAPI to create Python Unittest

This is a simple FastAPI app that performs simple historical weather queries for Plano, TX

    * It is from the time period February 29th, 1984 to February 29th, 2024

We will see how we can use ChatGPT to create python unittests for the following endpoints:

To create the app you will need docker, docker-compose and make then run:

    make build

To run the app, run the following command:

    make up

To run the tests, run the following command:

    make test

If you want to add more tests, put them within the tests directory

The app is accessible at url is:

    http://localhost:8080/

The Swagger API docs are at:

    http://localhost:8080/docs


## Resources:

Learn more about FastAPI

    https://fastapi.tiangolo.com/

To browse SQLite database using a GUI tool

    https://sqlitebrowser.org/

To learn more about Pytest

    https://docs.pytest.org/en/8.0.x/

Very cool weather api

    https://openweathermap.org/

### This is only for demo purposes and should not be used in a production environment!