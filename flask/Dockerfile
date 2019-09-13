FROM python:3.6
EXPOSE 80
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD code /app/
CMD ["python", "run.py"]
#CMD ["python", "app.py"]
