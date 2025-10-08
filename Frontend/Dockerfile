# Сборка Vue
FROM node:20 AS build
WORKDIR /app
COPY vue-taro/package*.json ./
RUN npm install
COPY vue-taro/ .
RUN npm run build

# Nginx для продакшена
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
