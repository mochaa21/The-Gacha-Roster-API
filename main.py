import json
import time
import functools
from typing import Callable, List, Dict

mock_roster_response = """
{
    "server": "Asia",
    "characters": [
        {"name": "Subaru", "power": 150, "element": "Shadow"},
        {"name": "Emilia", "power": 9500, "element": "Ice"},
        {"name": "Rem", "power": 8000, "element": "Water"},
        {"name": "Ram", "power": 8000, "element": "Wind"},
        {"name": "Ariel", "power": 9999, "element": "Wind"}
    ]
}
"""

# TUGAS 1: Buat @timer_decorator di sini (Jangan lupa tampung dan return hasilnya)


# TUGAS 2: Buat fungsi get_top_characters(api_data: str) -> List[str]
# Wajib dipasangkan @timer_decorator di atasnya.
# Perbaiki cara penulisan f-string lu menggunakan kutip tunggal di dalam kurung kurawal.


# --- EKSEKUSI ---
# print("=== GACHA ROSTER SORTING ===")
# roster = get_top_characters(mock_roster_response)
# for char in roster:
#     print(char)