FROM kalilinux/kali-rolling
RUN apt-get update

RUN mkdir C2concealer
COPY ./ /C2concealer
WORKDIR /C2concealer
RUN ./install.sh
ENTRYPOINT [ "/C2concealer/.venv/bin/C2concealer" ] 