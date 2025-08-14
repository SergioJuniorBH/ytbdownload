import os
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

# Cria a pasta para salvar os arquivos
output_folder = "downloads"
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
            'preferredquality': '320',  # Máxima qualidade para MP3
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Download concluído: {video_url}")
    except Exception as e:
        print(f"Erro ao baixar {video_url}: {e}")

def download_video(video_url):
    """
    Função para baixar um único vídeo do YouTube na máxima qualidade.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Máxima qualidade de vídeo e áudio
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  # Garante que o arquivo final seja MP4
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Download concluído: {video_url}")
    except Exception as e:
        print(f"Erro ao baixar {video_url}: {e}")

def process_url(input_url):
    """
    Processa a URL fornecida, baixando uma playlist ou um vídeo individual.
    """
    # Pergunta ao usuário se deseja baixar como vídeo ou áudio
    while True:
        choice = input("Deseja baixar como [1] MP4 (vídeo) ou [2] MP3 (música)? Digite 1 ou 2: ").strip()
        if choice in ['1', '2']:
            break
        print("Opção inválida. Por favor, digite 1 para MP4 ou 2 para MP3.")

    is_playlist = "playlist?list=" in input_url

    if is_playlist:
        print("Detectado: URL de playlist. Processando...")
        ydl_opts = {'extract_flat': 'in_playlist', 'quiet': True}
        try:
            with YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(input_url, download=False)

            # Verifica se 'entries' existe no playlist_info
            if 'entries' not in playlist_info or not playlist_info['entries']:
                print("Erro: Não foi possível obter os vídeos da playlist. Verifique a URL ou se a playlist é pública.")
                print(f"Conteúdo de playlist_info: {playlist_info}")
                return

            # Obtém URLs dos vídeos da playlist
            video_urls = [video['url'] for video in playlist_info['entries']]
            print(f"Total de vídeos encontrados na playlist: {len(video_urls)}")

            # Limita a execução a 10 threads simultâneas
            with ThreadPoolExecutor(max_workers=10) as executor:
                if choice == '1':
                    executor.map(download_video, video_urls)
                else:
                    executor.map(download_audio, video_urls)

        except Exception as e:
            print(f"Erro ao processar a playlist: {e}")
    else:
        print("Detectado: URL de vídeo individual. Baixando...")
        try:
            if choice == '1':
                download_video(input_url)
            else:
                download_audio(input_url)
        except Exception as e:
            print(f"Erro ao processar o vídeo: {e}")

if __name__ == "__main__":
    input_url = input("Insira a URL do YouTube (playlist ou vídeo): ")
    if not input_url.strip():
        print("Erro: Nenhuma URL fornecida.")
    else:
        process_url(input_url)