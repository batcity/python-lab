# Multiprocessing in Python

Python’s Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecode simultaneously.  

This means:

- Threads can run concurrently,
- But CPU-bound programs do not gain real parallelism with threads.

To achieve true multi-core parallelism, Python provides the multiprocessing module.


## Why Multiprocessing Works

Each process has:

- its own memory space
- its own Python interpreter
- its own GIL

This allows multiple processes to run in parallel on different CPU cores.


## When to Use Multiprocessing

### Use multiprocessing for CPU-bound tasks
Examples:
- heavy mathematical computation
- image or video processing
- scientific simulations
- data transformations
- hashing and encryption

### Do not use multiprocessing for:
- I/O-bound workloads (network, disk, API calls)
- tasks with deep shared-memory needs
- very small or quick tasks (process startup overhead is high)

For I/O tasks, prefer threading or asyncio.


## Threading vs Multiprocessing

| Feature          | Threading | Multiprocessing          |
| --- |---  |---  |
| GIL              | Yes       | Each process has its own |
| Best for         | I/O-bound | CPU-bound                |
| Memory           | Shared    | Separate                 |
| Startup overhead | Low       | High                     |
| Communication    | Simple    | Requires IPC             |


## Summary

* Python threads cannot execute CPU-bound Python instructions in parallel because of the GIL.
* Multiprocessing launches independent processes that run truly in parallel on multiple cores.
* It is ideal for CPU-heavy programs.
* It requires awareness of memory separation, pickling, and process startup overhead.