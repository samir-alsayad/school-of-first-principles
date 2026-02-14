# Mission: The Pulse (Replacing the Doorbell)

## The Context
You currently have a control system called **Parallax**. It works using a "Doorbell" system:
1.  **Signal**: `kill -USR1 $$`
2.  **Fetch**: Read from `/tmp/px-signal-PID.sh`

**The Problem**: If you send 10 signals very fast, your shell might only hear 3 or 4. Signals don't queue; they collide. To build a powerful assistant, you need a "Persistent Phone Line."

## The Challenge
You must rebuild the Parallax "Link" using a **Unix Domain Socket**.

### 1. The Server (The PBX)
You already have a Python server at `nexus-shell/core/bus/event_server.py`. 
-   **Run it**: `python3 event_server.py`
-   **The Socket**: It creates a socket at `/tmp/nexus_$USER/default/bus.sock`.

### 2. The Subscriber (The Phone)
Your mission is to replace `TRAPUSR1` in your shell with a background listener.
1.  **Requirement**: The listener must use `nc -U` (netcat) to "listen" to the socket.
2.  **Logic**: 
    -   Connect to the socket.
    -   Send a subscription message: `{"action": "subscribe", "type": "COMMAND"}`.
    -   Pipe the output into a loop that executes the commands.

## Constraints
-   **NO SIGNALS**: You are not allowed to use `kill -USR1`.
-   **JSON Only**: Commands must be parsed from JSON: `{"type": "COMMAND", "data": "echo Hello"}`.

## Verification
-   Run the server.
-   Start your new listener.
-   Run `python3 verify.py`. It will flood the socket. If you miss even ONE message, you fail.
