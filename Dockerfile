FROM django
FROM python

WORKDIR /django stripe

COPY ./requirements.txt django_stripe/requirements.txt
RUN pip install -r ./django_stripe/requirements.txt

COPY . /django_stripe

EXPOSE 8000

RUN py manage\local.py runserver
CMD ["py", "manage", "/", "local.py", "runserver"]

