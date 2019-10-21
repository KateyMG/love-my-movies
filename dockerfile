FROM python:3-alpine
WORKDIR /movie.py
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "movie.py" ]

EXPOSE 5000
