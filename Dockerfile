FROM resin/rpi-raspbian:jessie

# Install Python 3
RUN apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    --no-install-recommends

RUN pip3 install --upgrade pip

CMD ['bash']