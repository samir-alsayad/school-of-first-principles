import socket
import json
import os
import time
import subprocess

def verify():
    print("🚀 Initializing Stress Test (Socket Persistence)...")
    
    user = os.environ.get("USER", "unknown")
    project = "default"
    socket_path = f"/tmp/nexus_{user}/{project}/bus.sock"
    
    if not os.path.exists(socket_path):
        print(f"❌ Error: Event Server NOT running at {socket_path}")
        print("Tip: Run `python3 core/bus/event_server.py` first.")
        return False

    # Check for the verification flag file
    # The student's listener should write to this file when it receives a command.
    target_history = "/tmp/px_verify_pulse.log"
    if os.path.exists(target_history):
        os.remove(target_history)

    print("📡 Connected to Event Bus.")
    print("⏳ Sending 20 rapid fire commands...")

    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
            s.connect(socket_path)
            
            for i in range(20):
                msg = {
                    "action": "publish",
                    "type": "COMMAND",
                    "data": f"echo PULSE_{i} >> {target_history}"
                }
                s.sendall((json.dumps(msg) + "\n").encode())
                time.sleep(0.01) # Very fast

        print("🚦 Commands sent. Waiting for Shell Processing (3s)...")
        time.sleep(3)

        if not os.path.exists(target_history):
            print("❌ Failure: No messages processed by shell.")
            return False

        with open(target_history, "r") as f:
            lines = f.readlines()
            count = len(lines)
            
        print(f"📈 Result: {count}/20 messages received.")
        
        if count == 20:
            print("✅ PERFECT SCORE. Sockets are persistent.")
            return True
        elif count > 0:
            print(f"⚠️  Partial success. You missed {20-count} messages. Signals used to miss more, but we want 100%.")
            return False
        else:
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if verify():
        print("\n🎉 MISSION ACCOMPLISHED.")
    else:
        print("\n❌ MISSION FAILED. Try again.")
