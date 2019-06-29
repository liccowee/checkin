FROM alpine
EXPOSE 3000
ADD config/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /var/www/localhost/htdocs
COPY . /var/www/localhost/htdocs
RUN apk add nginx && \
    mkdir /run/nginx && \
    apk add nodejs && \
    apk add npm && \
    cd /var/www/localhost/htdocs && \
    rm -rf node_modules && \
    npm install;
CMD ["/bin/sh", "-c", "exec nginx -g 'daemon off;';"]
CMD ["npm", "start"]