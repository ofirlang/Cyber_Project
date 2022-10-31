decoded = "ehT neZ fo nohtyP yb miT lufituaeB sreteP si retteb naht ticilpxE ylgu si retteb naht elpmiS ticilpmi si retteb naht xelpmoC xelpmoc si retteb naht talF detacilpmoc si retteb naht esrapS detsen si retteb naht ytilibadaeR esned laicepS stnuoc sesac tnera laiceps hguone ot kaerb eht hguohtlA selur ytilacitcarp staeb srorrE ytirup dluohs reven ssap sselnU yltnelis ylticilpxe nI decnelis eht ecaf fo ytiugibma esufer eht noitatpmet ot erehT sseug dluohs eb eno dna ylbareferp ylno eno suoivbo yaw ot od hguohtlA ti taht yaw yam ton eb suoivbo ta tsrif sselnu eruoy woN hctuD si retteb naht hguohtlA reven reven si netfo retteb naht thgir fI won eht noitatnemelpmi si drah ot nialpxe sti a dab fI aedi eht noitatnemelpmi si ysae ot nialpxe ti yam eb a doog secapsemaN aedi era eno gniknoh taerg aedi stel od erom fo esoht"""
decoded = decoded.split()
for word in decoded:
    word = word[::-1]
    print(word + " ", end='')

print()
print(decoded)