# Glossary: note / family / season -> (ru, az)
G = {
 # notes
 'bergamot':('бергамот','berqamot'),'pepper':('перец','istiot'),'Sichuan pepper':('сычуаньский перец','Siçuan istiotu'),
 'pink pepper':('розовый перец','çəhrayı istiot'),'lavender':('лаванда','lavanda'),'vetiver':('ветивер','vetiver'),
 'patchouli':('пачули','paçuli'),'geranium':('герань','ətirşah'),'ambroxan':('амброксан','ambroksan'),
 'cedar':('кедр','sidr'),'labdanum':('лабданум','labdanum'),'grapefruit':('грейпфрут','qreypfrut'),
 'lemon':('лимон','limon'),'mint':('мята','nanə'),'ginger':('имбирь','zəncəfil'),'nutmeg':('мускатный орех','muskat qozu'),
 'jasmine':('жасмин','jasmin'),'melon':('дыня','yemiş'),'incense':('ладан','buxur'),'amber':('амбра','kəhrəba'),
 'sandalwood':('сандал','səndəl ağacı'),'white musk':('белый мускус','ağ müşk'),'musk':('мускус','müşk'),
 'pineapple':('ананас','ananas'),'iris':('ирис','süsən'),'hyacinth':('гиацинт','sümbül'),'vanilla':('ваниль','vanil'),
 'orange':('апельсин','portağal'),'mandarin':('мандарин','mandarin'),'orange blossom':('цветок апельсина','portağal çiçəyi'),
 'rose':('роза','qızılgül'),'mimosa':('мимоза','mimoza'),'ylang-ylang':('иланг-иланг','ilanq-ilanq'),'tonka bean':('бобы тонка','tonka paxlası'),
 'truffle':('трюфель','trüfel'),'blackcurrant':('чёрная смородина','qara qarağat'),'gardenia':('гардения','qardeniya'),
 'orchid':('орхидея','orxideya'),'spices':('специи','ədviyyatlar'),'dark chocolate':('тёмный шоколад','tünd şokolad'),
 'black cherry':('чёрная вишня','qara albalı'),'cherry liqueur':('вишнёвый ликёр','albalı likörü'),'bitter almond':('горький миндаль','acı badam'),
 'Peru balsam':('перуанский бальзам','Peru balzamı'),'cinnamon':('корица','darçın'),'tobacco leaf':('табачный лист','tütün yarpağı'),
 'cacao':('какао','kakao'),'dried fruits':('сухофрукты','quru meyvələr'),'woody notes':('древесные ноты','odunsu notlar'),
 'rosewood':('розовое дерево','gül ağacı'),'cardamom':('кардамон','hil'),'oud':('уд','ud ağacı'),
 'apple':('яблоко','alma'),'birch':('берёза','tozağacı'),'oakmoss':('дубовый мох','palıd mamırı'),'ambergris':('серая амбра','ənbər'),
 'lychee':('личи','liçi'),'rhubarb':('ревень','rəvənd'),'peony':('пион','pion'),'cashmeran':('кашмеран','kaşmeran'),
 'violet':('фиалка','bənövşə'),'guaiac wood':('гваяковое дерево','qvayak ağacı'),'lime':('лайм','laym'),'sea notes':('морские ноты','dəniz notları'),
 'neroli':('нероли','neroli'),'peach':('персик','şaftalı'),'freesia':('фрезия','freziya'),'rosemary':('розмарин','rozmarin'),
 'pear':('груша','armud'),'coffee':('кофе','qəhvə'),'licorice':('лакрица','biyan'),'almond':('миндаль','badam'),
 'tuberose':('тубероза','tüberoza'),'praline':('пралине','pralin'),'saffron':('шафран','zəfəran'),'amberwood':('амбровое дерево','kəhrəba ağacı'),
 'fir resin':('смола пихты','küknar qatranı'),'bellflower':('колокольчик','zəngçiçəyi'),'bamboo':('бамбук','bambuk'),'white rose':('белая роза','ağ qızılgül'),
 'bay leaf':('лавровый лист','dəfnə yarpağı'),'leather':('кожа','dəri'),'raspberry':('малина','moruq'),'honey':('мёд','bal'),
 'passion fruit':('маракуйя','çarxıfələk meyvəsi'),'strawberry':('клубника','çiyələk'),'red berries':('красные ягоды','qırmızı giləmeyvələr'),
 'lily of the valley':('ландыш','inciçiçəyi'),'suede':('замша','zamşa'),'Iso E Super':('Iso E Super','Iso E Super'),
 'coconut':('кокос','hindistan cevizi'),'plum':('слива','gavalı'),'apricot':('абрикос','ərik'),'caraway':('тмин','ziyirə'),
 'yuzu':('юдзу','yuzu'),'pomegranate':('гранат','nar'),'lotus':('лотос','lotus'),'magnolia':('магнолия','maqnoliya'),
 'mahogany':('красное дерево','qırmızı ağac'),'fruity notes':('фруктовые ноты','meyvəli notlar'),'carnation':('гвоздика','qərənfil'),
 'white pepper':('белый перец','ağ istiot'),'honeysuckle':('жимолость','doqquzdon'),'violet leaf':('лист фиалки','bənövşə yarpağı'),
 # families
 'Aromatic Fougère':('Ароматический фужерный','Aromatik fujer'),'Woody Aromatic':('Древесный ароматический','Odunsu-aromatik'),
 'Floral Chypre':('Цветочный шипровый','Çiçəkli şipr'),'Oriental Floral':('Восточный цветочный','Şərq çiçəkli'),
 'Oriental Gourmand':('Восточный гурманский','Şərq qurman'),'Oriental Spicy':('Восточный пряный','Şərq ədviyyatlı'),
 'Woody':('Древесный','Odunsu'),'Fruity Chypre':('Фруктовый шипровый','Meyvəli şipr'),'Floral Fruity':('Цветочный фруктовый','Çiçəkli-meyvəli'),
 'Amber Spicy':('Амбровый пряный','Kəhrəba-ədviyyatlı'),'Aromatic Aquatic':('Ароматический водный','Aromatik dəniz'),
 'Oriental Vanilla':('Восточный ванильный','Şərq vanilli'),'Amber Floral':('Амбровый цветочный','Kəhrəba-çiçəkli'),
 'Woody Aquatic':('Древесный водный','Odunsu-dəniz'),'Spicy Leather':('Пряный кожаный','Ədviyyatlı dəri'),'Floral Woody':('Цветочный древесный','Çiçəkli-odunsu'),
 'Woody Leather':('Древесный кожаный','Odunsu dəri'),'Woody Amber':('Древесный амбровый','Odunsu-kəhrəba'),'Citrus Fruity':('Цитрусовый фруктовый','Sitrus-meyvəli'),
 # seasons
 'ALL':('Всесезонный; день и вечер','Bütün fəsillər; gündüz və axşam'),'WARM':('Весна–лето; день','Yaz–yay; gündüz'),
 'COLD':('Осень–зима; вечер','Payız–qış; axşam'),'COLDDAY':('Осень–зима; день и вечер','Payız–qış; gündüz və axşam'),
 'SPRING':('Весна–осень; день','Yaz–payız; gündüz'),
}
SEASON_EN = {'ALL':'All seasons; day & evening','WARM':'Spring–summer; daytime','COLD':'Autumn–winter; evening',
             'COLDDAY':'Autumn–winter; day & evening','SPRING':'Spring–autumn; daytime'}

# base name -> (family, top, heart, base, season, {en, ru, az} description)
D = {
'Christian Dior Sauvage': ('Aromatic Fougère',['bergamot','pepper'],['Sichuan pepper','lavender','pink pepper','geranium','vetiver','patchouli'],['ambroxan','cedar','labdanum'],'ALL',{
 'en':'A bold, fresh-spicy fragrance with a juicy bergamot opening and a powerful ambroxan trail. A versatile choice for a confident man, for every day and evenings out.',
 'ru':'Смелый свежо-пряный аромат с сочным бергамотом в начале и мощным шлейфом амброксана. Универсальный выбор для уверенного мужчины — на каждый день и на вечер.',
 'az':'Şirəli berqamotla açılan və güclü ambroksan izi buraxan cəsur, təravətli-ədviyyatlı ətir. Özünə inamlı kişi üçün universal seçim — hər gün və axşam üçün.'}),
'Chanel Bleu de Chanel': ('Woody Aromatic',['grapefruit','lemon','mint','pink pepper'],['ginger','nutmeg','jasmine','melon'],['incense','cedar','sandalwood','amber'],'ALL',{
 'en':'Elegant woody-aromatic scent: citrus freshness over a smooth base of incense and sandalwood. Works equally well in the office and on a date.',
 'ru':'Элегантный древесно-ароматический парфюм: цитрусовая свежесть на мягкой базе из ладана и сандала. Одинаково хорош в офисе и на свидании.',
 'az':'Zərif odunsu-aromatik ətir: buxur və səndəl ağacından ibarət yumşaq baza üzərində sitrus təravəti. Ofisdə də, görüşdə də eyni dərəcədə yaxşıdır.'}),
'Chanel Chance': ('Floral Chypre',['pink pepper','lemon','pineapple'],['jasmine','hyacinth','iris'],['patchouli','vanilla','white musk','vetiver'],'ALL',{
 'en':'A bright, playful floral with a hint of pepper and a soft musky-patchouli base. A cheerful everyday fragrance for women of any age.',
 'ru':'Яркий, игривый цветочный аромат с ноткой перца и мягкой мускусно-пачулиевой базой. Жизнерадостный парфюм на каждый день для женщин любого возраста.',
 'az':'İstiot çaları və yumşaq müşk-paçuli bazası olan parlaq, şux çiçəkli ətir. İstənilən yaşda qadınlar üçün gündəlik şən ətir.'}),
'Chanel Coco Mademoiselle': ('Floral Chypre',['orange','mandarin','bergamot'],['rose','jasmine','mimosa','ylang-ylang'],['patchouli','white musk','vanilla','vetiver'],'ALL',{
 'en':'A modern classic: sparkling citrus, a rose-jasmine heart and a sensual patchouli trail. Feminine and refined, suitable for any occasion.',
 'ru':'Современная классика: искристые цитрусы, сердце из розы и жасмина и чувственный шлейф пачули. Женственный и утончённый, подходит для любого случая.',
 'az':'Müasir klassika: parlaq sitruslar, qızılgül və jasmin ürəyi, həssas paçuli izi. Qadınsı və incə, istənilən hal üçün uyğundur.'}),
'Tom Ford Black Orchid': ('Oriental Floral',['truffle','ylang-ylang','bergamot','blackcurrant'],['orchid','spices','fruity notes'],['patchouli','incense','vanilla','dark chocolate','sandalwood'],'COLD',{
 'en':'Dark, luxurious and mysterious: black orchid with truffle, chocolate and incense. A rich evening scent for those who love to stand out.',
 'ru':'Тёмный, роскошный и загадочный: чёрная орхидея с трюфелем, шоколадом и ладаном. Насыщенный вечерний аромат для тех, кто любит выделяться.',
 'az':'Tünd, dəbdəbəli və sirli: trüfel, şokolad və buxurla qara orxideya. Seçilməyi sevənlər üçün zəngin axşam ətri.'}),
'Tom Ford Lost Cherry': ('Oriental Gourmand',['black cherry','cherry liqueur','bitter almond'],['rose','jasmine'],['Peru balsam','tonka bean','sandalwood','vetiver','cinnamon'],'COLDDAY',{
 'en':'Juicy black cherry and cherry liqueur with almond and warm tonka. A sweet, seductive gourmand that leaves a memorable trail.',
 'ru':'Сочная чёрная вишня и вишнёвый ликёр с миндалём и тёплыми бобами тонка. Сладкий, соблазнительный гурманский аромат с запоминающимся шлейфом.',
 'az':'Badam və isti tonka ilə şirəli qara albalı və albalı likörü. Yaddaqalan iz buraxan şirin, cazibədar qurman ətir.'}),
'Tom Ford Tobacco Vanille': ('Oriental Spicy',['tobacco leaf','spices'],['vanilla','cacao','tonka bean'],['dried fruits','woody notes'],'COLD',{
 'en':'Warm and enveloping: tobacco leaf, creamy vanilla, cocoa and dried fruits. A cosy, rich scent for cold evenings.',
 'ru':'Тёплый и обволакивающий: табачный лист, сливочная ваниль, какао и сухофрукты. Уютный, насыщенный аромат для холодных вечеров.',
 'az':'İsti və bürüyən: tütün yarpağı, kremli vanil, kakao və quru meyvələr. Soyuq axşamlar üçün rahat, zəngin ətir.'}),
'Tom Ford Oud Wood': ('Woody',['rosewood','cardamom','pepper'],['oud','sandalwood','vetiver'],['tonka bean','vanilla','amber'],'COLDDAY',{
 'en':'A smooth, polished oud softened by sandalwood, cardamom and vanilla. Noble and calm — a great introduction to oud fragrances.',
 'ru':'Мягкий, отшлифованный уд, смягчённый сандалом, кардамоном и ванилью. Благородный и спокойный — отличное знакомство с ароматами уда.',
 'az':'Səndəl ağacı, hil və vanillə yumşaldılmış zərif ud. Nəcib və sakit — ud ətirləri ilə tanışlıq üçün əla seçim.'}),
'Creed Aventus': ('Fruity Chypre',['pineapple','bergamot','blackcurrant','apple'],['birch','patchouli','jasmine','rose'],['musk','oakmoss','ambergris','vanilla'],'ALL',{
 'en':'The legendary "scent of success": juicy pineapple with a smoky birch accord and a musky base. Confident, charismatic and long-lasting.',
 'ru':'Легендарный «аромат успеха»: сочный ананас с дымным аккордом берёзы и мускусной базой. Уверенный, харизматичный и стойкий.',
 'az':'Əfsanəvi "uğur ətri": tüstülü tozağacı akkordu və müşk bazası ilə şirəli ananas. İnamlı, xarizmatik və davamlı.'}),
'Parfums de Marly Delina': ('Floral Fruity',['lychee','rhubarb','bergamot','nutmeg'],['rose','peony','vanilla'],['cashmeran','incense','cedar','vetiver'],'SPRING',{
 'en':'A romantic bouquet of Turkish rose and peony with juicy lychee and rhubarb. Tender, bright and very feminine.',
 'ru':'Романтичный букет турецкой розы и пиона с сочными личи и ревенём. Нежный, яркий и очень женственный.',
 'az':'Şirəli liçi və rəvəndlə türk qızılgülü və piondan romantik buket. İncə, parlaq və çox qadınsı.'}),
'Parfums de Marly Layton': ('Amber Spicy',['apple','lavender','bergamot','mandarin'],['geranium','violet','jasmine'],['vanilla','cardamom','sandalwood','pepper','patchouli','guaiac wood'],'COLDDAY',{
 'en':'Fresh apple and lavender over a warm base of vanilla, cardamom and woods. An elegant, crowd-pleasing scent with excellent projection.',
 'ru':'Свежее яблоко и лаванда на тёплой базе из ванили, кардамона и древесины. Элегантный аромат, который нравится всем, с отличным шлейфом.',
 'az':'Vanil, hil və odunsu notlardan isti baza üzərində təzə alma və lavanda. Hamının xoşuna gələn, gözəl iz buraxan zərif ətir.'}),
'Giorgio Armani Acqua di Gio': ('Aromatic Aquatic',['lime','lemon','bergamot','neroli'],['sea notes','jasmine','peach','freesia','rosemary'],['white musk','cedar','oakmoss','patchouli'],'WARM',{
 'en':'A timeless aquatic classic: citrus, sea breeze and light florals. Clean and refreshing — perfect for hot summer days.',
 'ru':'Вечная морская классика: цитрусы, морской бриз и лёгкие цветы. Чистый и освежающий — идеален для жарких летних дней.',
 'az':'Əbədi dəniz klassikası: sitruslar, dəniz mehi və yüngül çiçəklər. Təmiz və sərinləşdirici — isti yay günləri üçün ideal.'}),
'Giorgio Armani Si Armani': ('Fruity Chypre',['blackcurrant'],['rose','freesia'],['vanilla','patchouli','ambroxan','woody notes'],'ALL',{
 'en':'Blackcurrant nectar with rose and a soft vanilla-patchouli base. Elegant and modern — for a strong, graceful woman.',
 'ru':'Нектар чёрной смородины с розой и мягкой ванильно-пачулиевой базой. Элегантный и современный — для сильной и изящной женщины.',
 'az':'Qızılgül və yumşaq vanil-paçuli bazası ilə qara qarağat nektarı. Zərif və müasir — güclü və incə qadın üçün.'}),
'Yves Saint Laurent (YSL) Black Opium': ('Oriental Vanilla',['pear','pink pepper','orange blossom'],['coffee','jasmine','bitter almond','licorice'],['vanilla','patchouli','cedar'],'COLD',{
 'en':'An addictive mix of black coffee, white flowers and vanilla. A bold, sweet evening scent with a rock-chic character.',
 'ru':'Притягательное сочетание чёрного кофе, белых цветов и ванили. Смелый сладкий вечерний аромат с характером рок-шик.',
 'az':'Qara qəhvə, ağ çiçəklər və vanilin cəlbedici birləşməsi. Rok-şik xarakterli cəsur, şirin axşam ətri.'}),
'Caroline Herrera (CH) Good Girl': ('Oriental Floral',['almond','coffee','bergamot','lemon'],['tuberose','jasmine','orange blossom','rose'],['tonka bean','cacao','vanilla','praline','sandalwood'],'COLD',{
 'en':'Contrasting and seductive: white tuberose and jasmine with dark notes of cocoa and tonka. For a woman who is both sweet and daring.',
 'ru':'Контрастный и соблазнительный: белая тубероза и жасмин с тёмными нотами какао и тонки. Для женщины, которая одновременно нежная и дерзкая.',
 'az':'Kontrastlı və cazibədar: kakao və tonkanın tünd notları ilə ağ tüberoza və jasmin. Eyni zamanda həm incə, həm cəsur qadın üçün.'}),
'M. F. Kurkdijian Baccarat Rouge 540': ('Amber Floral',['saffron','jasmine'],['amberwood','ambergris'],['fir resin','cedar'],'ALL',{
 'en':'An iconic airy-amber scent with saffron, jasmine and a crystalline woody trail. Recognisable from a distance and incredibly long-lasting.',
 'ru':'Культовый воздушно-амбровый аромат с шафраном, жасмином и кристальным древесным шлейфом. Узнаётся издалека и невероятно стоек.',
 'az':'Zəfəran, jasmin və kristal kimi odunsu izlə ikonik, havadar kəhrəba ətri. Uzaqdan tanınır və inanılmaz dərəcədə davamlıdır.'}),
'Dolce & Gabbana Light Blue': ('Floral Fruity',['lemon','apple','cedar','bellflower'],['bamboo','jasmine','white rose'],['cedar','musk','amber'],'WARM',{
 'en':'Sicilian lemon and crisp apple with a light floral heart — the scent of a Mediterranean summer. Fresh, easy and joyful.',
 'ru':'Сицилийский лимон и хрустящее яблоко с лёгким цветочным сердцем — аромат средиземноморского лета. Свежий, лёгкий и радостный.',
 'az':'Siciliya limonu və xırtıldayan alma, yüngül çiçəkli ürək — Aralıq dənizi yayının ətri. Təravətli, yüngül və şən.'}),
'Paco Rabanne Invictus': ('Woody Aquatic',['grapefruit','sea notes','mandarin'],['bay leaf','jasmine'],['ambergris','guaiac wood','oakmoss','patchouli'],'WARM',{
 'en':'Sporty and energetic: grapefruit and sea notes over a woody-amber base. A fresh scent for active men.',
 'ru':'Спортивный и энергичный: грейпфрут и морские ноты на древесно-амбровой базе. Свежий аромат для активных мужчин.',
 'az':'İdmanlı və enerjili: odunsu-kəhrəba bazası üzərində qreypfrut və dəniz notları. Aktiv kişilər üçün təravətli ətir.'}),
'Paco Rabanne 1 Million': ('Spicy Leather',['grapefruit','mint','mandarin'],['rose','cinnamon','spices'],['leather','amber','woody notes','patchouli'],'COLD',{
 'en':'A warm, spicy scent of cinnamon, leather and amber with a fresh citrus start. Noticeable and charismatic, ideal for evenings.',
 'ru':'Тёплый пряный аромат корицы, кожи и амбры со свежим цитрусовым началом. Заметный и харизматичный, идеален для вечера.',
 'az':'Təravətli sitrus başlanğıcı ilə darçın, dəri və kəhrəbanın isti, ədviyyatlı ətri. Diqqət çəkən və xarizmatik, axşam üçün ideal.'}),
'Paco Rabanne Lady Million': ('Floral Woody',['raspberry','neroli','lemon'],['jasmine','orange blossom','gardenia'],['honey','patchouli','amber'],'COLDDAY',{
 'en':'Raspberry and neroli with sparkling white flowers and a honeyed patchouli base. Glamorous and radiant.',
 'ru':'Малина и нероли с искрящимися белыми цветами и медово-пачулиевой базой. Гламурный и сияющий аромат.',
 'az':'Parlaq ağ çiçəklər və ballı paçuli bazası ilə moruq və neroli. Qlamurlu və işıltılı ətir.'}),
'Victoria’s Secret Bombshell': ('Floral Fruity',['passion fruit','grapefruit','pineapple','strawberry'],['peony','orchid','red berries','jasmine'],['musk','woody notes','oakmoss'],'WARM',{
 'en':'A juicy cocktail of passion fruit and berries with peony. Light, flirty and youthful — great for every day.',
 'ru':'Сочный коктейль из маракуйи и ягод с пионом. Лёгкий, кокетливый и молодёжный — отлично на каждый день.',
 'az':'Pionla çarxıfələk meyvəsi və giləmeyvələrdən şirəli kokteyl. Yüngül, şux və gənc — gündəlik üçün əla.'}),
'Lacoste L.12.12 Blanc': ('Woody Aromatic',['grapefruit','rosemary','cardamom'],['tuberose','ylang-ylang'],['cedar','suede','vetiver'],'WARM',{
 'en':'Clean and minimalist, like a crisp white polo shirt: grapefruit, cardamom and cedar. A light everyday scent.',
 'ru':'Чистый и минималистичный, как свежая белая рубашка-поло: грейпфрут, кардамон и кедр. Лёгкий аромат на каждый день.',
 'az':'Təzə ağ polo köynək kimi təmiz və minimalist: qreypfrut, hil və sidr. Gündəlik yüngül ətir.'}),
'Molecule 01 Escentric': ('Woody',[],['Iso E Super'],[],'ALL',{
 'en':'Built on a single molecule, Iso E Super: a soft, velvety woody aura that blends with your skin and smells different on everyone.',
 'ru':'Построен на одной молекуле — Iso E Super: мягкая бархатистая древесная аура, которая сливается с кожей и звучит на каждом по-своему.',
 'az':'Tək bir molekul — Iso E Super üzərində qurulub: dəri ilə birləşən və hər kəsdə fərqli səslənən yumşaq, məxməri odunsu aura.'}),
'Christian Dior Hypnotic Poison': ('Oriental Vanilla',['coconut','plum','apricot'],['jasmine','tuberose','rose','caraway'],['vanilla','almond','sandalwood','musk'],'COLD',{
 'en':'Hypnotic almond and vanilla with jasmine and a hint of caraway. A sensual, enveloping evening scent.',
 'ru':'Гипнотический миндаль и ваниль с жасмином и ноткой тмина. Чувственный, обволакивающий вечерний аромат.',
 'az':'Yasəmən və ziyirə çaları ilə hipnotik badam və vanil. Həssas, bürüyən axşam ətri.'}),
'Christian Dior Fahrenheit': ('Woody Leather',['nutmeg','lavender','mandarin','bergamot','lemon'],['violet leaf','honeysuckle','carnation','jasmine'],['leather','vetiver','musk','patchouli','tonka bean'],'COLDDAY',{
 'en':'A bold cult classic with a distinctive violet-leaf and leather accord. Unconventional and masculine.',
 'ru':'Смелая культовая классика с узнаваемым аккордом листьев фиалки и кожи. Нестандартный и мужественный.',
 'az':'Bənövşə yarpağı və dəridən tanınan akkordu olan cəsur kult klassika. Qeyri-adi və kişisayağı.'}),
'Versace Bright Crystal': ('Floral Fruity',['yuzu','pomegranate'],['peony','lotus','magnolia'],['musk','mahogany','amber'],'WARM',{
 'en':'Fresh pomegranate and yuzu with delicate peony and magnolia. A light, transparent floral for daytime.',
 'ru':'Свежий гранат и юдзу с нежным пионом и магнолией. Лёгкий, прозрачный цветочный аромат для дня.',
 'az':'İncə pion və maqnoliya ilə təzə nar və yuzu. Gündüz üçün yüngül, şəffaf çiçəkli ətir.'}),
'Sospiro Erba Pura': ('Citrus Fruity',['orange','lemon','bergamot'],['fruity notes'],['white musk','vanilla','amber'],'ALL',{
 'en':'A bright, juicy explosion of citrus and fruits on a soft musk-vanilla base. Cheerful, noticeable and very long-lasting.',
 'ru':'Яркий сочный взрыв цитрусов и фруктов на мягкой мускусно-ванильной базе. Жизнерадостный, заметный и очень стойкий.',
 'az':'Yumşaq müşk-vanil bazası üzərində sitrus və meyvələrin parlaq, şirəli partlayışı. Şən, diqqət çəkən və çox davamlı.'}),
'Ajmal Aurum': ('Floral Fruity',['lemon','raspberry'],['gardenia','jasmine','orange blossom'],['amber','musk','vanilla'],'ALL',{
 'en':'A sunny, golden fragrance: juicy raspberry and lemon open onto white flowers — jasmine, gardenia and orange blossom — over a soft amber-vanilla base. Radiant and feminine, close in mood to Lady Million.',
 'ru':'Солнечный «золотой» аромат: сочная малина и лимон раскрываются белыми цветами — жасмином, гарденией и цветком апельсина — на мягкой амброво-ванильной базе. Сияющий и женственный, по настроению близок к Lady Million.',
 'az':'Günəşli, "qızıl" ətir: şirəli moruq və limon yumşaq kəhrəba-vanil bazası üzərində ağ çiçəklərə — jasmin, qardeniya və portağal çiçəyinə açılır. İşıltılı və qadınsı, ab-havasına görə Lady Million-a yaxındır.'}),
'Ajmal Amber wood': ('Woody Amber',['apple','white pepper','lavender','cardamom'],['iris','cedar'],['amber','patchouli','woody notes'],'COLDDAY',{
 'en':'A warm woody-amber scent: crisp apple, cardamom and white pepper lead into powdery iris and cedar, settling on amber and patchouli. Refined and cosy — a great unisex choice for autumn and winter.',
 'ru':'Тёплый древесно-амбровый аромат: хрустящее яблоко, кардамон и белый перец переходят в пудровый ирис и кедр, а затем в амбру и пачули. Утончённый и уютный — отличный унисекс-вариант на осень и зиму.',
 'az':'İsti odunsu-kəhrəba ətri: xırtıldayan alma, hil və ağ istiot pudralı süsən və sidrə, sonra kəhrəba və paçuliyə keçir. Zərif və rahat — payız və qış üçün əla uniseks seçim.'}),
}

# Not confidently known -> marked "check"
UNKNOWN = ['Afnan Tribute Blue','Afnan Supermacy','Arabic Al Hayati','Arabic Ci-Ci']

G.update({
 'Aromatic Spicy':('Ароматический пряный','Aromatik-ədviyyatlı'),'Citrus Aromatic':('Цитрусовый ароматический','Sitrus-aromatik'),
 'Floral':('Цветочный','Çiçəkli'),'Floral Aldehydic':('Цветочный альдегидный','Çiçəkli-aldehidli'),'Floral Amber':('Цветочный амбровый','Çiçəkli-kəhrəba'),
 'Floral Aquatic':('Цветочный водный','Çiçəkli-dəniz'),'Floral Gourmand':('Цветочный гурманский','Çiçəkli qurman'),'Floral Musk':('Цветочный мускусный','Çiçəkli-müşk'),
 'Leather':('Кожаный','Dəri'),'Oriental':('Восточный','Şərq'),'Oriental Amber':('Восточный амбровый','Şərq kəhrəba'),
 'Oriental Fougère':('Восточный фужерный','Şərq fujer'),'Oriental Woody':('Восточный древесный','Şərq odunsu'),
 'Woody Floral Musk':('Древесный цветочный мускусный','Odunsu-çiçəkli-müşk'),'Woody Spicy':('Древесный пряный','Odunsu-ədviyyatlı'),
 'absinthe':('абсент','absent'),'agarwood':('агаровое дерево','aqar ağacı'),'aldehydes':('альдегиды','aldehidlər'),
 'almond flower':('цветок миндаля','badam çiçəyi'),'almond milk':('миндальное молоко','badam südü'),'amaryllis':('амариллис','amarilis'),
 'ambrette':('амбретта','ambret'),'ambrofix':('амброфикс','ambrofiks'),'ambrox':('амброкс','ambroks'),'amyris':('амирис','amiris'),
 'angelica':('дягиль','mələkotu'),'anise':('анис','anis'),'apple tree wood':('древесина яблони','alma ağacı'),'artemisia':('полынь','yovşan'),
 'basil':('базилик','reyhan'),'beeswax':('пчелиный воск','arı mumu'),'benzoin':('бензоин','benzoin'),'black pepper':('чёрный перец','qara istiot'),
 'black tea':('чёрный чай','qara çay'),'black vanilla':('чёрная ваниль','qara vanil'),'blackberry':('ежевика','böyürtkən'),
 'blood orange':('красный апельсин','qırmızı portağal'),'blue poppy':('голубой мак','mavi lalə'),'blueberry':('черника','qaragilə'),
 'brandy':('бренди','brendi'),'brown sugar':('коричневый сахар','qəhvəyi şəkər'),'bulgarian rose':('болгарская роза','Bolqar qızılgülü'),
 'cactus flower':('цветок кактуса','kaktus çiçəyi'),'calla lily':('калла','kalla'),'camellia':('камелия','kameliya'),
 'candied orange':('цукаты апельсина','portağal sukatı'),'cannabis':('конопля','çətənə'),'carambola':('карамбола','karambola'),
 'caramel':('карамель','karamel'),'carrot seeds':('семена моркови','yerkökü toxumu'),'cashmere wood':('кашемировое дерево','kaşmir ağacı'),
 'champagne':('шампанское','şampan'),'cherry':('вишня','albalı'),'cherry blossom':('цветок вишни','albalı çiçəyi'),'chestnut':('каштан','şabalıd'),
 'chili':('перец чили','çili bibəri'),'cistus':('ладанник','sistus'),'citron':('цитрон','sitron'),'citrus':('цитрусы','sitruslar'),
 'clary sage':('мускатный шалфей','muskat adaçayı'),'clove':('гвоздика (пряность)','mixək'),'clover':('клевер','yonca'),'cognac':('коньяк','konyak'),
 'coriander':('кориандр','keşniş'),'cotton candy':('сахарная вата','pambıq konfet'),'cucumber':('огурец','xiyar'),'cumin':('кумин','zirə'),
 'cyclamen':('цикламен','siklamen'),'cypress':('кипарис','sərv'),'daffodil':('нарцисс','nərgiz'),'dates':('финики','xurma'),'elemi':('элеми','elemi'),
 'fig':('инжир','əncir'),'fig leaf':('лист инжира','əncir yarpağı'),'fir':('пихта','küknar'),'frangipani':('франжипани','frangipani'),
 'frankincense':('ладан','buxur'),'galbanum':('гальбанум','qalbanum'),'goji berry':('ягоды годжи','qoji giləmeyvəsi'),'green apple':('зелёное яблоко','yaşıl alma'),
 'green mandarin':('зелёный мандарин','yaşıl mandarin'),'green notes':('зелёные ноты','yaşıl notlar'),'green tea':('зелёный чай','yaşıl çay'),
 'guava':('гуава','quava'),'hazelnut':('фундук','fındıq'),'heliotrope':('гелиотроп','heliotrop'),'hibiscus':('гибискус','hibiskus'),
 'immortelle':('бессмертник','ölməzçiçək'),'juniper':('можжевельник','ardıc'),'kiwi':('киви','kivi'),'kulfi':('кульфи','kulfi'),'lilac':('сирень','yasəmən'),
 'lily':('лилия','zanbaq'),'mandarin leaf':('лист мандарина','mandarin yarpağı'),'mango':('манго','manqo'),'maninka fruit':('фрукт манинка','maninka meyvəsi'),
 'marigold':('бархатцы','məxmərçiçəyi'),'marshmallow':('маршмеллоу','zefir'),'mirabelle':('мирабель','mirabel gavalısı'),'moss':('мох','mamır'),
 'myrrh':('мирра','mirra'),'myrtle':('мирт','mərsin'),'narcissus':('нарцисс','nərgiz'),'oak':('дуб','palıd'),'olibanum':('олибанум','olibanum'),
 'olive blossom':('цветок оливы','zeytun çiçəyi'),'opoponax':('опопанакс','opopanaks'),'oregano':('орегано','kəklikotu'),'orris':('корень ириса','süsən kökü'),
 'osmanthus':('османтус','osmantus'),'papaya flower':('цветок папайи','papaya çiçəyi'),'papyrus':('папирус','papirus'),'peppermint':('перечная мята','bibərnanə'),
 'petitgrain':('петитгрейн','petitqren'),'pimento':('душистый перец','yeni istiot'),'pine':('сосна','şam'),'pine needles':('сосновая хвоя','şam iynəsi'),
 'pineapple leaf':('лист ананаса','ananas yarpağı'),'pink grapefruit':('розовый грейпфрут','çəhrayı qreypfrut'),'pistachio':('фисташка','püstə'),
 'pitahaya':('питахайя','pitahaya'),'powdery notes':('пудровые ноты','pudralı notlar'),'quince':('айва','heyva'),'rangoon creeper':('рангунский вьюн','ranqun sarmaşığı'),
 'red currant':('красная смородина','qırmızı qarağat'),'red pepper':('красный перец','qırmızı bibər'),'redcurrant':('красная смородина','qırmızı qarağat'),
 'resins':('смолы','qatranlar'),'rice':('рис','düyü'),'rice husk':('рисовая шелуха','düyü qabığı'),'rum':('ром','rom'),'sage':('шалфей','adaçayı'),'salt':('соль','duz'),
 'sapodilla':('саподилла','sapodilla'),'seaweed':('морские водоросли','dəniz yosunu'),'shaving soap':('мыло для бритья','təraş sabunu'),
 'silk tree blossom':('цветок шёлковой акации','ipək akasiya çiçəyi'),'smoke':('дым','tüstü'),'star anise':('бадьян','ulduz anis'),'styrax':('стиракс','stiraks'),
 'sweet pea':('душистый горошек','ətirli noxud'),'tea':('чай','çay'),'teak wood':('тик','tik ağacı'),'thyme':('тимьян','kəklikotu'),'tiger liana':('тигровая лиана','pələng lianası'),
 'toffee':('ирис (конфета)','iris konfeti'),'tomato leaf':('лист томата','pomidor yarpağı'),'tropical fruits':('тропические фрукты','tropik meyvələr'),
 'vanilla orchid':('ванильная орхидея','vanil orxideyası'),'vodka':('водка','araq'),'water hyacinth':('водяной гиацинт','su sümbülü'),
 'water jasmine':('водяной жасмин','su jasmini'),'water lily':('кувшинка','su zanbağı'),'watermelon':('арбуз','qarpız'),'wheat':('пшеница','buğda'),
 'whipped cream':('взбитые сливки','çalınmış qaymaq'),'whiskey':('виски','viski'),'white narcissus':('белый нарцисс','ağ nərgiz'),
 'wild berries':('лесные ягоды','meşə giləmeyvələri'),'wisteria':('глициния','visteriya'),'wormwood':('полынь','yovşan'),
})
G.update({'cranberry':('клюква','mərcanı'),'white flowers':('белые цветы','ağ çiçəklər'),'cola':('кола','kola'),
 'bubble gum':('жевательная резинка','saqqız'),'grapefruit blossom':('цветок грейпфрута','qreypfrut çiçəyi')})
G.update({'akigalawood':('акигалавуд','akiqala ağacı'),'bracken':('папоротник','qıjı'),'chocolate':('шоколад','şokolad'),
 'clementine':('клементин','klementin'),'coumarin':('кумарин','kumarin'),'hay':('сено','quru ot'),'lemongrass':('лемонграсс','limon otu'),
 'limoncello':('лимончелло','limonçello'),'milk':('молоко','süd'),'tangerine':('тангерин','naringi'),'tiare':('тиаре','tiare'),
 'tulip':('тюльпан','lalə'),'white tea':('белый чай','ağ çay')})
