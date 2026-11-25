import sqlite3
import json
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent / "nutrition_advisor.db"

def _connect():
    return sqlite3.connect(DB_PATH)

def init_db():
    with _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                name TEXT,
                age INTEGER,
                sex TEXT,
                height_cm REAL,
                weight_kg REAL,
                activity TEXT,
                goal TEXT,
                dietary TEXT,
                targets_json TEXT
            )
        """)

def save_profile(profile, targets):
    if not profile or not targets:
        return
    init_db()
    with _connect() as conn:
        conn.execute("""
            INSERT INTO profiles
            (created_at, name, age, sex, height_cm, weight_kg, activity, goal, dietary, targets_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(timespec="seconds"),
            profile.get("name"), profile.get("age"), profile.get("sex"),
            profile.get("height_cm"), profile.get("weight_kg"),
            profile.get("activity"), profile.get("goal"), profile.get("dietary"),
            json.dumps(targets),
        ))

def get_recent_profiles(limit=10):
    init_db()
    with _connect() as conn:
        rows = conn.execute("""
            SELECT created_at, name, age, weight_kg, goal, dietary, targets_json
            FROM profiles ORDER BY id DESC LIMIT ?
        """, (limit,)).fetchall()
    result = []
    for created_at, name, age, weight, goal, dietary, targets_json in rows:
        targets = json.loads(targets_json)
        result.append({
            "Saved at": created_at,
            "Name": name,
            "Age": age,
            "Weight (kg)": weight,
            "Goal": goal,
            "Diet": dietary,
            "Calories": targets.get("calories"),
            "Protein (g)": targets.get("protein_g"),
        })
    return result
