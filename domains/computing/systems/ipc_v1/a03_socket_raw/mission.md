# Mission: The Pipe (Raw Sockets)

## The Objective
Forget signals. Sockets are like "Pipes" that stay open. You don't "ring a doorbell" and hope they are awake; you connect to a persistent line.

## The Logic
In Unix, a **Socket** looks like a file on disk (usually `.sock`), but it behaves like a phone line. 
- One person "Listens" on the socket.
- Another person "Connects" to it.

## The Challenge: `talk.sh`
We will use `nc` (netcat), the Swiss Army knife of networking.

1. **The Server (The Receiver)**:
   In one terminal, run this to create a listener:
   ```bash
   nc -lkU /tmp/test-bus.sock
   ```
   *(-l = listen, -k = keep open, -U = Unix socket)*

2. **The Client (The Sender)**:
   In a **second** terminal, send a message into that socket:
   ```bash
   echo "Hello from the other side" | nc -U /tmp/test-bus.sock
   ```

3. **The Observation**:
   Did the message appear in the first terminal? 
   Notice that the first terminal didn't close. It is still waiting for more.

## Verification
- Can you send 3 different messages?
- Run `python3 verify.py` to prove you understand the socket path.
