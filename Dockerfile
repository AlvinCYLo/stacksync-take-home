FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    pkg-config \
    git \
    bison \
    flex \
    libc6-dev \
    libprotobuf-dev \
    protobuf-compiler \
    libnl-3-dev \
    libnl-route-3-dev \
    libprotobuf-c-dev \
    protobuf-c-compiler \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/google/nsjail.git /nsjail

WORKDIR /nsjail
RUN make
RUN mv nsjail /usr/local/bin/

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY /app .
EXPOSE 8080
CMD ["python", "app.py"]
