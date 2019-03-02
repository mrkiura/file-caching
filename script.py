import argparse
from file_cacher import FileCacher

file_cacher = FileCacher()

def store(name, infile):
    if file_cacher.store(name, infile):
        print(f'{infile} successfully saved to cache')
    else:
        print(f'There was an error storing {infile}')

def retrieve(name, outfile):
    if file_cacher.retrieve(name, outfile):
        print(f'{name} successfully retrieved from cache and can be accessed at {outfile}')
    else:
        print(f'{name} could not be retrieved')

def main():
    """ Process Command Line Arguments """
    parser = argparse.ArgumentParser(description='Store and retrieve files in Memcached')
    parser.add_argument('action', help='Action to process (store, retrieve)')
    parser.add_argument('name', help='Name of the file')
    parser.add_argument('file', help='File for processing')

    args = parser.parse_args()
    if args.action == 'store':
        store(args.name, args.file)
    elif args.action == 'retrieve':
        retrieve(args.name, args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()