# Test Poker - Automated Testing

## 📌 Description
This project is designed for automated testing of a web application using `pytest` and `selenium`. The tests verify key functionalities such as authentication, UI interactions.

---

## 🔧 Installation and Setup

### 1️⃣ Install Dependencies
Before running the tests, install all dependencies from `requirements.txt` by executing:

```sh
pip install -r requirements.txt
```

---

### 2️⃣ Set Environment Variables
Before running tests, define the `USER_NAME` and `PASSWORD` environment variables used for authentication.

#### 💻 **Linux/macOS**
```sh
export USER_NAME="your_username"
export PASSWORD="your_password"
```
To persist these variables after reboot, add them to `~/.bashrc` or `~/.zshrc`.

#### 🖥 **Windows (PowerShell)**
```powershell
[System.Environment]::SetEnvironmentVariable("USER_NAME", "your_username", [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("PASSWORD", "your_password", [System.EnvironmentVariableTarget]::User)
```
After executing these commands, restart your terminal.

---

## 🚀 Running Tests
After installing dependencies and setting up the environment, run tests using:

```sh
pytest
```

If you need to specify a browser, use the `--bn` argument, for example:
```sh
pytest --bn=firefox
```

Other available test run options can be found in the `pytest.ini` file.

### 📊 Generating Allure Reports
The tests are executed with Allure reports enabled. View the reports, follow one step:

1. Generate and open the report:
   ```sh
   allure serve allure-results
   ```

This will start a local server displaying the test results in an interactive format.

---



## 📌 Useful Commands


📌 **Run only a specific group of tests (by marker):**
```sh
pytest -m smoke
```
(Markers can be found in `pytest.ini`)