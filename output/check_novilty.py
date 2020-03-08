trainset=set()
with open('../data/lenta.train.txt') as fin:
    for line in fin:
         trainset.add(line.strip()+' <eos>')

for _type in ['zero','cyclic','constant','linear','seqGAN','seqGAN-pre']:
    sentences=[]
    with open('{}.samples'.format(_type)) as fin:
        for line in fin:
            sentences.append(line.strip())    

    sentences=set(sentences[3:-10])
    novel=[s for s in sentences if s not in trainset]
    with open('{}.novel'.format(_type),'w') as fout:
        fout.write('\n'.join(novel))
    
    print('##',_type)
    print("Unique generated out of 10000",len(sentences)-1)
    print("Unique generated/ not in train set", len(novel)-1)
