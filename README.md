# 🎬 YouTube Summarizer

Um aplicativo web que gera resumos automáticos de vídeos do YouTube usando IA (Groq).

## ✨ Features

- ✅ Extrair áudio de vídeos YouTube
- ✅ Transcrição automática com Whisper
- ✅ Resumo inteligente com LLM (Llama 3.3)
- ✅ Interface web moderna com Streamlit
- ✅ Download do resumo em Markdown
- ✅ Informações do vídeo (título, thumbnail, autor)

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **APIs**: 
  - Groq (Transcrição + LLM)
  - YouTube (via PyTubeFix)
- **Processamento**: FFmpeg

## 📋 Requisitos

- Python 3.8+
- FFmpeg instalado
- API Key do Groq (grátis em https://console.groq.com)

## 🚀 Quick Start

### 1. Clone/Copie os arquivos

```bash
git clone seu-repo
cd youtube-summarizer
```

### 2. Instale as dependências

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
```

### 3. Configure a API Key

```bash
cp .env.example .env
# Edite .env com sua chave Groq
```

### 4. Execute

```bash
streamlit run app.py
```

## 📖 Como Usar

1. Abra `http://localhost:8501`
2. Cole a URL de um vídeo YouTube
3. Clique em "Processar"
4. Aguarde a transcrição e geração do resumo
5. Baixe ou copie o resultado

## 🔒 Segurança

- Nunca commit `.env` com sua API key
- Use variáveis de ambiente em produção
- Para deploy, use Secrets do Streamlit Cloud

## 📦 Estrutura

```
.
├── app.py                 # App Streamlit principal
├── youtube_processor.py   # Classe de processamento
├── requirements.txt       # Dependências
├── .env                   # Config (não commitar!)
└── SETUP.md              # Guia de instalação
```

## 🐛 Troubleshooting

**"FFmpeg not found"** → Instale FFmpeg conforme o SO

**"API Key inválida"** → Gere uma nova em https://console.groq.com

**"Streaming error"** → Tente outra URL do YouTube

## 📝 Licença

MIT

## 🙋 Suporte

Qualquer dúvida, abra uma issue ou me contacte!

---

Feito com ❤️ usando Streamlit + Groq
