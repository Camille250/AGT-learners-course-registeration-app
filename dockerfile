FROM python:alpine3.20
WORKDIR /app
COPY . /app
RUN pip install --no cache-dir -r-requirements.txt
EXPOSE 5000
CMD ["python" "./main.py"]
