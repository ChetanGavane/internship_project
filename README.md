# Universal Credit Act 2025 - AI Legal Compliance Agent

## 📌 Project Overview
This project is an automated **AI Legal Analyst** designed to process the *Universal Credit Act 2025*. It reads the raw PDF legislation, generates a semantic summary, extracts key obligations, and performs an automated compliance audit against 6 statutory rules.

**Objective:** To demonstrate how Large Language Models (LLMs) can act as intelligent agents for legal compliance, reducing manual review time from hours to seconds.

## ⚙️ Architecture
The solution follows a modular **Extract-Analyze-Verify** pipeline:

1.  **Extraction Layer (`pdfplumber`)**:
    * Converts the unstructured PDF into clean text.
    * Selected over standard OCR for its superior handling of multi-column legal layouts.
2.  **Reasoning Engine (Groq API + Llama 3.3)**:
    * Processes the extracted text to understand legal nuance (e.g., distinguishing between "eligibility" and "entitlement").
    * **Why Groq?** Chosen for low-latency inference, allowing real-time analysis.
3.  **Validation Logic**:
    * Maps the AI's findings against a hard-coded set of 6 compliance rules.
    * Outputs a "Pass/Fail" status with specific evidence quotes.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **PDF Engine:** `pdfplumber`
* **AI Inference:** Groq API (Model: `llama-3.3-70b-versatile`)
* **Output:** JSON (Structured Report)

## 🚀 How to Run
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ChetanGavane/internship_project
    cd internship_project
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set API Key**
    * Replace your Groq API key in main.py:
    ```bash
    GROQ_API_KEY="your_api_key_here"
    ```

4.  **Run the Agent**
    ```bash
    python main.py
    ```

5.  **View Results**
    * The script will generate `final_report.json` in the root directory.

## 📂 Project Structure
* `main.py`: The core logic script.
* `Universal_Credit_Act_2025.pdf`: The source legal document.
* `final_report.json`: The output containing summaries and rule checks.

* `requirements.txt`: List of dependencies.
