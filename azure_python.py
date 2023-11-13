from sys import stdin

def main():
    print("Azure Python")
    line = stdin.readline(256) # TODO hardcoded
    print(line)
    print(USAGE)

USAGE = """Usage: python azure_python.py
where
  - "python" is the Python runtime
"""

if __name__ == "__main__":
    main()
