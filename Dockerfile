FROM python:3.9

WORKDIR ./docker_demo

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./tests/demo_test.py"]