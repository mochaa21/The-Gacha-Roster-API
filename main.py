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

def timer_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def myinner(*args, **kwargs):
        print("process...")
        time.sleep(3)
        hasil = func(*args, **kwargs)
        print("success!")
        time.sleep(1.5)
        return hasil
    return myinner

@timer_decorator
def get_top_characters(api_data: str) -> List[str]:
    parsed_json = json.loads(api_data)
    daftar_char = parsed_json["characters"]
    def char_criteria(data: Dict) -> tuple:
        name = data["name"]
        element = data["element"]
        power = int(data["power"])
        return (-power, name, element)

    pro_results = sorted(daftar_char, key=char_criteria)
    results = [f"{char["name"]} ({char["element"]}) - {char["power"]}" for char in pro_results]
    return results

# --- EKSEKUSI ---
print("=== GACHA ROSTER SORTING ===")
roster = get_top_characters(mock_roster_response)
for char in roster:
    print(char)