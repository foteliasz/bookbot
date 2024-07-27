FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Reference: https://go.dev/wiki/GOPATH
ENV GOPATH=/opt/go/

# Installing go 1.22.5 according to instructions from: https://go.dev/doc/install
RUN wget https://go.dev/dl/go1.22.5.linux-amd64.tar.gz  && \
    #
    # Remove any previous Go installation by deleting the /usr/local/go folder
    rm -rf /usr/local/go && \
    #
    # Extracting downloaded archive to /usr/local/go
    tar -C /usr/local -xzf go1.22.5.linux-amd64.tar.gz

# Adding go to PATH
ENV PATH=/usr/local/go/bin:$PATH
ENV PATH=$GOPATH/bin:$PATH

# Installing Bootdev CLI.
# Reference: https://github.com/bootdotdev/bootdev?tab=readme-ov-file#installation
RUN go install github.com/bootdotdev/bootdev@latest 

WORKDIR /workspaces/bookbot
