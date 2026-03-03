# 🎬 YouTube Summarizer

Um aplicativo que gera resumos automáticos de vídeos do YouTube usando IA (Groq).

**⚠️ Importante:** Este projeto roda **localmente na sua máquina**. Você precisa fornecer sua própria API Key do Groq.

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

## 📋 Pré-requisitos

- Python 3.8+
- FFmpeg instalado no seu sistema
- **API Key do Groq** (grátis em https://console.groq.com)

## 🚀 Instalação e Configuração

### Passo 1: Clone o Repositório

```bash
git clone https://github.com/seu-usuario/youtube-summarizer.git
cd youtube-summarizer
```

### Passo 2: Obtenha sua API Key do Groq

1. Vá para https://console.groq.com
2. Crie uma conta (é grátis!)
3. Vá em **API Keys**
4. Clique em **Create API Key**
5. Copie a chave (algo como `gsk_xxx...`)

### Passo 3: Configure o Arquivo .env

```bash
cp .env.example .env
```

Abra o arquivo `.env` com um editor de texto e adicione sua chave:

```
GROQ_API_KEY=gsk_sua_chave_aqui
```

**Exemplo completo:**
```
GROQ_API_KEY=insira_sua_API_KEY_aqui
```

### Passo 4: Instale as Dependências

**Windows (CMD ou PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Passo 5: Execute o Aplicativo

```bash
streamlit run app.py
```

Seu navegador abrirá automaticamente em `http://localhost:8501`

Se não abrir, copie e cole manualmente no navegador.

---

## 📖 Como Usar

1. **Abra o app** em `http://localhost:8501`
2. **Cole a URL** de um vídeo YouTube
3. **Clique em "Processar"**
4. **Aguarde** a transcrição e geração do resumo (~1-2 minutos)
5. **Baixe o resumo** em Markdown ou copie o texto

## 🔒 Segurança

- ✅ Sua API Key fica apenas em `.env` (seu computador, privado)
- ✅ `.env` está no `.gitignore` e nunca é enviado ao GitHub
- ✅ Código é público, suas chaves são privadas
- ❌ **Nunca** coloque a chave diretamente no código

## 📦 Estrutura do Projeto

```
youtube-summarizer/
├── app.py                  # Interface Streamlit
├── youtube_processor.py    # Lógica de processamento
├── requirements.txt        # Dependências Python
├── .env                    # Sua configuração (não commitar!)
├── .env.example            # Modelo do .env (público)
├── .gitignore              # Arquivos a ignorar (protege .env)
└── README.md               # Este arquivo
```

## 🐛 Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'streamlit'"

**Solução:**
```bash
# Certifique-se que o venv está ATIVADO
source venv/bin/activate  # Mac/Linux
# ou
venv\Scripts\activate  # Windows

# Depois instale:
pip install -r requirements.txt
```

### ❌ "FFmpeg not found"

**Windows:**
```bash
# Com Chocolatey:
choco install ffmpeg

# Ou baixe em: https://ffmpeg.org/download.html
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

### ❌ "GROQ_API_KEY not found"

**Solução:**
1. Verifique se você criou o arquivo `.env`
2. Verifique se `.env` contém sua chave real
3. Não use aspas: `GROQ_API_KEY=gsk_...` (sem `"`)
4. Reinicie o app depois de alterar `.env`

### ❌ "API Key inválida"

**Solução:**
1. Gere uma nova chave em https://console.groq.com
2. Atualize seu `.env`
3. Reinicie o app

### ❌ "Error 403 ao processar vídeo"

**Solução:**
1. Tente outro vídeo do YouTube
2. Verifique sua conexão com internet
3. Aguarde alguns minutos e tente novamente

## 📋 Requisitos do Sistema

- **Windows 10+**, **Mac OS 10.13+**, ou **Linux**
- **Python 3.8+** (verifique com `python --version`)
- **FFmpeg** (verifique com `ffmpeg -version`)
- **Internet** para acessar YouTube e Groq API

## 🎯 Próximos Passos (Opcional)

- [ ] Adicionar histórico de resumos
- [ ] Suporte para múltiplas URLs
- [ ] Exportar em PDF/DOCX
- [ ] Cache de vídeos processados

## 📝 Licença

MIT - Sinta-se livre para usar, modificar e distribuir.

## 🤝 Contribuições

Encontrou um bug? Tem uma sugestão? Abra uma [issue](https://github.com/seu-usuario/youtube-summarizer/issues)!

## 💬 Dúvidas?

- 📚 Documentação do Streamlit: https://docs.streamlit.io
- 🤖 Documentação da Groq API: https://console.groq.com/docs
- 🎥 PyTubeFix: https://github.com/Komo1119/PyTubeFix

---

Feito com ❤️ usando Streamlit + Groq

**Última atualização:** 2024
