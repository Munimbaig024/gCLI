# gcli — Your Personal Git CLI Tool

A personal command line tool that wraps Git commands into simple, fast shortcuts. Built with Python and Click.

---

## Installation

**1. Clone the repo**
```bash
git clone git@github.com:yourname/gcli.git
cd gcli
```

**2. Install dependencies**
```bash
pip3 install click
```

**3. Make it a global command**
```bash
chmod +x gcli.py
sudo cp gcli.py /usr/local/bin/gcli
```

**4. Verify installation**
```bash
gcli --help
```

---

## Commands

### `gcli save "message"`
Add, commit, and push all in one command.
```bash
gcli save "fixed login bug"
```
Runs: `git add .` → `git commit -m "msg"` → `git push`

---

### `gcli status`
Show current git status.
```bash
gcli status
```

---

### `gcli history`
Show recent commit history as a graph. Default shows last 10 commits.
```bash
gcli history
gcli history --lines 20
```

---

### `gcli branch <name>`
Create and switch to a new branch.
```bash
gcli branch feature-login
```
Runs: `git checkout -b feature-login`

---

### `gcli switch <name>`
Switch to an existing branch.
```bash
gcli switch main
gcli switch feature-login
```

---

### `gcli merge <name>`
Merge a branch into your current branch.
```bash
gcli merge feature-login
```

---

### `gcli branches`
List all local and remote branches.
```bash
gcli branches
```

---

### `gcli undo`
Undo the last commit but keep your changes.
```bash
gcli undo
```
Runs: `git reset HEAD~1`

---

### `gcli discard`
Discard all uncommitted changes. Asks for confirmation first.

> Warning: This cannot be undone.

```bash
gcli discard
```

---

### `gcli stash`
Temporarily save your current changes without committing.
```bash
gcli stash
```

---

### `gcli pop`
Bring back the most recently stashed changes.
```bash
gcli pop
```

---

### `gcli init <remote_url>`
Initialize a new repo, make the first commit, and push to GitHub in one step.
```bash
gcli init git@github.com:yourname/my-project.git
```
Runs: `git init` → `git add .` → `git commit` → `git remote add origin` → `git push`

---

## Quick Reference

| Command | Description |
|---|---|
| `gcli save "msg"` | Add + commit + push |
| `gcli status` | Show git status |
| `gcli history` | Show commit history |
| `gcli history --lines N` | Show last N commits |
| `gcli branch <name>` | Create and switch to new branch |
| `gcli switch <name>` | Switch to existing branch |
| `gcli merge <name>` | Merge branch into current |
| `gcli branches` | List all branches |
| `gcli undo` | Undo last commit, keep changes |
| `gcli discard` | Discard all uncommitted changes |
| `gcli stash` | Stash current changes |
| `gcli pop` | Restore stashed changes |
| `gcli init <url>` | Init repo and push to GitHub |

---

## Built With

- [Python 3](https://www.python.org/)
- [Click](https://click.palletsprojects.com/)

---

## Project Structure

```
gcli/
├── gcli.py       # Main CLI tool
└── README.md     # This file
```

---

## Author

Made by **You** — for personal use and learning.

> *"Writing something you use yourself is the fastest way to learn what good code actually feels like."*
> — Programming Hub
