# autoscab

------------

Still experimental! Tools for automatically applying for many of the same job.

## Installation

You will need 

- Python 3 (most operating systems come with it preinstalled, otherwise see the [download page](https://www.python.org/downloads/))
- pip (you should have it, otherwise type `python -m ensurepip --upgrade` into your command line/terminal)

For all of this you will need to be on your command line or terminal! 

- Mac: Go to "Applications," then "Utilities" then "Terminal"
- Windows: (someone help me out here I don't use windows!)

### From PyPI: 

```
pip install autoscab
```

### From GitHub:

Either download the code using the green "Code" button above and to the right, and then clicking "Download Zip,"
and unzip the files into a directory, or use `git clone https://github.com/sneakers-the-rat/autoscab.git` if you have git installed

Then, opening a terminal/command prompt in that directory (use `cd` in linux/mac and `dir` in windows to change directories), type:

```pip install .```

## Usage

To get help, type `autoscab --help`

```
(autoscab--E_yShkX-py3.8) bash-3.2$ autoscab --help
usage: APPLY FOR MANY OF THE SAME JOB [-h] [-n N] [--relentless] [--list] [--noheadless] [--leaveopen]
                                      [deployment]

positional arguments:
  deployment    Which deployment to run

optional arguments:
  -h, --help    show this help message and exit
  -n N          Apply for n jobs (default: 1)
  --relentless  Keep applying forever
  --list        List all available deployments and exit
  --noheadless  Show the chromium driver as it fills in the application
  --leaveopen   Try to leave the browser open after an application is completed

IF THEY WANT SCABS, WE'LL GIVE EM SCABS

```

The basic usage is 

```
autoscab <NAME_OF_DEPLOYMENT>
```

So for example

```
autoscab fredmeyer
```

You can then customize how many applications you want to submit with `-n`, run it indefinitely with `--relentless`,
or show the window as the application is being submitted with `--noheadless`

```angular2html
autoscab fredmeyer --relentless --noheadless
```

or

```
autoscab fredmeyer -n 3 --leaveopen
```

## Contribution

**TODO!**

## Changelog

## 0.3.0

- Added `starbucks` deployment
- new `Locator` structure that includes action-types and ability to refer to 
  fields in the `identity` object, so one can make a locator like:

```python
from autoscab.locators import Locator, Location
from selenium.webdriver.common.by import By

my_locator = Locator(locations={
  'my_location': Location(
      By.XPATH,
      '<some-xpath>',
      'send_keys',
      '{first_name}'
  ),
  'a_button': Location(
      By.XPATH,
      '<another-xpath>',
      'click'
  )
})
```

and then use them in the `PostBot` like
```python
self.execute(['my_location', 'a_button'])
```

- `Deployment`s now have `active_dates` which are pprinted in the console like
```
--------------------------------------------------------------------------------
Autoscab Deployments (0.3.0)
starbucks - [ ACTIVE ]   22-01-16 - (indefinite)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fredmeyer - [ INACTIVE ] 21-12-01 - 21-12-31
--------------------------------------------------------------------------------
```

- added ability to specify university in resume maker, pending a fuller rewrite
- `identity` objects have new fields: dob, age, username, university, degree, company, job
- `PostBots` should now have a `confirm` method, though it is not enforced yet by ABC, that lets you make sure you actually submit an app instead of 
  just running indefinitely doing nothing.

## 0.2.2

- Default to "random" email using Faker().free_email() when email confirmation is not required
- Add `identity_params` passed through from `PostBot` class to `Identity` 

## 0.2.1

-  Add pause at end of `fredmeyer` deployment to ensure application submission

# Original KelloggBot Readme:

# KelloggBot
[Setup](#setup)\
[Usage](#usage)

Credit to SeanDaBlack for the basis of the script.

main.py is selenium python bot.
sc.js is a the base of the ios shortcut [COMING SOON]

# Setup

On mac/pc:

`pip install -r requirements.txt`

This will install `webdriver-manager` to automatically download the correct chrome driver. If you are having issues opening having it open chrome, check https://github.com/SergeyPirogov/webdriver_manager.

Poppler must also be installed for pdf2image. Follow the instructions at https://pdf2image.readthedocs.io/en/latest/installation.html to install.

It needs to be found in your `PATH` variable.

`export PATH=$PATH:$(pwd)`

`python main.py` to run. It will loop until you kill the job. `ctrl + c` in your terminal to give the pro lifes a break (optional).

mac:

You might also get a trust issue with the downloaded driver being unverified. To fix that, run 

`xattr -d com.apple.quarantine chromedriver`

this just tells the OS it's safe to use this driver, and Selenium will start working. See https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/ for more info.

You will also need to install ffmpeg if it is not already installed: [Mac installation guide](https://superuser.com/a/624562) [Windows installation guide](https://www.wikihow.com/Install-FFmpeg-on-Windows)

# Usage
```
usage: A script to automate very legitimate applications to kellogg's production plants affected by union strikes
       python3 main.py [-h] [--debug] [--mailtm]

options:
  -h, --help  show this help message and exit
  --debug     Puts script in a 'debug' mode where the Chrome GUI is visible
  --mailtm    Uses mail.tm instead of guerrilla mail by default

Kellogg bad | Union good | Support strike funds
```
