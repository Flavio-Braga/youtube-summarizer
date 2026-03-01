import pytubefix
import subprocess
import imageio_ffmpeg
from groq import Groq
import os
from pathlib import Path
import tempfile


class YouTubeProcessor:
    def __init__(self, groq_api_key: str):
        """Inicializa o processador com a chave da API Groq"""
        self.client = Groq(api_key=groq_api_key)
        self.temp_dir = tempfile.gettempdir()
    
    def obter_info_video(self, url: str) -> dict:
        """Extrai informações básicas do vídeo"""
        try:
            yt = pytubefix.YouTube(url)
            return {
                "titulo": yt.title,
                "thumbnail": yt.thumbnail_url,
                "duracao": yt.length,
                "autor": yt.author
            }
        except Exception as e:
            raise Exception(f"Erro ao obter informações do vídeo: {str(e)}")
    
    def baixar_audio(self, url: str) -> str:
        """Baixa o áudio do YouTube, comprime e retorna o caminho do arquivo"""
        try:
            yt = pytubefix.YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            
            if not stream:
                raise Exception("Nenhum stream de áudio encontrado")
            
            # Usa arquivo temporário comprimido
            audio_path = os.path.join(self.temp_dir, "audio_temp.wav")
            
            # Obtém o caminho do ffmpeg via imageio_ffmpeg
            ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
            
            # Executa ffmpeg com compressão
            subprocess.run([
                ffmpeg_path,
                "-i", stream.url,
                "-f", "wav",
                "-ar", "16000",      # reduz sample rate para 16kHz (suficiente para voz)
                "-ac", "1",          # converte para mono (1 canal)
                "-b:a", "64k",       # bitrate de 64k (menor tamanho)
                "-loglevel", "error",
                "-y", audio_path
            ], check=True)
            
            return audio_path
        except Exception as e:
            raise Exception(f"Erro ao baixar áudio: {str(e)}")
    
    def transcrever_audio(self, audio_path: str) -> str:
        """Transcreve o áudio usando Groq Whisper"""
        try:
            with open(audio_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-large-v3-turbo",
                    file=audio_file
                ).text
            
            return transcript
        except Exception as e:
            raise Exception(f"Erro na transcrição: {str(e)}")
    
    def gerar_descricao(self, transcript: str) -> str:
        """Gera descrição usando LLM da Groq"""
        try:
            completion = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "Você é um assistente que resume vídeos detalhadamente em português. Responda com formatação Markdown bem estruturada."
                    },
                    {
                        "role": "user",
                        "content": f"Descreva o seguinte vídeo de forma detalhada, organizado e bem estruturado:\n\n{transcript}"
                    }
                ]
            )
            
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Erro ao gerar descrição: {str(e)}")
    
    def processar_completo(self, url: str) -> dict:
        """Processa a URL completa e retorna todas as informações"""
        try:
            # Obter informações
            info = self.obter_info_video(url)
            
            # Baixar áudio
            audio_path = self.baixar_audio(url)
            
            # Transcrever
            transcript = self.transcrever_audio(audio_path)
            
            # Gerar descrição
            descricao = self.gerar_descricao(transcript)
            
            # Limpar arquivo temporário
            if os.path.exists(audio_path):
                os.remove(audio_path)
            
            return {
                "sucesso": True,
                "info": info,
                "transcript": transcript,
                "descricao": descricao
            }
        except Exception as e:
            return {
                "sucesso": False,
                "erro": str(e)
            }
