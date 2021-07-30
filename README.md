# Mega-Meld-Windows
------------Requires Python 3.8+ to Run--------------------
1. How to set up configuration files to review in MEGA-Meld:

	A. It is recommended to create a folder with two sub-folders, one for Initial Files and one for Delta Files, I will refer to these as Initial Root and Delta Root folders/directories
	  respectively

	B. Obtain a set of Initial Files and add them into the Initial Root Directory (initial meaning original files that have not been altered)

	### NOTE: Both the Initial and Delta Root Directories can contain sub-directories (containing the files), this script will automatically traverse all sub-directories within a respective root folder
	### EXAMPLE: 
		
		(Root Folder Name) 'Initial Switch Configurations'
		|_ _ _> (Sub Folder Name) A Switches'
					|_ _ > (File Name) A.conf
		|_ _ _> (Sub Folder Name) B Switches'
					|_ _ > (File Name) B.conf
		|_ _ _>	(Sub Folder Name) C Switches'
					|_ _ > (File Name) C.conf
	
	C. Obtain a set of Delta Files and add them into the Delta Root Directory (delta meaning files that are/may have changed)

	### EXAMPLE:
	
		(Root Folder Name) 'Delta Switch Configurations'
		|_ _ _> (Sub Folder Name) 'A Switches'
					|_ _ > (File Name) A.conf
		|_ _ _> (Sub Folder Name) 'B Switches'
					|_ _ > (File Name) B.conf
		|_ _ _>	(Sub Folder Name) 'C Switches'
					|_ _ > (File Name) C.conf

	D. The overall folder structure for file comparison can look something like these examples ([d] - direcory [f] - file):

		[d]'SWITCH_CONFIGURATION_COMPARISON'
		|
		|_ _ _> [d]'Initial Switch Configurations'
		|	|
		|	|_ _ _> [d]'A Switches'
		|	|	|
		|	|	|_ _ _> [f]'A.conf'
		|	|
		|	|_ _ _> [d]'B Switches'
		|	|	|
		|	|	|_ _ _> [f]'B.conf'
		|	|
		|	|_ _ _> [d]'C Switches'
		|		|
		|		|_ _ _> [f]'C.conf'
		|
		|_ _ _>	[d]'Delta Switch Configurations'
			|
			|_ _ _> [d]'A Switches'
			|	|
			|	|_ _ _> [f]'A.conf'
			|
			|_ _ _> [d]'B Switches'
			|	|
			|	|_ _ _> [f]'B.conf'
			|
			|_ _ _> [d]'C Switches'
				|
				|_ _ _> [f]'C.conf'

		[d]'SWITCH_CONFIGURATION_COMPARISON'
		|
		|_ _ _> [d]'Initial Switch Configurations'
		|	|
		|	|_ _ _> [f]'A.conf'
		|	|
		|	|_ _ _> [f]'B.conf'
		|	|
		|	|_ _ _> [f]'C.conf'
		|
		|_ _ _>	[d]'Delta Switch Configurations'
			|
			|_ _ _> [f]'A.c
			|
			|_ _ _> [f]'B.conf'
			|
			|_ _ _> [f]'C.conf'
	
	### NOTE: The file names in the Initial Root Directory and Delta Root Directory DO NOT have to match in order for the script to compare files properly, the script uses pattern matching in the text of each file to pull hostnames and compare

	### IMPORTANT NOTE: The amount of files in the Delta Root Directory CANNOT exceed the amount of files in the Initial Root Directory, essentially, Delta Root Files <= Initial Root Files

2. Using the MEGA-Meld tool:
	
	A. Run the MEGAMeld.bat script
	B. A dialog box will appear notifying you to select an Intial Root Folder, hit OK
		I. A File Explorer window will open and have you select the Initial Root Folder, as mentioned before all sub-directories within that folder will be traversed
	C. A dialog box will appear notifying you to select a Delta Root Folder, hit OK
		I. A File Explorer window will open and have you select the Delta Root Folder, as mentioned before all sub-directories within that folder will be traversed
	D. The output will appear in the python IDLE shell, there are several characters and color codes to note:
		I. Blue text will appear in two lines at the top of each file comparison, specifying the name of the routers/switches being compared. The Initial File Name will be followed by the Delta File Name
		II. Green text may appear in the output preceded by a (-) character. This signifies text that was present in the Initial File that is not present in the Delta File (configuration removed).
		III. Red text may appear in the output preceded by a (+) character. This signifies text that was not present in the Initial File but is present in the Delta File (configuration added).
		IV. Black text may appear in the output. This is used for context between green/red text and signifies that the text is the same between both files (black text only appears above and below green/red text to provide context to where changes have occured).
		V. Green text (-) immediately followed by red text (+) usually signifies a partial value change in the text string; for example: logging buffered 32768 -> logging buffered 65536 will appear as (-)Green -> (+)Red.
		VI. Blue text lines denoting Router/Switch names followed by a blank space signifies that the Intial File and Delta File are identical
	
	### NOTE: Like Meld, MEGA-Meld also recognizes spaces and newlines. You may come across unimportant changes such as these between files
	### NOTE: It is recommended to make 30-70 comparisons at a time (30-70 Initial to Delta file comparisons), hundreds of comparisons may make it difficult to scroll through the IDLE shell to review changes. Test to see what works best for you.

3. Misc

	### A. This script uses lawsie's idlecolors.py to function properly, which can be found here: https://github.com/lawsie/idlecolors
	B. The Python file included can be edited to whatever changes are necessary for better use of the tool, 
	   the entire Python script includes documentation and comments on logic for overall understanding on how it works
	C. Context lines can be increased/decreased on the script (line 105 n=5)
	D. In the script's v1.0 state it is only useful for comparing configurations of routers and switches in larger volumes
