import pandas as pd
def load():
    u=pd.read_csv('unique.csv'); bases=set(u.base); brands=set(u.Qrup)
    data={}; unmatched=[]
    for f in ['bulk1.txt','bulk2.txt','bulk3.txt','bulk4.txt','bulk5.txt','bulk6.txt']:
        brand=None
        for line in open(f,encoding='utf8'):
            line=line.strip()
            if not line: continue
            if line.startswith('## '): brand=line[3:]; continue
            name,fam,top,heart,base,sea=line.split('|')
            full=name if name.lower().startswith(brand.lower()) and (name in bases) else f'{brand} {name}'
            if full not in bases and name in bases: full=name
            if full not in bases: unmatched.append(full); continue
            sp=lambda s:[x.strip() for x in s.split(',') if x.strip()]
            data[full]=(fam,sp(top),sp(heart),sp(base),sea)
    return data,unmatched
