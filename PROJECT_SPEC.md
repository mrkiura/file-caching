## Project Details

Please consider this document as a set of requirements, and deliver the code necessary to fulfill these requirements. If a requirement seems ambiguous, state your understanding of the requirements in a readme or inline comments along with your solution.

## Scenario

Your mission is to write a Python library that will accept a large file (50MB) as an input and store it in Memcache. Once stored, the library will then be used to retrieve the file from Memcache and return it.

---

You might be asking "what's the catch?" 

Well, using the default slab size, Memcached can only store up to 1MB per key. That means you'll have to implement some means of chunking the file to store it in Memcached.

Further, Memcached can evict keys when it runs out of memory. A complete solution should detect these cases and handle them appropriately.

## Deliverables

There are three deliverables for this project:

1. A small library to store and retrieve large files in Memcached
2. At set of unit tests to validate the store and retrieve functionality
3. A command line utility (example below) to store and retrieve the files using your library

## Specs

### Library:

* Your library should be small and self contained.
* Your library should use `pymemcache` or similar memcached client, along with the Python standard library, and any other resources.
* Your library should accept any file size from 0 to 50MB. Files larger than 50MB should be rejected.
* Your library should accept a file, chunk it, and store as bytes in Memcached with a minimum amount of overhead. 
* Your library should retrieve a file's chunks from Memcached and return a single stream of bytes. 
* Your library may chunk the file in any way appropriate.
* Your library can key the chunks in any way appropriate.
* Your library should check for file consistency to ensure the data retrieved is the same as the original data stored.
* Your library should handle edge cases appropriately by raising an Exception or similar. Some examples of edge cases may include: trying to store a file that already exists, trying to retrieve a file that does not exist, or when a file retrieved is inconsistent/corrupt. 
* Your library should have at least two tests.

**NOTE:** you can use this command to generate a 50MB file of random data if needed:

```bash
dd if=/dev/urandom of=bigoldfile.dat bs=1048576 count=50
```

Example Store:
`python script.py store bigfile bigoldfile.dat`

Example Retrieve:
`python script.py retrieve bigfile newbigoldfile.dat`
