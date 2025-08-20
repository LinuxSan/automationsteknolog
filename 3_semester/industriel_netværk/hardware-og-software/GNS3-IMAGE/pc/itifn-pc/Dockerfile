FROM alpine:3.20
LABEL maintainer="Anders Sandø Østergaard <aso@aams.dk>"
RUN apk add --no-cache bash iproute2 iputils busybox-extras ethtool \
    dhclient bind-tools curl netcat-openbsd mtr tcpdump \
    openssh-client ca-certificates tini
COPY entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
ENTRYPOINT ["/sbin/tini","--","/bin/entrypoint.sh"]
CMD ["bash"]
