from CwnGraph import CwnBase
from CwnGraph import CwnImage
import json

cwn = CwnImage.latest()
# the original base data
# from CwnGraph import CwnImage
#cwn = CwnBase()

# for test begin
lemmas = cwn.find_lemma("漂亮")
for lemma in lemmas:
    senses = lemma.senses
    print('sense: ' + str(senses) + "\n")
    for sense in senses:
        print('sense: ' + sense.head_word  + "," + sense.pos + "\n")
        for synonym in sense.synonym:
            print('synonym: ' + str(synonym) + "," + synonym.head_word + "," + synonym.pos  + "\n" )
        for antonym in sense.antonym:
            print('antonym: ' + str(antonym) + "," + antonym.head_word + "," + antonym.pos  + "\n" )
# for test end            

lemmas = cwn.get_all_lemmas_jimmy()
count = 0
senseAry = []
for lemma in lemmas:
    #if count > 200 :
    #    break
    count = count + 1
    senses = lemma.senses
    for sense in senses:
        print('sense: ' + sense.head_word  + "," + sense.pos)
        senseObj = {}
        senseObj['word'] = sense.head_word
        senseObj['pos'] = sense.pos
        synonymAry = []
        for synonym in sense.synonym:
            if hasattr(synonym, 'head_word'):
                synonymAry.append(synonym.head_word);
                print('  synonym: ' + synonym.head_word)
                
        if len(synonymAry) > 0:
            senseObj['synonym'] = synonymAry
        antonymAry = []   
        for antonym in sense.antonym:
            if hasattr(antonym, 'head_word'):
                antonymAry.append(antonym.head_word);
                print('  antonym: ' + antonym.head_word)
        if len(antonymAry) > 0:
            senseObj['antonym'] = antonymAry
        senseAry.append(senseObj)
jsonFile = open('allword.json','w', encoding='utf8')
w = json.dumps(senseAry, ensure_ascii=False);
jsonFile.write(w)
jsonFile.close()
