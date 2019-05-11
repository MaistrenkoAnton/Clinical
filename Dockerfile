FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /clinicaltrials
WORKDIR /clinicaltrials
ADD requirements.txt /clinicaltrials/
RUN pip install --default-timeout=100 -r requirements.txt
ADD . /clinicaltrials/
RUN chmod +x /clinicaltrials/docker/start.sh

CMD ["/clinicaltrials/docker/start.sh"]
