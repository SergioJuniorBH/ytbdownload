YouTube Downloader
Este é um script em Python para baixar vídeos ou áudios do YouTube, incluindo playlists, de forma eficiente, utilizando a biblioteca yt-dlp. O script suporta até 10 downloads simultâneos e permite escolher entre salvar os arquivos como MP4 (vídeo) ou MP3 (música).
Funcionalidades

Baixa vídeos ou playlists do YouTube em formato de vídeo (MP4) ou áudio (MP3).
Escolha de formato: Permite selecionar entre vídeo (MP4) na máxima qualidade disponível ou áudio (MP3) com qualidade de 320 kbps.
Simultaneidade: Baixa até 10 arquivos ao mesmo tempo usando threads.
Salvamento organizado: Os arquivos são salvos em uma pasta específica chamada downloads.

Pré-requisitos
Antes de usar este script, instale os seguintes requisitos:

Python 3.7 ou superior.
yt-dlp: Para instalação, use o comando:pip install yt-dlp


FFmpeg: Necessário para a conversão de áudio e vídeo. Para instalar:
Linux: sudo apt update && sudo apt install ffmpeg


Windows: Baixe o FFmpeg e adicione ao PATH.
macOS: brew install ffmpeg





Como usar

Faça o download do arquivo youtube_downloader.py e salve-o localmente.
Execute o script no terminal:python youtube_downloader.py


Insira a URL do YouTube (vídeo individual ou playlist) quando solicitado:Insira a URL do YouTube (playlist ou vídeo): https://youtube.com/playlist?list=EXEMPLO


Escolha o formato desejado (1 para MP4 ou 2 para MP3) quando solicitado.
O script baixará os arquivos na pasta downloads.

Notas

Certifique-se de que a URL inserida seja válida (vídeo ou playlist pública do YouTube).
O script cria uma pasta chamada downloads na mesma localização do arquivo Python, onde os arquivos serão salvos.
Para vídeos, o script seleciona automaticamente a melhor qualidade disponível (vídeo + áudio combinados em MP4).
Para áudios, a qualidade é configurada para 320 kbps (máxima para MP3).

Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
