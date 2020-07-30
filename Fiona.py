# kennismaking
naam = input ("Hallo, wie ben jij? (Typ je naam en druk op enter) " ).title()
lezen = input ("Kan jij al lezen en schrijven? (Typ ja of nee en druk enter.) ").lower()

if lezen == "ja":
  print (f"\nFijn dat je er bent {naam}, en goed dat je al kunt lezen en typen!" )
elif lezen == "nee":
  print (f"\nFijn dat je er bent {naam}, je zult moeten vragen aan iemand om samen te spelen.")

""" variabelen die een hele tijd meegenomen worden:
    gezonheidspunten: indien deze 0 bereiken is het game over.
    rugzak: wat de speler bij zich heeft om zicht uit lastige situaties te redden.
"""
# beginwaarde aantal gezondheidspunten
gezondheidspunten = 10

""" functions:
        print_health: weergeven hoeveel gezondheidspunten de speler nog over heeft.
            wordt gebruikt in de min_health en plus_health functions.
        check_health: controleren of de speler nog gezondheidspunten over heeft.
            wordt gebruikt in de min_health en plus_health functions.
        min_health: trekt 2 gezondheidspunten af, toont de speler hoeveel gezondheidspunten hij nog heeft en checkt of de speler nog genoeg punten heeft om verder te spelen.
            wordt gebruikt wanneer er iets gebeurt in het spel waarbij de speler gezondheidspunten.
        plus_health: voegt 2 gezondheidspunten toe, toont de speler hoeveel punten hij nog heeft en checkt of de speler nog genoeg punten heeft om verder te spelen.
"""
def print_health (health):
  print (f"Je hebt nu {health} gezondheidspunten.")


def check_health (health):
  if health <= 0:
    print("\n\nJe hebt te veel pijntjes, je moet naar het ziekenhuis en kunt de prinses niet meer redden. \nHopelijk lukt het de volgende keer wel!")
    afsluiten =input ("\n\nOm het spel af te sluiten, typ ja en druk op enter" )
    if afsluiten == "ja":
        exit()


def min_health (health):
  health -= 2
  print_health (health)
  check_health (health)
  return health


def plus_health (health):
  health += 2
  print_health (health)
  check_health (health)
  return health
"""
Voorbeeld voor gebruik min_health function.
print ("Je deed je been pijn en verliest 2 gezondheidspunten")
gezondheidspunten = min_health(gezondheidspunten)
"""

"""
Voorbeeld voor gebruik plus_health function.
print ("Je vond een zalfje en deed dat op een wonde. Je krijgt 2 gezondheidspunten.")
gezondheidspunten = plus_health(gezondheidspunten)
"""




# Intro
print ("\n\nIk kreeg net telefoon van prinses Fiona. \nZe was erg bang... Ze zei dat ze ontvoerd werd. \nFiona wordt ergens in de kelder van een huis in het bos vastgehouden. Ze heeft echt hulp nodig. \nZe kon me nog snel bellen, maar toen namen ze haar gsm mee.\n")
# Start spel?
spelen = input("\n\nWil je me helpen om prinses Fiona te zoeken en haar te redden? (typ ja of nee en dan enter) ").lower()

if spelen == "nee":
  print ("\noh nee, jammer dat je de prinses niet wilt helpen. \nMaar veel plezier met je andere activiteiten. \nIk ga op zoek naar iemand die prinses Fiona wel wil helpen.")
elif spelen == "ja":
  print ("\nOh, wat goed dat je me wilt helpen!!! \nBij elke stap kun je kiezen uit meerdere mogelijkheden, deze staan tussen haakjes. \nHet is belangrijk dat je je keuze op de correcte manier typt en daarna op enter drukt. \n\nKom, laten we snel gaan ")
  # Start variabele rugzak.
  rugzak = input ("\nWe moeten snel vertrekken. Je kunt nog snel 1 iets meenemen, wat kies je? (touw/water/zwemboeitjes/eten) ").lower()
print ("\nKom, waar blijf je nu toch! Als je blijft treuzelen zullen we de prinses nooit vinden…")
startpunt = input ("\n\nWaar wil je naartoe gaan om te beginnen? (links/rechts) ").lower()

# Startpunt links
if startpunt == "links" :

# Meer
    meer = input ("\n\nWe komen aan een meer. Het ziet er een groot meer uit. \nWil je rond het meer wandelen of wil je erdoor zwemmen (wandelen/zwemmen)? ").lower()
    if meer == "wandelen":
        print ("\nAmai dat was lastig. Het meer was groter dan verwacht. \nWandelen rond het meer duurde echt superlang.")
    elif meer == "zwemmen":
        if rugzak == "zwemboeitjes":
            print ("\nIn de helft van het meer was het echt lastig. \nAl goed dat je zwemboeitjes mee had, anders was je misschien verdronken. \nJe bent aan de overkant en hebt je zwemboeitjes terug mee.")
        elif rugzak != "zwemboeitjes":
            print ("\nDat meer was toch groter dan verwacht. \nToen je er bijna was, kon je echt niet meer en was je bijna verdronken. \nGelukkig was er iemand die dit zag en je kon helpen. \nNu ben je wel echt moe. Je verliest 2 gezondheidspunten.")
            gezondheidspunten = min_health(gezondheidspunten)

# Grot
    grot = input ("\n\nOk, je bent aan de overkant en volgt het pad verder.\nHet pad loopt dood. Er is enkel nog een grot. \nWil je door de grot gaan of terugkeren? (grot/terug) ").lower()
    if grot == "grot":
        if rugzak == "eten":
            print ("\nOH NEE! ER ZIT EEN BEER IN DE GROT!! Snel, RENNEN!!!! \nJe kan de beer nog ontwijken door het eten dat je mee had aan de beer te geven. \n Gelukkig maar. \nNu kunnen we niet anders dan terug naar het meer te gaan. Jammer dat we zo veel tijd verloren hebben.")
        else:
            print ("\nOH NEE! ER ZIT EEN BEER IN DE GROT!! Snel, RENNEN!!!! \nJe kon snel genoeg lopen, dus de beer heeft je niet kunnen pakken. \nMaar je bent wel gevallen en hebt je knie pijn gedaan. Je verliest 2 gezondheidspunten. ")
            gezondheidspunten = min_health(gezondheidspunten)
            print ("\n\nNu kunnen we niet anders dan terug naar het meer te gaan. Jammer dat we zo veel tijd verloren hebben.")
    elif grot == "terug":
        print ("\nOk, op naar het meer. Jammer dat we de verkeerde weg gekozen hadden.")

# Meer tweede keer
    meer2 = input ("\n\nWe zijn terug aan het meer. We weten al dat het meer erg groot is. \nAls we er rond wandelen verliezen we nog meer tijd., maar als we er door willen zwemmen wordt het wel erg lastig. \nWat wil je doen? (wandelen/zwemmen). ").lower()
    if meer2 == "wandelen":
        print ("\nAmai, amai, amai. Waarom hebben we dan ook gekozen om richting het meer te wandelen in de eerste plek. \nNu gaan we gewoon terug naar ons startpunt en zijn we zo veel energie en tijd kwijt geraakt. Kom op, dan gaan we verder om de prinses te redden. \nNu gaan we sowieso de andere kant op!")
        startpunt = "rechts"
    elif meer2 == "zwemmen":
        if rugzak == "zwemboeitjes":
            print ("\nToen je er bijna was werd het echt superlastig. \nGelukkig had je je boeitjes mee. Anders had je misschien de overkant niet gehaald. \nWe moeten nu wel terug bij het startpunt beginnen en hebben veel tijd en energie verloren. \nKom op, dan gaan we verder om de prinses te redden. \nNu gaan we sowieso de andere kant op!")
            startpunt = "rechts"
        else:
            print ("\nAmai dat meer was echt groot. Het zwemmen heeft je echt ontzettend moe gemaakt. \nJe verliest 2 gezondheidspunten. ")
            gezondheidspunten = min_health(gezondheidspunten)
            print ("\nWe moeten nu wel terug bij het startpunt beginnen en hebben veel tijd en energie verloren. \nKom op, dan gaan we verder om de prinses te redden. \nNu gaan we sowieso de andere kant op!")
            startpunt = "rechts"


# Startpunt rechts
if startpunt == "rechts":

# Boom
    boom = input ("\n\nJe komt aan bij een boom met mooie stevige takken, perfect om in te klimmen. \nWil je in de boom klimmen om te kijken wat je volgende stappen zullen zijn. (ja/nee)? ").lower()
    if boom == "ja":
        print ("\nJe klimt in de boom en je ziet het bos in de verte. \nHet ziet eruit dat je een hutje moet passeren en daarna over een berg moet klimmen.")
    elif boom == "nee":
        print ("\nOk, dan hopen we maar dat we steeds de juiste richting uit lopen.")
# Splitsing
    splitsing = input ("\n\nJe bent al een hele tijd aan het stappen en het begint donker te worden. \nDe weg splitst. Aan de ene kant zie je in de verte een hutje. \nAan de andere kant kronkelt het pad erg veel dus kun je niet zien waar het heen gaat. \nWelke richting kies je? (hutje/kronkelpad) ").lower()
    if splitsing == "kronkelpad":
        print ("\nJe volgt het kronkelpad een hele tijd. \nOndertussen is het donker en zie je bijna niets meer. \nPlots val je naar beneden in een klif die je niet had gezien.")
        if rugzak == "touw":
            print ("\nJe kan nog snel het touw nemen dat je meegenomen had en die over een steen gooien. \nZo kan je ervoor zorgen dat je toch niet helemaal in de ravijn valt en jezelf terug naar boven trekken. \nJe beslist dat je toch beter het andere padje had genomen en keert terug.")
            splitsing = "hutje"
        else:
            print ("\nJe valt in de ravijn en raakt gewond. Je verliest 2 gezondheidspunten. ")
            gezondheidspunten = min_health(gezondheidspunten)
            print ("\nHet is erg moeilijk, maar je kan toch terug naar boven klimmen. \nJe beslist dat je toch beter het andere padje had genomen en keert terug. ")
            splitsing = "hutje"
    if splitsing == "hutje":
        hutje = input ("\n\nJe bent aangekomen bij het hutje, ondertussen is het al middernacht. \nWil je graag even rusten of wil je blijven doorgaan (rusten/ doorgaan)? ").lower()
        if hutje == "rusten":
            print ("\nGoed gedaan, door dat rusten voel je je veel beter! Je krijgt 2 gezondheidspunten extra.")
            gezondheidspunten = plus_health(gezondheidspunten)
            print ("\nJe staat op en begint onmiddellijk het padje verder te volgen.")
        elif hutje == "doorgaan":
            print ("\nHet is donker en je ziet bijna niets, maar je gaat toch door. \nJe wandelt maar door en door tot je het einde van het padje bereikt. \nDoordat het zo donker is ben je al een paar keer gevallen. \nJe staat vol met muggenbeten en je bent doodmoe. \nJe verliest 2 gezondheidspunten.")
            gezondheidspunten = min_health(gezondheidspunten)

# Berg
    berg = input ("\n\nEr zijn 2 padjes. \nEén padje heeft wat rotsen en stenen en gaat over de berg, het andere padje gaat langs de berg. \nWelk padje kies je (over/langs)? ")
    if berg == "over":
        print ("\nHet was wat moeilijk, maar je hebt de berg beklommen. \nNu je zo hoog staat zie je beneden het bos liggen. \nIemand heeft een heel grote glijbaan gemaakt die naar het bos gaat. \nJe neemt de glijbaan en bent supersnel beneden. Dat was echt leuk!!! Je krijgt 2 gezondheidspunten.")
        gezondheidspunten = plus_health(gezondheidspunten)
    elif berg == "langs":
        print ("\nJe maakt een erg lange wandeling langs 3 andere bergen en doet er ontzettend lang over. \nUiteindelijk kom je toch bij het bos.")

# Open plek
    open_plek = input ("\n\nJe hebt al een stuk in het bos gewandeld wanneer je aan een open plek komt. Je beslist om even te rusten en te genieten. \nIn het midden van de open plek staat een heel mooie grote bloem. Wil je die even gaan bekijken (ja/nee)? ").lower()
    if open_plek == "ja":
        print ("\nje beslist om aan de bloem te ruiken, maar plots grijpen de blaadjes je vast en trekken ze je naar binnen in de bloem. \nEen paar seconden later spuwt de bloem je terug uit, maar nu hang je vol stuifmeel en je ziet de bijen al naar je toe komen.")
        if rugzak == "water":
            print ("\nJe weet dat je je heel snel zal moeten wassen voor de bijen er zijn. \nje neemt snel het water dat je mee had en spoelt jezelf helemaal af. \nNu ben je helemaal nat, maar je bent niet gestoken door een bij. \nGelukkig maar!")
        else:
            print ("\nJe loopt nog snel weg van de bijen, maar door de bloem plak je ook helemaal en kun je niet zo snel lopen. \nDe bijen halen je in en je hebt wel 10 bijensteken!! \nJe verliest 2 gezondheidspunten.")
            gezondheidspunten = min_health(gezondheidspunten)
    elif open_plek == "nee":
        print ("\nJe vind dat het goed genoeg is om van op afstand naar de bloem te kijken. Ze is toch groot genoeg. \nWat later ga je verder met de zoektocht naar de prinses.")

# Waterval
    waterval = input ("\n\nJe wandelt nog een heel stuk door het bos, tot je een mooie waterval ziet. \nEr is een padje langs de waterval, maar de waterval ziet er ook uit alsof je achter het water kan. \nWil je langs de waterval wandelen of wil je toch proberen om erdoor te gaan. (langs/door) ").lower()
    if waterval == "langs":
        print ("\nJe wandelt langs de waterval en ziet een huisje in het midden van het bos… \nDaar moet prinses Fiona gevangen zitten! \nJe rent naar het huisje, struikelt over een draadje en plots hang je in een groot net aan een boom. \nJe werd gevangen. Je roept om hulp, en plots komen er 3 kabouters uit het huisje. \nZe maken je handen aan elkaar vast en nemen je mee naar het huisje. \nJe legt uit dat je de prinses wilt redden en dat ze gevangen werd. \nDe kabouters maken je los en zeggen dat er een geheim pad is achter de waterval en dat daar het huis is van de gemene tovenaar. \nDie moet vast en zeker de prinses ontvoerd hebben. \nJe rent snel terug naar de waterval en gaat onder de waterval door.")
    elif waterval == "door":
        print ("\nJe wandelt in de richting van de waterval, maar je moet voorzichtig zijn dat je niet uitglijdt, want anders val je in het water. \nJe gaat onder de waterval door.")

# Geheim pad
    geheim_pad = input ("\n\nEens je onder de waterval bent, kom je in een ontzettend mooie grot met allerlei glimmende stenen en overal zie je mooie diertjes in allerlei kleurtjes. \nHet is echt magisch. Je bent naar één van de diertjes aan het kijken en plots zie je dat het in een gleufje gaat achter een rots en dan is het weg. \nWil je de grot verder verkennen en een ander padje zoeken of wil je het diertje volgen? (verkennen/volgen)? ").lower()
    if geheim_pad == "verkennen":
        print ("\nJe loopt door de grot, het wordt steeds donkerder en donkerder, plots zak je weg in een put met slijm. \nNu ben je echt supersmerig, maar je kan wel uit de slijmput geraken. \nJe verliest 2 gezondheidspunten.")
        gezondheidspunten = min_health(gezondheidspunten)
        print ("\nDan nemen we misschien toch beter het andere padje.")
        geheim_pad = "volgen"
    if geheim_pad == "volgen":
        print ("\nJe gaat door de gleuf waar het diertje in ging. \nHet diertje is ondertussen weg, maar je komt bij een magische plek waar eenhoorns aan het eten zijn. \nAlle bomen en planten hebben mooie kleuren en wat verder zie je een rivier die alle kleuren van de regenboog heeft. ")

# Rivier
    rivier = input ("\n\nJe wandelt naar de rivier en je ziet dat er een gouden padje is die naar allebei de kanten van de rivier lopen. \nWil je stroomafwaarts lopen of stroomopwaarts (af/op)? ").lower()
    if rivier == "af":
        print ("\nHet gouden pad wordt steeds donkerder en donkerder. \nOok de bomen en de planten zien er niet meer goed uit en de rivier stroomt nu zwart dik water. \nJe maakt je wat zorgen en je bent wat bang. \nJe stapt toch dapper door, want je wil heel graag de prinses redden. ")
    elif rivier == "op":
        print ("\nJe wandelt stroomopwaarts en het padje gaat omhoog. \nJe wandelt steeds steiler omhoog en het is echt lastig. \nJe bent ook al moe van al die avonturen die je al beleefd hebt. \nOp het moment dat je denkt dat je toch beter stroomafwaarts had gelopen, verandert het pad in een glijbaan. \nJe glijdt naar beneden, voorbij de mooie tuin met de eenhoorns van daarstraks. \nJe ziet dat het pad steeds donkerder en donkerder wordt. \nOok de bomen en de planten zien er niet meer goed uit en de rivier stroomt nu zwart dik water. \nJe maakt je wat zorgen en je bent wat bang, maar je kan jezelf niet tegenhouden en je glijdt helemaal naar beneden. \nOp een bepaald moment zie je dat er een boom op het einde van de glijbaan staat en je knalt tegen de boom. \nJe verliest 2 gezondheidspunten.")
        gezondheidspunten = min_health(gezondheidspunten)
        print ("\nNadat de pijn wat weg is, zie je dat de glijbaan terug veranderd is in een pad.")

# Huis
    huis = input("\n\nPlots hoor je een zware mannenstem roepen. \nJe verstopt je snel achter 1 van de zwarte struiken en je bent heel stil. \nDe man wandelt over het pad in de richting van de eenhoorntuin. \nAls hij even gepasseerd is zie je wat verder een huis. \nDat moet het huis zijn waar de prinses gevangen zit. \nJe rent naar het huis en gaat naar binnen. Het is een erg eng, donker huis. \nAllemaal dode dieren aan de muur, een grote heksenketel op het vuur, overal flitsen vreemde lichten,… \nJe ziet 2 deuren.  Een witte en een zwarte. \nDoor welke deur wil je gaan (wit/zwart)? ").lower()
    if huis == "wit":
        print ("\nJe doet de witte deur open en wordt verblind door een wit licht. \nJe stapt in de kamer, maar kan nog steeds niet goed zien. \nPlots hoor je uit het niets een stem. \nAls je goed kijkt zie je een eenhoorn door de lucht vliegen. \nDe eenhoorn zegt dat de boze tovenaar hem ook had opgesloten, maar dat hij zichzelf kan bevrijden als je de deur open laat. \nDe eenhoorn zegt ook dat de prinses verstopt zit in de zwarte kamer. \nJe laat dus de deur open en gaat snel naar de zwarte kamer.")
        huis = "zwart"
    if huis == "zwart":
        print ("\nJe doet de deur open van de zwarte kamer en ziet de prinses. \nZe is vastgebonden en ziet er vuil uit. \nJe maakt haar snel los en samen lopen jullie uit het huis, terug naar de eenhoorntuin.")
        print ("\nDaar zie je dat de boze tovenaar weer een eenhoorn aan het proberen te vangen is. \nJe ziet ook de eenhoorn van in het huis van de tovenaar. \nDe eenhoorn komt naar jullie toe en vraagt om te helpen de boze tovenaar te veranderen. \nAls we hem in de regenboogrivier kunnen duwen dan zal de tovenaar lief worden en zal het volledige bos er ook weer goed uit zien. \nJe spreekt met de eenhoorn af dat je 1 van de takken zal pakken die op de hoogte van het gezicht van de tovenaar hangt en dat je die zal laten schieten tegen zijn gezicht.")
        print ("\nJe gaat door de struiken naar de tak en geeft een seintje aan de prinses. \nDe prinses roept de tovenaar en de tovenaar schrikt omdat de prinses vrij is. \nOp hetzelfde moment laat jij de tak los en schiet de tak in het gezicht van de tovenaar. \nDe tovenaar weet niet wat er gebeurd en loopt achteruit richting rivier. \nOp een rotsblok aan de rand van de rivier probeert de tovenaar zich nog tegen te houden, maar de eenhoorn duwt hem in het water. \nDe slechte magie van de tovenaar wordt helemaal van hem afgespoeld en je ziet ook het bos terug helemaal kleurrijk worden.")
        print ("De tovenaar komt terug uit het water en voelt zich veel beter. \nHij bedankt jullie om hem te bevrijden van de kwaadaardigheid en samen met de eenhoorns en de prinses doen jullie een groot feest. \nDe prinses had nog wel even tijd nodig want die moest zich nog wassen in de rivier. \nNa het feest gaan jullie naar huis en de prinses is superblij dat ze gered werd. \nElk jaar gaan jullie nog terug naar de eenhoorntuin en de tovenaar voor een groot feest… \n\nTHE END!!")
# Spel afsluiten?
afsluiten = input ("\n\nWil je het spel afsluiten? (ja/nee)")
if afsluiten == "ja":
    exit()
