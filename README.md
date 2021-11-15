# "Studio Company"
This application display the services, portfolio, about, and team information about the "Studio Company"




# App Concepts
<ul>
<li>The back-end of this app is builded on Django. Django will prepare the data to server to the front-end.</li>
<li>The front-end of this app is builed on React, React will digest end-points to display the company information.  </li>
<li> Docker is being used to package the front-end, back-end,nginx  into containers </li>
</ul>

# Stack
<ul>

<li>Django</li>
<li>Django Rest Framework </li>
<li>Reactjs </li>
<li>nginx </li>
<li>Docker</li>
<li>docker-compose</li>

</ul>


## Dev Enviroment- <b style='color:red'>Run the followings commands  to start the dev-environment</b>
<ul>
<li>
 
```bash
$ docker-compose -f docker-compose-dev.yml  build
```
</li>
<li>
 
```bash
$ docker-compose -f docker-compose-dev.yml  Up
```
</li>
</ul>


### The front-end run on port 3000. Ex: http://localhost:3000/
![Alt text](frontend/client/src/assets/dev_front.png "Home" )


### The back-end run on port 8000. Ex: http://localhost:8000/
![Alt text](frontend/client/src/assets/dev_back.png "Home" )
 

 ## Production Enviroment- <b style='color:red'>Run the followings commands  to start the prod-environment</b>
<ul>
<li>
 
```bash
$ docker-compose -f docker-compose-prod.yml  build
```
</li>
<li>
 
```bash
$ docker-compose -f docker-compose-prod.yml  Up
```
</li>
</ul>


### On production, the front-end is not longer being serve on port 3000; nginx is being used to manage the traffic
![Alt text](frontend/client/src/assets/prod_front.png "Home" )


### On production, the back-end is not longer being serve on port 8000; nginx is being used to manage the traffic
![Alt text](frontend/client/src/assets/prod_back.png "Home" )








####  API end-points:
<ul>
<li>/api/services/</li>
<li>/api/portfolio/</li>
<li>/api/team/</li>
<li>/api/about/</li>
</ul>