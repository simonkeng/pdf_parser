FROM python:2.7-slim

WORKDIR /tmp

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --assume-yes apt-utils

RUN \
    apt-get -y install git-core && \
    git clone --recursive https://github.com/bambocher/pocketsphinx-python

COPY ad_openal.c /tmp/pocketsphinx-python/deps/sphinxbase/src/libsphinxad/ad_openal.c

RUN apt-get -y install swig3.0 
RUN ln -s /usr/bin/swig3.0 /usr/bin/swig
    
RUN \    
    apt-get -y install libevent-dev && \
    apt-get -y install python-dev && \
    apt-get -y install libpulse-dev && \
    apt-get -y install libjack-dev && \
    apt-get -y install libasound-dev && \
    apt-get -y install libxml2-dev && \
    apt-get -y install libxslt1-dev && \
    apt-get -y install antiword && \
    apt-get -y install unrtf && \
    apt-get -y install poppler-utils && \
    apt-get -y install pstotext && \
    apt-get -y install tesseract-ocr && \
    apt-get -y install flac && \
    apt-get -y install ffmpeg && \
    apt-get -y install lame && \
    apt-get -y install libmad0 && \
    apt-get -y install libsox-fmt-mp3 && \
    apt-get -y install sox && \
    apt-get -y install libjpeg-dev && \
    apt-get -y install gcc

RUN cd pocketsphinx-python/ && python setup.py install

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY test_data.pdf /tmp/test_data.pdf
COPY pdf_rip.py /tmp/pdf_rip.py

# Usage: 
# COPY document.pdf /tmp/document.pdf
# CMD ["python", "pdf_rip.py", "document.pdf"]

