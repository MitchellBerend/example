# README
---


This repo does require docker and docker-compose and sudo privileges. Make sure
you review the scripts before you actually run them.

There are a number of tests that live in `example/tiny/tests.py`. These can be
run with `./run_tests.sh`.

You can also just run the app as a stand alone project if you want to actually
interact with it via a browser or shell. To make this happen use
`./run_server.sh`. This script will start 2 docker containers. One with the
django app and one with a postgres database.

This will not create any (super)users so you will need to do that manually if
you want superuser access. You can do this by running the command `sudo
docker-compose run --rm example createsuperuser` and following the prompts. The
[login](http://localhost:8001/admin) is straightforward if you create a super
user.

Running the app this way create some garbage. to clean this up run
`./run_cleanup.sh`. This will delete the file store of the postgres database and
the docker image that was built last by the `run_server` script.


Todo:
- [x] make runscript
- [x] write tests
- [x] finish readme
