# Learning Requirements: Parallax Socket Transition (v1)

## Introduction
The current command-execution bridge in `parallax` relies on shell signals (`SIGUSR1`) and file-polling. While functional, it is "Disconnected." To build a Sovereign Assistant like Letta or MiniCPM-o, the Student must understand **Persistent Inter-Process Communication (IPC)** using Unix Sockets. This filling the gap for low-latency, ordered command dispatch.

## Conceptual Glossary
- **IPC (Inter-Process Communication)**: Mechanisms provided by the OS to allow processes to manage shared data.
- **Unix Domain Socket (UDS)**: A bidirectional data stream for processes on the same host (faster/safer than TCP for local work).
- **Pub/Sub**: A messaging pattern where senders (publishers) do not program the messages to be sent directly to specific receivers (subscribers), but instead categorize published messages.
- **AsyncIO Reader/Writer**: Python's high-level abstractions for non-blocking stream handling.

## Learning Objectives

### Objective 1: Understanding Stream Persistence
**Student Story:** As a Software Engineer, I want to understand how a "Phone Line" (Socket) differs from a "Doorbell" (Signal), so that I can implement low-latency, multi-payload control loops.

#### Verification Criteria (Acceptance of Knowledge)
1. The Student SHALL be able to explain why a Socket allows for ordered command queues while Signals can be dropped.
2. The Student SHALL implement a minimal ZSH listener that subscribes to a Python-managed socket.
3. The Student SHALL identify the failure state when the server dies and implement a reconnection logic.

### Objective 2: JSON-Protocol Implementation
**Student Story:** As a Tools Builder, I want to understand how to serialize commands into JSON, so that my shell and my Python assistant share a common "Language."

#### Verification Criteria (Acceptance of Knowledge)
1. The Student SHALL produce a Python script that parses incoming socket bytes into a JSON object.
2. The Student SHALL implement a ZSH hook that maps a specific "type" in JSON to a shell function.
