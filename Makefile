PROCESSES=4
THREADS=4

env:
	python3 -mvenv env
	env/bin/pip install --upgrade pip setuptools
	env/bin/pip install "django<3" channels uvicorn[standard] gunicorn requests

asgi:
	cd uvitest && \
	DJANGO_SETTINGS_MODULE=uvitest.settings \
	../env/bin/gunicorn uvitest.asgi:application \
	--worker-class uvicorn.workers.UvicornWorker \
	--workers $(PROCESSES) \
	--access-logfile - \

asgi-threads:
	cd uvitest && \
	ASGI_THREADS=$(THREADS) \
	DJANGO_SETTINGS_MODULE=uvitest.settings \
	../env/bin/gunicorn uvitest.asgi:application \
	--access-logfile - \
	--worker-class uvicorn.workers.UvicornWorker \
	--workers $(PROCESSES) \


wsgi:
	cd uvitest && \
	DJANGO_SETTINGS_MODULE=uvitest.settings \
	../env/bin/gunicorn uvitest.wsgi:application \
	--access-logfile - \
	--workers $(PROCESSES) \
	--threads $(THREADS) \

wsgi-fair:
	cd uvitest && \
	DJANGO_SETTINGS_MODULE=uvitest.settings \
	../env/bin/gunicorn uvitest.wsgi:application \
	--access-logfile - \
	--workers $(PROCESSES) \
	--threads $(THREADS) \
	--worker-connections $(THREADS) \
