FROM node:20 AS build

WORKDIR /app
COPY vue-taro/package*.json ./
RUN npm install
COPY vue-taro/ ./
RUN npm run build

# Финальный образ просто собирает статику для хостового Nginx
FROM alpine:latest
WORKDIR /app
COPY --from=build /app/dist ./dist