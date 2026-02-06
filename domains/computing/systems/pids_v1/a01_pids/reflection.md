# Reflection: Process IDs
**Status**: [Verified]

## The Mirror
1. When you ran the script multiple times, did the PID change? Why?
> Yes, because setiap kali script dijalankan, OS memberikan ID proses yang baru.

2. If you have two terminals open and run the same script in both, do they share a PID?
> No, separate processes get separate PIDs.

## My Notes
OS is a module in Python that allows the script to interact with the Operating System. Any Python process automatically gets a PID assigned by the kernel.

## The Discovery
The python file when run created its own process and cleanly outputted its own PID.

## The Gap
[How does one process talk to another?]

## Evidence
```bash
❮ python3 getting_pid.py 
64306
```

