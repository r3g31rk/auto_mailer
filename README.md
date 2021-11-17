# auto_mailer

Automated email sender (from a protonmail account only) built with Python

# Requirements

- you need some python libs, and it easier to install them with pip
    - on LInux:
    ```commandline
    sudo pip3 install selenium fake-useragent
    ```
    - on Windows:
    ```commandline
    py -m pip install selenium fake-useragent
    ```

##Usage
## Step 0: before you start
Inside the folder _[inputs](inputs)_ you **must** create a file named `credentials.txt`.

## Step 1: configuring your [inputs](inputs)
TLDR: Each text file from _[inputs/emails](inputs/emails)_ will be sent to each address in _[inputs/recipients.txt](inputs/recipients.txt)_ using a random address from _inputs/credentials.txt_.  

### FROM WHO
- You must provide, inside the recently created file _inputs/credentials.txt_: the account[s] **FROM** which you want to send some email[s].  
- Two values _login;password_ per line, separated by a semicolon `;`.  
- The program will randomly used one of the provided account to send the emails.  
- Provide only one account credntials if you do not want randomness.  
- Your file should look like something like this:
    ```text
    my_email@protonmail.com;admin1234
    my_second_email@protonmail.com;PreviousPasswordWasWeakButNotLIkeJohn
    a_third_email_I_created_for_the_occasion@protonmail.com;c0mpl!c4t"dPasswordWith$tr4ngeCharacters!§
    ```

**ONLY protonmail ACCOUNTS CAN BE USED TO SEND EMAIL FROM** (for now)



### TO WHO
- You must provide, inside the file _[inputs/recipients.txt](inputs/recipients.txt)_, the account[s] **TO** which you want to send some email[s]. 
- One email address per line.  
- Your file should look like something like this:  
    ```text
    mickey@gmail.com
    zorro.kicks.ass@yahoo.be
    dalai_lama@protonmail.com
    zorro@yandex.ru
    ```

### ABOUT WHAT
- You must provide, inside the folder _[inputs/emails/](inputs/emails)_, some text file[s] containg some email[s].  
- The **name** (without the `.txt` extension) of each text file will be used as the email **subject**.  
- The **content** of each text file will be used as the email **message**.  
- Each text file contained in the folder _[inputs/emails/](inputs/emails)_ will be sent to EACH recipient from the the file _[inputs/recipients.txt](inputs/recipients.txt)_. 
