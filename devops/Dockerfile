FROM python:3.8

COPY ./ .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8091"]
