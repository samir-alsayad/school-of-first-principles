
import os
import ast
import json
import re

# Mapping commonly imported names to PyPI package names
PACKAGE_MAP = {
    "sklearn": "scikit-learn",
    "PIL": "Pillow",
    "yaml": "PyYAML",
    "cv2": "opencv-python",
    "bs4": "beautifulsoup4",
    "dotenv": "python-dotenv",
    "postgres": "psycopg2-binary" # Guessing preference
}

STDLIB = {
    "os", "sys", "json", "time", "subprocess", "ast", "re", "math", "random", 
    "datetime", "typing", "collections", "pathlib", "shutil", "logging", 
    "abc", "functools", "itertools", "threading", "multiprocessing", "io",
    "platform", "signal", "socket", "urllib", "uuid", "hashlib", "argparse",
    "copy", "enum", "inspect", "textwrap", "traceback", "warnings", "weakref"
}

def get_imports_from_file(filepath):
    imports = set()
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            root = ast.parse(f.read(), filename=filepath)
        
        for node in ast.walk(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
    except:
        pass # Skip unparseable files
    return imports

def scan_project_root(root_path):
    print(f"[*] Scanning {root_path}...")
    used_packages = set()
    
    # 1. Scan Code
    for dirpath, _, filenames in os.walk(root_path):
        if "venv" in dirpath or "node_modules" in dirpath or ".git" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".py"):
                used_packages.update(get_imports_from_file(os.path.join(dirpath, f)))
    
    # Filter stdlib
    used_packages = {pkg for pkg in used_packages if pkg not in STDLIB}
    
    # Map to PyPI
    pypi_packages = {PACKAGE_MAP.get(pkg, pkg) for pkg in used_packages}
    
    # 2. Check Manifests
    declared = set()
    req_file = os.path.join(root_path, "requirements.txt")
    if os.path.exists(req_file):
        with open(req_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    declared.add(re.split(r'[=<>~!]', line)[0].lower())

    return {
        "used": list(pypi_packages),
        "declared": list(declared),
        "undeclared": list(pypi_packages - declared) if declared else list(pypi_packages) # If no manifest, everything is undeclared
    }

def run_deep_scan():
    projects_root = "/Users/Shared/Projects"
    intelhub_path = os.path.join(projects_root, "IntelHub")
    
    # Focus on IntelHub for now as it's the suspected "Shadow Zone"
    report = scan_project_root(intelhub_path)
    
    output_path = "../intelhub_dependency_gap.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"[+] Scan Complete for IntelHub.")
    print(f"    Used Imports: {len(report['used'])}")
    print(f"    Declared: {len(report['declared'])}")
    print(f"    GAP (Undeclared): {len(report['undeclared'])}")
    
    # Show top 5 undeclared
    if report['undeclared']:
        print("    Top Undeclared (Sample):", report['undeclared'][:5])

if __name__ == "__main__":
    run_deep_scan()
