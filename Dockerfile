FROM debian:stable-slim

# Update repos and install dependencies
RUN apt-get -y update \
  && apt-get -y install pandoc fonts-roboto fonts-jetbrains-mono

# Copy fonts in required directory
RUN cp \
  /usr/share/fonts/truetype/jetbrains-mono/* /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/* \
  /usr/share/fonts/

WORKDIR /data
