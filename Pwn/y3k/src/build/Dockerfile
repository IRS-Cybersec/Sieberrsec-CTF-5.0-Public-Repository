FROM pwn.red/jail

COPY --from=ubuntu:22.04@sha256:77906da86b60585ce12215807090eb327e7386c8fafb5402369e421f44eff17e / /srv

COPY ./flag.txt /srv/app/flag.txt
COPY ./chall /srv/app/run

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run
