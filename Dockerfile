FROM node:15.3.0-alpine3.10
RUN apk add --no-cache tini curl
WORKDIR /app
COPY runapp.js .
EXPOSE 6060
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "runapp.js"]
