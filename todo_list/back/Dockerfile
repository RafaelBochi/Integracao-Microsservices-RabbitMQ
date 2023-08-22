FROM alpine:latest

WORKDIR /app

COPY requirements.txt /app

RUN apk add cmake python3-dev g++ make py-pip

# RUN apk add build-essential libdbus-glib-1-dev libgirepository1.0-dev 

RUN apk add dbus-dev glib-dev dbus-x11 

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

# RUN python manage.py migrate

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]