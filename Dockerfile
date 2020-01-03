FROM frankwolf/rpi-python3

RUN mkdir /app/

COPY . /app
WORKDIR /app

RUN pip install requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]