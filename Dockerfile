FROM python:3.6-slim
MAINTAINER danielabrgel91@gmail.com
COPY . /devalore-test
WORKDIR /devalore-test
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "main.py"]
CMD tail -f /dev/null