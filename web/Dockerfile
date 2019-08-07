FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Heroku should ignore this and use the "run" config in the heroku.yml file
CMD ["flask", "run", "--host=0.0.0.0"]
