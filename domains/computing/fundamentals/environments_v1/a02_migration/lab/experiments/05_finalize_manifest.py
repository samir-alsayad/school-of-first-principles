
import os

# Packages to filter out (Internal/Local/Sibling)
LOCAL_ONLY = {
    "rlm", "minisweagent", "swerex", "lasj", "EvolveLab", "Experiment", "FlashCore", 
    "MemEvolve", "canon", "core", "lab", "mini-swe-agent", "runtime", "evolve_cli", 
    "setup", "IntelHub", "agent_kb_provider", "agent_types", "agents", "auto_evolver", 
    "base_agent", "base_memory", "config", "create_nexus_agent", "dispatcher", 
    "engine", "eval_utils", "expel_provider", "inject_middleware", "integration", 
    "memory", "memory_creator", "memory_evolver", "memory_types", "mirror", 
    "mm_tools", "mm_tools_utils", "mobilee_provider", "models", "monitoring", 
    "nexus_client", "persona_lock", "phase_analyzer", "phase_generator", 
    "phase_validator", "phases", "prime_sandboxes", "routes", 
    "run_flash_searcher_mm_gaia", "run_provider", "search_tools", 
    "skillweaver_provider", "swe_agent_validator", "tests", "thought_filter", 
    "tool_sandbox", "tools", "trajectory_tools", "translator", "utils"
}

def finalize_manifest():
    input_path = "../rescue_requirements_refined.txt"
    output_path = "/Users/Shared/Projects/IntelHub/requirements.txt"
    
    print(f"[*] Filtering {input_path}...")
    
    if not os.path.exists(input_path):
        print(f"[!] Error: {input_path} not found.")
        return

    external_packages = []
    skipped = []

    with open(input_path, "r") as f:
        for line in f:
            pkg = line.strip()
            if not pkg or pkg.startswith("#"):
                continue
            
            if pkg in LOCAL_ONLY:
                skipped.append(pkg)
            else:
                external_packages.append(pkg)

    # Dedup and sort
    external_packages = sorted(list(set(external_packages)))

    with open(output_path, "w") as f:
        f.write("# IntelHub Requirements (External Only)\n")
        f.write("# Generated from Module 02 Audit\n")
        f.write("# Siblings (rlm, minisweagent) should be installed via -e\n\n")
        for pkg in external_packages:
            f.write(f"{pkg}\n")

    print(f"[+] Finalized manifest written to {output_path}")
    print(f"    Kept: {len(external_packages)} external packages.")
    print(f"    Filtered: {len(skipped)} local/sibling modules.")
    if skipped:
        print(f"    Example Filtered: {skipped[:5]}")

if __name__ == "__main__":
    finalize_manifest()
