# **Chandy-Misra-Haas Algorithm for the AND Model**

This Python program is a simulation of the Chandy-Misra-Haas algorithm for distributed deadlock detection in the AND model. It serves as an educational tool to understand the algorithm's implementation and how it detects deadlocks in a distributed system.

## Prerequisites
Python 3.6 or higher

## Usage
1. Navigate to the directory containing the chandy_misra_haas.py script.
2. Run the script using the command: 
`python chandy_misra_haas.py` or `python3 chandy_misra_haas.py`
3. Observe the output to see if a deadlock has been detected.


## Customization

You can modify the `process_connections` dictionary in the `main()` function of the `chandy_misra_haas.py` script to test different scenarios.

The keys of the dictionary represent process IDs, and the values are lists of dependent process IDs:

```python
process_connections = {
 0: [1, 2],
 1: [2],
 2: [0, 3],
 3: [4],
 4: [1]
}

```
## Limitations
This implementation is a simplified simulation of a distributed system and is not suitable for use in real distributed systems. It is designed for educational purposes to help understand the Chandy-Misra-Haas algorithm for the AND model.

## Algorithm Description

The Chandy-Misra-Haas algorithm is a distributed deadlock detection algorithm for the AND model. In the AND model, a process is considered deadlocked if it is waiting for all of its requested resources to be granted. In this algorithm, each process maintains a local wait-for graph and sends probe messages to its dependent processes. The algorithm detects a deadlock when a process receives a probe message with its own identifier.

The provided Python implementation defines a `Process` class that represents a process in a distributed system. Each process has a unique `id`, a list of `dependent_processes`, a local `wait_for_graph`, and a `message_queue`. The `run` method of the `Process` class listens for incoming messages and calls the `send_probe` method to send probe messages to dependent processes.

The `setup_processes` function initializes the processes with their dependencies, and the main function sets up the threads for each process and initiates the deadlock detection.


