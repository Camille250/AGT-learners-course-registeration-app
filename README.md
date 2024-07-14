# AGT-learners-course-registeration-app
WHAT ARE CONTAINERS
Containers are isolated environments that packages our application or software and its dependencises and libery to run smoothly on any host..
It compresses makes the application compact and light weight which is easily deployed.

How to Containerized a simple Python Flask Application
Flask is an amazing python framwork for building frontend app
For us to package the simple flask web page we need a dockerfile
Then an env that contains the colors

docker build -t simple-flask-app .
docker tag simple-flask-app <container-repo>/simple-flask-app
docker push <container-repo>/simple-flask-app

docker run -d -p 8000:8080 -e APP_COLOR=<color-name> <container-repo>/simple-flask-app