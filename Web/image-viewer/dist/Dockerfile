FROM node:18-alpine

WORKDIR /chal
COPY . .
WORKDIR /chal/codeNstuff/codeNstuff

RUN npm install express
RUN npm install ejs

CMD ["node", "frontend.js"]
EXPOSE 2001
    
