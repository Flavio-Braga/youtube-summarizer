# 🚀 YouTube Summarizer - Guia de Instalação

## Estrutura de Pastas

```
seu-projeto/
├── app.py                 # ← Arquivo principal do Streamlit
├── youtube_processor.py    # ← Lógica de processamento
├── requirements.txt        # ← Dependências
├── .env                    # ← Variáveis de ambiente (não commitar!)
├── .env.example            # ← Template do .env
└── README.md              # ← Documentação
```

---

## Passo 1: Clonar / Copiar Arquivos

Copie os arquivos `app.py` e `youtube_processor.py` para sua pasta do projeto.

---

## Passo 2: Configurar a API Key

### Opção A: Arquivo .env (RECOMENDADO)

1. Copie `.env.example` para `.env`
   ```bash
   cp .env.example .env
   ```

2. Abra `.env` e coloque sua API key:
   ```
   GROQ_API_KEY=gsk_sua_chave_aqui
   ```

3. **IMPORTANTE**: Nunca commit o `.env` no Git!
   Adicione ao `.gitignore`:
   ```
   .env
   *.wav
   resumo.md
   __pycache__/
   .streamlit/
   ```

---

## Passo 3: Instalar Dependências

### 1. Criar um ambiente virtual (RECOMENDADO)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar pacotes

```bash
pip install -r requirements.txt
```

### 3. Verificar FFmpeg

O FFmpeg precisa estar instalado no seu sistema:

**Windows (com Chocolatey):**
```bash
choco install ffmpeg
```

**Mac (com Homebrew):**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

---

## Passo 4: Rodar o Streamlit

```bash
streamlit run app.py
```

Isso abrirá automaticamente no navegador em `http://localhost:8501`

---

## 🔧 Solução de Problemas

### "Módulo não encontrado"
```bash
pip install --upgrade -r requirements.txt
```

### "FFmpeg não encontrado"
Instale ffmpeg conforme as instruções acima.

### "API Key inválida"
- Verifique se está em `.env` (não em aspas)
- Obtenha uma nova em: https://console.groq.com

### Porta 8501 já em uso
```bash
streamlit run app.py --server.port 8502
```

---

## 📦 Deploy (Opcional)

### Streamlit Cloud (GRÁTIS)

1. Suba seu código no GitHub
2. Vá para https://streamlit.io/cloud
3. Conecte seu repositório
4. Configure as variáveis de ambiente em "Secrets"

**Adicione em Secrets:**
```
GROQ_API_KEY = gsk_sua_chave
```

---

## 📝 Comando Rápido de Testes

Para testar se tudo está funcionando:

```bash
# Teste a importação
python -c "from youtube_processor import YouTubeProcessor; print('✅ Tudo OK!')"

# Execute o Streamlit
streamlit run app.py
```

---

## 🎯 Próximos Passos

- [ ] Adicionar histórico de resumos (banco de dados)
- [ ] Suporte para múltiplas URLs
- [ ] Temas de resumo personalizados
- [ ] Exportar em diferentes formatos (PDF, DOCX)
- [ ] Cache de vídeos já processados

---

Qualquer dúvida, me chama! 🚀
