# progress.py – CSV-based progress tracking utilities

import os
import pandas as pd
from datetime import datetime

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "data", "progress.csv")
COLUMNS = ["date", "name", "weight", "bmi", "notes"]


def _ensure_file():
    os.makedirs(os.path.dirname(PROGRESS_FILE), exist_ok=True)
    if not os.path.exists(PROGRESS_FILE) or os.path.getsize(PROGRESS_FILE) == 0:
        pd.DataFrame(columns=COLUMNS).to_csv(PROGRESS_FILE, index=False)


def save_progress(name: str, weight: float, bmi: float, notes: str = "") -> bool:
    try:
        _ensure_file()
        df = load_progress()
        new_row = pd.DataFrame([{
            "date":   datetime.now().strftime("%Y-%m-%d %H:%M"),
            "name":   name,
            "weight": weight,
            "bmi":    bmi,
            "notes":  notes,
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(PROGRESS_FILE, index=False)
        return True
    except Exception:
        return False


def load_progress(name: str = "") -> pd.DataFrame:
    _ensure_file()
    try:
        df = pd.read_csv(PROGRESS_FILE)
        for col in COLUMNS:
            if col not in df.columns:
                df[col] = ""
        if name:
            df = df[df["name"].str.lower() == name.lower()]
        df = df.dropna(subset=["weight"])
        return df.reset_index(drop=True)
    except Exception:
        return pd.DataFrame(columns=COLUMNS)


def delete_entry(index: int) -> bool:
    try:
        df = load_progress()
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(PROGRESS_FILE, index=False)
            return True
        return False
    except Exception:
        return False


def get_stats(df: pd.DataFrame) -> dict:
    if df.empty:
        return {}
    df = df.copy()
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce")
    df = df.dropna(subset=["weight"])
    if df.empty:
        return {}
    return {
        "start_weight": df["weight"].iloc[0],
        "current_weight": df["weight"].iloc[-1],
        "change": round(df["weight"].iloc[-1] - df["weight"].iloc[0], 1),
        "min_weight": df["weight"].min(),
        "max_weight": df["weight"].max(),
        "entries": len(df),
    }
