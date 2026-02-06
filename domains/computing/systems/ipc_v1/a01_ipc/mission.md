# Mission: The Socket Operator

## 🎯 Objective
Understand **Inter-Process Communication (IPC)** by building a primitive "Event Bus" using Unix Domain Sockets. This is the nervous system of `nexus-shell`.

## 📜 Prerequisite Concepts
*   **The File Descriptor**: Everything in Unix is a file, even a network connection.
*   **The Socket**: A specialized file that processes can read from and write to.
*   **Serialized Data**: Sending structured text (JSON) through the stream.

## 🛠️ The Build
1.  **The Server**: Write a python script that creates a socket at `/tmp/my_bus.sock` and listens for data.
2.  **The Client**: Use `nc` (netcat) to send JSON messages to that socket.
3.  **The Protocol**: Define a simple handshake ("Hello", "Ack").

## 🔬 Use Case
This specific mechanism is how `nexus-shell` panes talk to each other without blocking the user interface.
