FROM python:3.11.4-slim-buster
RUN apt update -y && apt install awscli -y
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 5000
#CMD [ "python3","app.py" ]
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0" ]
#CMD ["python3","main.py","--host=0.0.0.0"]

