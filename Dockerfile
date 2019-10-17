FROM python:3.7

# Install wait to wait for MongoDB
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /usr/local/bin/wait
RUN chmod +x /usr/local/bin/wait

ENV PYTHONUNBUFFERED 1
RUN mkdir /oldschoolmtgdb
WORKDIR /oldschoolmtgdb
COPY . /oldschoolmtgdb/
RUN pip install -r requirements.txt
