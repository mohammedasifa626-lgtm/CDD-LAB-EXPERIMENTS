# Experiment 3 — Branching, merging, rebasing and conflict resolution

```bash
git switch -c feature/example-change
# Edit and save a file
git add .
git commit -m "Add example change"
git switch main
git merge feature/example-change
```

To practise rebasing on a practice branch:
```bash
git switch feature/example-change
git fetch origin
git rebase origin/main
```

For a conflict: run `git status`, edit conflicted files to resolve markers, stage the result with `git add <file>`, then finish the merge with `git commit` if requested or continue a rebase with `git rebase --continue`. Use `git rebase --abort` to cancel. Avoid rebasing shared branches without team agreement.

Record what happened and add your own screenshots to `screenshots/`.
