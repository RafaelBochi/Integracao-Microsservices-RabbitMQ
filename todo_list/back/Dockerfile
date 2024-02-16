FROM python

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && \
    apt-get install -y libsystemd-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8003

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
