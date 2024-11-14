import subprocess
import requests
import questionary

def get_commit_message_from_api():
    url = "https://www.blackbox.ai/api/chat"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Iltimos, commit xabarini taqdim eting."
            }
        ],
        "previewToken": None,
        "userId": None,
        "codeModelMode": True,
        "agentMode": {},
        "trendingAgentMode": {},
        "isMicMode": False,
        "userSystemPrompt": None,
        "maxTokens": 1024,
        "playgroundTopP": 0.9,
        "playgroundTemperature": 0.5,
        "isChromeExt": False,
        "githubToken": "",
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "clickedForceWebSearch": False,
        "visitFromDelta": False,
        "mobileClient": False,
        "userSelectedModel": None
    }
    headers = {
        "accept": "*/*",
        "accept-language": "uz,en-US;q=0.9,en;q=0.8,ru;q=0.7",
        "content-type": "application/json",
        "priority": "u=1, i"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        # Javobdan commit xabarini olish
        commit_message = response.json().get("choices", [{}])[0].get("message", {}).get("content", "Commit xabari topilmadi.")
        return commit_message
    else:
        print("API so'rovi bajarilmadi, xato!")
        return None
