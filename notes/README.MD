# Py Notes
A simple notes app that uses Vim (VI Improved) as his default editor and stores the notes on a git repo.

## Setup
The first time you run this script a folder **~/Documents/Notes** will be created, but you will probably see a git error.

This app works via **git**, so for it to work well you will need to create a git repo on the **/Notes** folder. (you can host it on GitHub, GitLab...)

### Create Git Repo
On the **/Notes** folder run the following commands:
```bash
git init

git commit -m "first commit"

git branch -M main

git remote add origin https://link/to/the/remote/git/repo

git push -u origin main
```
### Change Editor
I know **VIM** is something not everyone likes.

If you prefer to use other editor (ie sublime, vscode, micro, atom...) you can open the **settings.json** file and change the editor.

## How does it work
When you run the **main.py** file the following path will be created **~/Documents/Notes/*year*/*month*/*day.md***

The *day.md* file will have the following structure:

```markdown
# day/month/year

## hour/minute
*notes go here*

## hour/minute
*notes go here*

...
```
When you exit the file a git command will push it to the repo.