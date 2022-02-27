import numpy as np
class Visual(object):

    def __init__(self):
        self.visual = []
#Fonksiyon, başlangıç için belirlediğim harf sayısı kadar _ işareti kullanması ve bir dizi oluşturması için çalışır.
    def visuality(self, num_of_letter):
        for i in range(0, num_of_letter):
            self.visual.append("_")
#Tahmin edilen harf doğru ise bulunduğu index ve harf alınır. İndexin gösterdiği alana harf yazılır.
    def set(self, vis_loc, prediction):
        self.visual[vis_loc] = prediction
#Görsel main dosyasına geri döndürülür.
    def get(self):
        return np.array(self.visual)