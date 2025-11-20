import os
import json
import pdfplumber
from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY",
)

def extract_text(pdf_path):
    """Extracts text from the Universal Credit Act 2025 PDF."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def analyze_text(text):
    """Uses Groq (Llama 3.3) to summarize and extract key legislative sections."""
    
    prompt = f"""
    You are a legal AI agent. Analyze the following text from the 'Universal Credit Act 2025'.
    
    TEXT CONTENT:
    {text[:15000]} 
    
    ### TASK A: SUMMARY
    Provide a summary in 5-10 bullet points focusing on: Purpose, Key definitions, Eligibility, Obligations, and Enforcement elements.
    
    ### TASK B: EXTRACTION
    Extract the specific sections into a JSON format with keys: "definitions", "obligations", "responsibilities", "eligibility", "payments", "penalties", "record_keeping".

    ### TASK C: RULE CHECKS
    Evaluate the text against these rules and provide a status (pass/fail), evidence, and confidence score (0-100):
    1. Act must define key terms
    2. Act must specify eligibility criteria
    3. Act must specify responsibilities of the administering authority
    4. Act must include enforcement or penalties
    5. Act must include payment calculation or entitlement structure
    6. Act must include record-keeping or reporting requirements
    
    Return ONLY valid JSON with this structure:
    {{
        "summary": ["point 1", "point 2"...],
        "extracted_sections": {{
            "definitions": "...",
            "obligations": "...",
            "responsibilities": "...",
            "eligibility": "...",
            "payments": "...",
            "penalties": "...",
            "record_keeping": "..."
        }},
        "rule_checks": [
            {{ "rule": "Act must define key terms", "status": "pass", "evidence": "...", "confidence": 95 }}
        ]
    }}
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful legal assistant that outputs strictly valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile", 
            temperature=0.1,
            response_format={"type": "json_object"} 
        )
        
        return json.loads(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"API Error: {e}")
        return {}

def main():
    print("Extracting text from PDF...")
    text = extract_text("ukpga_20250022_en.pdf")
    
    if not text:
        print("No text extracted. Exiting.")
        return

    print("Analyzing document with Groq (Llama 3)...")
    analysis = analyze_text(text)
    
    output_filename = "final_report.json"
    with open(output_filename, "w") as f:
        json.dump(analysis, f, indent=4)
    
    print(f"Done! Analysis saved to {output_filename}")

if __name__ == "__main__":
    main()
