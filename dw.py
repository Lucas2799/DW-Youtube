from pytube import YouTube

URL= input('Digite a URl :')

YouTube = YouTube(URL)

print ('Titulo' + YouTube.title)

Video = YouTube.streams.get_highest_resolution()
Video.download()


