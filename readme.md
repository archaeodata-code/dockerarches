dockerarches 0.0.1 
february 2022

This docker-compose.yml and related instructions can be used to set up a basic container running Arches for development / learning puposes. The Arches Dockerfile is put in a separate directory so that you can expand the apps in the docker-compose.yml (example, add another django based app) without having to rewrite the docker-compose.yml

The files here were developed both on Win 10 and Ubuntu 20.04 and presently are working on both.

Postgres/Postgis and Elasticsearch are pulled as self-contained images meant to run in their own containers.  Arches is installed in a third container.

The dockerfile for arches mimickes the full install documented in Arches installation guide (except here there is no venv established as arches will already be in a container)

Versions of software are:

Ubuntu: 20.04
Arches: whatever is offered via pip install arches (presently 6.01)
Nodejs: 12.22.5 with Yarn 1.22.17
Postgis: 12.3.2
Elasticsearch: 7.4 

Install docker and docker compose, or docker desktop.  For the latter, possibly useful links:
Mac OS:  https://www.cprime.com/resources/blog/docker-for-mac-with-homebrew-a-step-by-step-tutorial/
Ubuntu 21.04 or 21.10:  https://docs.docker.com/desktop/linux/

Issues encountered:

1) Time settings in the arches container.  I having issues with arches/postgis communication that appeared to be related to local time settings.  Hence in the docker-compose.yml and the Dockerfile for arches, you see specific items for managing local time for those two containers.  You will want to edit those to your particulars.

2) I do not have an appropriate technique in place to ensure Postgis is up before launching arches. There is an entrypoint script that I am presently not using but can be adapted. Instead I am using an entrypoint to keep the arches container running so that is accessible for the commands to build the arches project etc.

4) see start_arches for the steps to actually build the project, load a package and run the server.