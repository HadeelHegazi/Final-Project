FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY ./view.py /app/view.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["view.py" ]cta