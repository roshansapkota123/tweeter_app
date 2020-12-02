FROM python:3.6

RUN mkdir /app
WORKDIR /app

# System prerequisites
RUN apt-get update \
 && apt-get -y install build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Gunicorn. If Gunicorn is already present in your requirements.txt,
# you don't need that (but if won't hurt).
RUN pip install gunicorn

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

RUN ./docker_prebuild.sh

EXPOSE 8000

CMD ["gunicorn", "--access-logfile=-", "--error-logfile=-", "--bind=0.0.0.0:8000", "--workers=1", "tweeter_app.wsgi"]
