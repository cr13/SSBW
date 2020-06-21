FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install
RUN npm i jquery --save
RUN npm install react-bootstrap bootstrap
RUN npm install react-router
RUN npm install react-router-dom
RUN npm install axios
RUN npm install popper

EXPOSE 3000
CMD ["npm", "start"]
