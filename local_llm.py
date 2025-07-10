import requests
from typing import Optional, List

class LocalLLM:
    """
    Real LLM interface for MindWeaver using Ollama REST API.
    """
    def __init__(self, persona: Optional[str] = None, model: str = "phi3"):
        self.persona = persona or "default"
        self.model = model

    def answer(self, query: str, context: str) -> str:
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": self.model, "prompt": prompt, "stream": False},
                timeout=60
            )
            response.raise_for_status()
            return response.json().get('response', '[No answer returned]')
        except Exception as e:
            return f"[LLM Error: {e}]"

    def compare(self, text1: str, text2: str) -> str:
        """Simulate comparison between two texts."""
        return (
            "Comparison:\n"
            f"Text 1 (start): {text1[:100]}...\n"
            f"Text 2 (start): {text2[:100]}...\n"
            "(This is a placeholder. Actual LLM would provide a nuanced comparison.)"
        )

    def extract_facts(self, text: str, n: int = 3) -> List[str]:
        """Simulate fact extraction by returning random sentences."""
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if not sentences:
            return []
        import random
        return random.sample(sentences, min(n, len(sentences)))
