# Studio Application
This application  was created using Django,Reat. and Docker 




# App Concepts
<ul>
<li>The back-end of this app is builded on Django. The following endpoints are using by React to pupolate the front-end:</li>
<li>The front-end of this app is builed on React <li>
<li> Docker is being used to package the front-end, back-end,nginx  into containers</li>
<li>The app will display information  about the "Studio Company" </li>
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
 

 











## How to run this app

Download the app and Run
```bash
$ python manage.py runserver
```
 