info = audioinfo("/Users/gabriel/Desktop/PROJETOS/GuitarHero/Musics/frantic.mp3")

samples = info.TotalSamples
samplerate = info.SampleRate


[M,fs] = audioread("/Users/gabriel/Desktop/PROJETOS/GuitarHero/Musics/frantic.mp3")

data_fft = fft(M);
plot(abs(data_fft(:,1)))
