FROM python:3.9-alpine

RUN mkdir hh_servise

WORKDIR /hh_servise

COPY . /hh_servise/

RUN pip3 install -r req.txt

EXPOSE 8010

CMD python3 manage.py collectstatic --no-input && python3 manage.py makemigrations && python3 manage.py migrate &&  python3 manage.py runserver 0.0.0.0:8010