
.PHONY: run
run:
	# The django container does not wait for the database to be up and running so we
	# restart it after 3 seconds. There is probably a better way to do this.
	@sudo docker-compose build
	@sudo docker-compose up -d
	@sleep 3
	@sudo docker-compose restart example
	@sudo docker-compose run --rm example migrate

.PHONY: test
test:
	@sudo docker-compose build
	@sudo docker-compose up -d
	@sudo docker-compose run --rm example test
	@RV=$?
	@sudo docker-compose down -v
	@sudo docker rmi mitchellberend/example
	@exit $$RV

.PHONY: clean
clean:
	@sudo docker-compose down -v
	@sudo docker rmi example_example
	@sudo rm -rf db_data
