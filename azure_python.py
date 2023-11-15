from sys import stdin

from requests import get
from yaml import safe_load

def main():
    print("Azure Python")
    conf = safe_load(stdin)
    uri = conf["uri"]
    response = get(uri)
    print(response)
    print(USAGE)

USAGE = """usage: python azure_python.py
where
  - "python" is the Python runtime
"""

if __name__ == "__main__":
    main()
