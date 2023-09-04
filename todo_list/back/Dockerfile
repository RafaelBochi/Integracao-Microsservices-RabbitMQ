FROM python

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && \
    apt-get install -y libsystemd-dev


# RUN pip cache purge

# RUN pip install --upgrade setuptools pip PyYAML

RUN pip install -r requirements.txt

# RUN python manage.py migrate

COPY . .

# RUN python manage.py migrate

EXPOSE 8003

CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]