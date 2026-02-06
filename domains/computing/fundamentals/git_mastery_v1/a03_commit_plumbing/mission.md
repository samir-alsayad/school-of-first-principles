# Mission: a03_commit_plumbing

## The Objective
You have Blobs (files) and Trees (folders). Now, you need to turn them into a **Commit**. In this mission, you will learn that a Commit is just a metadata object that points to a Tree and (usually) a Parent commit.

---

## 🏗️ The Setup
Continue in your `workbench/git_lab` directory.
You will need your top-level Tree hash from the previous mission.

---

## 🛠️ The Tasks

### 1. The Anatomy of a Commit
Use the `commit-tree` command to create a commit object from your tree.
```bash
# git commit-tree <tree_hash> -m "First Manual Commit"
echo "First Manual Commit" | git commit-tree <tree_hash>
```
> [!NOTE]
> This command returns a **Commit Hash**.

### 2. The Chain of History
A real commit has a **Parent**.
Create a second commit that points to the SAME tree but uses your first commit as a parent.
```bash
echo "Second Manual Commit" | git commit-tree <tree_hash> -p <first_commit_hash>
```

### 3. The Audit
Use `cat-file -p` on your second commit hash.
Notice the fields: `tree`, `parent`, `author`, `committer`.

### 4. The Visibility Test
Now, use the standard `git log` on your commit hash.
```bash
git log <second_commit_hash>
```
> [!TIP]
> Git sees the "History" because it simply follows the `parent` pointers in the commit objects!

---

## 🎯 Verification Criteria
- [ ] You can explain why a Commit has a different hash even if the Tree hash is identical (Metadata changes: timestamp, author).
- [ ] You see that "History" in Git is just a linked list of commit objects.
- [ ] You understand that a Commit doesn't "contain" files—it points to a Tree that contains files.
