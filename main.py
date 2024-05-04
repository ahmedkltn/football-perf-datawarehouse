import argparse
from .services import etl_process

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filepath", "-task")
    args = parser.parse_args()
    if args.task == 'csvtodb':
        etl_process()


if __name__ == "__main__":
    main()