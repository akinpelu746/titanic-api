# Titanic End points

The endpoints was developed  using flask. 

Flask is a lightweight web application framework designed euipped only with web app development and  to get results fast.Its strength lies in its customizability and thus leave room to make the app more detailed in the future.To read more about [Flask] (https://flask.palletsprojects.com/en/2.0.x/).

The endpoint specification given can be found [here]

# Project Architecture




The project structure goes thus :

 - app - This contains the implemntation of the end points. It contains the Database  directory which contains the database model and the connection to the database. It also contains  the configuration model and the env file.

 - test: This contains testing of the app logic

 - K8s: for kubernetes

 - .sh files:  script for automating for linux user



 # Running the App Locally
    
    Perequsite : Ensure Python is installed, if not follow this [link] and mongodb 


    - Clone the repo

        git clone   

    - Install the dependecies
         While in the directory
            pip install -r requirements.txt
    
    -  Create a database and Collection 

    - Import titanic.csv using the cli or mongoimport


    
    - Create a `.env` and update needed variables for the  MongoDB server; check `.env.example`


    -   Run the api.py in the app directory

            Go to http://127.0.0.1:5000 to view the app

# Building the  using Image

You can install docker from [here](https://docs.docker.com/get-docker/)

 the flask app image:

 Make sure you create the ´env´ has discussed above. 



. While in the project root directory, run:
```
docker build -t titanic-api .

docker run -e MONGO_URI="{URL_TO_MONGODB_SERVER}" -p 8000:8000 titanic-api # You can switch the first 8000 to any port of choice or leave empty to let Docker randomly assign a port
```
Check the live API docs at http://0.0.0.0:8000/docs *# Swap 8000 for port used while executing `docker run`*

if you have docker install- run docker database which runs  and run
it pull the database , create user and filled it with the data 


Running Docker-compose 

 while in the project Directory - Run Docker Compose up .. The app should be started already. The directory.



Kubernetes:
Also if the env hostname,port and db is cahged in the .env , it should also be updated  in the  config .yaml

for username and password chaged it should be updated in the screte .yaml here

- You can install a minuikube cluster from [here](https://minikube.sigs.k8s.io/docs/start/) 

- To create the mongodb in kubernetes:

    run kubectl apply    -f k8s/Mongo --recursive 

    confirmn it's running by  runnning


- To create the App pods:

    Run  -f k8s/app --recursive

     confirmn it's running by  runnning


- For linux users:

You can use chmod +x kubectl_deploy.sh

bash ./kubectl_deploy.sh


kubectl apply -f ./k8s/manifests/ # Create a secret, deployment, and service (type is LoadBalancer)

kubectl get svc titanic-api # Get EXTERNAL-IP for the titanic-api deployment and go to http://{EXTERNAL-IP}:8000/docs to view live API docs

