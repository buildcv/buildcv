FROM python:3.9-bullseye 
WORKDIR /code
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && apt-get install -y gcc curl gnupg build-essential
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -y && ACCEPT_EULA=Y apt-get install -y msodbcsql18

RUN apt-get update -y && ACCEPT_EULA=Y apt-get install -y mssql-tools18

RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

RUN apt-get install -y unixodbc-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app0

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


