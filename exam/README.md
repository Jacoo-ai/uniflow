# Backend Interview README

## Dockerize the Application

### 1. Preparation
Make sure Docker is installed. If not, please install Docker https://docs.docker.com/desktop/ according to the operating system.

### 2. Build and Run a Docker Container

#### (1) Export all the dependencies
Run `pip freeze > requirements.txt`, which will include all the dependencies needed in `requirements.txt`.

#### (2) Create a `Dockerfile` under the project's root dictionary.
```
# Base image
FROM python:3.9

# Work dictionary in the image
WORKDIR ./docker_demo

# Copy the current dictionary to the image
COPY . .

# Install all the dependencies
RUN pip install -r requirements.txt

# Run the python file
CMD ["python", "./tests/demo_test.py"]
```

#### (3) Build a Docker image
Run `docker build -t uniflow-docker-demo .`  
  
It will build a Docker image named "uniflow-docker-demo".


#### (4) Run the Docker image
Run `docker run uniflow-docker-demo`.
  
It will start a container to execute the Python application in the `demo_test.py` file.

## API Usage Guide

### 1. Preparation
Run `/api/async.py`  
In this case, the endpoint of this API is `/async-expand-reduce `.
### 2. Request
Vist url with the following format: http://localhost:8080/async-expand-reduce?input_dict=` string format of input dictionary`
  
For example:
  http://localhost:8080/async-expand-reduce?input_dict=1:2,3:4,5:6,7:8   means that the input dictionary is {"1": "2", "3": "4", "5": "6", "7": "8"}

### 3. Response
You will get a response in the following format:
  
    {
    "status": "success",
    "message": "Async executed",
    "job_id": "6a23e39a-73f3-4e85-828a-c3986a4a1665",
    "result": [
        {
            "1 5": "2 6",
            "3 7": "4 8"
        }
    ]
    }