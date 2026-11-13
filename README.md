# 💬 Ollama Terminal Chat

[فارسی](README.fa.md) | **English**

A minimal terminal assistant that talks to a **local LLM** through [Ollama](https://ollama.com). Responses are streamed token by token, everything runs on your machine, and no API key is needed.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 🔒 Fully local and private: no cloud, no API key
- ⚡ Real-time streaming output
- 🪶 Tiny: a single Python file with one dependency (`requests`)
- 🧯 Clear error messages (server down, timeout, HTTP errors)
- 🔁 Interactive loop: keep asking until you type `exit`

## 📋 Requirements

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running
- A pulled model (the default is `gemma3:1b`)

## 📦 Installation

```bash
git clone https://github.com/Ali-salek/ollama-terminal-chat.git
cd ollama-terminal-chat

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Pull the model and make sure Ollama is running:

```bash
ollama pull gemma3:1b
ollama serve        # skip if Ollama already runs in the background
```

## 🚀 Usage

```bash
python terminal_chat_ollama.py
```

```text
==================================================
Send request to model: gemma3:1b
If you are done, type 'exit'
==================================================

You: Explain what a REST API is in one sentence.
Assistant: A REST API lets programs communicate over HTTP ...
```

Type `exit` or press `Ctrl+C` to quit.

## 🔧 Configuration

Edit the constants at the top of `terminal_chat_ollama.py`:

| Constant | Default                  | Description                          |
| -------- | ------------------------ | ------------------------------------ |
| `MODEL`  | `gemma3:1b`              | Any model you have pulled in Ollama  |
| `SERVER` | `http://localhost:11434` | Address of your Ollama server        |

List your installed models with `ollama list`. Request timeouts are set in `get_response` (`timeout=(5, 120)`: 5 s to connect, 120 s to wait for data).

## ⚠️ Limitations

- Each message is sent **independently**: the assistant does not remember earlier turns. To add memory, switch to Ollama's `/api/chat` endpoint and keep a message history.
- Small models such as `gemma3:1b` are fast but less accurate than larger ones.

## 🗺️ Ideas for Contributions

- Conversation memory via `/api/chat`
- Model name and server address as command-line arguments or environment variables
- System prompt support
- Saving chat history to a file
- Colored / Markdown-rendered output

## 📄 License

Released under the [MIT License](LICENSE).
