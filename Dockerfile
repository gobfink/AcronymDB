FROM mysql

# Copy the database schema to the /data directory
COPY files/epcis_schema.sql /data/epcis_schema.sql

# Change the working directory
WORKDIR data

CMD mysql -u $MYSQL_USER -p $MYSQL_PASSWORD $MYSQL_DATABASE < epcis_schema.sql
