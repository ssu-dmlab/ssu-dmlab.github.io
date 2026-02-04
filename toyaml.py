import json
import yaml
import requests

'''
get publlications data from google sheet and save it to yaml files
'''
url = "https://script.google.com/macros/s/AKfycbxO17hMwj9jdoHT5imxfTgTITt1JOxLYXNwHz42ZS9VGg1k1qpunpfPvu1pnP6_sSPFKw/exec"

international_conference = requests.get(url + '?sheet=International%20Conference').json()
international_journal = requests.get(url + '?sheet=International%20Journal').json()
domestic_conference = requests.get(url + '?sheet=Domestic%20Conference').json()

with open('_data/international_conference.yml', 'w', encoding='utf8') as f:
    yaml.dump(international_conference, f, allow_unicode=True, sort_keys=False)
with open('_data/international_journal.yml', 'w', encoding='utf8') as f:
    yaml.dump(international_journal, f, allow_unicode=True, sort_keys=False)
with open('_data/domestic_conference.yml', 'w', encoding='utf8') as f:
    yaml.dump(domestic_conference, f, allow_unicode=True, sort_keys=False)

'''
get seminars data from google sheet and save it to yaml files
'''
seminar_url = "https://script.google.com/macros/s/AKfycbzkHvVaplMOJp9tkEoJTX7-X0hy6o6IQz94tm4xyUBaA-Pf50LuEtwqOCgbHmModBDc5A/exec"

response = requests.get(seminar_url)
# print("status:", response.status_code)
# print("content-type:", response.headers.get("Content-Type"))
# print("final url:", response.url)
# print("text head:", response.text[:300])
data = response.json()

with open('_data/seminars.yml', 'w', encoding='utf8') as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)