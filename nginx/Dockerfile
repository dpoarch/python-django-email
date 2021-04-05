FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY sites-enabled/ /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]