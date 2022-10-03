FROM python:3.7.14-alpine3.16

# Environment variables for flask app
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "server.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

COPY . /api

WORKDIR /api

RUN pip3 install -r requirements.txt 

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
