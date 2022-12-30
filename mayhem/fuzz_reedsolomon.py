#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    from reedsolo import RSCodec, ReedSolomonError

rsc = RSCodec(10)

@atheris.instrument_func
def test_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    s = bytearray(fdp.ConsumeUnicodeNoSurrogates(4096), 'utf-8')

    encoded = rsc.encode(s)
    decoded = rsc.decode(encoded)[0]
    if not (s == decoded):
        print(f"orig: {s} \n decoded: {decoded}")
        raise Exception("encode/decode mismatch")

    return data

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
