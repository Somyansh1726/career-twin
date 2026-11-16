from pathlib import Path
from openai import OpenAI

# Configuration
MODEL = "llama3.2:3b"
PROFILE_FILE = Path(__file__).with_name("profile.md")

# Connect to our locally running Ollama model
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def load_profile():
    """Read our professional profile from profile.md."""
    if not PROFILE_FILE.exists():
        raise FileNotFoundError("profile.md was not found!")

    return PROFILE_FILE.read_text(encoding="utf-8")



def ask_career_twin(question, profile):
    """Ask the AI a question using our professional profile."""

    messages = [
        {
            "role": "system",
            "content": f"""
You are Somyansh Bishnoi's professional AI assistant.

Your ONLY source of facts about Somyansh is the profile below.

STRICT RULES:
1. Never invent skills, tools, projects or achievements.
2. Never assume a feature was implemented.
3. Never invent performance metrics or business impact.
4. If information is missing, say:
   "My profile does not specify that."
5. Answer questions directly and professionally.
6. Use first person when answering on Somyansh's behalf.
7. Do not add technologies or experiences absent from the profile.

PROFILE:
{profile}
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content



def main():
    profile = load_profile()

    print("\n=== SOMYANSH'S CAREER TWIN ===")
    print("Ask questions about your professional profile.")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Career Twin shutting down. Goodbye!")
            break

        if not question:
            continue

        try:
            answer = ask_career_twin(question, profile)
            print(f"\nCareer Twin: {answer}\n")

        except Exception as error:
            print(f"\nSomething went wrong: {error}\n")


if __name__ == "__main__":
    main()
