# SendIT

[![Build Status](https://travis-ci.org/kevpy/send-It.svg?branch=ft-user-login-apiv1-161773626)](https://travis-ci.org/kevpy/send-It)  [![Coverage Status](https://coveralls.io/repos/github/kevpy/send-It/badge.svg?branch=ft-user-login-apiv1-161773626)](https://coveralls.io/github/kevpy/send-It?branch=ft-user-login-apiv1-161773626)  [![Maintainability](https://api.codeclimate.com/v1/badges/1aa534e219da7a29a899/maintainability)](https://codeclimate.com/github/kevpy/send-It/maintainability)

**SendIt** is a courier service that helps users deliver parcels to different destinations.

It provides courier quotes based on weight categories

In `backend/` directory you will find a flask app.
It has the following features:

- `POST` -- Login as a user - `api/v1/login`
- `POST` -- Create/register a user - `api/v1/register`
- `POST` -- Create a parcel delivery order - `api/v1/parcels`
- `GET` -- Fetch all parcel delivery orders  - `api/v1/parcels`
- `GET` -- Fetch a specific parcel delivery order  - `api/v1/parcels/<parcel_id>`
- `GET` -- Fetch all parcel delivery orders by a specific user  - `api/v1/users/<user_id>/parcels`
- `PUT` -- Cancel a specific parcel delivery order - `api/v1/parcels/<parcel_id>/cancel`

You can get a running instance of the API on **Heroku**. 
Here's the [documentation](https://documenter.getpostman.com/view/5866871/RzZAkype).
For authorization, on successful login you are given a token. Use the token as a beares token for all requests except `login` and `signup`

If you wish to run a local instance please

Here's the [documentation](https://documenter.getpostman.com/view/5866871/RzZAkybV) on how to consume the API on a local machine. Register then login to get a token or use the example login in the documentatin.

All routes other than `api/v1/login` and `api/v1/register` need authorization

But first lets setup a working app

## Instructions to run the app

Clone this git repository
-` git clone https://github.com/kevpy/send-It.git`

Checkout the latest working branch
-`git checkout ft-user-login-apiv1-161773626`

If you are not on the specified branch run `git fetch --all` and re-run the above command

On the root directory i.e **send-It/**, create a python virtual environment.
-`virtualenv env` _env_ can be any environment name you git it.
If you do not have virtual env installed on your system install it first, though any
latest python version up from `3.4.*` comes with virtualenv

Activate the virtual environment. If in the root directory of `send-It/` run the following
command in your terminal:
-`source env/bin/activate`

If you have gotten your virtual environment working, install the dependencies
to the environment. Run this command
-`pip install -r requirements.txt`

On successfully installing the requirements, export the flask entry point to your 
system environment virables.
-`cd backend`
-`export FLASK_APP=run.py`

Run flask
-`flask run`

You should now have a running flask instance.

## Running Tests

If you wish to run tests on this repository follow these instructions.

On your virtual environment install these two other python libraries with the following commands.
 - `pip install pytest`
 - `pip install pytest-cov`

 To run the tests, navigate to the root directory of `send-It/`.
 On your terminal run `py.test` or `pytest`. You should be able to see the tests results.

 To see tests with test coverage run `pytest --cov=backend/`. This command specifies to `pytest` which directory to run tests and coverage against.

 You can alternatively click on the top badges and check agaisnt the specified tests.
