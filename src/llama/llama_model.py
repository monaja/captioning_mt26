from llama_cpp import Llama
from typing import Optional, List, Dict


class LlamaExtension:
    """
    Lightweight LLaMA extension for existing projects.
    Keeps model loading and inference isolated.
    """

    def __init__(
        self,
        model_path: str,
        n_ctx: int = 512,
        n_threads: int = 4,
    ):
        self._model = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 256,
        temperature: float = 0.7,
        stop: Optional[List[str]] = None,
    ) -> str:
        result = self._model(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=stop,
        )
        return result["choices"][0]["text"].strip()

    def run_llama_model(prompt, model_path="../llama/models/LFM2.5-1.2B-Instruct-Q8_0.gguf", max_tokens=100):
        """
        Run the LLaMA model to generate a response based on the given prompt.

        Args:
            prompt (str): The input prompt for the LLaMA model.
            model_path (str): Path to the LLaMA model file in GGUF format.
            max_tokens (int): Maximum number of tokens to generate.

        Returns:
            str: The generated response from the LLaMA model.
        """
        logging.info(f"Running LLaMA model with prompt: {prompt}")
        logging.info(f"Model path: {model_path}, Max tokens: {max_tokens}")
        try:
            llama = Llama(model_path=model_path, verbose=False,)
            response = llama(prompt, max_tokens=max_tokens)
            logging.info("LLaMA model response generated successfully.")
            return response["choices"][0]["text"].strip()
        except Exception as e:
            logging.error(f"Error running LLaMA model: {e}")
            return "Error generating response from LLaMA."
        