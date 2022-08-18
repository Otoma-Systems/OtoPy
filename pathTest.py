from requests import get

TOKEN = "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"
url = f"https://api.github.com/repos/Otoma-Systems/OtoPy/releases/latest"
header = {
"Accept": "application/vnd.github+json", 
"Authorization": f"token {TOKEN}"
}
response = get(url, headers=header).json().get("tag_name").split("v")[-1]

print(response)
