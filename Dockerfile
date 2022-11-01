FROM python:3.10.6

EXPOSE 8001:8000

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

RUN rm /tmp/requirements.txt

COPY example /srv/example

WORKDIR /srv/example

CMD ["runserver", "0.0.0.0:8000"]

ENTRYPOINT ["python", "-u", "manage.py"]
