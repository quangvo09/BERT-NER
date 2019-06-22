from bert import Ner

model = Ner("out/")

# output = model.predict("KD13921 RG19049640, 19049641")
output = model.predict("Rg.19048725 31.01.2019, 3.183,98")
for word in output:
    key, value = list(word.items())[0]
    if value['tag'] != 'O':
        print("%s %s" % (key, value['tag']))
