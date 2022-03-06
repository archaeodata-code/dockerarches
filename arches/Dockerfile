#ubuntu client build
# build from Ubuntu LTS
FROM ubuntu:20.04

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# get updated packages
RUN apt update
RUN apt -y upgrade

# install curl
RUN apt update && apt -y install curl

# set timezone
RUN ln -snf /usr/share/zoneinfo/$(curl https://ipapi.co/timezone) /etc/localtime

# Install system packages required by Arches-Django
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev

# install GDAL
RUN apt install -y gdal-bin

RUN apt update -y && apt -y install \
    libproj-dev \
    libjson-c-dev \
    xsltproc \
    docbook-xsl \
    docbook-mathml \
    libgdal-dev \
    libpq-dev

# install apt repository
RUN apt -y install software-properties-common 
RUN apt -y install dirmngr 
RUN apt -y install apt-transport-https 
RUN apt -y install lsb-release 
RUN apt -y install ca-certificates

# Install yarn and node.  In theory this could be in requirements.txt but I had problems with that
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt update
RUN apt -y install yarn
#RUN apt -y install netcat

# add pip
RUN apt -y install python3-pip
RUN python3 -m pip install --upgrade pip

# add arches
RUN pip install arches

# add nano for editing
RUN apt -y install nano

# copy in local settings
COPY ./arches/settings_local.py /settings_local.py
RUN sed -i 's/\r$//g' /settings_local.py

# copy in a pkg zip
COPY ./arches/pkg /pkg


ENTRYPOINT ["tail", "-f", "/dev/null"]
