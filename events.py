import random




#all events

def event_0():
    print("juhu")

# def event_1():
#     print("Dir wird berichtet, dass eine Gruppe ausgehungerter Kinder in den Wäldern nahe deines Dorfes lebt. Möchtest du sie aufnehmen?")
#     answer = input("Ja oder Nein?")
#     if answer.lower() == "Ja" or "ja":
#         for i in 5:
#             create_villager(random.randint(1, 15), random.choice(["female","male"]), random.randint(10, 40))  # create minor villager
#             change_resources(-30)
#         print("Die Kinder schliessen sich dankbar deiner Dorfgemeinschaft an. Allerdings sind sie in einem schlechten gesundheitlichen Zustand\nund benötigen viele Ressourcen, um nur schon eine Chance zu haben, die nächsten Tage zu überleben.")
#     else:
#         print("Du triffst die harte Entscheidung, die Ressourcen deines Dorfes für deine eigenen Dorfbewohner zu sparen.\nNach und nach verstummen die Geräusche aus dem Wald.")
#
#
# def event_2():
#     print("Ein hustender Händler klopft ans Tor des Dorfes. Er ist erschöpft und bittet darum, aufgenommen und gesund gepflegt zu werden.\nIm Gegenzug will er euch 30 seiner Ressourcen überlassen. Stimmst du zu?")
#     answer = input("Ja oder Nein?")
#     if answer.lower() == "Ja" or "ja":
#         reduce_health_of_all_villagers(30)
#         change_resources(30)
#         print("Der Händler schwört dir ewige Dankbarkeit. Eine Woche später reist er, um seine Ressourcen erleichtert,\nwieder ab. Doch als du auf den Dorfplatz trittst, und von überall her Husten hörst, fragst du dich, ob es das wert gewesen war...")
#     else:
#         print("Der Händler reist verzweifelt ab. Sein Husten klingt noch lange in deinen Ohren nach...")
#
#
# def event_3():
#     print("Ein sehr charismatischer Mann erscheint eines Morgens am Dorfeingang. Jeder Mensch, mit dem er spricht,\nist sofort in seinen Bann gezogen. Er möchte ins Dorf ziehen. Möchtest du ihm diesen Wunsch gewähren?")
#     answer = input("Ja oder Nein?")
#     if answer.lower() == "Ja" or "ja":
#         create_villager(random.randint(18, 85), "male", random.randint(20, 100)) #create male adult villager named Dolus
#         print("Der Mann freut sich über deine Antwort und zieht zugleich ins Dorf. Er wird schnell zum neuen Liebling\nund alle Dorfbewohner hängen an seinen Lippen.")
#         doom3 = 1
#     else:
#         print("Eine groteske Grimasse zieht über das Gesicht des Mannes. Er fängt an zu schreien und stampft wütend davon. Nicht alles was glänzt ist gold!")
#
# def event_3b():
#     #if Dolus is still alive
#     print("Der Mann hat eine Sekte aufgebaut und verlässt eines Morgens mit 5 weiteren Bewohnern das Dorf, ohne jemals zurückzukehren.")
#     #Dolus und 5 random Leute löschen
#     doom3 = 0
#
# def event_4():
#     print("Ein Bote kommt mit einer düsteren Botschaft zu euch: Entweder, das Dorf schliesst sich freiwillig dem Herzogtum Balisgtal an,\noder der Herzog schickt seine Soldaten, um das Dorf einzunehmen.")
#     answer = input("Anschliessen oder Kämpfen?")
#     if answer.lower() == "Anschliessen" or "anschliessen":
#         #von nun an 10% weniger Ressourcen, da Abgaben
#         print("Der Herzog ist erfreut und deine Dorfbewohner sicher. Dafür nimmt sich der Herzog nun jeden Monat 10% deiner Ressourcen. War es das wohl wert?")
#     else:
#         print(village.name, "soll unabhänngig bleiben! Deine Dorfbewohner verteidigen das Dorf ehrenvoll.\n20% der Männer zwischen 12 und 60 sterben, doch das Dorf bleibt frei.")
#         #20% der Männer zwischen 12 und 60 sterben
#
# def event_5():
#     print("Dieser Sommer ist besonders heiss. Das Wasser im Brunnen geht langsam aber sicher zu Neige.\nSollen die Dorfbewohner im Schatten bleiben und weniger arbeiten, oder aber das Wasser aus dem dreckigen Fluss trinken?")
#     answer = input("Schatten oder Fluss?")
#     if answer.lower() == "Schatten" or "schatten":
#         print("Deine Dorfbewohner versuchen, so wenig wie möglich zu schwitzen. Tatsächlich geht der Wasservorrat gerade noch so auf, und niemand muss verdursten.\nAllerdings konnten die Dorfbewohner in dieser Zeit keine Ressourcen erarbeiten.")
#         change_resources(-40)
#     else:
#         print("Deine Dorfbewohner sind nun nicht mehr durstig und arbeiten wie gehabt weiter. Das dreckige Wasser hat aber Auswirkungen auf ihre Gesundheit...")
#         reduce_health_of_all_villagers(30)
#
# def event_6():
#     print("Eine mysteriöse Frau steht eines morgens vor dem Tor. Sie verkauft zwei verschiedene Elixiere. Jedes kostet 20 Ressourcen. Welches möchtest du kaufen?")
#     answer = input("Fruchtbarkeit, Gesundheit oder keines?")
#     if answer.lower() == "Fruchtbarkeit" or "fruchtbarkeit":
#             # Fruchtbarkeit aller Frauen ab 16 für 1 Jahr um 30 erhöhen
#         change_resources(-20)
#         print("Du verteilst das Elixier all deinen Einwohnern. Wirst du in wenigen Monaten einen Baby-Boom beobachten können?")
#     elif answer.lower() == "Gesundheit" or "gesundheit":
#         change_resources(-20)
#         # Gesundheit aller Bewohner ab 16 für 1 Jahr um 30 erhöhen
#         print("Du verteilst das Elixier all deinen Einwohnern. Sie sehen bereits ein bisschen gesünder als zuvor aus!")
#     else:
#         print("Die Frau verschwindet so schnell wie sie gekommen war. Wer weiss, ob ihre Elixiere dir tatsächlich geholfen hätten...")
#
# def event_7():
#     victim = random.choice(female_villagers)
#     offender = random.choice(male_villagers)
#     print("Eine blutige Bandage verbigt das Auge von", name.victim, "die deine Hilfe ersucht. Sie erzählt, dass sie von", name.offender, ",\ndem reichsten Mann im Dorf geschlagen wurde. Du hast den Eindruck, er wird als wie gewaltätiger. Was möchtest du tun?")
#     answer = input("Verbannen oder Verzeihen?")
#     if answer.lower() == "Verbannen" or "verbannen":
#         del (offender)
#         change_resources(-20)
#         print("Die Dorfbewohner bedanken sich bei dir. Sie fühlen sich jetzt alle sicherer.\nDer Wegzug von " , name.offender,  "hinterlässt allerdings ein klaffendes Loch in der Dorfkasse.")
#     else:
#         kill_villager(victim)
#         print("Jemand so reiches aus dem Dorf zu verbannen, kannst du dir einfach nicht leisten - Gefahr hin oder her!\nAm nächsten Tag findest du", name.victim, "tot in einem Innenhof")
#
#
# def event_8():
#     print("Ein Zirkus fährt durchs Dorf. Der Direktor beobachtet, wie [Kind] akrobatisch auf einem Baum herumklettert.\nEr ist begeistert und bietet 20 Ressourcen dafür an, ihm das Kind zu verkaufen")
#     answer = input("Verkaufen oder Ablehnen?")
#     if answer.lower() == "Verkaufen" or "verkaufen":
#             # Kind wird deleted
#         change_resources(20)
#         print("Die Schreie von Kind und seiner Eltern klingen noch lange in deinen Ohren nach. Doch das Dorf kann die neuen Ressourcen gut gebrauchen.")
#         doom8 = 1
#     else:
#         print("Das Kind und seine Familie sind erleichtert, und der Direktor verlässt genervt das Dorf.")
#
# def event_8b():
#     print("Plötzlich locken dich Schreie an dein Fenster. Auf dem Dorfplatz siehst du, wie ein junger Mensch drei Leute niedersticht,\nbevor er selber getötet wird. Als du dir den Täter aus der Nähe anschaust realisierst du, dass du ihn kennst. Offensichtlich hat KIND seinem Dorf nie verziehen, dass ihr es an den Zirkus verkauft habt.")
# # kill random villager *3
#     doom8 = 0
#
# def event_9():
#     print("Der Betreiber eines Waisenhauses klopft an euer Tor. Er kann es sich nicht mehr leisten, seinen Betrieb weiterzuführen.\nEr bittet euch darum, ihm entweder 30 Ressourcen zu geben oder 5 Babies zu adoptieren. Was machst du?")
#     answer = input("Zahlen, Adoptieren, oder Ablehnen?")
#     if answer.lower() == "Zahlen" or "zahlen":
#         change_resources(-20)
#         print("Der Betreiber ist begeistert und dankt dir, für deine Grosszügigkeit. Mitsamt seinen Schützlingen macht er sich auf den Heimweg.")
#     elif answer == "Adoptieren" or "adoptieren":
#         print("Der Betreiber ist begeistert und überlässt dir alle fünf Babies.")
#         for i in range (5):
#             create_villager(random.randint(1, 2), random.choice(["female","male"]), random.randint(20, 100))
#     else:
#         print("Der Betreiber fleht verzweifelt um Hilfe, aber du bleibst bei deiner Entscheidung.\nEr macht sich mit seinen Schützlingen auf die Weiterreise. Was wohl mit ihnen passieren wird?")
#
#
#
# def event_10():
#     print("Einer deiner Dorfbewohner hat beim Buddeln ein kleines Stückchen Gold gefunden. Möchtest du 30 Ressourcen investieren, um nach weiterem Gold zu schürfen, oder ist es dir das Risik nicht wert?")
#     answer = input("Schürfen oder Verzichten?")
#     if answer.lower() == "Schürfen" or "schürfen":
#         chance_gold = random.randint(0, 100)
#         if chance_gold > 90:
#                 change_resources(100)
#                 print("Unglaublich, du stösst tatsächlich auf ein riesiges Goldvorkommen! Deine Schatzkammer ist nun gut gefüllt.")
#         elif chance_gold > 70:
#                 print("Du findest tatsächlich ein bisschen Gold. Doch nur gerade genug, um deine Ausgaben wieder reinzuholen. Gewinn machst du keinen.")
#         else:
#                 print("Leider findest du kein bisschen Gold. Frustriert gibst du auf.")
#                 change_resources(-30)
#     else:
#             print("Du lässt dich nicht von potenziellen Reichtümern locken. Deine Dorfbewohner haben schliesslich einen vernünftigen Leader verdient...\nAber was, wenn da doch Gold unter der Erde liegt?")
#
#
# def event_11():
#     print("Ein merkwürdig gekleideter alter Mann klopft an dein Tor und schreit: Heute ist Tag der Alten!\nDiese Gruppe wird viel zu wenig wertgeschätzt. Deshalb schenke ich heute jedem Menschen über 60 zehn Goldtaler!")
#           old_people = 0
#           for villager in villagers:
#             if villager.age > 60:
#                 change_resources(10)
#                 old_people += 1
#     if old_people > 6:
#     print("Wow, ",old_peple,"alte Leute! Dein Dorf ist zwar ein halbes Altersheim, aber dieses mal lohnt sich das auch!")
#     if old_people < 3:
#     print("Nur",old_peple," alte Leute? Es scheint, als würdest du alte Leute hassen...")
#
#
#
# def event_12():
#     print("Der König braucht mehr Bedienstete. Wähle eine Personengruppe, welche du dem König für immer zusendest.")
#     answer = input("Kinder,Alte, Weibliche oder Männliche?")
#     if answer.lower() == "Kinder"
#           for villager in villagers:
#             if villager.age < 12:
#                 #delete
#         print("Alle Kinder wurden dem König entsendet.")
#     elif answer.lower() == "Alte":
#           for villager in villagers:
#             if villager.age > 60:
#                 #delete
#         print("Alle Alten wurden dem König entsendet.")
#     elif answer.lower() == "Weibliche" or "weiblich":
#           for villager in villagers:
#             if villager.gender == "female"
#                 #delete
#         print("Alle Mädchen und Frauen wurden dem König entsendet.")
#     elif answer.lower() == "Männlich" or "männliche"
#           for villager in villagers:
#             if villager.gender == "male"
#                 #delete
#         print("Alle Männer wurden dem König entsendet.")
#
#
# def event_13():
#     print("Ein edel gekleideter Mann klopft an dein Tor. Anscheinend ist er Marketingexperte.\nEr bietet an, Werbung für dein Dorf zu machen, damit neue Leute zuziehen.\nWie viel möchtest du in diese Werbung investieren?")
#     answer = input("0,10 oder 30 Ressourcen zahlen?")
#     if answer == "0":
#         print("Der Mann verabschiedet sich höflich und zieht von Dannen.")
#         return answer #dies sollte die Funktion beenden
#     elif answer.lower() == "10":
#         anz_neue_db = 4
#     elif answer.lower() == "30":
#         anz_neue_db = 12
#     print("Der Mann freut sich, dass du mit ihm Geschäfte machen willst. Welche Personengruppe willst du denn anwerben?")
#     answer = input("Kinder,Alte, Weibliche oder Männliche?")
#     if answer.lower() == "Kinder"
#           #anz_neue_db neue Kinder generieren
#         print(anz_neue_db,"neue Kinder sind zu deinem Dorf hinzugestossen.")
#     elif answer.lower() == "Alte":
#                 # anz_neue_db neue Kinder generieren
#                 print(anz_neue_db, "neue alte Menschen sind zu deinem Dorf hinzugestossen.")
#     elif answer.lower() == "Weibliche" or "weiblich":
#                 # anz_neue_db neue mädchen und Frauen generieren
#                 print(anz_neue_db, "neue Mädchen und Frauen sind zu deinem Dorf hinzugestossen.")
#     elif answer.lower() == "Männlich" or "männliche"
#                 # anz_neue_db neue Jungen und Männer generieren
#                 print(anz_neue_db, "neue Jungen und Männer sind zu deinem Dorf hinzugestossen.")
#
# def event_14():
#     print("Einer deiner Dorfbewohner hat im Wald ein seltenes und hoch wirksames Heilkraut gefunden.")
#     answer = input("Welchem deiner Dorfbewohner möchtest du dieses zu essen geben?")
#     for villager in villagers:
#         if villager.name = answerlower()
#             villager.health = 100
#     print("Gratulation,", answer, "wirkt nun wieder deutlich gesünder!")
#
#
# def event_15():
#     print("Eines Morgens bemerkst du, dass in euer Lagerhaus eingebrochen wurde! An der Tür hängt ein Zettel, auf dem steht 'Robin Hood war da'")
#     if ressourcen > 60:
#         ressourcen -= 30
#         print("Du hattest viele Ressourcen im Lagerhaus!... Mit Betonung auf 'hattest'. Vielleicht lernst du jetzt, etwas bescheidener zu leben.")
#     elif ressourcen > 40:
#         print("Nichts scheint zu fehlen. Offenbar bist du Robin Hood zu 'middle Class'!")
#     else:
#         ressourcen += 30
#         print("Als du ins Lagerhaus reintrittst bemerkst du sofort, dass mehr da ist, als zuvor - Danke, Robin Hood!")
#
#
# def event_16():
#     print("Ein erschöpfter Bote klopft an die Tür. Der König wünsche sich sofort einen 'Stephen' und ist bereit, grosszügig für ihn zu zahlen.")
#     if villager.name of villager in villagers == "Stephen":
#         answer = input("Möchtest du Stephen verkaufen? Ja oder Nein?")
#         if answer.lower() == "Ja":
#             #stephen löschen
#             change_resources(50)
#             print("Der Bote ist enorm erleichtert. Er zieht, mit einem verwirrten Stephen im Schlepptau davon.\nDu schaust ihm hinterher und streichelst den grossen Sack Gold, den du soeben erhlten hast.")
#         else:
#             print("'Stephen? Nein, noch gehört. Schönen Tag noch!' Der Bote macht sich verzweifelt aus dem Staub und Stephen schuldet dir jetzt einen Gefallen!")
#
#     else:
#         print("Stephen?")
#         print("...")
#         print("'Stephen?! Haben wir hier irgendwo einen Stephen?!\nDu klopfst an alle Türen im Dorf, doch niemand mit diesem Namen ist auffindbar. Schade. Der Bote zieht von dannen.")
#
# def event_17():
#     from villagers random.select villager.age <8:
#     #wenn es keinen gibt, dann ein anderes event abspielen!
#     print("Ein edel gekleidetes Ehepaar klopft an dein Tor. Es kann selber keine Kinder bekommen, und möchte deshalb",villager.name,"adoptieren.\nEs ist bereit, einen guten Preis dafür zu zahlen. Bist du einverstanden?")
#     answer = input("Möchtest du",villager.name,"verkaufen? Ja oder Nein?")
#     if answer.lower() == "Ja":
#     # villager.name löschen
#         change_resources(50)
#         print("Das Ehepaae freut sich und verschwindet zusammen mit",villager.name, "im Horizont. \nDu schaust ihnen hinterher und streichelst den grossen Sack Gold, den du soeben erhlten hast.")
#     else:
#         print(
#             "Das Ehepaar macht sich entrüstet aus dem Staub. So eine Frechheit von dir!")
#
# def event_18():
#     print("Ein Kaufmann ist zu Besuch. Er schlägt ein kleines Glücksspiel vor. Er denkt sich eine Zahl zwischen 1 und 10 aus, und du errätst sie! Gewinnst du, bekommst du das 5-Fache deines Einsatzes zurück.")
#     answer = input("Wieviel möchtest du investieren? Bitte mit einer Zahl antworten.")
#     if answer.lower() > resources:
#         print("So viel Geld hast du nicht! Wähle einen realistischeren Betrag.")
#         answer = input("Wieviel möchtest du investieren? Bitte mit einer Zahl antworten.")
#     guess = input("Welche Zahl rätst du?")
#     if guess.lower() == random.randint(1, 20):
#         print("Bravo, du hast richtig geraten! Ich hatte tatsächlich an",guess,"gedacht. Hier hast du deine Belohnung von",int(answer)*5, "!")
#         change_resources(int(answer)*5)
#
# def event_19():
#     print("Du hilfst einer mysteriösen Frau, die sich verirrt hat. Als Dank schenkt sie dir eine Verjüngungskur.")
#     answer = input("Welchem deiner Dorfbewohner möchtest du diese geben?")
#     for villager in villagers:
#         if villager.name = answerlower() and villager.age >16:
#             villager.age = 16
#     print("Gratulation,", answer,"wirkt nun wieder deutlich jünger!")
#
# def event_20():
#     print("Auf dem Dorfplatz streiten sich zwei Leute. Der eine glaubt, die Erde dreht sich um die Sonne (1.). Der andere glaubt, die Sonne dreht sich um die Erde (2.).")
#     answer = input("Was stimmt? 1. oder 2.?")
#     if answer.lower() == 1.
#         print("Das stimmt! Deine Dorfbewohner sind jetzt alle ein wenig schlauer. Der Lebensstil, der damit einhergeht, verbessert auch deren Gesundheit.")
#         #Gesundheit von allen  leicht verbessern
#     else:
#         print("Das stimmt nicht! Aber niemand kann's überprüfen. Tja!")
#

#ein zufälliges Event wählen und ausführen

events = [event_0]

doom3 = 0
doom8 = 0

def random_event():
    # if doom3 == 1:
    #     event_3b()
    # elif doom8 == 1:
    #     event_8b()
    # else:
        chance_event = random.randint(1, 8)
        if chance_event == 7:
            event_0()


            #events[random.randint(0,1)]()

