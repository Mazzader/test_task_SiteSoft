FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /habr_scraper
COPY requirements.txt /habr_scraper/
RUN pip install -r requirements.txt
COPY . /habr_scraper/

