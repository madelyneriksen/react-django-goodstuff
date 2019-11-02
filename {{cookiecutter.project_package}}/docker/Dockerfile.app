# vim: set syntax=dockerfile:

# Dockerfile for the frontend application.
FROM node:latest

WORKDIR /usr/src

COPY ./frontend/package-lock.json ./frontend/package.json ./
RUN npm ci

COPY ./frontend ./
RUN npm run build
