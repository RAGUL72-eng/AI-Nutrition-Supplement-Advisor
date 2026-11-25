# NutriFit AI — Nutrition & Supplement Advisor

A beginner-friendly Streamlit application for general nutrition education.

## Features
- Estimate daily calorie and macronutrient targets
- Generate flexible meal ideas based on dietary preference
- Read general supplement information and cautions
- Ask nutrition questions using Google Gemini
- Save profile calculations in a local SQLite database

## Setup on Windows

1. Extract this project ZIP.
2. Open the extracted project folder in VS Code.
3. Open Terminal in VS Code. Confirm the terminal is in the folder containing `app.py` and `requirements.txt`.
4. Create and activate a virtual environment:

   ```powershell
   py -3.13 -m venv .venv
   .venv\\Scripts\\activate
   ```

5. Install packages:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Copy `.env.example` and rename the copy to `.env`.
7. Open `.env` and replace the placeholder with your Gemini API key:

   ```env
   GOOGLE_API_KEY=your_real_key_here
   GEMINI_MODEL=gemini-2.0-flash
   ```

   Get a key from https://aistudio.google.com/ . Do not share it or commit `.env` to GitHub.

8. Run the app:

   ```powershell
   streamlit run app.py
   ```

## Notes
- If Gemini model access changes, update `GEMINI_MODEL` in `.env` to a model available in your Google AI Studio account.
- The calorie calculation uses the Mifflin-St Jeor equation and activity multipliers. It is an estimate, not a medical prescription.
- Meal plans are examples, not exact calorie or nutrient calculations.
- Supplement content is general educational information. Ask a healthcare professional for advice about individual needs.
