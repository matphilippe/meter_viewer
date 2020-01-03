FROM maidbot/resin-raspberrypi3-qemu
RUN [ "cross-build-start" ]

#switch on systemd init system in container
ENV INITSYSTEM off

RUN apt-get update && apt-get install -y \
        python-pip \
	&& rm -rf /var/lib/apt/lists/*

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
ENV READTHEDOCS True
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN [ "cross-build-end" ]

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 5000

CMD ["bash","flask", "run", "--host=0.0.0.0", "--port=5000"]