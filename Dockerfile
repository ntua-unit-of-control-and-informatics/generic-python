FROM python:3
MAINTAINER Pantelis Karatzas <pantelispanka@gmail.com>

RUN pip install --upgrade pip
RUN pip install tornado==4.5.3
RUN pip install numpy
RUN pip install sklearn
RUN pip install pandas
RUN pip install xgboost

# Expose the ports we're interested in
EXPOSE 8002


ADD source /generic-python/source
ADD application.py /generic-python/application.py



CMD ["python","/generic-python/application.py"]
