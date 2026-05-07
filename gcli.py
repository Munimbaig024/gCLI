#!/usr/bin/env python3

import click
import subprocess
import sys

def run(command):
    """Run a shell command and print output"""
    result = subprocess.run(command, shell=True, text=True)
    if result.returncode != 0:
        click.echo(click.style(f"❌ Error running: {command}", fg='red'))
        sys.exit(1)

@click.group()
def cli():
    """gcli — Your Personal Git CLI Tool"""
    pass

# ─────────────────────────────────────────
# SAVE = add + commit + push
# ─────────────────────────────────────────
@cli.command()
@click.argument('message')
@click.option('--file', default=None, help='Stage a specific file only')
def save(message, file):
    """Add, commit and push in one command"""
    if file:
        click.echo(click.style(f"Staging file: {file}", fg='cyan'))
        run(f"git add {file}")
    else:
        click.echo(click.style("Staging all files...", fg='cyan'))
        run("git add .")
    click.echo(click.style(f"Committing: {message}", fg='cyan'))
    run(f'git commit -m "{message}"')
    click.echo(click.style("Pushing to GitHub...", fg='cyan'))
    run("git push")
    click.echo(click.style("Done! Code pushed to GitHub.", fg='green'))

# ─────────────────────────────────────────
# STATUS — pretty git status
# ─────────────────────────────────────────
@cli.command()
def status():
    """Show current git status"""
    click.echo(click.style("📊 Current Status:", fg='cyan'))
    run("git status")

# ─────────────────────────────────────────
# HISTORY — pretty git log
# ─────────────────────────────────────────
@cli.command()
@click.option('--lines', default=10, help='Number of commits to show')
def history(lines):
    """Show recent commit history"""
    click.echo(click.style(f"📜 Last {lines} commits:", fg='cyan'))
    run(f"git log --oneline --graph --decorate -{lines}")

# ─────────────────────────────────────────
# BRANCH — create and switch branch
# ─────────────────────────────────────────
@cli.command()
@click.argument('name')
def branch(name):
    """Create and switch to a new branch"""
    click.echo(click.style(f"🌿 Creating branch: {name}", fg='cyan'))
    run(f"git checkout -b {name}")
    click.echo(click.style(f"✅ Switched to branch: {name}", fg='green'))

# ─────────────────────────────────────────
# SWITCH — switch to existing branch
# ─────────────────────────────────────────
@cli.command()
@click.argument('name')
def switch(name):
    """Switch to an existing branch"""
    run(f"git checkout {name}")
    click.echo(click.style(f"✅ Switched to: {name}", fg='green'))

# ─────────────────────────────────────────
# MERGE — merge branch into current
# ─────────────────────────────────────────
@cli.command()
@click.argument('name')
def merge(name):
    """Merge a branch into current branch"""
    click.echo(click.style(f"🔀 Merging {name} into current branch...", fg='cyan'))
    run(f"git merge {name}")
    click.echo(click.style("✅ Merge complete!", fg='green'))

# ─────────────────────────────────────────
# BRANCHES — list all branches
# ─────────────────────────────────────────
@cli.command()
def branches():
    """List all branches"""
    click.echo(click.style("🌿 All branches:", fg='cyan'))
    run("git branch -a")

# ─────────────────────────────────────────
# UNDO — undo last commit (keep changes)
# ─────────────────────────────────────────
@cli.command()
def undo():
    """Undo last commit but keep your changes"""
    click.echo(click.style("⏪ Undoing last commit...", fg='yellow'))
    run("git reset HEAD~1")
    click.echo(click.style("✅ Last commit undone. Changes kept.", fg='green'))

# ─────────────────────────────────────────
# DISCARD — discard all uncommitted changes
# ─────────────────────────────────────────
@cli.command()
def discard():
    """Discard all uncommitted changes"""
    click.confirm(
        click.style("⚠️  Discard ALL changes? This cannot be undone!", fg='red'),
        abort=True
    )
    run("git restore .")
    click.echo(click.style("✅ All changes discarded.", fg='green'))

# ─────────────────────────────────────────
# STASH — stash changes
# ─────────────────────────────────────────
@cli.command()
def stash():
    """Stash your current changes"""
    run("git stash")
    click.echo(click.style("✅ Changes stashed.", fg='green'))

# ─────────────────────────────────────────
# POP — pop stashed changes back
# ─────────────────────────────────────────
@cli.command()
def pop():
    """Bring back stashed changes"""
    run("git stash pop")
    click.echo(click.style("✅ Stash restored.", fg='green'))

# ─────────────────────────────────────────
# INIT — init repo + connect to github
# ─────────────────────────────────────────
@cli.command()
@click.argument('remote_url')
def init(remote_url):
    """Init repo and connect to GitHub"""
    click.echo(click.style("🔧 Initializing repo...", fg='cyan'))
    run("git init")
    run("git add .")
    run('git commit -m "initial commit"')
    run(f"git remote add origin {remote_url}")
    run("git branch -M main")
    run("git push -u origin main")
    click.echo(click.style("✅ Repo created and pushed to GitHub!", fg='green'))

if __name__ == '__main__':
    cli()
