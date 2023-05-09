# FROM nvidia/cuda:11.7.0-base-ubuntu22.04
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    sudo wget vim cmake \
    coreutils \
    grep \
    iproute2 \
    iputils-ping \
    traceroute \
    tcpdump \
    bind9-dnsutils \
    dnsmasq-base \
    netcat-openbsd \
    iptables \
    procps \
    isc-dhcp-client \
    git \
    curl \
    ca-certificates \
    tzdata \
    libopencv-dev \
    opencv-data \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg \
    python3.9 \
    python3 python3-pip \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    build-essential \
    python3-dev \
    python3-setuptools

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
