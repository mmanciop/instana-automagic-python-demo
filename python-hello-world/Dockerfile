FROM jfloff/alpine-python
COPY . /app
WORKDIR /app

RUN pip install uwsgi

ENTRYPOINT ["uwsgi"]
CMD ["--http", ":5000", "--wsgi-file", "app.py"]