# Async / Await and Coroutines

Coroutines are a specific type of function (aka subroutine) that allows for running non-blocking code, this allows a single CPU thread to make progress on other tasks while waiting for I/O operations (such as downloading files or reading from databases) to complete.

Before Python 3.5, asynchronous programming in Python relied on generators and external libraries, lacking native language-level syntax.

Python 3.5 introduced native support for coroutines (via PEP 492), bringing in dedicated syntax and semantics to make writing non-blocking code much cleaner and more intuitive.

* **The `async` keyword** denotes that a given function is a coroutine.
* **The `await` keyword** suspends the execution of the coroutine, handing control back to the event loop until the awaited task is complete.

    > ⚠️ **Note:** The `await` keyword can only be used inside an `async` function.

## References:

Introduced in this proposal: https://peps.python.org/pep-0492/