FROM ubuntu:rolling
MAINTAINER grupo-9

# Change working dirs
WORKDIR /build

# Install python3-pip and project requirements
RUN apt-get update -qqy && \
    apt-get install --no-install-recommends -y \
                        build-essential \
                        cmake \
                        git \
                        pkg-config \
                        \
                        # To install python requirements
                        python-pip \
                        python3-pip \
                        libssl-dev \
                        libffi-dev \
                        python-dev \
                        python3-setuptools \
                        python-setuptools \
                        \
                        # For generating mp3 files
                        fluidsynth \
                        freepats \
                        timidity \
                        timidity-interfaces-extra \
                        lame \
                       &&\
    \
    # Clean the cache to keep the image small
    apt-get autoclean autoremove &&\
        rm -rf /var/lib/apt/lists/* \
               /tmp/* \
               /var/tmp/*

RUN git clone https://github.com/vishnubob/python-midi && \
    cd python-midi && \
    python2 setup.py install

RUN pip3 install pydot ply coverage

# Define default command.
CMD ["bash"]
