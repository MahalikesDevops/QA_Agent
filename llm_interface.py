import subprocess

# uses ollama mistra model to get the chunks from the embedded model and retur the answer in accordance to the prompt
def ask_ollama(question, context_chunks, model='mistral'):
    joined_context = "\n".join(context_chunks)
    prompt = f"""
You are an expert assistant. Use the detailed context below, extracted from multiple sections of a website, to answer the question accurately.

### Instructions:
1. Only answer if the information is clearly found in the provided context.
2. Every piece of information in your answer **must be followed by its exact source URL** in square brackets. You must include the exact URL from which the information was taken.
3. If the relevant information is not found in the context, respond with the **exact message**
"sorry, I could find any information about this feature in the documentation"
4. Do NOT use your own knowledge or make assumptions.
5. Do NOT paraphrase without citing.
6. Do NOT include sources that are not shown in the context.

Context:
\"\"\"
{joined_context}
\"\"\"

Question:
{question}

Provide a detailed answer based strictly on the above context.
""".strip()

    result = subprocess.run(
        ['ollama', 'run', model],
        input=prompt.encode('utf-8'),
        capture_output=True
    )
    return result.stdout.decode('utf-8')
