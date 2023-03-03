ARG IMAGE_VARIANT=slim-buster
ARG PYTHON_VERSION=3.9.8

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3

RUN pip --no-cache-dir install numpy
RUN pip --no-cache-dir install pandas
RUN pip --no-cache-dir install xgboost
RUN pip --no-cache-dir install scikit-learn
RUN pip --no-cache-dir install numpy
RUN pip --no-cache-dir install pandas
RUN pip --no-cache-dir install tqdm
RUN pip --no-cache-dir install requests

RUN mkdir -p /my_dir
COPY code /my_dir/
WORKDIR /my_dir

# ENTRYPOINT ["python"]
