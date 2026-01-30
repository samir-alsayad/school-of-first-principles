print("--- PART 1: The List (Binder) ---")
my_list = [1, 2]
print(f"Before: {my_list}")
# We change the first page
my_list[0] = 99
print(f"After:  {my_list}")
print("Success! Lists are mutable.")

print("\n--- PART 2: The Tuple (Sealed Envelope) ---")
my_tuple = (1, 2)
print(f"Before: {my_tuple}")

# EXPERIMENT: Uncomment the next line to see the crash
my_tuple[0] = 99

print("If you see this, the tuple did not stop you.")
