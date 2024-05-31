# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder
# FROM disconnect3d/nsjail

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

# #https://medium.com/techloop/ctf-challenges-dockerizing-and-repository-structure-bd3aed9314de
# RUN chmod -R 755 .

#./nsjail -Ml --port 9000 --chroot /chroot/ --user 99999 --group 99999 -- /bin/sh -i
# nsjail -Ml --port 9002 --disable_proc --chroot /jail -- /bin/bash
COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

EXPOSE 8080