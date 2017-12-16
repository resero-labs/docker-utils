FROM python:3.6.3

WORKDIR /workdir
ADD requirements.txt /workdir/requirements.txt
RUN pip install -r requirements.txt

# any customization of the image goes here

# pip install of the project is deferred to a differnt image that uses this image as it's base