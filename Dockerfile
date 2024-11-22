# Use the official Python 3.12 image as a base
FROM python:3.12

# Set the working directory in the container
WORKDIR /usr/src

# Copy the Poetry configuration files from your src directory
COPY src/pyproject.toml src/poetry.lock ./

COPY src/pytest.ini ./
COPY src/.test.env ./

# Install Poetry, dependencies then clean up
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && pip install poetry && poetry config virtualenvs.create false \
    && poetry install --with test \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Copy your application folder into the container
COPY src/app/ ./app
COPY src/data/ ./data

CMD ["poetry", "run", "pytest"]