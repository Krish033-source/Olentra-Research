"""
LiteLLM demo: one code path for OpenAI, Claude and Gemini,
plus fallback and load balancing using litellm.Router.

Setup:
    pip install -r requirements.txt
    cp .env.example .env   # add your own API keys
    python litellm_demo.py

Model names change often. If a model errors out, update the
*_MODEL values in your .env file.
"""
import os

from dotenv import load_dotenv
from litellm import Router

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "anthropic/claude-sonnet-4-5")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini/gemini-2.5-flash")

PROMPT = "In one sentence, what does an LLM gateway do?"

model_list = [
    # One alias per provider
    {
        "model_name": "openai",
        "litellm_params": {"model": OPENAI_MODEL, "api_key": os.getenv("OPENAI_API_KEY")},
    },
    {
        "model_name": "claude",
        "litellm_params": {"model": ANTHROPIC_MODEL, "api_key": os.getenv("ANTHROPIC_API_KEY")},
    },
    {
        "model_name": "gemini",
        "litellm_params": {"model": GEMINI_MODEL, "api_key": os.getenv("GEMINI_API_KEY")},
    },
    # Deliberately broken model, used to show fallback
    {
        "model_name": "broken",
        "litellm_params": {
            "model": "openai/this-model-does-not-exist",
            "api_key": os.getenv("OPENAI_API_KEY"),
        },
    },
    # Two deployments under one alias, used to show load balancing
    {
        "model_name": "balanced",
        "litellm_params": {"model": OPENAI_MODEL, "api_key": os.getenv("OPENAI_API_KEY")},
    },
    {
        "model_name": "balanced",
        "litellm_params": {"model": ANTHROPIC_MODEL, "api_key": os.getenv("ANTHROPIC_API_KEY")},
    },
]

router = Router(
    model_list=model_list,
    # If "broken" fails, try claude, then gemini
    fallbacks=[{"broken": ["claude", "gemini"]}],
    routing_strategy="simple-shuffle",
    num_retries=1,
    timeout=30,
)


def ask(alias: str) -> str:
    """Same function for every provider; only the alias changes."""
    response = router.completion(
        model=alias,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=80,
    )
    return f"[{response.model}] {response.choices[0].message.content.strip()}"


def section(title: str) -> None:
    print(f"\n=== {title} ===")


if __name__ == "__main__":
    section("1. Same code, three providers")
    for alias in ("openai", "claude", "gemini"):
        try:
            print(ask(alias))
        except Exception as e:  # key missing or model name outdated
            print(f"{alias}: failed ({type(e).__name__}: {str(e)[:100]})")

    section("2. Fallback (broken model -> claude -> gemini)")
    try:
        print(ask("broken"))
    except Exception as e:
        print(f"fallback failed ({type(e).__name__}: {str(e)[:100]})")

    section("3. Load balancing (5 calls to 'balanced')")
    for i in range(5):
        try:
            print(f"call {i + 1}: {ask('balanced')[:90]}")
        except Exception as e:
            print(f"call {i + 1}: failed ({type(e).__name__})")
