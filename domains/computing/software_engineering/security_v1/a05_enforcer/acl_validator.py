# Simple ACL Validator (Enforcer Component)

ALLOWED_PATHS = ["src/main.py", "README.md"]

def validate_access(path):
    if path in ALLOWED_PATHS:
        print(f"✅ Access Granted: {path}")
    else:
        # Standard GAP Fail-Shut response
        raise PermissionError(f"🚫 SECURITY BREACH: Access to {path} is forbidden!")

# Test 1: Authorized
validate_access("src/main.py")

# Test 2: Forbidden
try:
    validate_access("/etc/passwd")
except PermissionError as e:
    print(e)
