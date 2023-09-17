FROM python:3.11
LABEL authors="SzymKam"
ENV PYTOHNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
