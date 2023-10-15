FROM python:3.10.9

SHELL ["/bin/bash", "-c"]

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV PIP_ROOT_USER_ACTION=ignore

RUN pip install --upgrade pip --default-timeout=100 future

RUN apt update && apt -qy install gcc python3-dev libpq-dev netcat openssh-client flake8\
    && pip install psycopg2 \
    && pip install pillow \
    && pip install gunicorn

RUN useradd -rms /bin/bash userapp && chmod 777 /opt /run

WORKDIR /app

RUN mkdir /app/static && mkdir /app/media && chown -R userapp:userapp /app && chmod 755 /app

COPY --chown=userapp:userapp . .

RUN pip install -r requirements.txt

USER userapp

CMD ["gunicorn","-b","0.0.0.0:8001","app.wsgi:application"]
