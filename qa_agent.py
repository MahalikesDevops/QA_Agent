import argparse
from crawler import crawl_site_with_links
from indexer import create_index
from query_engine import query_index
from llm_interface import ask_ollama

def main():
    # to receive the url
    parser = argparse.ArgumentParser(description="AI agent")
    parser.add_argument('--url', type=str, required=True, help='Base URL of the documentation site')
    args = parser.parse_args()

    # to crawl the base url and internal links
    docs = crawl_site_with_links(args.url)

    # to use embedding model and create FAISS index
    index, texts, urls, embeddings = create_index(docs)

    while True:
        question = input(">")
        if question.strip().lower() == "quit":
            print("Thank you!")
            break
        # to query the question and search for answer from the embeddings
        top_chunks = query_index(question, index, texts, urls, embeddings)
        top_texts = [chunk for chunk, _ in top_chunks]
        # to get the answer from the ollama in NLP form
        answer = ask_ollama(question, top_texts)
        #print("\nAnswer:")
        print(answer)
if __name__ == "__main__":
    main()

