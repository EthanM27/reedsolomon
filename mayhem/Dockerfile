FROM fuzzers/atheris:2.0.7-python3.9

RUN pip install reedsolo
COPY . /src
WORKDIR /src
RUN chmod +x /src/mayhem/fuzz_reedsolomon.py
CMD ["/src/mayhem/fuzz_reedsolomon.py"]
