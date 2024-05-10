FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt


COPY . .
RUN adduser ctf

RUN chmod 777 db.json
RUN chmod 555 app.py
RUN chmod 444 flag.txt


USER ctf

CMD ["python3", "-m", "gunicorn", "--bind", "0.0.0.0", "app:app", "--workers", "5"]

EXPOSE 8000