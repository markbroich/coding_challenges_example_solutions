FROM python:3.7-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

# RUN pip install dagster dagit pandas geopandas numpy Rtree great-circle-calculator
RUN pip install dagster dagit pandas geopandas numpy Rtree fuzzywuzzy python-Levenshtein great-circle-calculator keplergl

# Copy your code and workspace to /opt/dagster/app
# COPY hello-dagster.py /opt/dagster/app/
COPY code.py /opt/dagster/app/

ENV DAGSTER_HOME=/output

WORKDIR /opt/dagster/app

# ENTRYPOINT ["dagster", "job", "execute", "-f", "hello-dagster.py"]
ENTRYPOINT ["dagster", "job", "execute", "-f", "code.py"]


