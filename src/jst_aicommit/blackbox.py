from typing import Union
import requests
import re
from tenacity import retry, stop_after_attempt


class Blackbox:
    block_texts = [
        "Generated by BLACKBOX.AI, try unlimited chat https://www.blackbox.ai",
        "bash",
        "git commit -m ",
        "git commit -m",
    ]

    def __init__(self) -> None:
        self.url = "https://www.blackbox.ai/api/chat"

    @retry(stop=stop_after_attempt(5))
    def get_commit(self, text: Union[str]) -> Union[str]:
        """Blackboxdan commit generatsiya qilish uchun api request"""
        response = ""
        request = "Manabunga o'zbekcha git commit yozib ber iloji boricha qisqa bo'lsin ```{}```".format(text)
        for chunk in self.request(request):
            response += chunk
        response = re.match("(.*)```(.*)```(.*)", response).groups()[1]
        if response.startswith('"'):
            response = response[1:]
        if response.endswith('"'):
            response = response[:-1]
        return response

    def request(self, text):        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": text
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

        response = requests.post(self.url, json=payload, headers=headers, stream=True)
        for chunk in response.iter_lines(decode_unicode=True):
            for block in self.block_texts:
                chunk = chunk.replace(block, "")
            if len(chunk.strip()) == 0:
                continue
            yield chunk

