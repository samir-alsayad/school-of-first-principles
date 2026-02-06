# Mission: a05_reset_logic

## The Objective
You now know that Git is a system of pointers. In this mission, you will learn the most powerful tool for moving those pointers: **`git reset`**. You will master the difference between `--soft`, `--mixed`, and `--hard`, and how they affect the **Three Trees**: the Working Directory, the Index (Staging), and the HEAD.

---

## 🏗️ The Setup
Continue in your `workbench/git_lab` directory.
Ensure you have a clean state with at least 3 commits.

---

## 🛠️ The Tasks

### 1. The Soft Reset
Imagine you want to "un-commit" your last commit but keep your changes staged.
```bash
git reset --soft HEAD~1
```
> [!AUDIT]
> Use `git status`. Notice the changes are in the "Green" (staged) zone. 
> Compare `.git/HEAD` to `.git/refs/heads/master`. HEAD moved, but your files didn't change.

### 2. The Mixed Reset (The Default)
Now, imagine you want to unstage those changes too.
```bash
git reset --mixed HEAD # (or just git reset)
```
> [!AUDIT]
> Use `git status`. The changes are now in the "Red" (unstaged) zone.
> Your Working Directory is still safe, but the Index (Staging area) has been reset to match HEAD.

### 3. The Hard Reset (The Point of No Return)
Wipe everything out and match a previous commit exactly.
```bash
git reset --hard <commit_hash>
```
> [!CAUTION]
> This command syncs all three trees. Your unsaved changes in the Working Directory are GONE.

---

## 🎯 Verification Criteria
- [ ] You can explain what happens to the "Index" during a `--soft` reset. (Nothing! It stays as it was).
- [ ] You understand that `reset` is primarily about moving the **Branch Pointer**.
- [ ] You can predict the state of `git status` after each type of reset.
