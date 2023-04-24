import threading
import queue

class Process:
    def __init__(self, id, dependent_processes):
        self.id = id
        self.dependent_processes = dependent_processes
        self.local_wait_for_graph = set()
        self.message_queue = queue.Queue()
        self.deadlocked = False

    def send_probe(self, initiator_id, process_id):
        if process_id == initiator_id:
            self.deadlocked = True
            print(f"Deadlock detected: Process {self.id}")
        else:
            self.local_wait_for_graph.add(process_id)
            for dependent_process in self.dependent_processes:
                dependent_process.message_queue.put((initiator_id, self.id))

    def run(self):
        while not self.deadlocked:
            initiator_id, process_id = self.message_queue.get()
            self.send_probe(initiator_id, process_id)

def setup_processes(process_connections):
    processes = [Process(id, []) for id in process_connections.keys()]

    for process_id, dependent_ids in process_connections.items():
        process = processes[process_id]
        process.dependent_processes = [processes[dep_id] for dep_id in dependent_ids]

    return processes

def main():
    process_connections = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [1]
    }

    processes = setup_processes(process_connections)

    # Start all process threads
    process_threads = []
    for process in processes:
        process_thread = threading.Thread(target=process.run)
        process_threads.append(process_thread)
        process_thread.start()

    # Initiate deadlock detection
    processes[0].message_queue.put((0, 0))

    # Wait for deadlock detection
    for process_thread in process_threads:
        process_thread.join()

if __name__ == "__main__":
    main()
