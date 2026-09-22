from llm.client import LLMClient


def main():
    llm = LLMClient()
    prompt = input("Enter your prompt: ")
    response = llm.generate(prompt)
    print(f"Query: {prompt}\nResponse: {response}")


if __name__ == "__main__":
    main()