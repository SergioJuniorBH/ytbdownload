import os
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

# Cria a pasta para salvar os arquivos
output_folder = "playlist"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def download_audio(video_url):
    """
    Função para baixar um único áudio de vídeo do YouTube.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Download concluído: {video_url}")
    except Exception as e:
        print(f"Erro ao baixar {video_url}: {e}")

def download_playlist(playlist_url):
    """
    Baixa uma playlist do YouTube com até 10 downloads simultâneos.
    """
    ydl_opts = {'extract_flat': 'in_playlist', 'quiet': True}
    with YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

    # Obtem URLs dos vídeos da playlist
    video_urls = [video['url'] for video in playlist_info['entries']]

    # Limita a execução a 10 threads simultâneas
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_audio, video_urls)

if __name__ == "__main__":
    playlist_url = input("Insira a URL da playlist do YouTube: ")
    download_playlist(playlist_url)
