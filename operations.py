
class Operations(object):
    def __init__(self):
        self.word = None
        self.prediction = None
        self.word_loc = None
#Refresh fonksiyonunu verileri almak için kullanıyorum.
    def refresh(self, word, prediction):
        self.word = word
        self.prediction = prediction
        self.analyze()
#Analyze fonksiyonuna gelen veriler tahmin edilen harfin kelimede olup/olmadığını kontrol ediyor. Burada find fonksiyonu özelliğini kullanıyorum.
    def analyze(self):
        if self.word.find(self.prediction) == -1:
            return -1
#Harf kelimede bulunuyor ise görselleştirme yapmak üzere index numarasını main dosyamıza geri yolluyoruz.
        else:
            self.word_loc = self.word.find(self.prediction)
            return self.word_loc


