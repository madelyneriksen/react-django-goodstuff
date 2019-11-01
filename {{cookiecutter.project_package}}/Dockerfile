FROM python:3.7-slim

WORKDIR /src/app

ARG REQUIREMENTS=requirements.txt

RUN useradd app

COPY ./requirements.* ./
RUN pip install -r ${REQUIREMENTS}

USER app

COPY --chown=app:app . .

CMD python manage.py runserver
