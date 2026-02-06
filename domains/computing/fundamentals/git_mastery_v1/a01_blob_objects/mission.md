# Mission: a01_blob_objects

## The Objective
In this mission, you will bypass the "Porcelain" commands (like `git add`) and interact directly with Git's **Object Database**. You will learn that Git is simply a key-value store where the key is a SHA-1 hash and the value is your content.

---

## 🏗️ The Setup
Create a new directory for this mission:
```bash
mkdir -p workbench/git_lab && cd workbench/git_lab
git init
```

---

## 🛠️ The Tasks

### 1. The Hashing Void
Create a file called `secret.txt` with the content "First Principles".
Now, calculate its SHA-1 hash without using Git. Then use Git to see if it matches.

```bash
# Verify the hash
echo -n "First Principles" | openssl sha1
# vs
git hash-object secret.txt
```
> [!IMPORTANT]
> Git adds a header (`blob <size>\0`) before hashing. This is why the hashes might differ!

### 2. Injecting the Blob
Manually inject the content into the Git database.
```bash
git hash-object -w secret.txt
```

### 3. The Audit
Verify that a new file appeared in `.git/objects/`.
Use `cat-file` to read it back from the hash.

```bash
# How does Git store it?
ls -R .git/objects/

# Read it back (Porcelain forbidden)
git cat-file -p <your_hash>
git cat-file -t <your_hash> # Check the type
```

---

## 🎯 Verification Criteria
- [ ] You can explain why the file is stored in a folder with a 2-character name.
- [ ] you can recover the content of a file using only its hash, even if the file in the working directory is deleted.
- [ ] You understand that Git doesn't care about filenames yet—only content.
