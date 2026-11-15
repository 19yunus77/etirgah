import re, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment
from desc_data import G, SEASON_EN, D, UNKNOWN
from parse import load
B,_=load()
def tr(x,l): return x if l=='en' else G[x][0 if l=='ru' else 1]
def lst(xs,l,n=3):
    xs=[tr(x,l) for x in xs[:n]]
    if not xs: return ''
    if len(xs)==1: return xs[0]
    return ', '.join(xs[:-1])+{'en':' and ','ru':' и ','az':' və '}[l]+xs[-1]
WHO={'en':{'M':'for men','W':'for women','U':'for men and women'},
     'ru':{'M':'для мужчин','W':'для женщин','U':'для мужчин и женщин'},
     'az':{'M':'Kişilər üçün','W':'Qadınlar üçün','U':'Kişi və qadınlar üçün'}}
SEA={'en':{'ALL':'Versatile: suits any season, day or evening.','WARM':'At its best in spring and summer, during the day.','COLD':'Ideal for autumn, winter and evenings out.','COLDDAY':'Especially good in the cooler months.','SPRING':'Suits spring and autumn, especially in the daytime.'},
     'ru':{'ALL':'Универсален: подходит для любого сезона, днём и вечером.','WARM':'Лучше всего раскрывается весной и летом, в дневное время.','COLD':'Идеален для осени, зимы и вечерних выходов.','COLDDAY':'Особенно хорош в прохладное время года.','SPRING':'Подходит для весны и осени, особенно днём.'},
     'az':{'ALL':'Universaldır: istənilən fəsildə, gündüz və axşam uyğundur.','WARM':'Ən yaxşı yaz və yay aylarında, gündüz açılır.','COLD':'Payız, qış və axşam çıxışları üçün idealdır.','COLDDAY':'Xüsusilə sərin havalarda yaxşıdır.','SPRING':'Yaz və payız üçün, xüsusən gündüz uyğundur.'}}
def template(fam,top,heart,base,sea,g,l):
    t,h,b=lst(top,l),lst(heart,l,2),lst(base,l)
    if l=='en':
        s=f"{tr(fam,l).capitalize()} fragrance {WHO[l][g]}."
        parts=[]
        if t: parts.append(f"opens with {t}")
        if h: parts.append(f"reveals {h} in the heart")
        if b: parts.append(f"settles on {b}")
        if parts: s+=' It '+(', '.join(parts[:-1])+' and '+parts[-1] if len(parts)>1 else parts[0])+'.'
    elif l=='ru':
        f0=tr(fam,l); s=f"{f0[0]+f0[1:].lower()} аромат {WHO[l][g]}."
        parts=[]
        if t: parts.append(f"начало — {t}")
        if h: parts.append(f"в сердце — {h}")
        if b: parts.append(f"в базе — {b}")
        if parts: s+=' '+'; '.join(parts).capitalize()[0]+'; '.join(parts)[1:]+'.'
    else:
        s=f"{WHO[l][g]} {tr(fam,l).lower()} ətir."
        parts=[]
        if t: parts.append(f"açılışda {t}")
        if h: parts.append(f"ürəyində {h}")
        if b: parts.append(f"bazasında isə {b}")
        if parts: s+=' '+(', '.join(parts))[0].upper()+(', '.join(parts))[1:]+' hiss olunur.'
    return s+' '+SEA[l][sea]
def base(n):
    n=str(n).strip()
    while True:
        m=re.sub(r'\s*(\([^)]*\)|\*)\s*$','',n)
        if m==n: return n
        n=m
def build(src_path,out_path,sheet='Sheet1'):
    src=openpyxl.load_workbook(src_path).active
    wb=openpyxl.Workbook(); ws=wb.active; ws.title=sheet
    orig=[c.value for c in src[1]]
    L={'az':['Ailə','Üst notlar','Ürək notları','Baza notları','Mövsüm / vaxt','Təsvir'],
       'ru':['Семейство','Верхние ноты','Ноты сердца','Базовые ноты','Сезон / время','Описание'],
       'en':['Family','Top notes','Heart notes','Base notes','Season / time','Description']}
    hdr=orig+['Status']+[f'{h} ({x.upper()})' for x in ['az','ru','en'] for h in L[x]]
    ws.append(hdr)
    fills={'az':'DDEBF7','ru':'FCE4D6','en':'E2EFDA'}
    for i,h in enumerate(hdr,1):
        c=ws.cell(1,i); c.font=Font(name='Arial',bold=True); c.alignment=Alignment(wrap_text=True,vertical='top')
        if i>7: c.fill=PatternFill('solid',start_color=fills[['az','ru','en'][(i-8)//6]])
    yel=PatternFill('solid',start_color='FFFF00'); stats={}
    for r in range(2,src.max_row+1):
        v=[c.value for c in src[r]]; b=base(v[0]); g=v[2] if v[2] in ('M','W','U') else 'U'
        note=src.cell(r,6).comment
        if b in D:
            fam,top,heart,bas,sea,desc=D[b]; st='Əl ilə / вручную'
        elif b in B:
            fam,top,heart,bas,sea=B[b]; desc={l:template(fam,top,heart,bas,sea,g,l) for l in ['az','ru','en']}; st='Şablon / шаблон'
        else:
            st='Yoxlamaq / проверить'
        row=v+[st]
        if st.startswith('Yox'): row+=['']*18
        else:
            for l in ['az','ru','en']:
                row+=[tr(fam,l),', '.join(tr(x,l) for x in top),', '.join(tr(x,l) for x in heart),', '.join(tr(x,l) for x in bas),
                      SEASON_EN[sea] if l=='en' else tr(sea,l),desc[l]]
        ws.append(row); rr=ws.max_row; stats[st]=stats.get(st,0)+1
        for c in ws[rr]: c.font=Font(name='Arial'); c.alignment=Alignment(wrap_text=True,vertical='top')
        ws.cell(rr,4).number_format='#,##0.##'; ws.cell(rr,6).number_format='0.00'
        if st.startswith('Yox'):
            for c in ws[rr][:7]: c.fill=yel
        if note:
            ws.cell(rr,6).comment=Comment(note.text,'Claude')
            ws.cell(rr,6).fill=PatternFill('solid',start_color='F4B084')
    widths=[38,22,6,11,8,9,20]+[16,24,24,24,18,55]*3
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes='B2'; ws.auto_filter.ref=ws.dimensions
    wb.save(out_path); return stats
if __name__=='__main__':
    print(build('Anbar_perakende.xlsx','Anbar_tesvir.xlsx'))
