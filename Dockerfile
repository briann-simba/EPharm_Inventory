FROM python:3.8.10

COPY requirements.txt /app/requirements.txt

#configure server
RUN set -ex\
    && pip3 install --upgrade pip \
    && pip3 install -r /app/requirements.txt

#working directory
WORKDIR /app

ADD . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", ":8000","--workers","3","storefront.wsgi:application" ]

# CMD gunicorn storefront.wsgi:application --bind 0.0.0.0:$PORT