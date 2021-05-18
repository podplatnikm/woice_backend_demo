FROM python:3.8

# Outputs is sent straight to terminal without being first buffered
ENV PYTHONUNBUFFERED=1

# Prevents Python from writing out pyc file
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR code

# Allows docker to cache installed dependencies between builds
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile /code/
COPY Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . code

EXPOSE 8016