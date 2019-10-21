FROM python:3-alpine
WORKDIR /movies.py
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "movies.py" ]

EXPOSE 5000
