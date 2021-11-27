# auto_mailer

Automated email sender (from a protonmail account only) built with Python

# Requirements

- To use the **application** `app.exe` (recommended usage), there is NO requirements 

- To use the **script** `app.py` (for dev purpose), you need some python libs  

    - what I did on Ubuntu: `sudo pip3 install selenium fake-useragent` 
  
    - what I did on Windows10: `py -m pip install selenium fake-useragent`
  
  **Nota bene: These are probably not the proper ways of doing it, but it get the job done!**



## Usage
TLDR:    
- using a random pair of credentials provided in `inputs/from.txt` 
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
**Any** mail account can be used to send email **TO**

### ABOUT what
- Put your email[s] in `inputs/messages`, as **txt** file[s]:  
  - The **name** of each text file (without the `.txt` extension) will be used as the email **subject**.  
  - The **content** of each text file will be used as the email **message**.  

> The program will sent **every txt file** provided in `inputs/messages`



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
 
