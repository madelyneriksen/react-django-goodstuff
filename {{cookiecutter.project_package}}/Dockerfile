FROM python:3.7

WORKDIR /src/app

ARG REQUIREMENTS=requirements.txt

RUN useradd app

COPY ./requirements.* ./
RUN pip install -r ${REQUIREMENTS}

COPY --chown=app:app . .

USER app

CMD python manage.py runserver
