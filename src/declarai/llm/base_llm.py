from abc import abstractmethod
from typing import TypeVar, Optional


class LLMResponse:
    def __init__(
        self,
        response: str,
        model: Optional[str] = None,
        prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
    ):
        self.response = response
        self.model = model
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = total_tokens


class BaseLLM:
    @abstractmethod
    def predict(self, prompt, *args, **kwargs) -> LLMResponse:
        raise NotImplementedError()


LLM = TypeVar("LLM", bound=BaseLLM)
