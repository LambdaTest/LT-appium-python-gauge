# Additional Setup Notes (Updated Configuration)

This document contains additional setup instructions and fixes required to run the project with newer versions of Python, Appium Python Client, and dependencies.

These updates ensure compatibility with modern versions of:
- Python 3.13+
- Appium Python Client 2.x
- Selenium 4.x
- Gauge Python plugin

---

# 1. Python Version Compatibility

This project works with Python 3.13+. If you encounter protobuf related errors when running Gauge, set the following environment variable before executing tests.

## Windows

set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

## macOS / Linux

export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

---

# 2. Updated Python Dependencies

Install dependencies using:

pip install -r requirements.txt

Recommended compatible versions:

Appium-Python-Client>=2.11.1
selenium>=4.9.1
getgauge>=0.5.0
protobuf>=6.31.1
urllib3>=2.0
requests>=2.31

---

# 3. Updated Appium Driver Initialization

The driver initialization has been updated to use the modern Appium Python Client syntax.

Key changes include:
- Using UiAutomator2Options
- Passing capabilities using W3C format
- Using LambdaTest vendor capabilities inside `lt:options`
- Correct Appium hub endpoint

Example driver initialization:

from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

username = os.getenv("LT_USERNAME")
access_key = os.getenv("LT_ACCESS_KEY")

caps = {
"platformName": "Android",
"appium:platformVersion": "13",
"appium:deviceName": "Galaxy S21 Ultra 5G",
"appium:app": "lt://proverbial-android",
"lt:options": {
"name": "Gauge Sample Test",
"build": "Python_Gauge_LambdaTest",
"isRealMobile": True
}
}

options = UiAutomator2Options().load_capabilities(caps)

hub_url = f"https://{username}:{access_key}@mobile-hub.lambdatest.com/wd/hub"

driver = webdriver.Remote(
command_executor=hub_url,
options=options
)


---

# 4. LambdaTest Hub Endpoint Fix

Older examples used incorrect or incomplete hub URLs.

Correct endpoint for Appium tests on LambdaTest:

https://mobile-hub.lambdatest.com/wd/hub

---

# 5. Running the Tests

Once dependencies and environment variables are configured, run the tests using:

gauge run specs

After execution, the results will appear in:

reports/html-report/index.html

and on the LambdaTest App Automation Dashboard.

---

# 6. Troubleshooting

### Invalid Command Error

If you see:

Message: Invalid Command

Ensure that:

1. The hub URL includes `/wd/hub`
2. Capabilities are passed using W3C format
3. LambdaTest capabilities are inside `lt:options`

### Protobuf Error

If you see errors similar to:

TypeError: Descriptors cannot be created directly

Set:

PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

before running Gauge.

---

# Summary of Changes

The following updates were applied to make the project compatible with modern environments:

- Updated Appium Python Client usage
- Updated driver initialization with UiAutomator2Options
- Added W3C compliant capability structure
- Added LambdaTest capability namespace (`lt:options`)
- Fixed LambdaTest hub endpoint
- Added Python 3.13 compatibility workaround
- Updated dependency recommendations


## Important Note on Python and Gauge Compatibility

This project has been tested with Python 3.13.7. Since the current latest Gauge Python plugin version is 0.5.0, running the project on higher Python versions may require additional configuration such as setting PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python.

The current latest version of the **Gauge Python plugin** (`getgauge`) is **0.5.0**. This version has limited compatibility with newer Python releases.

If you use a **Python version higher than the supported range**, you may encounter issues such as:

* Protobuf compatibility errors
* Gauge step execution failures
* Session initialization errors during Appium driver startup

To avoid these issues, ensure the following:

* Use **getgauge version 0.5.0**
* If using newer Python versions (e.g., Python 3.13+), set the following environment variable before running the tests:

### Windows

```
set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

### macOS / Linux

```
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

This workaround allows the project to run successfully with newer Python versions even though the Gauge Python plugin has not yet released an updated version for full compatibility.
