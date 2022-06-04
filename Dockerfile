FROM python:3.10-bullseye

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /src
COPY . /src

WORKDIR /src

EXPOSE 8000
ENV STORAGE_HOST=host.docker.internal

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]