FROM python:3.11
MAINTAINER Egor Bogdanov <>
WORKDIR /app/

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.0.3 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# add ssh keys for copying private repo
COPY ssh /root/.ssh
RUN touch /root/.ssh/known_hosts
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
RUN ssh-keyscan -H github.com >> ~/.ssh/known_hosts
RUN chmod -R 600 /root/.ssh/

COPY pyproject.toml /app/
COPY poetry.lock /app/
COPY wshub /app/wshub/
COPY run.py /app/

RUN pip install poetry
RUN poetry lock
RUN poetry install

RUN rm -r /root/.ssh/

CMD ["poetry", "run", "python", "run.py"]