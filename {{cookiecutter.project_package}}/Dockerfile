# Build + minify frontend assets.
FROM node AS frontend
WORKDIR /src/app

COPY ./package.* ./
RUN npm ci

COPY ./frontend ./

RUN npm run build

# Python application container.
FROM python:3.7 AS app

WORKDIR /src/app

ARG REQUIREMENTS=requirements.txt

RUN useradd app

COPY ./requirements.* ./
RUN pip install -r ${REQUIREMENTS}

COPY --chown=app:app . .

COPY --from=frontend --chown=app:app /src/app/dist ./public

USER app

CMD python manage.py runserver
