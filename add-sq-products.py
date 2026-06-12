#!/usr/bin/env python3
"""Add SQ description translations to products.json."""

import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(BASE, 'products.json')

with open(fp) as f:
    data = json.load(f)

# SQ translations for descriptions
SQ = {}
SQ["backyard-hero"] = "Seria Backyard Hero \u00ebsht\u00eb linja ideale e furrave p\u00ebr familjet private q\u00eb duan t\u00eb p\u00ebrjetojn\u00eb tymosje autentike BBQ. Me gjurm\u00eb kompakte dhe dizajne efikase, k\u00ebto furra japin rezultate profesionale n\u00eb nj\u00eb paket\u00eb q\u00eb p\u00ebrshtatet n\u00eb \u00e7do oborr."
SQ["gf-serie"] = "Seria GF \u00ebsht\u00eb linja jon\u00eb m\u00eb e shitur e furrave me ushqim nga graviteti, e dizajnuar p\u00ebr ambiente tregtare k\u00ebrkuese. Me kapacitete nga 30 deri n\u00eb 110 kg p\u00ebr sesion, k\u00ebto nj\u00ebsi japin shije t\u00eb q\u00ebndrueshme dhe autentike tymi n\u00eb shkall\u00eb t\u00eb gjer\u00eb."
SQ["bfb-rf"] = "Seria BFB RF paraqet teknologjin\u00eb reverse flow p\u00ebr shp\u00ebrndarje t\u00eb barabart\u00eb t\u00eb nxeht\u00ebsis\u00eb dhe ruajtje t\u00eb lag\u00ebshtir\u00ebs. E p\u00ebrkryer si p\u00ebr entuziast\u00eb privat\u00eb ashtu edhe p\u00ebr operator\u00eb tregtar\u00eb q\u00eb k\u00ebrkojn\u00eb q\u00ebndrueshm\u00ebri."
SQ["b-oven"] = "B Oven \u00ebsht\u00eb nj\u00eb furr\u00eb tradicionale buke dhe pjekjeje me dru q\u00eb sjell shijen autentike t\u00eb buk\u00ebs s\u00eb pjekur me dru dhe mishit t\u00eb pjekur n\u00eb kuzhin\u00ebn tuaj. Mjaft kompakte p\u00ebr p\u00ebrdorim privat dhe e aft\u00eb p\u00ebr aplikime t\u00eb lehta tregtare."
SQ["d-oven"] = "Seria D Oven ofron nj\u00eb gam\u00eb t\u00eb gjithanshme furrash me dru t\u00eb p\u00ebrshtatshme p\u00ebr \u00e7do gj\u00eb nga grumbullimet private deri te operacionet profesionale t\u00eb kateringut. \u00c7do model \u00ebsht\u00eb punuar me dor\u00eb p\u00ebr mbajtje dhe shp\u00ebrndarje optimale t\u00eb nxeht\u00ebsis\u00eb."
SQ["asado-grill"] = "Seria ASADO Grill kombinon pjekjen tradicionale argjentinase asado me dizajn modern. K\u00ebto vatra zjarri t\u00eb l\u00ebvizshme jan\u00eb perfekte si p\u00ebr grumbullime intime ashtu edhe p\u00ebr evente n\u00eb shkall\u00eb t\u00eb gjer\u00eb."
SQ["offset-bbq"] = "Furrat offset t\u00eb shkall\u00ebs profesionale t\u00eb dizajnuara p\u00ebr operacione serioze BBQ. Me kapacitete nga 10 deri n\u00eb 210 kg p\u00ebr sesion, k\u00ebto nj\u00ebsi jan\u00eb nd\u00ebrtuara p\u00ebr p\u00ebrdorim tregtar me v\u00ebllim t\u00eb lart\u00eb ku q\u00ebndrueshm\u00ebria dhe shija jan\u00eb par\u00ebsore."
SQ["nyp-offset"] = "Seria NYP Offset BBQ sjell tymosjen profesionale offset n\u00eb mund\u00ebsi t\u00eb entuziast\u00ebve serioz\u00eb t\u00eb sht\u00ebpis\u00eb dhe operacioneve t\u00eb vogla tregtare. Kompakte por t\u00eb fuqishme, k\u00ebto furra japin shije autentike offset."
SQ["whole-hog"] = "Whole Hog \u00ebsht\u00eb furra jon\u00eb offset m\u00eb e madhe, e dizajnuar p\u00ebr operator\u00eb tregtar\u00eb serioz\u00eb q\u00eb kan\u00eb nevoj\u00eb p\u00ebr kapacitet masiv pa kompromentuar shijen. E aft\u00eb p\u00ebr t\u00eb tymosur derra t\u00eb t\u00ebr\u00eb, briskets t\u00eb shumta ose sasi t\u00eb m\u00ebdha brinj\u00ebsh n\u00eb nj\u00eb sesion t\u00eb vet\u00ebm."

SQ["compact-smoker-xxs"] = "Compact Smoker XXS \u00ebsht\u00eb nj\u00eb zgjidhje efikase p\u00ebr tymosje, perfekte p\u00ebr kuzhina t\u00eb vogla, restorante pop-up dhe familje private me hap\u00ebsir\u00eb t\u00eb kufizuar."
SQ["compact-smoker-xxs-plus"] = "Compact Smoker XXS Plus ofron kapacitet shtes\u00eb n\u00eb krahasim me modelin XXS duke ruajtur nj\u00eb gjurm\u00eb kompakte."
SQ["compact-smoker-xs"] = "Compact Smoker XS mbush hendekun midis kapacitetit kompakt dhe standard, ideal p\u00ebr bizneset n\u00eb rritje."
SQ["compact-smoker-s"] = "Compact Smoker Size S \u00ebsht\u00eb dizajnuar p\u00ebr operacione serioze gastronomie q\u00eb kan\u00eb nevoj\u00eb p\u00ebr prodhim t\u00eb q\u00ebndruesh\u00ebm."
SQ["smoker-size-s"] = "BBQ Pit Box Smoker Size S ofron aft\u00ebsi t\u00eb gjithanshme tymosjeje n\u00eb nj\u00eb paket\u00eb t\u00eb madh\u00ebsis\u00eb s\u00eb mesme."
SQ["duck-oven-xs"] = "Duck Oven XS specializohet n\u00eb ros\u00eb, shpend\u00eb dhe pjekje n\u00eb nj\u00eb form\u00eb kompakte."
SQ["duck-oven-xs-plus"] = "Duck Oven XS Plus ofron kapacitet shtes\u00eb pjekjeje duke ruajtur kontrollin e sakt\u00eb t\u00eb temperatur\u00ebs."
SQ["duck-oven-s"] = "Duck Oven Size S \u00ebsht\u00eb nd\u00ebrtuar p\u00ebr pjekje t\u00eb v\u00ebllimit t\u00eb mes\u00ebm me nxeht\u00ebsi t\u00eb q\u00ebndrueshme dhe t\u00eb barabart\u00eb."
SQ["duck-oven-m"] = "Duck Oven Size M trajton v\u00ebllime m\u00eb t\u00eb larta duke ruajtur cil\u00ebsin\u00eb karakteristike t\u00eb pjekjes."
SQ["duck-oven-l"] = "Duck Oven Size L \u00ebsht\u00eb furra jon\u00eb m\u00eb e madhe e pjekjes, e aft\u00eb p\u00ebr t\u00eb trajtuar derra t\u00eb t\u00ebr\u00eb dhe porosi t\u00eb m\u00ebdha katering."
SQ["yakitori-bbq-grill-s"] = "Yakitori BBQ Grill Size S sjell pjekjen tradicionale japoneze yakitori n\u00eb kuzhin\u00ebn ose eventet tuaja."
SQ["yakitori-bbq-grill-m"] = "Yakitori BBQ Grill Size M ofron kapacitet m\u00eb t\u00eb madh p\u00ebr sh\u00ebrbim yakitori me v\u00ebllim t\u00eb lart\u00eb."
SQ["yakitori-bbq-grill-l"] = "Yakitori BBQ Grill Size L \u00ebsht\u00eb nd\u00ebrtuar p\u00ebr operacione tregtare me kapacitet maksimal hellash."
SQ["nyp-regular-offset-xs"] = "NYP Regular Offset XS \u00ebsht\u00eb furra offset hyr\u00ebse p\u00ebr entuziast\u00ebt q\u00eb duan shije autentike offset."
SQ["nyp-regular-offset-s"] = "NYP Regular Offset S rrit kapacitetin duke ruajtur kontrollin e sakt\u00eb t\u00eb temperatur\u00ebs."
SQ["whole-hog-monster"] = "Whole Hog BBQ Grill \u00ebsht\u00eb furra jon\u00eb offset m\u00eb e madhe e dizajnuar p\u00ebr kapacitet masiv tregtar."

# Add description_sq to series
for s in data["series"]:
    slug = s["slug"]
    if slug in SQ:
        s["description_sq"] = SQ[slug]
    for v in s["variants"]:
        v_slug = v["slug"]
        if v_slug in SQ:
            v["description_sq"] = SQ[v_slug]

# Add description_sq to individuals
for p in data["individuals"]:
    slug = p["slug"]
    if slug in SQ:
        p["description_sq"] = SQ[slug]

with open(fp, 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated products.json with {len(SQ)} SQ translations")
