FROM python:3.10

RUN apt-get update

RUN groupadd -r userapp && useradd -r -g userapp userapp

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

WORKDIR /home/userapp

RUN chown -R userapp:userapp /home/userapp

COPY src src

RUN chown -R userapp:userapp ./src

USER userapp

EXPOSE 8000

CMD [ "python", "-m", "src.main" ]