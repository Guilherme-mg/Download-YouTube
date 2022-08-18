from pytube import YouTube
import os

print('-=' * 10, 'Download de video do YouTube', '-=' * 10)
print('Os downloads serão salvos na área de trabalho e no formato MP4 ou MP3.')
print('-=' * 35)


#  Faz o download do vídeo.
def video(link):
    try:
        user = os.getlogin()
        YouTube(link).streams.get_highest_resolution().download(f'C:\\Users\\{user}\\Desktop')
        print('\033[32mDownload realizado com sucesso!\033[m')
        print('-=' * 35)
    except:
        print('\033[31mErro ao realizar o download.\033[m')
        print('-=' * 35)


#  Faz o download somente do áudio e transforma em MP3.
def audio(link):
    try:
        user = os.getlogin()
        somente_audio = YouTube(link).streams.filter(only_audio=True).first()
        arquivo = somente_audio.download(output_path=f'C:\\Users\\{user}\\Desktop')
        base, ext = os.path.splitext(arquivo)
        novo_arquivo = base + '.mp3'
        os.rename(arquivo, novo_arquivo)
        print('\033[32mDownload realizado com sucessso!\033[m')
        print('-=' * 35)
    except:
        print('\033[31mErro ao realizar o download.\033[m')
        print('-=' * 35)


while True:
    resp = str(input('Selecione a opção: \n[ 1 ] - Video \n[ 2 ] - Áudio \n[ 3 ] - Sair \nR:'))
    if resp not in '123':
        print('\033[31mComando inválido, tente novamente\033[m')
        print('-=' * 35)
    if resp == '1':
        url = input('Insira a URL do video (Digite fim para sair): ')
        if url in 'Fimfim':
            break
        else:
            video(url)
    elif resp == '2':
        url = input('Insira a URL do video (Digite fim para sair): ')
        if 'fim' in url.lower():
            break
        else:
            audio(url)
    elif resp == '3':
        print('Finalizando...')
        break
