# A base stage that installs all of the base dependencies
FROM python:alpine AS base
WORKDIR /usr/local/app
COPY app/requirements.txt .
RUN pip install -r requirements.txt


# A stage used for local development
FROM base AS dev

# Install watchdog to support file watching and automatic restarts
RUN pip install watchdog
ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]



# A stage used for deployment
FROM base AS prod
COPY src .
CMD ["flask", "run", "--host=0.0.0.0"]
