FROM python:3.10

WORKDIR /app

COPY ./ /app

RUN pip3 install -r req.txt --no-cache-dir

CMD ["gunicorn", "call_center.wsgi:application", "--bind", "0:8000" ]