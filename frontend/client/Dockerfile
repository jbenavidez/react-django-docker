FROM  node:14.9

WORKDIR /react_app

COPY . . 
COPY package.json /react_app
COPY package-lock.json /react_app

RUN npm install

# COPY . /react_app

# Get build argument and set environment variable
ARG base_url
ENV REACT_APP_URI=${base_url}

#RUN npm run build 
#CMD ["npm", "start"]