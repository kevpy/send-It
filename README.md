# SendIT

[![Build Status](https://travis-ci.org/kevpy/SendIT.svg?branch=ft-user-login-apiv1-161773626)](https://travis-ci.org/kevpy/SendIT)  [![Coverage Status](https://coveralls.io/repos/github/kevpy/send-It/badge.svg?branch=ft-user-login-apiv1-161773626)](https://coveralls.io/github/kevpy/send-It?branch=ft-user-login-apiv1-161773626)  [![Maintainability](https://api.codeclimate.com/v1/badges/1aa534e219da7a29a899/maintainability)](https://codeclimate.com/github/kevpy/send-It/maintainability)

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