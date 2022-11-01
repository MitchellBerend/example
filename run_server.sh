#! /bin/bash

sudo docker-compose build
sudo docker-compose up -d

# The django container does not wait for the database to be up and running so we
# restart it after 3 seconds. There is probably a better way to do this.
sleep 3

sudo docker-compose restart example

sudo docker-compose run --rm example migrate
