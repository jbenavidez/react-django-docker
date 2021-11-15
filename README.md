# Studio Application
This application  was created using Django,Reat. and Docker 




# App Concepts
<ul>
<li>The back-end of this app is builded on Django. The following endpoints are using by React to pupolate the front-end:
    <ol>
    <li>/api/services/<li>
    <li>/api/portfolio/<li>
    <li>/api/team/<li>
    <li>/api/about/<li>
    </ol>
</li>
<li>The front-end of this app is builed on React <li>
<li> Docker is being use to package the front-end, back-end,nginx  into containers
  
</li>
 <li>The uses will be able to generate the report by filter the data according to their needs </li>


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
# Result

### The fron-end run on port 3000. Ex: http://localhost:3000/
![Alt text](/frontend/client/src/assets/homepage.png "Home" )

 

 











## How to run this app

Download the app and Run
```bash
$ python manage.py runserver
```
 