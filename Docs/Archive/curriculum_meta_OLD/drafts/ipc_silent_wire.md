# Project: The Silent Wire (IPC)

**Objective:** Build a signaling system between two isolated processes using the OS Kernel as the medium.
**Prerequisites:** Functions, Loops, Basic Shell.

## The Atomic Units (Curriculum)

### 1. Identity (Discovery) ✅
*   **Concept:** Process Isolation & PIDs.
*   **The Code:** `os.getpid()`.
*   **Outcome:** "I have a number."
*   *Status: Archived in `library/systems/01_pid_discovery`.*

### 2. Persistence (The Daemon) ✅
*   **Concept:** The Event Loop vs. Linear Execution.
*   **The Code:** `while True`, `time.sleep()`.
*   **Outcome:** "I refuse to die."
*   *Status: Archived in `library/systems/02_persistence_loop`.*

### 3. The Receiver (The Ear) 🔄 **(CURRENT)**
*   **Concept:** Interrupts & Signal Handling.
*   **The Code:** `signal.signal(signal.SIGUSR1, handler)`.
*   **Goal:** A script that prints "Caught!" when hit by `kill -SIGUSR1`.

### 4. The Sender (The Finger) ⏳
*   **Concept:** System Calls from Python (`kill` is just a function).
*   **The Code:** `os.kill(target_pid, signal.SIGUSR1)`.
*   **Goal:** A script that asks for a PID and "pokes" it.

### 5. The Protocol (The Language) ⏳
*   **Concept:** Semantic Meaning.
*   **The Challenge:**
    *   `SIGUSR1` = "Print Status".
    *   `SIGUSR2` = "Reset Counter".
    *   `SIGTERM` = "Graceful Shutdown" (Save & Exit).
*   **Goal:** A fully interactive daemon controlled by a second terminal.

---

## Final Artifact
A working `sw_system/` (Silent Wire System) in the Library, containing `daemon.py` and `remote.py`.
