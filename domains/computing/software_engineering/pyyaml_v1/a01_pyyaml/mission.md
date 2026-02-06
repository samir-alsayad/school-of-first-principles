# Mission: PyYAML (Configuration)

## The Objective
JSON is for machines. JSON is annoying to write (commas, quotes).
YAML is for humans. GAP uses YAML for Manifests and Ledgers.

## The Challenge
1.  Create `config.yaml`:
    ```yaml
    agent:
      name: "007"
      license_to_kill: false
    ```
2.  Create `loader.py`:
    *   Imports `yaml` (`pip install pyyaml`).
    *   Opens and loads the file safely (`safe_load`).
    *   Prints the agent's name.

## Hints
*   Usage: `data = yaml.safe_load(file_object)`
*   Result is a standard Python Dictionary.

## Verification
Output: `007`
