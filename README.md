# auto_mailer

Automated email sender (from a protonmail account only) built with Python

# Requirements

- To use the **application** `app.exe` (recommended usage), there is NO requirements 

- To use the **script** `app.py` (for dev purpose), you need some python libs  

    - what I did on Ubuntu: `sudo pip3 install selenium fake-useragent` 
  
    - what I did on Windows10: `py -m pip install selenium fake-useragent`
  
  **Nota bene: These are probably not the proper ways of doing it, but it get the job done!**


# Warnings

Most of the free plans of the mailbox providers have some sending limits:
- [protonmail freeplan sending limits](https://protonmail.com/support/knowledge-base/sending-limit/) are **50 messages/hour and 150 messages/day**


## Usage
TLDR:    
- using each time a random pair of credentials provided in `inputs/from.txt` 
- each **txt** file provided in `inputs/messages` 
- will be sent to each account provided in `inputs/to.txt`

## Step 1: Configure your inputs

### FROM who
- Create a file named `from.txt` inside the folder `inputs`
- Write inside the account[s] **FROM** which you want to send some email[s]:  
  - Two values _login;password_ per line, separated by a semicolon `;`.  
  - Your file should look like something like this:
      ```text
      my_email@protonmail.com;admin1234
      my_second_email@protonmail.com;PreviousPasswordWasWeakButNotLikeJohn
      another_of_my_accounts@protonmail.com;stup1dPassw0rd
      ```

> The program will **randomly** use one of the provided account[s] contained in `from.txt`  
a rule in the `.gitignore` file **will prevent to expose publicly your credentials**  
**only protonmail accounts** can be used (for now) to send email **FROM**


### TO who
- Create a file named `to.txt` inside the folder `inputs`
- Write inside the account[s] **TO** which you want to send some email[s]: 
  - One email address per line.  
  - Your file should look like something like this:  
      ```markdown
      mickey@gmail.com
      zorro.kicks.ass@yahoo.be
      dalai_lama@protonmail.com
      zorro@yandex.ru
      ```
> The program will use **every one** of the provided account[s] contained in `to.txt`  
`annuaire.xlsx` contains all french députés + sénateurs + cabinets ministériels + médias  
**Any** mail account can be used to send email **TO**  


### ABOUT what
- Put your email[s] in `inputs/messages`, as **txt** file[s]:  
  - The **name** of each text file (without the `.txt` extension) will be used as the email **subject**.  
  - The **content** of each text file will be used as the email **message**.  

> The program will sent **every txt file** provided in `inputs/messages`
