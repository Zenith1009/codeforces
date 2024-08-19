import os
import json
from collections import Counter
import requests

def count_problems():
    count = 0
    for root, dirs, files in os.walk('.'):
        if 'problemset' in root or 'contests' in root:
            count += len([f for f in files if f.endswith(('.cpp', '.py', '.java', '.js'))])
    return count

def get_primary_language():
    extensions = []
    for root, dirs, files in os.walk('.'):
        if 'problemset' in root or 'contests' in root:
            extensions.extend([os.path.splitext(f)[1] for f in files if os.path.splitext(f)[1]])
    
    if not extensions:
        return "N/A"
    
    language_map = {'.cpp': 'C++', '.py': 'Python', '.java': 'Java'}
    most_common = Counter(extensions).most_common(1)[0][0]
    return language_map.get(most_common, most_common[1:].upper())

def get_codeforces_info(handle):
    url = f"https://codeforces.com/api/user.info?handles={handle}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            user = data['result'][0]
            return {
                'current_rating': user.get('rating', 'Unrated'),
                'max_rating': user.get('maxRating', 'Unrated'),
                'rank': user.get('rank', 'Unranked'),
                'max_rank': user.get('maxRank', 'Unranked')
            }
    return None

# Replace 'your_codeforces_handle' with your actual Codeforces handle
codeforces_handle = 'Zenith_1009'

total_problems = count_problems()
primary_language = get_primary_language()
codeforces_info = get_codeforces_info(codeforces_handle)

stats = {
    "total_problems": total_problems,
    "primary_language": primary_language,
    "codeforces_handle": codeforces_handle
}

if codeforces_info:
    stats.update(codeforces_info)

with open('stats.json', 'w') as f:
    json.dump(stats, f)

print(f"Total problems solved: {total_problems}")
print(f"Primary language: {primary_language}")
print(f"Codeforces info: {codeforces_info}")
