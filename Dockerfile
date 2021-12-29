
FROM python:3.8

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

#RUN adduser -D myuser
#
#

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "test.py" ]

