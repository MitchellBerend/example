#! /bin/bash

sudo docker-compose build
sudo docker-compose up -d
sudo docker-compose run --rm example test
sudo docker-compose down -v
sudo docker rmi example_example

