# SafePy
This is a script that provides access control and encryption capablities on a file or folder.
It is extremely useful for organizations wanting to get one step ahead of hackers by ensuring their files never get compromised by a bad actor.

It's key features are:
1. It can identify any modification in a folder set by you :- any renaming, any removal of files or addition.
2. It will alert you in case of any access to the folder via email. This wil work both ways if someone tries to access via hardware or software.
3. It will encrypt the remaining files and generate a 16 byte code that will be stored on the folder specified in the 'step3.py' script so that no more changes can be made.
4. It also includes a decryptor that will use the key file generated and decrypt the files.

You need to specify your sender email, recipent email and an application specific password for Gmail that can be created via sender's Gmail,
more instructions are given here - https://support.google.com/mail/answer/185833?hl=en

You need to change all the folders and directories according to your own need.
One can also change the extension of the encrypted file and even the size of the encryption key via making appropriate changes.

Finally, the pip packages needed -
`pip install pycryptography PyQt5 subprocess hashlib smtplib`

Usage-
1) Fill all the directory paths according to your need in all the scripts
2) Fill in the email details if that function is needed or delete that part of the script
3) Run startup (NOTE: All the files must be in the same folder)
4) Prefer running through a code editor such as VSCode
5) Sit back and relax while we monitor your folder for you!


