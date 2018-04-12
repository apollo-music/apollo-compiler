FROM ubuntu:rolling
MAINTAINER grupo-9

# Install python3-pip and project requirements
RUN apt-get update -qqy && \
    apt-get install --no-install-recommends -y \
                        build-essential \
                        cmake \
                        git \
                        pkg-config \
                        \
                        # To install python requirements
                        python3-pip \
                        libssl-dev \
                        libffi-dev \
                        python-dev \
                        python3-setuptools \
                        python-setuptools \
                        \
                        # For generating mp3 files
                        fluidsynth \
                       &&\
    \
    # Clean the cache to keep the image small
    apt-get autoclean autoremove &&\
        rm -rf /var/lib/apt/lists/* \
               /tmp/* \
               /var/tmp/*

# Change working dirs
WORKDIR /build

# Define default command.
CMD ["bash"]
