
Setup instructions:
==============
1. Clone the repository from git-hub:
git clone https://github.com/yourusername/qa-doc-agent.git
cd qa-doc-agent

2. Use pip to install all the packages mentioned in the requirement.txt
pip install -r requirements.txt

3. Need to install Ollama and ensure to check the box that says "Add to PATH" during installation (if available),
 else add the path of Ollama.exe to the environment variable.

4. run the agent
python qa_agent.py --url https://slack.com/help/articles/360035692913-What-is-Slack-  

 Dependencies:
============
1. Ollama application
2. python packages
requests
beautifulsoup4
sentence-transformers
faiss-cpu
numpy
all the above packages are mentioned in the requirements.txt

Usage examples:
===============
PS C:\Users\maha\Downloads\QA_Agent-main> python qa_agent.py --url https://slack.com/intl/en-in/
>what is slack?
 According to the provided context, Slack is a software or platform ([slack.com](http://slack.com)) that facilitates team collaboration by bringing all conversations with partners, clients, vendors, and colleagues in one place. It is designed to support how people naturally work together, making work simpler and more productive. The context mentions that 87% of users feel their ability to work remotely has improved, 91% feel more connected to their teams, and 89% say Slack has improved communication among team members. Additionally, the claim is made that users are 47% more productive when using Slack.

>what are its features?
1. The platform has features that enable reliable central channels for long-term projects, such as product features [Source URL: https://slack.com/intl/es-ar/features].
2. Work in Slack happens in collaborative spaces called channels, where conversations and files related to tasks can be organized based on specific projects or initiatives [Source URL: https://slack.com/intl/es-ar/features#channels].
3. There are features for fast-moving projects, including daily check-ins about tasks in progress [Source URL: https://slack.com/intl/es-ar/features#proj-campaign-q4-2019].
4. The platform offers integration with other tools and applications through Slack Connect and Workflow Builder [Source URL: https://slack.com/intl/es-ar/features#apps-integrations].
5. There are features for file sharing, including the ability to share files in the flow of work [Source URL: https://slack.com/intl/es-ar/features#file-sharing].       
6. The platform includes an AI-powered assistant, Agentforce, which helps users work more intelligently by automating daily tasks and providing enterprise search capabilities [Source URL: https://slack.com/intl/es-ar/features#SlackAIAgentforce].

>what is the moon?
 I'm sorry, I could find any information about the moon in the provided documentation.

>quit
Thank you!

Design decisions:
==============
1. Clean separate functions for crawling, indexing, querying, and generation 
2. Use recursive crawler to support multiple linked page
3. Use Ollama for LLM inference(mistral(for searching) and all-MiniLM-L6-v2(for embedding))
4. Used SentenceTransformer for dense embeddings (fast and good performance)
5. FAISS indexing chosen for scalable vector search

Known limitations:
==============
1.Only works with static HTML content
2. Doesn't support JavaScript-heavy help sites
3. Limited by the capabilities of local Ollama models
4. Maximum pages during web crawling is set to 50 to avoid over loading of websites.
