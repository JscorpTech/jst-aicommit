from typing import Union
from tenacity import retry, stop_after_attempt
from .exceptions import JstException
from g4f.client import Client


class AI:
    def __init__(self) -> None:
        self.client = Client()

    @retry(stop=stop_after_attempt(5))
    def get_commit(self, text: Union[str]) -> Union[str]:
        """Commit generatsiya qilish uchun api request"""
        request_text = "Manabunga o'zbekcha git commit yozib ber iloji boricha qisqa bo'lsin ```{}```".format(text)
        response = self.client.chat.completions.create(
            model="gpt-4o-mini", messages=[{"role": "user", "content": request_text}]
        )
        return response.choices[0].message.content
