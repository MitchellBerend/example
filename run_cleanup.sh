#! /bin/bash


sudo docker-compose down -v
sudo docker rmi example_example
sudo rm -rf db_data

