# auto_mailer

Automated email sender built with Python

## Requirements & dependencies

- you need some python libs, and it easier to install them with pip
```commandline
sudo apt-get install python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install selenium fake-useragent
```
- download the proper [geckodriver](https://github.com/mozilla/geckodriver/releases)
- extract and put the 'geckodriver' in /usr/bin/ (and verify this directory is in your PATH)

## Usage
### Step 0: before you start
Inside the folder _[inputs](inputs)_ you must create a file named _credentials.txt_.

### Step 1: configuring your [inputs](inputs)
TLDR: Each text file from _[inputs/emails](inputs/emails)_ will be sent to each address in _[inputs/recipients.txt](inputs/recipients.txt)_ using a random address from _inputs/credentials.txt_.  

#### FROM WHO
You must provide, inside the file _inputs/credentials.txt_: the account[s] **FROM** which you want to send a message.  
Two values _login;password_ per line, separated by a semicolon `;`.  
The program will randomly used one of the provided account to send the emails.  
Provide only one account credntials if you do not want randomness.  
Your file should look like something like this:
```text
my_email@protonmail.com;admin1234
my_second_email@protonmail.com;PreviousPasswordWasWeakButNotLIkeJohn
a_third_email_I_creted_for_the_occasion@protonmail.com;c0mpl!c4t"dPasswordWith$tr4ngeCharacters!§
```

**ONLY protonmail ACCOUNTS CAN BE USED TO SEND EMAIL FROM** (for now)



#### TO WHO
You must provide, inside the file _[inputs/recipients.txt](inputs/recipients.txt)_, the account[s] **TO** which you want to send a message. 
One email address per line.  
Your file should look like something like this:  
```text
mickey@gmail.com
zorro.kicks.ass@yahoo.be
dalai_lama@protonmail.com
zorro@yandex.ru
```

#### ABOUT WHAT
You must provide, inside the folder _[inputs/emails/](inputs/recipients.txt)_, some text file(s).  
The NAME of each text file will be used as the email SUBJECT.  
The CONTENT of each text file will be used as the email MESSAGE.  

