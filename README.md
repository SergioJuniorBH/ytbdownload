
# YouTube Playlist Downloader

Este é um script em Python para baixar playlists de áudio do YouTube de forma eficiente, utilizando a biblioteca **yt-dlp**. O script suporta até 10 downloads simultâneos, facilitando o processo de baixar múltiplos áudios de uma playlist.

## Funcionalidades
- **Baixa playlists completas do YouTube** em formato de áudio.
- **Simultaneidade**: Baixa até 10 áudios ao mesmo tempo usando threads.
- **Conversão automática** para o formato MP3 com qualidade de 192 kbps.
- **Salvamento organizado**: Os arquivos são salvos em uma pasta específica chamada `playlist`.

Pré-requisitos
Antes de usar este script, instale os seguintes requisitos:

1. **Python 3.7 ou superior**.
2. **yt-dlp**: Para instalação, use o comando:
   ```bash
   pip install yt-dlp
   ```
3. **FFmpeg**: Necessário para a conversão de áudio. Para instalar:
   - **Linux**: 
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **Windows**: [Baixe o FFmpeg](https://ffmpeg.org/download.html) e adicione ao PATH.
   - **macOS**: 
     ```bash
     brew install ffmpeg
     ```

## Como usar
1. Faça o download do arquivo `download.py` e salve-o localmente.
2. Execute o script no terminal:
   ```bash
   python download.py
   ```
3. Insira a URL da playlist do YouTube quando solicitado:
   ```
   Insira a URL da playlist do YouTube: https://youtube.com/playlist?list=EXEMPLO
   ```
4. O script baixará os arquivos na pasta `playlist`.

## Notas
- Certifique-se de que a URL inserida seja de uma playlist válida do YouTube.
- O script cria uma pasta chamada `playlist` na mesma localização do arquivo Python, onde os áudios serão salvos.

## Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.