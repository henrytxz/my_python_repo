FROM debian

# use \ && to create fewer layers
# running update separately from package install might fail.
# noninteractive and install with -y is necessary for scripted installs.
# cleaning up at the end minimizes layer and image size
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
 && apt-get install -y \
    git \
    openssh-client \
    sudo \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# image size: 268.7 MB