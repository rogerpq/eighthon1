 FROM python:3.9-slim-buster

 WORKDIR /app

 COPY requirements.txt requirements.txt
 RUN pip3 install -r requirements.txt

 COPY app.py app.py 

 CMD ["python3", "eighthon.py"]
