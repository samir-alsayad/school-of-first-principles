
import os
import ast
import sys
import json

# 1. Dynamic Standard Library Detection
try:
    STDLIB = set(sys.stdlib_module_names)
except AttributeError:
    # Fallback for older Python (though User has 3.12 mentioned elsewhere)
    STDLIB = {
        "os", "sys", "json", "time", "subprocess", "math", "random", "datetime", 
        "typing", "collections", "pathlib", "shutil", "logging", "abc", "functools", 
        "itertools", "threading", "multiprocessing", "io", "re", "ast", "argparse"
    }
# Add common missing ones
STDLIB.update({"json", "math", "re", "sys", "time", "os", "logging", "unittest", "shutil"})

# 2. Known Mapping (Import -> Pip Package)
PYPI_MAP = {
    "sklearn": "scikit-learn",
    "PIL": "Pillow",
    "cv2": "opencv-python",
    "yaml": "PyYAML",
    "bs4": "beautifulsoup4",
    "dotenv": "python-dotenv",
    "postgres": "psycopg2-binary",
    "google.generativeai": "google-generativeai"
}

# 3. Local Modules (Detected from previous list_dir)
LOCAL_MODULES = {
    "EvolveLab", "Experiment", "FlashCore", "MemEvolve", "canon", "core",
    "lab", "mini-swe-agent", "runtime", "evolve_cli", "setup",
    "IntelHub" # Self referential
}

def get_base_import(name):
    return name.split('.')[0]

def scan_file(filepath):
    imports = set()
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            root = ast.parse(f.read(), filename=filepath)
        for node in ast.walk(root):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(get_base_import(alias.name))
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(get_base_import(node.module))
    except:
        pass
    return imports

def run_refined_scan():
    root_path = "/Users/Shared/Projects/IntelHub"
    all_imports = set()
    
    print(f"[*] Scanning {root_path} (excluding venv, node_modules, tests)...")
    
    count = 0
    for dirpath, _, filenames in os.walk(root_path):
        # Exclusion logic
        if any(bad in dirpath for bad in ["venv", "node_modules", ".git", "__pycache__", "site-packages", "dist"]):
            continue
            
        for f in filenames:
            if f.endswith(".py"):
                path = os.path.join(dirpath, f)
                file_imports = scan_file(path)
                all_imports.update(file_imports)
                count += 1
                if count % 100 == 0:
                    print(f"    Scanned {count} files...", end="\r")

    print(f"\n[+] Scanned {count} files. Found {len(all_imports)} raw imports.")

    # Filtering
    refined = set()
    skipped_stdlib = 0
    skipped_local = 0
    skipped_private = 0
    
    for imp in all_imports:
        if imp.startswith("_"):
            skipped_private += 1
            continue
        if imp in STDLIB:
            skipped_stdlib += 1
            continue
        if imp in LOCAL_MODULES:
            skipped_local += 1
            continue
            
        # Add to list (mapping to PyPI if known)
        pkg = PYPI_MAP.get(imp, imp)
        refined.add(pkg)

    print(f"[-] Filtered Stats:")
    print(f"    Stdlib: {skipped_stdlib}")
    print(f"    Local: {skipped_local}")
    print(f"    Private: {skipped_private}")
    print(f"[+] Final Dependencies: {len(refined)}")

    # Write Result
    output_path = "../rescue_requirements_refined.txt"
    with open(output_path, "w") as f:
        f.write("# IntelHub Rescue Manifest (Refined)\n")
        for pkg in sorted(refined):
            f.write(f"{pkg}\n")
            
    print(f"[+] Written to {output_path}")

if __name__ == "__main__":
    run_refined_scan()
