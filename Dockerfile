FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install numpy
RUN pip install sklearn==0.22.0
RUN pip install pandas

EXPOSE 8002

ADD source /generic-python/source
ADD application.py /generic-python/application.py

CMD ["uvicorn", "application.py", "--host", "0.0.0.0", "--port", "8002"]