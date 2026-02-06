
import subprocess
import os
import json

def audit_global_env():
    print("[*] Auditing Global Environment (sovereign_core_env)...")
    
    # 1. Capture pip freeze
    try:
        freeze_output = subprocess.check_output(["pip", "freeze"], text=True)
        with open("../global_pip_freeze.txt", "w") as f:
            f.write(freeze_output)
        print(f"[+] 'pip freeze' captured to '../global_pip_freeze.txt'. ({len(freeze_output.splitlines())} packages)")
    except Exception as e:
        print(f"[-] Error running pip freeze: {e}")

    # 2. Scan for Project Dependencies
    print("[*] Scanning /Users/Shared/Projects for dependency files...")
    root_dir = "/Users/Shared/Projects"
    project_deps = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden folders and node_modules
        if any(part.startswith('.') for part in dirpath.split(os.sep)) or 'node_modules' in dirpath:
            continue
            
        found = []
        if "requirements.txt" in filenames:
            found.append("requirements.txt")
        if "pyproject.toml" in filenames:
            found.append("pyproject.toml")
        if "Pipfile" in filenames:
            found.append("Pipfile")
            
        if found:
            rel_path = os.path.relpath(dirpath, root_dir)
            project_deps.append({"path": rel_path, "files": found})

    # Save Scan Result
    with open("../project_dependency_scan.json", "w") as f:
        json.dump(project_deps, f, indent=2)
    
    print(f"[+] Found {len(project_deps)} directories with dependency definitions.")
    print("[+] Audit Complete.")

if __name__ == "__main__":
    audit_global_env()
