# Mission: a02_tree_objects

## The Objective
Blobs are just files. But a real project is a hierarchy of files and folders. In this mission, you will learn how Git represents directories using **Tree** objects. You will manually build a directory structure and "snapshot" it.

---

## 🏗️ The Setup
Continue in your `workbench/git_lab` directory.
Make sure you have at least one blob from the previous mission.

---

## 🛠️ The Tasks

### 1. The Tree Entry
A Tree object is basically a list of Blobs and other Trees.
Create a "draft" of a tree entry in a temporary file:
```bash
# Format: <mode> <type> <hash> \t <filename>
echo -e "100644 blob <your_hash_from_a01>\tsecret.txt" > my_tree.txt
```

### 2. Building the Tree
Use the plumbing command `mktree` to convert your text file into a Git Tree object.
```bash
cat my_tree.txt | git mktree
```
> [!NOTE]
> This command returns a new Hash. This is the hash of the **directory state**, not just the file.

### 3. Nested Architectures
Now, create a second tree that contains your first tree as a "subdirectory".
```bash
# Format for a subdirectory:
# 040000 tree <tree_hash_from_step_2>\tdocs
echo -e "040000 tree <tree_hash_from_step_2>\tdocs" | git mktree
```

### 4. The Structural Audit
Use `cat-file -p` on your top-level tree hash.
Notice how Git shows the "docs" folder pointing to the previous tree.

---

## 🎯 Verification Criteria
- [ ] You can explain why a Tree hash changes if you rename a file inside it, even if the file content (Blob hash) stays the same.
- [ ] You can browse your manual "snapshot" using `git ls-tree -r <top_hash>`.
- [ ] You understand that a Tree is just a recursive pointer system.
