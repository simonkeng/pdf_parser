FROM python:2.7-slim

WORKDIR /opt

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# COPY test_data.pdf /opt/test_data.pdf



CMD ["bash"]
