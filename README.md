# Mamikos-Automation-Behave-Selenium

BDD framework built using Python and Behave to support automation testing of websites on various browsers. This project tries to automate simple booking room flow on [Mamikos](mamikos) site.

behave-webdriver
================

behave-webdriver is a step library intended to allow users to easily write [Selenium](http://seleniumhq.org/) webdriver tests with the behave BDD testing framework.

For more details, see the [behave-webdriver documentation](https://behave-webdriver.readthedocs.io/en/stable/)

Setup
===============================

Cloning the repository
----------------------
You can get a copy of all files used in this tutorial by cloning this repository!

```shell
git clone https://github.com/manami27/Mamikos-Automation-Behave-Selenium.git
```
```shell
cd Mamikos-Automation-Behave-Selenium
```

Prerequisites and Installations
-------------------------------
To automate the test, you need to install required component:

1. Python 2.7.14 or above. You can download it from [here](https://www.python.org/downloads/release/python-360/). 

2. To install python package manager (pip). It can be downloaded from its [download page](https://pip.pypa.io/en/stable/installation/). All further installations in the blog post will make use of pip so it’s highly recommended to install it.

3. A development environment. The PyCharm Community edition will be used in this blog post. You can download it from the [Pycharm website](https://www.jetbrains.com/pycharm/). You can use any IDE of your choice since code snippets are not IDE dependent.

4. Behave-webdriver. Installation is easy via pip.
```
    pip install behave-webdriver
```

5. Allure report.

Using webdrivers
----------------

Selenium requires that you provide executables for the webdriver you want to use. Further, unless you specify the path to
the binary explicitly, selenium expects that this executable is in PATH. See these
[driver installation notes](https://selenium-python.readthedocs.io/installation.html#drivers) for more details.

Running the tests
----------------
**To run the test with allure report**
```behave -f allure_behave.formatter:AllureFormatter -o reports/ features/login.feature```

**To run the test without allure report** 
```behave features/login.feature```

**To generate the html allure report from the json files inside reports folder**
```allure serve reports/```

## Built with

* python >= 2.7.10
* behave >= 1.2.5
* parse >= 1.6.3
* parse_type >= 0.3.4
* selenium >= 2.48.0
* argparse
* PyHamcrest >= 1.8

Scenario on the feature file
------------------------

```code-block:: gherkin

    # my-minimal-project/features/myFeature.feature
    Feature: Sample Snippets test
    As a developer
    I should be able to use given text snippets

    Scenario: open URL
        Given the page url is not "http://webdriverjs.christian-bromann.com/"
        And   I open the url "http://webdriverjs.christian-bromann.com/"
        Then  I expect that the url is "http://webdriverjs.christian-bromann.com/"
        And   I expect that the url is not "http://google.com"


    Scenario: click on link
        Given the title is not "two"
        And   I open the url "http://webdriverjs.christian-bromann.com/"
        When  I click on the link "two"
        Then  I expect that the title is "two"
 ```
