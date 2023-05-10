FROM nvidia/cuda:11.7.0-base-ubuntu22.04
# FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    bash \
    sudo wget vim cmake \
    grep \
    git \
    curl \
    python3.10 \
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
RUN pip3 install --no-cache-dir packaging
RUN pip3 install blinker --ignore-installed
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-dev-11-4 \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install flash-attn==1.0.3.post0
RUN pip3 install triton==2.0.0.dev20221202
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]
