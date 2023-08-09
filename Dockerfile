FROM python:3.11

WORKDIR /app

# RUN pip install MLB-StatsAPI
 COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "test.py"]
