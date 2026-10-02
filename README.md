# E-Commerce Playwright Automation Framework

This is a professional-grade Test Automation Framework designed for comprehensive end-to-end UI and API testing. Built from scratch using Python and Playwright, it implements industry best practices like the Page Object Model (POM), Data-Driven Testing, and CI/CD integration.

## 🚀 Technology Stack & Tools
- **Language:** Python
- **Automation Tool:** Playwright (Python-Sync)
- **Test Runner:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **API Testing:** Requests Library
- **Credential Management:** Python-Dotenv (`.env`)
- **CI/CD Pipeline:** GitHub Actions

## 📂 Key Architecture Features
- **Page Object Model (POM):** Clean separation of web elements and test actions into reusable Page Classes.
- **Data-Driven Testing:** Test data is externalized into JSON files inside `test_data/` for clean execution.
- **Secure Configuration:** Environment variables handled via `.env` to keep production credentials safe.
- **Robust Reporting:** Dynamic test execution tracking with high-level Pytest-HTML configurations.
- **Automated CI/CD:** GitHub Actions configured (`tests.yml`) to run the entire suite automatically on every code push.

## 💻 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com
cd python_playwright_framework
```

### 2. Setup Virtual Environment & Install Dependencies
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
playwright install --with-deps
```

### 3. Run Automated Tests
```bash
# Run all tests (UI + API)
pytest

# Run only Smoke Tests
pytest -m smoke

# Run only API Tests
pytest -m api

# Run UI tests with Headed Browser and Slow-Motion (Visual Mode)
pytest tests/ --headed --slowmo 1500
```

---
Developed with 💻 by **Sanskar Gaikwad**
