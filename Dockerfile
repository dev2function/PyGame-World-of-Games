FROM python:3.8.18-alpine
ADD . /code
WORKDIR /code
COPY *.py /
COPY scores.txt /
RUN pip install dependencies
RUN pip install flask
CMD ["python3", "MainScores.py"]
