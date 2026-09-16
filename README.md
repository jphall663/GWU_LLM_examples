# Educational LLM Examples

Copyright 2026 jphall@gwu.edu. Licensed under the [MIT License](LICENSE).

This project contains small, readable examples for learning core large-language-model techniques with Azure AI Foundry / Azure OpenAI. The examples cover a mini benchmark, a conversational chatbot, embeddings and visualization, retrieval-augmented generation (RAG), LLM-as-judge evaluation, and natural-language-to-SQL.

## Contents

- `basic_config_connect.ipynb` — **start here**: a quick start for Azure configuration, Chat Completions, Responses, and embeddings.
- ``
- `benchmark_example/` — a small MMLU-like multiple-choice benchmark.
- `chatbot_example/` — a minimal terminal chatbot using the Responses API.
- `embedding_example/` — creates NIST AI RMF action embeddings and a UMAP plot.
- `rag_example/` — search → retrieve → augment → generate → cite over those actions.
- `llm_as_judge_example/` — generates answers and scores them with a rubric.
- `text2sql_example/` — turns plain-English questions into safe, inspectable SQLite queries.
- `data/` — source data and the embedding CSV produced for the RAG example.

## Setup in VS Code

1. Clone the repository and open its folder in Visual Studio Code.
2. Create a virtual environment from the integrated terminal (`Terminal` → `New Terminal`):

   ```bash
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   ```powershell
   # Windows PowerShell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. Set the key for the same terminal session. Never put it in a notebook or source file.

   ```bash
   export GW_AZURE_OPENAI_KEY="your-key"  # macOS/Linux
   ```

   ```powershell
   $env:GW_AZURE_OPENAI_KEY="your-key"  # Windows PowerShell
   ```

4. In VS Code, select `.venv` as the Python interpreter and, for notebooks, the matching Jupyter kernel. Open a notebook and choose **Run All**, or run `python chatbot_example/app.py`.

## Azure resource configuration

Each example starts with `RESOURCE = "gw-sb-XX"` and derives `ENDPOINT = f"https://{RESOURCE}.openai.azure.com/"`. Change `RESOURCE` to your assigned sandbox (for example, `gw-sb-02`). The examples read `GW_AZURE_OPENAI_KEY` first and prompt securely only if it is absent.

The Azure calls require access to the stated deployment names. The non-API portions of every notebook can be inspected and run locally; run `embedding_example/get_embeddings.ipynb` before `rag_example/rag_query.ipynb`.

## Running order and troubleshooting

Run the embedding notebook before the RAG notebook. It creates `data/rmf_action_embeddings.csv`, which RAG uses for retrieval. The generated dataset contains the four NIST AI RMF functions: GOVERN, MAP, MEASURE, and MANAGE.

The GPT-5 examples reserve output tokens for both internal reasoning and visible text. If a notebook reports that no visible text or SQL was returned, wait briefly and run that question again; shared educational resources can be rate-limited. Do not lower the example token limits or place an API key in a notebook to work around the issue.
