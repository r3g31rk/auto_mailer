# auto_mailer

Automated email sender (from a protonmail account only) built with Python

# Requirements

- you need some python libs, and it easier to install them with pip
    - what I did on LInux:
    ```commandline
    sudo pip3 install selenium fake-useragent
    ```
    - what I did on Windows:
    ```commandline
    py -m pip install selenium fake-useragent
    ```

**Nota bene: These are probably not the proper ways of doing it, but it get the job done!**


## Usage
TLDR: Each **txt** file will be sent to each address in `recipients.md` using a random address from `credentials.md`.  

## Step 1: configuring your inputs

### FROM WHO
- You must CREATE a file named `credentials.md`, containing the account[s] **FROM** which you want to send some email[s].  
- Two values _login;password_ per line, separated by a semicolon `;`.  
- The program will randomly used one of the provided account to send the emails.  
- Provide only one account credntials if you do not want randomness.  
- Your file should look like something like this:
    ```text
    my_email@protonmail.com;admin1234
    my_second_email@protonmail.com;PreviousPasswordWasWeakButNotLIkeJohn
    a_third_email_I_created_for_the_occasion@protonmail.com;c0mpl!c4t"dPasswordWith$tr4ngeCharacters!§
    ```

**a rule in the `.gitignore` file will prevent to expose publicly your created**
**ONLY protonmail ACCOUNTS CAN BE USED TO SEND EMAIL FROM** (for now)



### TO WHO
- You must provide, inside the file `recipients.md`, the account[s] **TO** which you want to send some email[s]. 
- One email address per line.  
- Your file should look like something like this:  
    ```markdown
    mickey@gmail.com
    zorro.kicks.ass@yahoo.be
    dalai_lama@protonmail.com
    zorro@yandex.ru
    ```

### ABOUT WHAT
- All other **txt** file[s] contained in this folder will be sent as email[s], considering the following rules:  
- The **name** (without the `.txt` extension) of each text file will be used as the email **subject**.  
- The **content** of each text file will be used as the email **message**.  
- Each text file will be sent to EACH recipient from `recipients.md` 




# Notes
## Protonmail html tags
### New message fields
#### Recipient
```html
<input  class="field w100 field-blurred" 
        aria-invalid="false" 
        aria-describedby="to-composer-11697-autocomplete-suggest-text" 
        id="to-composer-11697" 
        type="text" 
        placeholder="Email address" 
        autocomplete="off" 
        data-testid="composer:to" 
        aria-owns="to-composer-11697" 
        aria-activedescendant="to-composer-11697-0" 
        aria-autocomplete="list" 
        value="">
```
- 1st method
    ```python
    driver.find_element_by_xpath("//input[@type='text' and @placeholder='Email address']").send_keys(recipient)
    ```
- 2nd method
    ```python
    driver.find_element_by_xpath("//input[@type='text' and @data-testid='composer:to']").send_keys(recipient)
    ```
- TAB method is NOT advised because if the address is already known, you have to push it 3 times, else only 2!

#### Subject
```html
<input class="field w100 field-blurred field-dirty" 
       aria-invalid="false" 
       aria-describedby="input-6170" 
       id="subject-composer-6167" 
       type="text" 
       placeholder="Subject" 
       autocomplete="off" 
       data-testid="composer:subject" 
       value="">
```
- 1st method
    ```python
    driver.find_element_by_xpath("//input[@type='text' and @placeholder='Subject']").send_keys(subject)
    ```
- 2nd method
    ```python
    driver.find_element_by_xpath("//input[@type='text' and @data-testid='composer:subject']").send_keys(subject)
    ```



#### Message
```html
<iframe title="Editor" 
        class="w100 h100 squireIframe" 
        data-testid="squire-iframe" 
        data-test-id="composer:body" 
        frameborder="0"></iframe>
```
The code above is probably trigger/created with an event  
It's easier/possible to "manually" go to the next MESSAGE field (from the SUBJECT filed) with the TAB key
```python
driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
driver.find_element_by_tag_name('body').send_keys(message)
```

#### Send button

```html
<button 
        class="button button-group-item button-ghost-weak composer-send-button" 
        aria-busy="false" 
        type="button" 
        data-testid="composer:send-button" 
        aria-describedby="tooltip-10193"><svg 
        viewBox="0 0 16 16" 
        class="icon-16p no-desktop no-tablet on-mobile-flex" 
        role="img" 
        focusable="false">
    <use xlink:href="#ic-paper-plane"></use></svg><span class="pl1 pr1 no-mobile">Send</span></button>

```
The code above is probably trigger/created with an event  
It's easier/possible to "manually" go to the next SEND button (from the MESSAGE filed) with the TAB key
```python
driver.find_element_by_tag_name('body').send_keys(Keys.TAB)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.ENTER)
```
 
