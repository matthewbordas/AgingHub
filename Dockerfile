FROM python:3.8
COPY . .
RUN pip install -r requirements.txt
# options: development, production
ENV FLASK_ENV=production
ENV HTTP_PORT=80
EXPOSE 80
CMD ["gunicorn", "-c", "gunicorn.conf.py", "--worker-tmp-dir", "/dev/shm", "aginghub:create_app()"]
