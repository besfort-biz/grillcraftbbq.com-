#!/usr/bin/env python3
"""Translate SQ content pages body text from English to Albanian."""

import os, re

BASE = "/home/v/bbq/grillcraftbbq.com"

# Shared translations used across multiple pages
SHARED = {
    "Professional BBQ smokers, grills, and fireplaces for professional chefs and BBQ fans directly from the manufacturer.":
        "Furra profesionale BBQ, skara dhe vatra zjarri për kuzhinierë profesionistë dhe tifozë të BBQ direkt nga prodhuesi.",
    "Professional BBQ smokers, grills, and fireplaces for chefs and BBQ fans. Handcrafted in Switzerland.":
        "Furra profesionale BBQ, skara dhe vatra zjarri për kuzhinierë dhe tifozë të BBQ. Punuar me dorë në Zvicër.",
    "Out of stock": "Mungon në stok",
    "More Info": "Më Shumë Info",
    "Filter by": "Filtro nga",
    "Sort by": "Rendit nga",
    "All": "Të gjitha",
    "Best sellers": "Më të shiturat",
    "Featured": "Të zgjedhura",
    "Alphabetical": "Alfabetike",
    "New": "I ri",
    "Price": "Çmimi",
    "Any": "Çdo",
    "Explore Products": "Eksploro Produktet",
    "To the products": "Te produktet",
    "Get in touch": "Kontaktoni",
    "for custom BBQ solutions": "për zgjidhje të personalizuara BBQ",
    "I am a private customer": "Jam klient privat",
    "I'm a restaurateur": "Jam restorant",
    "I'm a butcher - caterer": "Jam kasap - katering",
}

# Per-page translations
PAGES = {
    "index": {
        "GrillCraft BBQ - Premium Smokers & Grills | Winterthur":
            "GrillCraft BBQ - Pajisje Premium BBQ & Skara | Winterthur",
        "Professional BBQ smokers, grills, and fireplaces for chefs and BBQ fans. Handcrafted in Zvicra.":
            "Furra profesionale BBQ, skara dhe vatra zjarri për kuzhinierë dhe tifozë të BBQ. Punuar me dorë në Zvicër.",
        "We Build Smokers from Experience": "Ne Ndërtojmë Furra nga Përvoja",
        "Professional BBQ smokers, grills, and fireplaces for professional chefs and BBQ fans directly from the manufacturer.":
            "Furra profesionale BBQ, skara dhe vatra zjarri për kuzhinierë profesionistë dhe tifozë të BBQ direkt nga prodhuesi.",
        "Professional BBQ Smoker, Grills &amp; Fireplaces": "Furra Profesionale BBQ, Skara &amp; Vatra Zjarri",
        "With our top products, we enable you to professionally create a wood-burning stove and BBQ feeling in your kitchen.":
            "Me produktet tona më të mira, ju mundësojmë të krijoni profesionalisht një sobë me dru dhe ndjenjë BBQ në kuzhinën tuaj.",
        "Premium Grills": "Skara Premium",
        "Handcrafted from high-quality materials for professional and private use.":
            "Të punuara me dorë nga materiale cilësore për përdorim profesional dhe privat.",
        "BBQ Is Our Passion": "BBQ Është Pasioni Ynë",
        "Since 2016 building highly professional smokers for customers who love BBQ.":
            "Që nga 2016 duke ndërtuar furra shumë profesionale për klientët që duan BBQ.",
        "Proven Quality": "Cilësi e Provuar",
        "Developed for professional kitchens, BBQ competitions, and event caterers.":
            "Zhvilluar për kuzhina profesionale, gara BBQ dhe katering për evente.",
        "Why Choose GrillCraft BBQ?": "Pse të Zgjidhni GrillCraft BBQ?",
        "Careful selection of the highest quality products for those passionate about grilling and gastronomy.":
            "Përzgjedhje e kujdesshme e produkteve të cilësisë më të lartë për ata që janë të apasionuar pas skarës dhe gastronomisë.",
        "Quality You Can Trust": "Cilësi që Mund t'i Besoni",
        "Our selection includes only the highest quality products with time-tested capabilities, characterized by efficiency, ease of use, durability, and smart, attractive design.":
            "Përzgjedhja jonë përfshin vetëm produkte të cilësisë më të lartë me aftësi të testuara me kohë, të karakterizuara nga efikasiteti, lehtësia e përdorimit, qëndrueshmëria dhe dizajni i zgjuar dhe tërheqës.",
        'According to the principle of "value for money", the user receives the highest level of reliability, usefulness, and functionality.':
            'Sipas parimit "vlerë për para", përdoruesi merr nivelin më të lartë të besueshmërisë, dobishmërisë dhe funksionalitetit.',
        "Find the Right Product": "Gjeni Produktin e Duhur",
        "The choice of smoker is just as important as the expertise. The smoker with reverse flow system from GrillCraft BBQ are ideal for smaller kitchens and private households. With a footprint of less than 1 square meter, they fit into even the tightest of spaces.":
            "Zgjedhja e furrës është po aq e rëndësishme sa ekspertiza. Furrat me sistem reverse flow nga GrillCraft BBQ janë ideale për kuzhina më të vogla dhe familje private. Me një gjurmë më pak se 1 metër katror, ato përshtaten edhe në hapësirat më të ngushta.",
        "If you want to process larger quantities of meat, the Gravity Feed series of gravity feed smokers are your best choice. These smokers feature a built-in charcoal hopper that continuously fuels the fire to keep you smoking all day long. Our largest smoker can smoke up to 80 spare ribs or 12-14 whole pork necks at once.":
            "Nëse dëshironi të përpunoni sasi më të mëdha mishi, seria Gravity Feed e furrave me ushqim nga graviteti është zgjedhja juaj më e mirë. Këto furra kanë një depozitë të integruar që ushqen vazhdimisht zjarrin për të tymosur gjatë gjithë ditës. Furra jonë më e madhe mund të tymosë deri në 80 brinjë ose 12-14 qafa derri të tëra në një herë.",
        "If you need a smaller capacity or want a portable smoker, the BFB RF series is the best choice. It's particularly popular with pop-up restaurants, event caterers, and chefs looking to bring authentic American-style BBQ to the table.":
            "Nëse keni nevojë për një kapacitet më të vogël ose dëshironi një furrë portative, seria BFB RF është zgjedhja më e mirë. Është veçanërisht e popullarizuar me restorantet pop-up, kateringët e eventeve dhe kuzhinierët që kërkojnë të sjellin BBQ autentike amerikane në tryezë.",
        "Our Partners": "Partnerët Tanë",
        "CROSS BBQ &mdash; Your official GrillCraft BBQ exclusive dealer in Switzerland":
            "CROSS BBQ &mdash; Shitësi juaj zyrtar ekskluziv i GrillCraft BBQ në Zvicër",
    },

    "produkte": {
        "For the Best \u2013 Only the Best": "Për më të Mirët \u2013 Vetëm më e Mira",
        "Professional smokers, grills and fireplaces by GrillCraft BBQ \u2014 developed for professional chefs who don't want to compromise on the authenticity of real fire and wood smoke.":
            "Furra profesionale, skara dhe vatra zjarri nga GrillCraft BBQ \u2014 të zhvilluara për kuzhinierë profesionistë që nuk duan të komprometojnë autenticitetin e zjarrit të vërtetë dhe tymit të drurit.",
        "Backyard Hero \u2013 3 Models": "Backyard Hero \u2013 3 Modele",
        "Private \u2022 6-25kg/Session": "Privat \u2022 6-25kg/Sesion",
        "GF Serie \u2013 4 Models": "GF Serie \u2013 4 Modele",
        "Private / Commercial \u2022 30-110kg/Session": "Privat / Tregtar \u2022 30-110kg/Sesion",
        "BFB RF Serie \u2013 4 Models": "BFB RF Serie \u2013 4 Modele",
        "Private / Commercial \u2022 8-35kg/Session": "Privat / Tregtar \u2022 8-35kg/Sesion",
        "Brot Holzofen \u2013 B Oven": "Brot Holzofen \u2013 B Oven",
        "Private / Commercial \u2022 2-10kg/Session": "Privat / Tregtar \u2022 2-10kg/Sesion",
        "D Oven \u2013 5 Models": "D Oven \u2013 5 Modele",
        "Private / Commercial \u2022 12-80kg/Session": "Privat / Tregtar \u2022 12-80kg/Sesion",
        "ASADO Grill \u2013 3 Models": "ASADO Grill \u2013 3 Modele",
        "Private / Commercial \u2022 4-60kg/Session": "Privat / Tregtar \u2022 4-60kg/Sesion",
        "Offset BBQ \u2013 2 Models": "Offset BBQ \u2013 2 Modele",
        "Commercial / Professional \u2022 10-210kg/Session": "Tregtar / Profesional \u2022 10-210kg/Sesion",
        "NYP Offset BBQ \u2013 2 Models": "NYP Offset BBQ \u2013 2 Modele",
        "Private / Commercial \u2022 8-60kg/Session": "Privat / Tregtar \u2022 8-60kg/Sesion",
        "Whole Hog \u2013 Monster": "Whole Hog \u2013 Monster",
        "Commercial / Professional \u2022 20-250kg/Session": "Tregtar / Profesional \u2022 20-250kg/Sesion",
    },

    "gastronomie": {
        "Gastronomy": "Gastronomi",
        "Professional BBQ smokers and grills for gastronomy and commercial kitchens.":
            "Furra profesionale BBQ dhe skara për gastronomi dhe kuzhina tregtare.",
        "Professional smokers, grills and ovens for commercial kitchens, restaurants, and catering businesses. Filter by category to find the perfect solution for your business.":
            "Furra profesionale, skara dhe furra buke për kuzhina tregtare, restorante dhe biznese katering. Filtroni sipas kategorisë për të gjetur zgjidhjen perfekte për biznesin tuaj.",
        "Gastro from 120 people": "Gastro nga 120 persona",
        "Yakitori Grill": "Yakitori Grill",
        "GRILL &amp; BBQ": "GRILL &amp; BBQ",
        "Duck Oven": "Duck Oven",
        "GF Serie": "GF Serie",
        "ASSADO Grillwagen": "ASSADO Grillwagen",
        "Reverse Flow": "Reverse Flow",
        "roasting and baking ovens": "furra pjekje dhe gatimi",
        "Profi Offset BBQ": "Profi Offset BBQ",
        "Whole Hog Monster": "Whole Hog Monster",
    },

    "private-haushalt": {
        "Private Household": "Familje Private",
        "Premium BBQ smokers and grills for home use. Handcrafted quality for private households.":
            "Furra dhe skara premium BBQ për përdorim shtëpiak. Cilësi e punuar me dorë për familje private.",
        "The taste and smell of wood-fired meat or home-baked bread with a crispy crust cannot be compared to that of an electric oven. The GrillCraft BBQ series has the great advantage that it is mobile and requires little space. They are easier to use, more versatile and more efficient.":
            "Shija dhe era e mishit të pjekur me dru ose bukës së pjekur në shtëpi me kore krokante nuk mund të krahasohet me atë të një furre elektrike. Seria GrillCraft BBQ ka avantazhin e madh se është e lëvizshme dhe kërkon pak hapësirë. Janë më të lehta për t'u përdorur, më të gjithanshme dhe më efikase.",
        "GRILL &amp; BBQ": "GRILL &amp; BBQ",
        "CABINET SMOKER": "CABINET SMOKER",
        "Yakitori Grill": "Yakitori Grill",
        "GF Serie": "GF Serie",
        "NYP Offset smoker": "NYP Offset smoker",
        "Under $2,000": "Nën $2,000",
        "$2,000 - $5,000": "$2,000 - $5,000",
        "Over $5,000": "Mbi $5,000",
    },

    "cabinet-smoker": {
        "Cabinet Smokers": "Furra Kabineti",
        "Cabinet smokers - reverse flow and gravity feed smokers for professional and private use.":
            "Furra kabineti - furra reverse flow dhe gravity feed për përdorim profesional dhe privat.",
        "The taste and smell of wood-fired meat or home-baked bread with a crispy crust cannot be compared to that of an electric oven. The GrillCraft BBQ series has the great advantage that it is mobile and requires little space.":
            "Shija dhe era e mishit të pjekur me dru ose bukës së pjekur në shtëpi me kore krokante nuk mund të krahasohet me atë të një furre elektrike. Seria GrillCraft BBQ ka avantazhin e madh se është e lëvizshme dhe kërkon pak hapësirë.",
        "private household": "familje private",
        "GRILL &amp; BBQ": "GRILL &amp; BBQ",
        "Reverse Flow": "Reverse Flow",
    },

    "offset-bbq-grill": {
        "Offset BBQ &amp; Grill": "Offset BBQ &amp; Grill",
        "Offset BBQ smokers and grills - professional offset smokers for commercial and private use.":
            "Furra dhe skara Offset BBQ - furra offset profesionale për përdorim tregtar dhe privat.",
        "Yakitori Grill": "Yakitori Grill",
        "Duck Oven": "Duck Oven",
        "ASSADO Grillwagen": "ASSADO Grillwagen",
        "Profi Offset BBQ": "Profi Offset BBQ",
        "NYP Offset smoker": "NYP Offset smoker",
    },

    "brat-und-backoefen": {
        "Brat und Back\u00f6fen": "Brat und Back\u00f6fen",
        "Duck ovens and roasting ovens for professional and private kitchens.":
            "Furra rosash dhe furra pjekjeje për kuzhina profesionale dhe private.",
        "The taste and smell of wood-fired meat or home-baked bread with a crispy crust cannot be compared to that of an electric oven. The GrillCraft BBQ series has the great advantage that it is mobile and requires little space.":
            "Shija dhe era e mishit të pjekur me dru ose bukës së pjekur në shtëpi me kore krokante nuk mund të krahasohet me atë të një furre elektrike. Seria GrillCraft BBQ ka avantazhin e madh se është e lëvizshme dhe kërkon pak hapësirë.",
        "private household": "familje private",
        "GRILL &amp; BBQ": "GRILL &amp; BBQ",
        "B Oven": "B Oven",
    },

    "catering": {
        "BBQ PIT BOX &amp; Catering Services": "BBQ PIT BOX &amp; Shërbime Katering",
        "Our company specializes in the sale of BBQ PIT BOX wood-fired ovens, grills, and smokers. The growing interest has prompted us to give our future partners and interested parties the opportunity to test the dishes and the great potential of the BBQ PIT BOX as a catering concept.":
            "Kompania jonë specializohet në shitjen e furrave me dru, skarave dhe furrave të tymit BBQ PIT BOX. Interesi në rritje na ka shtyrë t'u japim partnerëve tanë të ardhshëm dhe palëve të interesuara mundësinë të testojnë pjatat dhe potencialin e madh të BBQ PIT BOX si koncept katering.",
        "Our Constant Offer": "Oferta Jonë e Përhershme",
        "We exclusively process Swiss quality meat.": "Ne përpunojmë ekskluzivisht mish cilësor zviceran.",
        "BRISKET": "BRISKET",
        "The beef brisket is cooked for 16-18 hours at 120 degrees Celsius. After a resting time of at least 2 hours, it is served. The whole pieces come with a weight of 2.6 to 3.5 kg out of the smoker. We use only salt and pepper for the meat. Wagyu Beef Tallow available on request.":
            "Gjoksi i viçit gatuhet për 16-18 orë në 120 gradë Celsius. Pas një kohe pushimi prej të paktën 2 orësh, shërbehet. Copat e tëra dalin nga furra me peshë 2.6 deri në 3.5 kg. Ne përdorim vetëm kripë dhe piper për mishin. Wagyu Beef Tallow në dispozicion sipas kërkesës.",
        "PULLED BEEF": "PULLED BEEF",
        "The beef is first rubbed with a dry rub of salt and pepper. Smoked for 3-4 hours at 120 degrees Celsius, sprayed with apple cider vinegar and water, then wrapped in foil and cooked for 2-3 hours until core temperature is reached. Rest for 1.5-2 hours before serving.":
            "Mishi fillimisht fërkohet me një përzierje të thatë me kripë dhe piper. Tymoset për 3-4 orë në 120 gradë Celsius, spërkatohet me uthull molle dhe ujë, pastaj mbështillet në letër alumini dhe gatuhet për 2-3 orë derisa të arrihet temperatura e brendshme. Pushon për 1.5-2 orë para se të shërbehet.",
        "PULLED PORK": "PULLED PORK",
        "The meat is first rubbed with a special Pulled Pork Dry Rub, with mustard base optional. Smoked for 3-4 hours at 120 degrees, then wrapped in foil and cooked for 2-3 hours. After unpacking, it is placed on the rack for another 1-1.5 hours until the color is perfect.":
            "Mishi fillimisht fërkohet me një përzierje të thatë speciale Pulled Pork, me bazë mustardë opsionale. Tymoset për 3-4 orë në 120 gradë, pastaj mbështillet në letër alumini dhe gatuhet për 2-3 orë. Pas shpaketimit, vendoset në raft për 1-1.5 orë të tjera derisa ngjyra të jetë perfekte.",
        "PORK BABY RIBS": "PORK BABY RIBS",
        "The meat is first rubbed with a special Pulled Pork Dry Rub, with mustard base optional. Smoked for 3-4 hours at 120 degrees, sprayed with apple cider vinegar and water, then wrapped in foil and cooked until core temperature is reached.":
            "Mishi fillimisht fërkohet me një përzierje të thatë speciale Pulled Pork, me bazë mustardë opsionale. Tymoset për 3-4 orë në 120 gradë, spërkatohet me uthull molle dhe ujë, pastaj mbështillet në letër alumini dhe gatuhet derisa të arrihet temperatura e brendshme.",
        "Our Partners": "Partnerët Tanë",
    },

    "uber-uns": {
        "About BBQ and Us": "Rreth BBQ dhe Nesh",
        "BBQ": "BBQ",
        "The home of the classic grill is the United States. Outdoor baking and grilling is done in the kitchens of almost every nation, but what we call a classic grill, whether in recipes or equipment, comes from the USA.":
            "Shtëpia e skarës klasike janë Shtetet e Bashkuara. Pjekja në natyrë bëhet në kuzhinat e pothuajse çdo kombi, por ajo që ne e quajmë skarë klasike, qoftë në receta apo pajisje, vjen nga SHBA.",
        'Many people say that a good grill really depends on the cook, on the soul of the grill master, not that of the equipment. We don\'t entirely agree. Of course, knowledge is a big part of grilling, but without the right equipment, even the best grill master can\'t get juicy brisket or tender ribs. A good steak has to be prepared on the right grill to be as tender and smoky as it should be.':
            "Shumë njerëz thonë se një skarë e mirë varet nga kuzhinieri, nga shpirti i mjeshtrit të skarës, jo nga pajisja. Ne nuk pajtohemi plotësisht. Sigurisht, njohuria është një pjesë e madhe e pjekjes në skarë, por pa pajisjet e duhura, as mjeshtri më i mirë i skarës nuk mund të marrë brisket të lëngshëm ose brinjë të buta. Një biftek i mirë duhet të përgatitet në skarën e duhur për të qenë aq i butë dhe i tymosur sa duhet.",
        "Texas &amp; Memphis BBQ": "Texas &amp; Memphis BBQ",
        "Its main feature is a dry rub (often 2-3 ingredients, just salt, pepper and a spice), strong, smoky flavors, spicy sauces, tomato, garlic glazes, almost all types of meat, with the focus mainly on quality beef rather than pork or lamb. Sweet, pickled, savory, thick glazes, cornbread chips, toast and baked beans.":
            "Karakteristika kryesore e saj është një përzierje e thatë (shpesh 2-3 përbërës, vetëm kripë, piper dhe një erëz), shije të forta të tymosura, salca pikante, domate, lustrime hudhre, pothuajse të gjitha llojet e mishit, me fokus kryesisht në viçin cilësor në vend të derrit ose qengjit. Lustrime të ëmbla, turshi, të shijshme, të trasha, patate të skuqura misri, dolli dhe fasule të pjekura.",
        "North Carolina BBQ": "North Carolina BBQ",
        "Pork, ribs, pulled pork sandwiches, sausage, burgers are made in many different ways. The pig is often smoked whole. Typically served with lots of pickles and mustard, apple juice is found in almost everything from sauces to soups.":
            "Derri, brinjët, sanduiçët pulled pork, sallami, burgerët bëhen në shumë mënyra të ndryshme. Derri shpesh tymoset i tëri. Zakonisht shërbehet me shumë turshi dhe mustardë, lëng molle gjendet pothuajse në gjithçka nga salcat te supat.",
        "Kansas BBQ": "Kansas BBQ",
        "They use all types of meat, but perhaps the pork drives a little ahead of the beef. In addition to the classic BBQ roast, juicy, soupy dishes are also popular when baking outdoors. Strong, long fumigations, strong, large juicy slices of meat with sweet sauces.":
            "Ata përdorin të gjitha llojet e mishit, por ndoshta derri kalon pak përpara viçit. Përveç pjekjes klasike BBQ, pjatat e lëngshme dhe me supë janë gjithashtu të njohura gjatë pjekjes në natyrë. Tymosje të forta dhe të gjata, feta të mëdha e të lëngshme mishi me salca të ëmbla.",
        "San Francisco BBQ": "San Francisco BBQ",
        "The West Coast BBQ tradition is made up of many strands. On the one hand there is the roast beef and burgers of the inner states, alongside the classic American flavors, there is the richness of California orchards and the variety of seafood. Thai, Chinese and Japanese flavors are the order of the day.":
            "Tradita BBQ e Bregut Perëndimor përbëhet nga shumë fije. Nga njëra anë ka mish të pjekur dhe burgerë të shteteve të brendshme, krahas shijeve klasike amerikane, ka pasurinë e pemishteve të Kalifornisë dhe shumëllojshmërinë e ushqimeve të detit. Shijet tajlandeze, kineze dhe japoneze janë të zakonshme.",
        "Production Background": "Sfondi i Prodhimit",
        "Each of our stoves is made unique, in a special factory, in the hands of skilled Hungarian metalworkers, with industrial background and technology. Materials cut with plasma cutters, consumable electrodes and AVI manual welds, hydraulic edge bender curved walls. Many man hours \u2013 8-10 weeks production run time.":
            "Secila prej sobave tona bëhet unike, në një fabrikë të veçantë, në duart e punëtorëve të aftë hungarezë të metaleve, me sfond dhe teknologji industriale. Materiale të prera me prerës plazma, elektroda harxhuese dhe saldime manuale AVI, mure të lakuar me përkulës hidraulik. Shumë orë pune \u2013 8-10 javë kohë prodhimi.",
        "General Specification": "Specifikime të Përgjithshme",
        "Supercharged charcoal stove that can be precisely controlled at 70-200\u00b0C":
            "Sobë me qymyr me kontroll të saktë në 70-200\u00b0C",
        "Fire compartment and oven: LV4 plate, S 235 material quality":
            "Ndarja e zjarrit dhe furra: pllakë LV4, cilësi materiali S 235",
        "Combustion chamber: Plate LV10, material quality S 235":
            "Dhoma e djegies: Pllakë LV10, cilësi materiali S 235",
        "Closed section frames and brackets":
            "Korniza dhe mbajtëse seksionesh të mbyllura",
        "Covers: LV1, colored, powder-coated, on request":
            "Mbulesat: LV1, me ngjyrë, të veshura me pluhur, sipas kërkesës",
        "Fire doors + smoke butts: Heat-resistant matte black paint":
            "Dyert e zjarrit + pjesët e tymit: Bojë e zezë mat rezistente ndaj nxehtësisë",
        "Brushed aluminum edge protectors":
            "Mbrojtëse buzësh alumini të krehura",
        "Contact": "Kontakt",
        "KLERED GmbH, Stadthausstrasse 10b, 8400 Winterthur, Switzerland, Phone: +41 52 203 1111, Email: info@bbqpitbox.com":
            "KLERED GmbH, Stadthausstrasse 10b, 8400 Winterthur, Zvicër, Tel: +41 52 203 1111, Email: info@bbqpitbox.com",
    },

    "contact": {
        "Contact Us": "Kontaktoni",
        "Get in Touch": "Merrni Kontakt",
        "KLERED GmbH, Stadthausstrasse 10b, 8400 Winterthur, Switzerland":
            "KLERED GmbH, Stadthausstrasse 10b, 8400 Winterthur, Zvicër",
        "Phone: +41 52 203 1111, Email: info@bbqpitbox.com":
            "Tel: +41 52 203 1111, Email: info@bbqpitbox.com",
        "Cross BBQ": "Cross BBQ",
        "Your official GrillCraft BBQ exclusive dealer in Switzerland.":
            "Shitësi juaj zyrtar ekskluziv i GrillCraft BBQ në Zvicër.",
        "Your official GrillCraft BBQ exclusive dealer in Zvicra.":
            "Shitësi juaj zyrtar ekskluziv i GrillCraft BBQ në Zvicër.",
        "Salutation": "Përshëndetje",
        "First Name *": "Emri *",
        "Surname *": "Mbiemri *",
        "Phone": "Telefoni",
        "Email *": "Email *",
        "Message *": "Mesazhi *",
        "Mr.": "Z.",
        "Ms.": "Znj.",
        "Other": "Tjetër",
        "I have read the Privacy Policy note.": "Kam lexuar njoftimin e Politikës së Privatësisë.",
        "Send": "Dërgo",
        "Thank You!": "Faleminderit!",
        "Your message has been sent. We will get back to you shortly.":
            "Mesazhi juaj u dërgua. Ne do t'ju kontaktojmë së shpejti.",
    },

    "datenschutzerklarung": {
        "Privacy Policy": "Politika e Privatësisë",
        "This data protection declaration applies to the online shop of the company BBQ PIT BOX \u2013 KLERED GmbH.":
            "Kjo deklaratë e mbrojtjes së të dhënave vlen për dyqanin online të kompanisë BBQ PIT BOX \u2013 KLERED GmbH.",
        "1. How do we protect your personal data?":
            "1. Si i mbrojmë të dhënat tuaja personale?",
        "We have technical and organizational security procedures in place to maintain the security of your personal data and to protect your session data and personal data against unauthorized or unlawful processing and/or against accidental loss, alteration, disclosure or access.":
            "Ne kemi procedura teknike dhe organizative të sigurisë për të ruajtur sigurinë e të dhënave tuaja personale dhe për të mbrojtur të dhënat e sesionit dhe të dhënat personale kundër përpunimit të paautorizuar ose të paligjshëm dhe/ose kundër humbjes, ndryshimit, zbulimit ose aksesit aksidental.",
        "2. How long do we keep data?":
            "2. Sa kohë i mbajmë të dhënat?",
        "We retain your personal information for as long as we deem necessary or appropriate to comply with applicable law or as long as it is necessary for the purposes for which it was collected.":
            "Ne i mbajmë të dhënat tuaja personale për aq kohë sa e konsiderojmë të nevojshme ose të përshtatshme për të përmbushur ligjin në fuqi ose për aq kohë sa është e nevojshme për qëllimet për të cilat u mblodhën.",
        "3. What rights do you have?":
            "3. Cilat të drejta keni?",
        "You have the right to assert your data protection rights at any time and to receive information about your stored personal data, to correct or supplement your personal data, to object to the processing of your personal data or to request the deletion of your personal data.":
            "Ju keni të drejtë të ushtroni të drejtat tuaja të mbrojtjes së të dhënave në çdo kohë dhe të merrni informacion për të dhënat tuaja personale të ruajtura, të korrigjoni ose plotësoni të dhënat tuaja personale, të kundërshtoni përpunimin e të dhënave tuaja personale ose të kërkoni fshirjen e të dhënave tuaja personale.",
        "4. How can you contact us?":
            "4. Si mund të na kontaktoni?",
        "If you wish to assert your rights in relation to your personal data or have any questions or concerns regarding the processing of our personal data, you can contact us via our contact page.":
            "Nëse dëshironi të ushtroni të drejtat tuaja në lidhje me të dhënat tuaja personale ose keni ndonjë pyetje apo shqetësim në lidhje me përpunimin e të dhënave tona personale, mund të na kontaktoni përmes faqes sonë të kontaktit.",
        "5. What personal data do we collect?":
            "5. Cilat të dhëna personale mbledhim?",
        "We collect personal data that you make available to us, such as name, address, email, phone number, and payment information. We also collect data automatically when you use our website, including session data, IP addresses, and browsing behavior.":
            "Ne mbledhim të dhëna personale që ju na i vini në dispozicion, si emri, adresa, emaili, numri i telefonit dhe informacioni i pagesës. Ne gjithashtu mbledhim të dhëna automatikisht kur përdorni faqen tonë të internetit, duke përfshirë të dhënat e sesionit, adresat IP dhe sjelljen e shfletimit.",
        "6. Why do we process personal data?":
            "6. Pse i përpunojmë të dhënat personale?",
        "We process your personal data for providing and selling our goods and services, processing orders and contracts, customer communication, marketing (with your consent), and improving our services.":
            "Ne i përpunojmë të dhënat tuaja personale për ofrimin dhe shitjen e mallrave dhe shërbimeve tona, përpunimin e porosive dhe kontratave, komunikimin me klientët, marketingun (me pëlqimin tuaj) dhe përmirësimin e shërbimeve tona.",
        "7. Do we share your data with third parties?":
            "7. A i ndajmë të dhënat tuaja me palë të treta?",
        "In principle, we do not pass on any personal data to third parties. However, we may disclose your personal data if required to comply with applicable laws and regulations, in court proceedings, or at the request of competent authorities.":
            "Në parim, ne nuk i kalojmë të dhëna personale palëve të treta. Megjithatë, ne mund të zbulojmë të dhënat tuaja personale nëse kërkohet për të përmbushur ligjet dhe rregulloret në fuqi, në procedurat gjyqësore ose me kërkesë të autoriteteve kompetente.",
        "8. Cookies": "8. Cookies",
        "We use cookies to ensure the functions of our website, to adapt our internet offer to your customer requirements, and to optimize our advertising. Most internet browsers automatically accept cookies. You can instruct your browser not to accept cookies or to ask you before accepting a cookie.":
            "Ne përdorim cookies për të siguruar funksionet e faqes sonë të internetit, për të përshtatur ofertën tonë të internetit me kërkesat tuaja dhe për të optimizuar reklamat tona. Shumica e shfletuesve të internetit pranojnë automatikisht cookies. Ju mund të udhëzoni shfletuesin tuaj të mos pranojë cookies ose t'ju pyesë para se të pranoni një cookie.",
        "9. Web Analysis Tools": "9. Mjetet e Analizës së Uebit",
        "We use Google Analytics for web analysis. The data generated by cookies about your use of the website is transmitted to Google servers (including shortened IP addresses). You can prevent this by installing the Google Analytics opt-out browser add-on.":
            "Ne përdorim Google Analytics për analizën e uebit. Të dhënat e gjeneruara nga cookies në lidhje me përdorimin tuaj të faqes së internetit transmetohen në serverët e Google (përfshirë adresat IP të shkurtuara). Ju mund ta parandaloni këtë duke instaluar shtesën e shfletuesit për çaktivizimin e Google Analytics.",
        "10. Social Plugins": "10. Shtojcat Sociale",
        "Our website uses social plugins from Facebook, Twitter, and Google+. These plugins transmit data to the respective providers when you interact with them. We recommend logging out of these services before visiting our website if you do not wish data to be collected.":
            "Faqja jonë e internetit përdor shtojca sociale nga Facebook, Twitter dhe Google+. Këto shtojca transmetojnë të dhëna te ofruesit përkatës kur ndërveproni me to. Ne rekomandojmë të çkyçeni nga këto shërbime përpara se të vizitoni faqen tonë të internetit nëse nuk dëshironi që të dhënat të mblidhen.",
        "Version 1.1": "Versioni 1.1",
    },

    "shipping-and-returns": {
        "Shipping &amp; Returns Policy": "Politika e Transportit &amp; Kthimeve",
        "Shipping": "Transporti",
        "We ship our products throughout Switzerland and neighboring countries. Shipping costs and delivery times vary depending on the product and destination. Please contact us for a detailed quote including shipping.":
            "Ne i dërgojmë produktet tona në të gjithë Zvicrën dhe vendet fqinje. Kostot e transportit dhe kohët e dorëzimit ndryshojnë në varësi të produktit dhe destinacionit. Ju lutemi na kontaktoni për një ofertë të detajuar duke përfshirë transportin.",
        "Each of our stoves is made to order in our factory. Production time is typically 8-10 weeks. We will keep you informed about the status of your order.":
            "Secila prej sobave tona bëhet me porosi në fabrikën tonë. Koha e prodhimit është zakonisht 8-10 javë. Ne do t'ju mbajmë të informuar për statusin e porosisë tuaj.",
        "Returns": "Kthimet",
        "Due to the custom-made nature of our products, returns are accepted only for manufacturing defects. Each stove is thoroughly inspected before shipment. If you receive a defective product, please contact us within 14 days of receipt.":
            "Për shkak të natyrës së produkteve tona të bëra me porosi, kthimet pranohen vetëm për defekte prodhimi. Çdo sobë inspektohet tërësisht para dërgesës. Nëse merrni një produkt me defekt, ju lutemi na kontaktoni brenda 14 ditëve nga marrja.",
        "Custom-made products manufactured to your specifications cannot be returned unless they have a manufacturing defect.":
            "Produktet e bëra me porosi sipas specifikimeve tuaja nuk mund të kthehen përveç nëse kanë një defekt prodhimi.",
        "Cancellation": "Anulimi",
        "You may cancel your order within 14 days of placing it, provided production has not yet begun. Once production has started, cancellation may incur a fee covering materials already ordered.":
            "Ju mund të anuloni porosinë tuaj brenda 14 ditëve nga vendosja e saj, me kusht që prodhimi të mos ketë filluar. Pasi prodhimi të ketë filluar, anulimi mund të sjellë një tarifë që mbulon materialet e porositura tashmë.",
        "For any questions regarding shipping and returns, please contact us at info@bbqpitbox.com or via our contact form.":
            "Për çdo pyetje në lidhje me transportin dhe kthimet, ju lutemi na kontaktoni në info@bbqpitbox.com ose përmes formularit tonë të kontaktit.",
    },

    "store-policy": {
        "Store Policy": "Politika e Dyqanit",
        "Ordering": "Porositja",
        "All orders are processed in the order they are received. Each product is custom-made to order. Production time is typically 8-10 weeks depending on the complexity of the product and current production volume.":
            "Të gjitha porositë përpunohen sipas radhës së marrjes. Çdo produkt është i bërë me porosi. Koha e prodhimit është zakonisht 8-10 javë në varësi të kompleksitetit të produktit dhe vëllimit aktual të prodhimit.",
        "Payment": "Pagesa",
        "Payment terms will be agreed upon when placing the order. We accept bank transfers and other payment methods as agreed.":
            "Kushtet e pagesës do të bien dakord kur vendoset porosia. Ne pranojmë transferta bankare dhe metoda të tjera pagese siç është rënë dakord.",
        "Pricing": "Çmimet",
        "All prices are in Swiss Francs (CHF) unless otherwise stated. Prices include VAT where applicable. Shipping costs are not included and will be quoted separately.":
            "Të gjitha çmimet janë në Franga Zvicerane (CHF) përveç rasteve kur thuhet ndryshe. Çmimet përfshijnë TVSH-në kur është e aplikueshme. Kostot e transportit nuk përfshihen dhe do të kuotohen veçmas.",
        "Warranty": "Garancia",
        "Our products are covered by a manufacturer's warranty for manufacturing defects. The warranty period and terms will be provided with your product documentation.":
            "Produktet tona mbulohen nga garancia e prodhuesit për defekte prodhimi. Periudha dhe kushtet e garancisë do të sigurohen me dokumentacionin e produktit tuaj.",
        "For any questions regarding our store policy, please contact us via our contact form.":
            "Për çdo pyetje në lidhje me politikën e dyqanit tonë, ju lutemi na kontaktoni përmes formularit tonë të kontaktit.",
    },

    "impressum": {
        "Imprint": "Impressum",
        "Company: KLERED GmbH": "Kompania: KLERED GmbH",
        "Address: Stadthausstrasse 10b, 8400 Winterthur, Switzerland":
            "Adresa: Stadthausstrasse 10b, 8400 Winterthur, Zvicër",
        "Phone: +41 52 203 1111": "Tel: +41 52 203 1111",
        "Email: info@bbqpitbox.com": "Email: info@bbqpitbox.com",
        "Business Information": "Informacioni i Biznesit",
        "KLERED GmbH is a registered company in Switzerland.":
            "KLERED GmbH është një kompani e regjistruar në Zvicër.",
        "VAT Number: To be provided upon request.":
            "Numri i TVSH-së: Do të sigurohet me kërkesë.",
        "Disclaimer": "Mohim Përgjegjësie",
        "The author reserves the right not to be responsible for the topicality, correctness, completeness or quality of the information provided. Liability claims regarding damage caused by the use of any information provided, including any kind of information which is incomplete or incorrect, will therefore be rejected.":
            "Autori rezervon të drejtën të mos jetë përgjegjës për aktualitetin, korrektësinë, plotësinë ose cilësinë e informacionit të dhënë. Kërkesat për përgjegjësi në lidhje me dëmin e shkaktuar nga përdorimi i çdo informacioni të dhënë, duke përfshirë çdo lloj informacioni që është i paplotë ose i pasaktë, do të refuzohen.",
        "Copyright": "Të Drejtat e Autorit",
        "All content, images, and text on this website are the property of KLERED GmbH unless otherwise stated. Reproduction, distribution, or any other use of the content is prohibited without prior written consent.":
            "I gjithë përmbajtja, imazhet dhe teksti në këtë faqe interneti janë pronë e KLERED GmbH përveç rasteve kur thuhet ndryshe. Riprodhimi, shpërndarja ose çdo përdorim tjetër i përmbajtjes është i ndaluar pa pëlqimin paraprak me shkrim.",
    },
}

def normalize_html_entities(text):
    entities = {
        "&ndash;": "\u2013", "&mdash;": "\u2014",
        "&lsquo;": "\u2018", "&rsquo;": "\u2019",
        "&lbquo;": "\u201e", "&rbquo;": "\u201c",
        "&ldquo;": "\u201c", "&rdquo;": "\u201d",
        "&amp;": "&", "&lt;": "<", "&gt;": ">",
        "&quot;": '"', "&apos;": "'",
        "&deg;": "\u00b0",
    }
    for ent, uni in entities.items():
        text = text.replace(ent, uni)
    return text

def translate_page(page_name):
    if page_name == "index":
        sq_path = os.path.join(BASE, "sq", "index.html")
    else:
        sq_path = os.path.join(BASE, "sq", page_name, "index.html")
    if not os.path.exists(sq_path):
        return

    with open(sq_path) as f:
        html = f.read()

    # Normalize HTML entities to unicode for matching
    html_norm = normalize_html_entities(html)

    # Apply page-specific translations first (full sentences, more specific)
    if page_name in PAGES:
        for eng, sq in PAGES[page_name].items():
            html_norm = html_norm.replace(eng, sq)

    # Apply shared translations second (fragments, less likely to conflict on translated text)
    for eng, sq in SHARED.items():
        html_norm = html_norm.replace(eng, sq)

    # Write back the normalized + translated version
    with open(sq_path, "w") as f:
        f.write(html_norm)
    print(f"  Translated: sq/{page_name}")

def main():
    print("=== Translating SQ content pages ===")
    for page_name in PAGES:
        translate_page(page_name)
    print("\nDone! SQ content pages translated.")

if __name__ == "__main__":
    main()
