FROM python:3.8
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000

# Run the production server
# Gunicorn relies on the operating system to provide all of the load balancing when handling requests.
# Generally we recommend (2 x $num_cores) + 1 as the number of workers to start off
# Type of worker_class (-k) set to eventlet
CMD newrelic-admin run-program gunicorn --workers=5 -k eventlet --bind 0.0.0.0:$PORT --access-logfile - api.wsgi:application
