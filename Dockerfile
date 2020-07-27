FROM python:3.7

RUN mkdir -p /radix-tree/

WORKDIR /radix-tree/

COPY . /radix-tree/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN gunicorn pythonpath=./ --bind 0.0.0.0:5000 wsgi:app