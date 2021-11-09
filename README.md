# mailingSelenium

This is a POC to test if sending mail with selenium is doable.

## Requirements & dependencies

- you need some python libs, and it easier to install them with pip
```commandline
sudo apt-get install python3-pip
sudo pip3 install --upgrade pip
sudo pip3 install selenium fake-useragent
```
- download the proper [geckodriver](https://github.com/mozilla/geckodriver/releases)
- extract and put the 'geckodriver' in /usr/bin/ (and verify this directory is in your PATH)


# Code snippets and notes

## Functional snippet of code froms tackoverflow
```html
<input type="submit" class="button button_main" style="margin-left: 1.5rem;" value="something">
```
```python
driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click()
```


## New message fields
### RECIPIENT
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

### SUBJECT
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



### MESSAGE
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

### SEND BUTTON

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
