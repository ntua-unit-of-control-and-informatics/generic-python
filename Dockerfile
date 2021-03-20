FROM python:3.7

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn
RUN pip install numpy
RUN pip install scikit-learn==0.21.1
RUN pip install pandas

EXPOSE 8002

ADD source /generic-python/source
ADD application.py /generic-python/application.py

CMD ["uvicorn", "application.py", "--host", "0.0.0.0", "--port", "8002"]