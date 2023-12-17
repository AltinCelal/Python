########################################################################
# LİSTELER
########################################################################

# - değiştirilebilir.
# - sıralıdır , index işlemleri yapılabilir.
# - kapsayıcıdır

#listenin_ismi =['listeye eklenecek değerler'] 

notes = [1,2,3,4]
type(notes)

names=["a","b","v","d"]

not_nam=[1, 2, 3, 4, "a","b","c","d", True,[1,2,3]]#10 elmanlı,kapsayıcıdır(farklı veri türleri aynı listede tutulabilir)

not_nam[9][1]#index işlemleri yapılabilir

type(not_nam)
type(not_nam[9][1])

not_nam[0]=99#değiştirilebilir
not_nam

dir(list)#listeler için kullanılabilecek metotları gösterir.

notes.append(100)#listenin sonuna 100 ekler.

notes.remove(3)# 3 değerini notes isimli listeden siler


names.pop(1)#verilen indexdeki değeri siler

names.insert(0,'Ali')#verilen indexe değer ekleme.