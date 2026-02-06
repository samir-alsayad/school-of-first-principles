import os

# Find the machine-assigned process identity
pid = os.getpid()

print(f"Hello, I am a process! My PID is: {pid}")
