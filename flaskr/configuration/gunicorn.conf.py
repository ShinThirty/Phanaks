import multiprocessing

# Configurations for gunicorn

# Address and port where gunicorn will listen on
bind = "127.0.0.1:8080"

# Number of worker processes that gunicorn will spawn
workers = multiprocessing.cpu_count() * 2 + 1
