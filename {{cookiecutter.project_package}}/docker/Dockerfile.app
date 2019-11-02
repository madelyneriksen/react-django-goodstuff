# vim: set syntax=dockerfile:

# Dockerfile for the frontend application.
FROM node:latest

WORKDIR /src

RUN mkdir -p app && chown -R node:node /src

USER node

COPY ./frontend/package-lock.json ./frontend/package.json ./
RUN npm ci
ENV PATH /src/node_modules/.bin:$PATH

WORKDIR /src/app

COPY --chown=node:node ./frontend ./
RUN npm run build
