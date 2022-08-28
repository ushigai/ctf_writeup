FROM python:3.9.6

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y \
    socat

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org

COPY . .

CMD ["python", "solve.py"]

