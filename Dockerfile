FROM python:3.11
LABEL authors="SzymKam"
ENV PYTOHNBUFFERED=1
WORKDIR src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /src/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
