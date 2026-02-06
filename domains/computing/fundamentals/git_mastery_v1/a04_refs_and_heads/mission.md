# Mission: a04_refs_and_heads

## The Objective
You have a chain of commits. But how does Git know which one is "main"? In this mission, you will discover that a **Branch** is not a container—it is just a 40-character text file that points to a commit hash. You will also learn about the **HEAD**, the pointer that points to pointers.

---

## 🏗️ The Setup
Continue in your `workbench/git_lab` directory.
You should have at least two commits from the previous mission.

---

## 🛠️ The Tasks

### 1. Creating a Manual Branch
Git stores branches in `.git/refs/heads/`.
Create a branch called `master` manually:
```bash
echo "<your_last_commit_hash>" > .git/refs/heads/master
```

### 2. Verification
Use `git branch` to see if Git recognizes your manual file.
```bash
git branch
```

### 3. The HEAD of the Snake
Git needs to know which branch is "active". This is stored in the file `.git/HEAD`.
Check its content:
```bash
cat .git/HEAD
```
> [!NOTE]
> It usually says `ref: refs/heads/master`. This is a **Symbolic Ref**.

### 4. Moving the Pointer
Create a second branch `feature` pointing to the same commit.
Then, switch to it **without using git checkout**.
```bash
cp .git/refs/heads/master .git/refs/heads/feature
echo "ref: refs/heads/feature" > .git/HEAD
```
Verify with `git status`. Notice how the current branch changed!

---

## 🎯 Verification Criteria
- [ ] You can explain why a "Branch" doesn't take up any space (besides 41 bytes for the hash and newline).
- [ ] You understand that `git checkout <branch>` is just a command that updates the `.git/HEAD` file.
- [ ] You see that "Merging" will eventually just be moving these pointers around.
