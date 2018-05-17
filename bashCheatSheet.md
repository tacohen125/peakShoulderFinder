Directory manipulation
Hello! Editing!

Ls = list all content
	Modified by -a; all content
	-l long form of content
		Contains access rights
		Number of hard links (child directories)
		Username of file owner
		Name of group that owns file
		File size in bytes
		Date and time of file creation
		File name
	-t sort by time

Pwd = print working directory

Cd = change directory to
	.. Goes up a directory
	../.. Goes up 2 directories and so on
	/ goes to topvi
Mkdir = make directory
Touch = make a file (specify file name at end)
Cp = copy
	1st file, copy from
	2nd file, copy to
	Can overwrite files with this
	Can copy multiple files from different directories to a single directory
	*; Can copy all files in a directory to a new location
	*a; copies all files starting with letter 'a' to a new directory
Mv = move
	Works like cp
	Can rename files with this
	Old_name new_name
Rm = remove a file
	Need to preface with -r to remove directories
File = view what type of file a file is


Redirection

Echo = displays something on screen
	".." a string of stuff
	".." >, moves string to a file
Cat = displays contents of a file
	'file' > 'file1' moves content of file to file1
	'file' >> 'file1' adds content of file to file1
	< 'file' takes content from file and uses command to the left on it
	| = "pipe", uses left command output as input for command on right
Wc = displays numbers of lines, words, and characters
Sort = sorts the content of a specified file in alphabetical order
	Can use pipe to do further commands with sorted output
Uniq = displays unique values in a file
Grep = global regular expression print
	Recognizes a string and returns values in a file that contain the string
	-i = makes grep case insensitive
Gre

History = display all previous bash commands
	> write history to a file
Git = command to use git
