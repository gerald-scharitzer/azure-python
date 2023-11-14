from yaml import safe_load
from sys import stdin

def main():
    print("Azure Python")
    conf = safe_load(stdin)
    print(conf["uri"])
    print(USAGE)

USAGE = """usage: python azure_python.py
where
  - "python" is the Python runtime
"""

if __name__ == "__main__":
    main()
