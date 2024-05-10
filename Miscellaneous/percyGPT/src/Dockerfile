FROM python:3

COPY . .

RUN useradd -ms /bin/bash ctf

COPY . /home/ctf

RUN chown ctf /home/ctf/*

WORKDIR /home/ctf

RUN pip3 install -r requirements.txt

USER ctf

EXPOSE 8000

CMD ["python3", "-m", "gunicorn", "--bind", "0.0.0.0", "app:app"]
