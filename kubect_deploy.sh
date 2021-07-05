#!bin/bash

set -ex 


kubectl apply -f k8s/01-titanic-ns.yaml

kubectl apply  -f k8s/app --recursive  -f k8s/Mongo --recursive


sleep 30

kubectl -n titanic wait --for=condition=ready --timeout=300s pod -l app=mongo-pod
kubectl -n titanic wait --for=condition=ready --timeout=300s  pod -l app=titanic-api
