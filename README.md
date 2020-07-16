# StudentScorePrediction-ML-Project-with-Deployment

## This is an end to end project with deployment in Heroku.
This is a Flask web app which predicts score of student  based on hours  studied
Code is written in Python and the model is built using linear regression
The created model is exposed as a web API to be consumed by the client/client APIs,using the flask framework
We create a web app using Flask Framework.
Heroku is a Platform as a service (PAAS)
## Flow of Flask Framework :

Landing Page (Index.html)  ---> Python app (app.py) -----> Results page (results.html)

## Procfile : it contains the command to run the flask application once deployed on the server

  web: gunicorn app1:app
 web --> specifies its a web application
 app1: app   -----> program looks for a flask application called app inside the app1.py file.
 gunicorn is a web server gateway interface (WSGI)HTTP server  for python 
## pip freeze > requirements.txt. This command generates the ‘requirements.txt’ file
## Deployment to Heroku:

Create a app in heroku and use code from github to deploy.
After deployment, heroku gives you the URL to hit the web API. Once your application is deployed successfully, enter the command ‘heroku logs --tail’ to see the logs.

![heroku demo](https://github.com/Keerthana2701/StudentScorePrediction-ML-Project-with-Deployment/blob/master/heroku%20demo.PNG)



## Demo : 
https://studentscorepredictionapp.herokuapp.com/
![demoscore](https://github.com/Keerthana2701/StudentScorePrediction-ML-Project-with-Deployment/blob/master/demoscore.PNG)
