import numpy as np
import pandas as pd
import random
from operations import Operations
from visual import Visual

#Lütfen açıklama dosyasını okuyunuz.
#Verilerimi programa dahil ettim ve veri uzunluğumu belirledim.

df = pd.read_excel("resource/turkish_dictionary.xls")
word = df['Words']
word_length = df['Word_Length']
df_length = len(df)

opt = Operations()
vis = Visual()


def hangman():

    store = []
    counter = 0

    num_of_letter = int(input("Harf sayısını giriniz: "))


    for i in range(0, df_length-1): # Seçtiğim harf sayısına denk gelen kelimelerin hepsini bir dizide topladım.
        if word_length[i] == num_of_letter:
            store_word = word[i]
            store.insert(counter, store_word)
            counter += 1

#Oluşturmuş olduğum dizinin index numaralarından herhangi biri için tahmin işlemi gerçekleştirdim.Böylece istediğim harf sayısına sahip rastgele bir kelime seçtim.
    storage_len = len(store)
    rand = random.randint(0, storage_len - 1)
    retained_word = store[rand]
    print(retained_word)
    vis.visuality(num_of_letter)
    guess(retained_word)

def guess(retained_word):
    right_of_guess = 10
    true_pre = 0

    while right_of_guess > 0: # Tahmin hakkımızın 10'dan geriye doğru azaldığı bir döngüye giriyoruz.
        prediction = input("Harf tahmin ediniz: ")

        opt.refresh(retained_word, prediction) #operation sınıfı altındaki refresh fonksiyonuna verilerimizi yolluyoruz.
        if opt.analyze() == -1:
            right_of_guess -= 1
            print("WRONG GUESS ! REMAINING GUESS:" + str(right_of_guess))
        else:

            if true_pre == len(retained_word) - 1:  #Doğru bilme sayımız harf sayısına eşit olduğunda kazanıyoruz. Eşitlik olmadığında doğru bilgiğimizi söyleyerek görselleştirme yapılıyor.
                print("YOU WIN!")
                exit()
            else:
                print("RIGHT GUESS !")

                vis_loc = opt.analyze() #Görselleştime işlemini gerçekleştirmek için visual sınıfı altında bulunan set ile verilerimi iletiyorum, get ile veriyi çekiyorum.
                vis.set(vis_loc, prediction)
                print(vis_loc)
                print(vis.get())
                true_pre += 1

    print("GAME OVER !") #Haklarımız bitip bilemediğimizde eleniyoruz.


if __name__ == '__main__':
    hangman()

