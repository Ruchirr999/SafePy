# ccws-project
this is a access control monitoring and notifying script with a simple user interface 

Its key features are:
1)It can identify any modification in a folder set by you :- any renaming, any removal of files or addition.
2)It will alert you in case of any access to the folder via email. This wil work both ways if someone tries to access via hardware or software.
3)It will encrypt the remaining files and generate a 16 byte code that will be stored on the folder specified in the 'step3.py' script so that no more changes can be made.
4)It also includes a decryptor that will use the key file generated and decrypt the files.

You need to specify your sender email, recipent email and an application specific password for gmail that can be created via senders gmail
more instructions are given here - https://support.google.com/mail/answer/185833?hl=en

You need to change all the folders and directories according to your own need.
you can also change the extension of the encrypted file and even the size of the encryption key via making appropriate changes

Finally, the pip packages needed -
pycryptography
PyQt5
subprocess

