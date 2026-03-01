import streamlit as st
import os
from youtube_processor import YouTubeProcessor
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #FF0000;
            text-align: center;
        }
        .success-box {
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
            padding: 1rem;
            border-radius: 0.5rem;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🎬 YouTube Summarizer")
st.markdown("Gere resumos automáticos de vídeos do YouTube com IA")
st.divider()

# Sidebar para configuração
with st.sidebar:
    st.header("⚙️ Configurações")
    
    # Verificar se API key existe
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        st.warning("⚠️ Chave da API Groq não configurada!")
        st.info("Adicione `GROQ_API_KEY` no seu arquivo `.env`")
    else:
        st.success("✅ API Groq conectada")
    
    st.markdown("---")
    st.markdown("### 📋 Como usar:")
    st.markdown("""
    1. Cole a URL do vídeo do YouTube
    2. Clique em 'Processar Vídeo'
    3. Aguarde a transcrição e geração do resumo
    4. Copie ou baixe o resultado
    """)

# Formulário principal
col1, col2 = st.columns([3, 1])

with col1:
    url = st.text_input(
        "🔗 URL do vídeo do YouTube:",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Cole aqui a URL completa do vídeo"
    )

with col2:
    processar = st.button("▶️ Processar", use_container_width=True, type="primary")

st.divider()

# Processamento
if processar:
    if not url:
        st.error("❌ Por favor, insira uma URL válida")
    elif not api_key:
        st.error("❌ API key não configurada. Adicione a chave no arquivo .env")
    else:
        try:
            processor = YouTubeProcessor(api_key)
            
            # Container com progresso
            with st.spinner("🔄 Processando vídeo..."):
                resultado = processor.processar_completo(url)
            
            if resultado["sucesso"]:
                # Informações do vídeo
                st.markdown("### 📺 Informações do Vídeo")
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"**Título:** {resultado['info']['titulo']}")
                    st.markdown(f"**Autor:** {resultado['info']['autor']}")
                    st.markdown(f"**Duração:** {resultado['info']['duracao']} segundos")
                
                with col2:
                    if resultado['info']['thumbnail']:
                        st.image(resultado['info']['thumbnail'], use_container_width=True)
                
                st.divider()
                
                # Resumo gerado
                st.markdown("### 📝 Resumo Gerado")
                st.markdown(resultado['descricao'])
                
                # Botões de ação
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.download_button(
                        label="📥 Baixar Resumo (MD)",
                        data=resultado['descricao'],
                        file_name="resumo.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                
                with col2:
                    st.download_button(
                        label="📥 Baixar Transcrição",
                        data=resultado['transcript'],
                        file_name="transcricao.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
                
                with col3:
                    if st.button("📋 Copiar para Área de Transferência", use_container_width=True):
                        st.info("✅ Use Ctrl+C após clicar no resumo acima para copiar")
                
                st.success("✅ Processamento concluído com sucesso!")
            
            else:
                st.error(f"❌ Erro ao processar: {resultado['erro']}")
        
        except Exception as e:
            st.error(f"❌ Erro inesperado: {str(e)}")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.9rem;">
    Desenvolvido com Streamlit, Groq e PyTubeFix | 
    <a href="https://groq.com" target="_blank">Groq API</a>
</div>
""", unsafe_allow_html=True)
