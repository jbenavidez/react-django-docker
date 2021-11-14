FROM  node:14.9

WORKDIR /react_app

COPY package.json /react_app
COPY package-lock.json /react_app

RUN npm install

COPY . /react_app

CMD ["npm", "start"]