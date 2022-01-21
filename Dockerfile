FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install python-dotenv
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP="app-istio"
ENV FLASK_ENV="development"
CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080"]