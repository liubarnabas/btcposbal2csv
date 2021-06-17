FROM ubuntu
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
RUN apt-get update && apt-get install -y software-properties-common curl build-essential libleveldb-dev && add-apt-repository universe
RUN apt-get update && apt-get install -y python2 python-dev
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output /get-pip.py
RUN python2 /get-pip.py
RUN pip2 install plyvel base58

CMD ["python2", "/data/btcposbal2csv.py", "/chainstate", "/data/btcbal.csv"
