# random-python-app
Just a random app example in python. It creates a simple app, a sidecar fluentd logging into elastic

## Pre Requirements
- AWS Account
- Python Local
- Podman or Docker Desktop

## Create the cluster
eksctl create cluster \
  --name random-number-cluster \
  --region us-east-2 \
  --nodegroup-name random-number-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

## Criar um repositório
aws ecr create-repository --repository-name random-number-app --region us-east-1

## Get login password 
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-2.amazonaws.com

## Change account number
Change <account> on deployment.yaml

## Build your app
docker build -t random-number-app .

## Tag the app
docker tag random-number-app:v1 <account>.dkr.ecr.us-east-2.amazonaws.com/random-number-app:v1

## Push to ecr
docker push <account>.dkr.ecr.us-east-2.amazonaws.com/random-number-app:v1

## Deploy it
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

## Pod Checks
kubectl get svc random-guid-service \
kubectl get svc random-guid-service \
kubectl get pods -o custom-columns="POD:metadata.name,IMAGE:spec.containers[*].image"

## Create configmap
kubectl create configmap fluentd-config --from-file=fluent.conf

## Log Checks 
kubectl describe pod random-number-deployment-bcb4c974d-t9hzt \
kubectl logs elasticsearch-698648d5bb-x6h5s -c elasticsearch \
kubectl logs elasticsearch-698648d5bb-x6h5s -c fluentd \
curl -X GET "http://<elastic-ip>:9200/_cat/indices?v" \
http://<load-balance-ip>.us-east-2.elb.amazonaws.com:5601/ \
kubectl exec -it kibana-569b469d7f-hb84b -- curl http://elasticsearch:9200