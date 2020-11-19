This repository is a sample Django project to help test some issues with channels/uvicorn/gunicorn. It has a single view configured at `/delay/<ms>/` which will time.sleep for `ms` and return 200.

`load_test.py` takes two arguments, `concurrency` and `requests`. It will hit the `/delay/` endpoint with a sequence of request with random delays between 0 and 1 second. The random generator is seeded with 0 before each run, so subsequent runs test the same thing. It prints some statistics on the request results.


# Install dependencies

Install the required dependencies with:

```
python3 -mvenv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install "django<3" channels uvicorn gunicorn requests
```

# Test scenarios

## 1. Channels returns 500s when workers > 1

Start the server:

```
DJANGO_SETTINGS_MODULE=uvitest.settings ../env/bin/gunicorn uvitest.asgi:application --worker-class uvicorn.workers.UvicornWorker --workers 4 --access-logfile -
```

Hit the server with 100 requests and concurrency 20:

```
env/bin/python load_test.py 20 100
```

