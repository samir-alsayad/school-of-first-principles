# Mission: a06_recovery_reflog

## The Objective
You have mastered the DAG, the Pointers, and the Reset. But what happens if you make a mistake? In this final mission, you will learn about the **Reflog**—Git's secret diary of every move your HEAD has ever made. You will learn that in Git, almost nothing is ever really deleted.

---

## 🏗️ The Setup
Continue in your `workbench/git_lab` directory.
Perform a "destructive" operation:
```bash
# Move main back by 2 commits and wipe the working directory
git reset --hard HEAD~2
```

---

## 🛠️ The Tasks

### 1. The Oracle's Log
Check the diary of your HEAD.
```bash
git reflog
```
> [!NOTE]
> Even though `git log` no longer shows your "future" commits, the `reflog` remembers exactly where HEAD was before the reset.

### 2. The Resurrection
Recover your "lost" commit using its hash from the reflog.
```bash
# Method A: Direct Reset
git reset --hard <lost_commit_hash>

# Method B: The Temporary Branch (Safer)
git branch recovery <lost_commit_hash>
```

### 3. The Forgotten Branch
Delete a branch and then recover it.
```bash
git branch -D feature
git reflog
# Find the hash where 'feature' was last standing.
```

---

## 🎯 Verification Criteria
- [ ] You can explain why the `reflog` is local to your machine (it's not pushed to GitHub).
- [ ] You understand that a commit is only truly "deleted" during garbage collection (`git gc`), which happens rarely.
- [ ] You have lost your fear of `git reset --hard`.
