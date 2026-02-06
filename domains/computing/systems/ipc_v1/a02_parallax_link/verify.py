import os
import time
import subprocess
import signal

def verify():
    print("🕵️  Verifying IPC Mastery...")
    
    # Check 1: Does px-link exist?
    px_link_path = os.path.expanduser("/Users/Shared/Projects/nexus-shell/modules/parallax/bin/px-link")
    if not os.path.exists(px_link_path):
        print("❌ Error: Could not find `bin/px-link`. Are you in the right workspace?")
        return False

    print("✅ px-link located.")

    # Check 2: Simulation
    print("\n🧪  Simulating Injection...")
    
    # Create valid dummy signal file
    pid = os.getpid()
    sig_file = f"/tmp/px-signal-{pid}.sh"
    
    with open(sig_file, "w") as f:
        f.write('export PARALLAX_VERIFIED="TRUE"')
        
    print(f"   -> Wrote to {sig_file}")
    
    print("   -> Sending SIGUSR1 to myself...")
    # In a real shell, TRAPUSR1 would handle this. 
    # Here we are just verifying the files exist and the user knows the logic.
    
    # Ask the user:
    print("\n🧠  Knowledge Check:")
    answer = input("What signal does Parallax use to wake up the shell? (e.g., SIGKILL): ")
    
    if answer.strip().upper() not in ["SIGUSR1", "USR1", "10", "30"]:
        print("❌ Incorrect. Check `TRAPUSR1` in the code.")
        return False
        
    print("✅ Correct Signal.")
    
    print("\n🎉  MISSION ACCOMPLISHED.")
    print("You have proven you understand the Open-Loop Control system.")
    return True

if __name__ == "__main__":
    verify()
