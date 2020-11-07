FROM python:3.7-alpine
ADD . /code
WORKDIR /code
COPY MainScores.py /
COPY Live.py /
COPY MainGame.py /
COPY GuessGame.py /
COPY MemoryGame.py /
COPY Score.py / 
COPY Utils.py /
COPY e2e.py /
COPY scores.txt /
RUN pip install dependencies
RUN pip install flask
CMD ["python", ./"MainScores.py"]
