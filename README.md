# Titanic End points

The endpoints was developed  using flask. 

Flask is a lightweight web application framework designed euipped only with web app development and  to get results fast.Its strength lies in its customizability and thus 


leave room to make the app more detailed in the future.To read more about [Flask] (https://flask.palletsprojects.com/en/2.0.x/). 


The endpoint specification given can be found [here] (./API.md).


# Project Architecture

The project structure goes thus :

``` bash
 ├── build.sh
├── docker-compose.yml
├── dockerfile
├── k8s
│   ├── Mongo
│   │   ├── 01-mongo-ns.yaml
│   │   ├── 02-secret.yaml
│   │   ├── 03-volume.yaml
│   │   ├── 04-pvc.yaml
│   │   ├── db-deployment.yaml
│   │   └── mongo-service.yaml
│   └── app
│       ├── 01-titanic-ns.yaml
│       ├── 02-config.yaml
│       ├── 03-titanic-svc.yaml
│       └── 04-titanic.yaml
├── kubect_deploy.sh
├── mongodb.sh
├── requirements.txt
├── server
│   ├── README.md
│   ├── app
│   │   ├── API.md
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── api.cpython-39.pyc
│   │   │   ├── config_module.cpython-39.pyc
│   │   │   └── controllers.cpython-39.pyc
│   │   ├── api.py
│   │   ├── config_module.py
│   │   ├── controllers.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   ├── db.cpython-39.pyc
│   │   │   │   └── models.cpython-39.pyc
│   │   │   ├── db.py
│   │   │   └── models.py
│   │   └── wsgi.py
│   ├── pytest.ini
│   ├── swagger.yml
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-39.pyc
│       │   ├── test_client.cpython-39-pytest-6.2.4.pyc
│       │   └── test_client.cpython-39.pyc
│       ├── test.py
│       └── test_client.py
└── titanic.csv
 ```

 - app - This contains the implemntation of the end points. It contains the Database  directory which contains the database model and the connection to the database. It also contains  the configuration model and the env file.

 - test: This contains testing of the app logic

 - K8s: for kubernetes

 - .sh files:  script for automating for linux user


    The .env file should be created using the current .env as guide

    The Environment can only be dev,prod,test however a default mongodb uri has been set which can be found here .


 # Running the App Locally
    
    Perequsite : Ensure Python is installed, if not follow this [link](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html) and [here] (https://docs.mongodb.com/guides/server/install/)  for mongodb

    - Clone the repo

        git clone   

    - Install the dependecies : 

            ```python
            pip install -r requirements.txt
            ```
    
    -  Create a database and Collection 

    - Import titanic.csv using the mongo compass [link] (https://docs.mongodb.com/compass/current/import-export/)  or mongoimport [link] (https://docs.mongodb.com/manual/reference/program/mongoimport/)


    - Create a `.env` and update needed variables for the  MongoDB server; check `.env.example`


    -   Run the api.py in the app directory

            Go to http://127.0.0.1:5000 to view the app

# Using Docker
        You can install docker from [here](https://docs.docker.com/get-docker/). 


## Building only the Docker api Image

**NOTE**
        
The env file is still the env varaiables of the docker image ,it can be edited or  ovewrite through command line argument   by passing  -e with the argument along the  
        
docker command . Check here to  read more [here]  (https://docs.docker.com/engine/reference/commandline/run/)
        
While in the project root directory 

``` docker build -t daniel422/titanic-api:v1.0 .

    docker run daniel42233/titanic-api:v1.0 

```
Dont forget to specify the mongo details in .env file or as commad argument
        
Go to http://127.0.0.1:5000 to view the app
    

 ## Running Docker-compose 

**NOTE** Make sure the titanic.csv and mongodb.sh is in the  mongoseed folder. This is used to seed the mongodb image with titanic data.

while in the project Directory - Run 

```docker
  Docker Compose up -d  
```
        
The app should will be started. 
        
**Make**  sure All the cointainers is running, confirm with

docker-compose ps

Go to http://127.0.0.1:5000 to view the app


Kubernetes:

 You can install a minuikube cluster from [here](https://minikube.sigs.k8s.io/docs/start/) 


If you have an esiting cluster for the database , you wants to use. Configure it [here] (C:\Users\LENOVO\Dan-container-solution\k8s\app\02-config.yaml). Then move to second to the last step. 




**NOTE**
Create a .env file as shown in the env.example and update `hostname,port and db varaiable` in  config.yaml [here] (k8s/app/02-config.yaml) and here
    
Also , the username and password shoule also be updated in the secret.yaml [here] (Ck8s/Mongo/02-secret.yaml) 

Also, the  [path] (mongoseed)   to  should be changed [here] (C:\Users\LENOVO\Documents\Dan-container-solution\k8s\Mongo\08-mongoseed-deployment.yaml) 

A namespace will be created

- To create the mongodb in kubernetes:

run 

kubectl apply -f k8s/Mongo --recursive   # To create  namespace , secret,volume,pvc,svc , deployment for mongo

The service type uis Cluster Ip for the db so that it will not be exposed outside the cluster.

confirmn it's running by  runnning

   watch kubectl get deployment mongo-deployment

make sure all the pods have been started.

- To create the App pods:

 kubectl run  -f k8s/app --recursive                 # To create  namespace , secret,configmap,svc(load Balancer) , deployment for the api

confirmn it's running by  runnning

 watch kubectl get deployment titanic-deployment

make sure all the pods have been started.


- For linux users:

    You can use chmod +x `kubectl_deploy.sh`

```   
    bash ./kubectl_deploy.sh
```


Lastly run  

```
kubectl -n titanic get svc titanic-service 
```
Get EXTERNAL-IP for the titanic-api deployment and go to http://{EXTERNAL-IP}:8000 to view the app.


# API-exercise

This exercise is to assess your technical proficiency with Software Engineering, DevOps and Infrastructure tasks.
There is no need to do all the exercises, but try to get as much done as you can, so we can get a good feel of your skillset.  Don't be afraid to step outside your comfort-zone and try something new.

If you have any questions, feel free to reach out to us.

## Exercise

This exercise is split in several subtasks. We are curious to see where you feel most comfortable and where you struggle.

### 0. Fork this repository
All your changes should be made in a **private** fork of this repository. When you're done please, please:
* Share your fork with the **container-solutions-test** user (Settings -> Members -> Share with Member)
* Make sure that you grant this user the Reporter role, so that our reviewers can check out the code using Git.
* Reply to the email that asked you to do this API exercise, with a link to the repository that the **container-solutions-test** user now should have access to.

### 1. Setup & fill database
In the root of this project you'll find a csv-file with passenger data from the Titanic. Create a database and fill it with the given data. SQL or NoSQL is your choice.

### 2. Create an API
Create an HTTP-API (e.g. REST) that allows reading & writing (maybe even updating & deleting) data from your database.
Tech stack and language are your choice. The API we would like you to implement is described in [API.md](./API.md).
An OpenAPI specification is also provided (see [swagger.yml](./swagger.yml)). If you do not want to implement an API server from scratch, 
you can use something like [swagger-codegen](https://swagger.io/tools/swagger-codegen/) to generate server stubs for your solution.

### 3. Dockerize
Automate setup of your database & API with Docker, so it can be run everywhere comfortably with one or two commands.
The following build tools are acceptable:
 * docker
 * docker-compose
 * groovy
 * minikube (see 4.)

No elaborate makefiles please.

#### Hints

- [Docker Install](https://www.docker.com/get-started)

### 4. Deploy to Kubernetes
Enable your Docker containers to be deployed on a Kubernetes cluster.

#### Hints

- Don't have a Kubernetes cluster to test against?
  - [MiniKube](https://kubernetes.io/docs/setup/minikube/) (free, local)
  - [GKE](https://cloud.google.com/kubernetes-engine/) (more realistic deployment, may cost something)
- Remember that all scripts and code should be runnable either on Linux or MacOS

### 5. Whatever you can think of
Do you have more ideas to optimize your workflow or automate deployment? Feel free to go wild and dazzle us with your solutions.


