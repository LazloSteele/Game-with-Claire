Common git tasks howtos/etc.

Workflow:
	[create new working branch and checkout]
	identify next change
	break change into subchanges as approprite
	incrementally add into staging while working through change
		git add	[filepattern]	
	commit as subtasks are completed (at the least)
		git commit -m "commit change description" 
	push to remote as feature is complete
		git push
	merge back into main as approprite
	[optionally delete working branch after testing main]

Cautions:
	Do not checkout a different branch if the current branch has changes
	which have not been added to staging, you will lose those changes.
	[
	
Working with branches:
	Show available branches and current (checked out) branch
		git branch [--list [pattern]]

	Show remote branches:
		git branch -r

	Change working copy to branch:

	Fetch and merge from remote into current branch:
		git pull
	Fetch from remote w/o merge:
		git fetch
	
