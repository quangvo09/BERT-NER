from bert import Ner

model = Ner("out/")

output = model.predict("KD13921 RG19049640, 19049641")

print(output)