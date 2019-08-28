FROM alpine

MAINTAINER J4BB3R

WORKDIR /to

RUN apk add gcc \
            g++ \
            make \
            cmake tree

RUN cmake --version

COPY . /to/

RUN cmake .
RUN make -j8

CMD ["/to/traffic-orchestrator"]