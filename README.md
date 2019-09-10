# AcronymDB
## Database for storing acronyms

The subdirectory /docker-compose/ is the backbone of all the development for the Acronym DB project.
It is comprised of many different pieces that are brought together in the docker-compose.yml file.
It includes subdirectories with information about the various sub systems that are individually dockerized.

## The docker containers include:
   * php - a container containing the CGI for apache
   * apache - a container containing the apache web server (external port 8080)
   * db - a container containing the mysql instance (external port 3306)
   * adminer - a container containing the admin script to manage MySQL (external port 8081)
   * flask - a container containing the webservice flask (external port 5000)

## Networking
   The system also uses named networks to segment traffic between the pieces
   networks:
   * backend - used by php, apache, db, adminer, flask
   * frontend - used by apache, flask

## Persisted Volumes
The database has a persisted volume called **mysql-data** that holds the persisted database files

## Command to start the containers
To start everything you can issue the following docker compose command:
   * 'docker-compose up --build'
   * setup the database (you may have to run the SQL file in /docker-compose/schema)

## FOR THE FUTURE
   should have: 
   * a persisted volume for the public_html for the web server 
   * a persisted volume for the flask web services (everything under /code directory in the /flask sub directory)
   * perhaps move all of this code under /docker-compose up to the main level
