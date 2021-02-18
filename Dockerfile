FROM nikolaik/python-nodejs:python3.8-nodejs14
COPY . .
RUN pip install -r requirements.txt
RUN npm install
RUN npm run build-prod
# options: development, production
ENV FLASK_ENV=production
ENV HTTP_PORT=80
EXPOSE 80
CMD ["gunicorn", "-c", "gunicorn.conf.py", "--worker-tmp-dir", "/dev/shm", "aginghub:create_app()"]
