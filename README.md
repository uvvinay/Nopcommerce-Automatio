**nopCommerce UI Automation (Python & Selenium)**
This repository contains a Selenium-based UI Automation framework for testing the nopCommerce demo application. It is built using Python, Pytest, and a Page Object Model (POM) architecture, designed to run seamlessly in local environments and CI/CD pipelines like Jenkins.

**🚀 Features**
Language: Python 3.x

Framework: Pytest

Design Pattern: Page Object Model (POM)

Reporting: Allure Reports and HTML Reports

CI/CD Ready: Includes a Jenkinsfile for automated Linux-based execution.

Environment: Virtual Environment (venv) support to prevent system-wide dependency conflicts.

**📁 Project Structure**

.
├── Configurations/    # Configuration files (ini, properties)
├── PageObjects/       # POM classes defining page elements and actions
├── Test_cases/        # Pytest test scripts (test_*.py)
├── TestData/          # Excel/JSON files for Data Driven Testing
├── Reports/           # Generated test execution reports
├── Utilities/         # Reusable utility functions (logging, reading config)
├── Jenkinsfile        # Pipeline as Code for Jenkins CI
├── run.sh             # Shell script for Linux execution
├── requirements.txt   # Python dependencies
└── pytest.ini         # Pytest configuration (markers, options)


**Setup & Installation**
# Prerequisites
Python 3.12+

Google Chrome (and ChromeDriver)

Jenkins (optional for CI/CD)

Local Setup
**Clone the repository:**
git clone https://github.com/uvvinay/Nopcommerce-Automatio.git
cd Nopcommerce-Automatio

**Create and Activate Virtual Environment:**
python3 -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
**Install Dependencies**:
pip install -r requirements.txt

**🧪 Running Tests**
Running via Pytest

# Run all tests
pytest -v

# Run with HTML report
pytest -v --html=Reports/report.html --self-contained-html

# Run specific markers (e.g., Sanity)
pytest -v -m sanity

**Running on Jenkins (Linux and windows)**
The project includes a run.sh script specifically for Linux nodes. Ensure your code uses Headless Mode for Chrome to avoid execution errors on the server.

chmod +x run.sh
./run.sh
# windows
 use run.bat file script for windows server or local machine
 
**📊 Reporting**
HTML Reports: Located in the /Reports folder after execution.

Allure Reports: (If configured) Use allure serve allure-results to view interactive results.

**📝 Known Configurations**
Markers: Defined in pytest.ini. Current markers include sanity, regression, etc.

Jenkins Tip: If running on a Debian/Ubuntu Jenkins node, ensure python3-venv is installed on the host.
