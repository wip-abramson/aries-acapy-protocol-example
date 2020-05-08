FROM bcgovimages/von-image:py36-1.14-1

USER root

ADD . .

RUN pip3 install --no-cache-dir -e .

RUN chmod +x ./startup.sh

USER $user

CMD ./startup.sh