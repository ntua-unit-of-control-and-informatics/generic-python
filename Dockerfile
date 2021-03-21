FROM python:3.7

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn
RUN pip install numpy
RUN pip install scikit-learn==0.24.0
RUN pip install pandas

EXPOSE 8002

COPY ./source /app/source
COPY application.py /app/application.py

CMD ["python", "/app/application.py"]
# CMD ["uvicorn", "/app:app.py", "--host", "0.0.0.0", "--port", "8002"]