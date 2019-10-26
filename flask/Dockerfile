FROM python:3.6
EXPOSE 80
#VOLUME ["code/","/code"]
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
#ADD code /app/
CMD ["python", "run.py"]
#CMD ["python", "app.py"]
