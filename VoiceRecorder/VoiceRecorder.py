import sounddevice as sd ## Ses kaydetmek ve çalmak için kullanılan bir kütüphane
import wavio #Ses verisini WAV formatında kaydetmek için kullanılan bir kütüphane
import  numpy as np

#Kayıt ayarları
frekans = 44100 #Bu , CD kalitesinde bir ses kaydetmek için standart bir frekans
sure = 4 #Kayıt süresi
ses_arttirma_katsayisi = 40 # Ses seviyesi ayarlama 1.5 2 gibi

print("Kayit Basliyor...")
ses_vericisi = sd.rec(int(sure*frekans), samplerate=frekans,channels=1,dtype='int16') #Mono Kayıt
#sd.rec -> Ses kaydını başlatan fonksiyon
#int(sure*frekans) -> Kaç örnek kaydedileceğini söyler örneğin 5 saniye boyunca 44100 kaydedeceğiz yani 220500 örnekk alınacak.
#samprlerate -> Frekans Ayarlaması
# Mono kaydı yaptık (streo olsaydı 2 olacaktı)
#dtype -> 16 bitlik formatta sesi kaydet.
sd.wait()# Kaydin tamamlanmasini bekle
print("Kayit Tamamlandi")

#ses verisi arttırma
ses_vericisi = np.clip(ses_vericisi*ses_arttirma_katsayisi,-32768,32767) # Maksimum ses seviyesini aşmamak için


wavio.write("win_sound.wav",ses_vericisi.astype(np.int16),frekans,sampwidth=2)
#"kayit.wav" -> kaydedilecek dosya adi
# ses_verisi -> kaydedilen ses
# frekans -> Ses frekansını belirledik.
#sampwidth -> 2 Bayt yani 16 bit olacak şekilde ayarladık.
print("Ses Kayiti 'kayit.wav' olarak kaydedildi.")