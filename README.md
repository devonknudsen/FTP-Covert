# FTP-Covert
 A Python program that can extract a covert message from the file permissions of an
FTP server. (command line executable)
________________________________________________________________________________
- Fetches the file listing (including permissions) from the FTP server
- Isolates and decodes the file permissions
- Supports using only the 7 right-most “bits” of the file
permissions, filtering out any file with any of the first three “bits” set;
- Also supports using all ten “bits” 

(selects between the two options through a variable called METHOD that is declared at the top of your program)
- Should generate and output the covert message
