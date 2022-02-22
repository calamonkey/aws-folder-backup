FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /backup
RUN crontab crontab

# Start backup service
CMD [ "crond", "-f" ]
