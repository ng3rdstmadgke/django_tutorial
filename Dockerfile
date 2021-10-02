FROM python:3.8.12-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

#RUN apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
