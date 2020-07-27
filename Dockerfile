FROM python:3.7

RUN mkdir -p /radix-tree/

WORKDIR /radix-tree/

COPY . /radix-tree/
RUN chmod 600 gunicorn_starter.sh
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8003", "wsgi:app"]
#ENTRYPOINT ["./gunicorn_starter.sh"]
