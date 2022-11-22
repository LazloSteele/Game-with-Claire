

## Dev Workflow
1. identify next change, break change into subtasks as approprite
2. (except for the simplest of changes) we want to create new working branch (presumably from main) with an appropriate name *and checkout*
   * git switch main  -- presuming you want to branch from main then execute ...
   * git switch -c NewBranchName (-c creates the branch and then immediately switches/checksout )
   * NOTE: can optionally push the new branch to the remote or not, dependent on how involved the change is or if multiple devs are working.
   
4. incrementally work through subtasks, add changes into staging at the least as subtasks are completed

    git add (to stage all changes)
	
	git filepattern (to add specific changes)	
3.	commit as subtasks are completed (at the least), prior to a commit it's good form to check you've added all changes to staging using "git status"
  
    git commit -m "commit change description"
3.	as feature is completed either merge back into main then push to the remote, or just merge back into main then push to remote

     * git switch main 
     * git pull -- insure you're up to date with the remote
     * git merge NewBranchName
     * git push -- push commit to remote
   
3. [optionally delete working branch after satisfied main branch is functional]

## Cautions
	Do not checkout a different branch if the current branch has changes which have not been added to staging, you will lose those changes.
	
## Common git tasks howtos/etc.

Checking differences
   * git diff		(changes relative to staging)
   * git diff --cached    (changes staging to HEAD)
   * git diff HEAD	(changes working tree relative to HEAD)

Working with branches:
	Show available branches and current (checked out) branch
		git branch [--list [pattern]]

	Show remote branches:
		git branch -r

	Show all branches:
		git branch -a

	Fetch and merge from remote into current branch:
		git pull

	Fetch from remote w/o merge:
		git fetch
	
## Deleting branches (local / remote / localtracking)
See the following for both a tl;dr anwswer, and nice detailed description
* https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely/23961231#23961231
* Cheatsheet
  * git push origin -d (or --delete) <branch> 
    * this deletes the remote brach and the local remote-tracking branch
  * git branch -d (or --delete) <branch>
    * this deletes the local branch
  * git fetch origin -p (or --prune)
    * syncs your local remote-tracking directories (esp if someone else removed the branches from the remote)
  * In particular see the above link for how there are three branches involved with deletion

