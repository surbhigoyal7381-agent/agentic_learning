from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main() -> None:
    load_dotenv()

    prompt = ChatPromptTemplate.from_template(
        "Answer in one short sentence: {question}"
    )

    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL"), temperature=0)
    chain = prompt | llm

    question = "What is the capital of India"
    print("Invoking model...", flush=True)
    response = chain.invoke({"question": question})

    print(f"Prompt: {question}", flush=True)
    print(f"Response: {response.content}", flush=True)


if __name__ == "__main__":
    main()
