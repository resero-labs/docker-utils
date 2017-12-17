FROM rappdw/nvidia-python:p3.6.3-u16.04-c8.0-n6.0

ADD docker/tensorflow/requirements* /
ADD docker/tensorflow/setup-venv.py /

RUN /setup-venv.py \
    &&  pip install -r /requirements.txt \
    &&  /bin/bash -c "source /cpu-env; pip install -r requirements-cpu.txt" \
    &&  /bin/bash -c "source /gpu-env; pip install -r requirements-gpu.txt"

RUN rm /requirements* \
    && rm /setup-venv.py

ADD docker/tensorflow/.bashrc /root/.bashrc
