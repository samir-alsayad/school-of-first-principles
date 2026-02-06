import os

def verify():
    print("🕵️  Verifying Socket Mastery...")
    
    # Check 1: Did they use a Unix socket?
    socket_path = "/tmp/test-bus.sock"
    if not os.path.exists(socket_path):
        # Maybe they used a different name?
        print("❌ Error: socket file `/tmp/test-bus.sock` not found.")
        print("Did you run the `nc -lkU` command?")
        return False

    print("✅ Socket file detected.")
    
    # Knowledge Check
    print("\n🧠  Knowledge Check:")
    answer = input("Is a Socket a Signal or a persistent Connection? ")
    
    if "conn" not in answer.lower():
        print("❌ Not quite. Sockets keep the line open.")
        return False
        
    print("✅ Correct.")
    print("\n🎉 MISSION ACCOMPLISHED.")
    print("You now understand the 'Physical Layer' of the Event Bus.")
    return True

if __name__ == "__main__":
    verify()
