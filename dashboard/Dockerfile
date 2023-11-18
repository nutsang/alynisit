FROM python:3.9 AS builder

WORKDIR /dashboard

COPY ./requirements.txt /dashboard/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /dashboard

CMD dbus-uuidgen --ensure && streamlit run main.py
