# A dockerized version of the tool C2Concealer by Chris Truncer

FROM kalilinux/kali-rolling
RUN apt-get update

RUN mkdir C2concealer
COPY ./ /C2concealer
WORKDIR /C2concealer
RUN ./install.sh
ENTRYPOINT [ "C2concealer" ]