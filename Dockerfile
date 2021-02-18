FROM python:3.7-alpine
ADD . /code
WORKDIR /code
COPY *.py /
COPY scores.txt /
RUN pip install dependencies
RUN pip install flask
RUN pip install docker-compose
CMD ["python3", "MainScores.py"]
