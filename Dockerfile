FROM python:latest

WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "main:app", "--reload"]
