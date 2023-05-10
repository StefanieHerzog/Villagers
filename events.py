import random

from villager import create_random_minor_villager
from villager import create_random_baby_villager
from villager import create_random_old_villager
from villager import create_random_female_villager
from villager import create_random_male_villager


#all events


def event_1(game):
    print("Dir wird berichtet, dass eine Gruppe ausgehungerter Kinder in den Wäldern nahe deines Dorfes lebt. Möchtest du sie aufnehmen?")
    answer = input("Ja oder Nein?")
    if answer.lower() == "ja":
        for i in range (5):
            game.villagers.append(create_random_minor_villager())
        game.village.resources -= 30
        print("Die Kinder schliessen sich dankbar deiner Dorfgemeinschaft an. Allerdings sind sie in einem schlechten gesundheitlichen Zustand\nund benötigen viele Ressourcen, um nur schon eine Chance zu haben, die nächsten Tage zu überleben.")
    else:
        print("Du triffst die harte Entscheidung, die Ressourcen deines Dorfes für deine eigenen Dorfbewohner zu sparen.\nNach und nach verstummen die Geräusche aus dem Wald.")


def event_2(game):
    print("Ein hustender Händler klopft ans Tor des Dorfes. Er ist erschöpft und bittet darum, aufgenommen und gesund gepflegt zu werden.\nIm Gegenzug will er euch 30 seiner Ressourcen überlassen. Stimmst du zu?")
    answer = input("Ja oder Nein?")
    if answer.lower() == "ja":
        game.village.change_health_of_all_villagers(-30,game.villagers)
        game.village.resources += 30
        print("Der Händler schwört dir ewige Dankbarkeit. Eine Woche später reist er, um seine Ressourcen erleichtert,\nwieder ab. Doch als du auf den Dorfplatz trittst, und von überall her Husten hörst, fragst du dich, ob es das wert gewesen war...")
    else:
        print("Der Händler reist verzweifelt ab. Sein Husten klingt noch lange in deinen Ohren nach...")


def event_3(game):
    print("Ein sehr charismatischer Mann erscheint eines Morgens am Dorfeingang. Jeder Mensch, mit dem er spricht,\nist sofort in seinen Bann gezogen. Er möchte ins Dorf ziehen. Möchtest du ihm diesen Wunsch gewähren?")
    answer = input("Ja oder Nein?")
    if answer.lower() == "ja":
        dolus = create_random_male_villager()
        dolus.name = "dolus"
        dolus.age = 35
        game.villagers.append(dolus)
        print("Der Mann freut sich über deine Antwort und zieht zugleich ins Dorf. Er wird schnell zum neuen Liebling\nund alle Dorfbewohner hängen an seinen Lippen.")
        doom3 = 1
    else:
        print("Eine groteske Grimasse zieht über das Gesicht des Mannes. Er fängt an zu schreien und stampft wütend davon. Nicht alles was glänzt ist gold!")

def event_3b(game):
    for villager in game.villagers:
        if villager.name == "dolus":
            print("Der Mann, den du vor kurzem aufgenommen hast, hat eine Sekte aufgebaut und verlässt eines Morgens mit fünf weiteren Bewohnern das Dorf, ohne jemals zurückzukehren.")
            for villager in game.villagers:
                if villager.name == "dolus":
                    game.villagers.remove(villager)
            for i in range (5):
                game.villagers.remove(random.choice(game.villagers))
            doom3 = 0
        else:
            random_event()

def event_4(game):
    random_number = int()
    print("Ein Bote kommt mit einer düsteren Botschaft zu euch: Entweder, das Dorf schliesst sich freiwillig dem Herzogtum Balisgtal an,\noder der Herzog schickt seine Soldaten, um das Dorf einzunehmen.")
    answer = input("Anschliessen oder Kämpfen?")
    if answer.lower() == "anschliessen":
        game.village.resources -= 50
        print("Der Herzog ist erfreut und deine Dorfbewohner sicher. Dafür verlangt der Herzog hohe Abgaben. War es das wohl wert?")
    else:
        print(game.village.name, "soll unabhänngig bleiben! Deine Dorfbewohner verteidigen das Dorf ehrenvoll.\nViele Männer zwischen 12 und 60 sterben, doch das Dorf bleibt frei.")
        for villager in game.villagers:
            random_number = random.int(1,5)
            if villager.gender == "male" and villager.age < 60 and villager.age > 12 and random_number == 5:
                game.villagers.remove(villager)

def event_5(game):
    print("Es ist gerade besonders heiss. Das Wasser im Brunnen geht langsam aber sicher zu Neige.\nSollen die Dorfbewohner im Schatten bleiben und weniger arbeiten, oder aber das Wasser aus dem dreckigen Fluss trinken?")
    answer = input("Schatten oder Fluss?")
    if answer.lower() == "schatten":
        print("Deine Dorfbewohner versuchen, so wenig wie möglich zu schwitzen. Tatsächlich geht der Wasservorrat gerade noch so auf, und niemand muss verdursten.\nAllerdings konnten die Dorfbewohner in dieser Zeit keine Ressourcen erarbeiten.")
        game.village.resources -= 40
    else:
        print("Deine Dorfbewohner sind nun nicht mehr durstig und arbeiten wie gehabt weiter. Das dreckige Wasser hat aber Auswirkungen auf ihre Gesundheit...")
        game.village.change_health_of_all_villagers(-40, game.villagers)

def event_6(game):
    print("Eine mysteriöse Frau steht eines morgens vor dem Tor. Sie verkauft zwei verschiedene Elixiere. Jedes kostet 20 Ressourcen. Welches möchtest du kaufen?")
    answer = input("Fruchtbarkeit, Gesundheit oder keines?")
    if answer.lower() == "fruchtbarkeit":
        print("Du verteilst das Elixier all deinen Einwohnern. Wirst du in wenigen Monaten einen Baby-Boom beobachten können?")
        for i in range (3):
            game.village.try_for_baby()
        game.village.resources -= 20
    elif answer.lower() == "gesundheit":
        game.village.resources -= 20
        for villager in game.villagers:
            villager.health += 30
        print("Du verteilst das Elixier all deinen Einwohnern. Sie sehen bereits ein bisschen gesünder als zuvor aus!")
    else:
        print("Die Frau verschwindet so schnell wie sie gekommen war. Wer weiss, ob ihre Elixiere dir tatsächlich geholfen hätten...")

def event_7(game):
    females = []
    males = []
    for villager in game.villagers:
        if villager.gender == "male":
            males.append(villager)
        else:
            assert(villager.gender == "female")
            females.append(villager)
    victim = random.choice(females)
    offender = random.choice(males)
    print("Eine blutige Bandage verbigt das Auge von", victim.name, "die deine Hilfe ersucht. Sie erzählt, dass sie von", offender.name, ",\ndem reichsten Mann im Dorf geschlagen wurde. Du hast den Eindruck, er wird als wie gewaltätiger. Was möchtest du tun?")
    answer = input("Verbannen oder Verzeihen?")
    if answer.lower() == "Verbannen" or "verbannen":
        del (offender)
        game.village.resources -= 20
        print("Die Dorfbewohner bedanken sich bei dir. Sie fühlen sich jetzt alle sicherer.\nDer Wegzug von " , name.offender,  "hinterlässt allerdings ein klaffendes Loch in der Dorfkasse.")
    else:
        kill_villager(victim)
        print("Jemand so reiches aus dem Dorf zu verbannen, kannst du dir einfach nicht leisten - Gefahr hin oder her!\nAm nächsten Tag findest du", name.victim, "tot in einem Innenhof")


def event_8():
    children = []
    for villager in game.villagers:
        if villager.age < 10:
            children.append(villager)
    kind = random.choice(children)
    print("Ein Zirkus fährt durchs Dorf. Der Direktor beobachtet, wie", [kind], "akrobatisch auf einem Baum herumklettert.\nEr ist begeistert und bietet 20 Ressourcen dafür an, ihm das Kind zu verkaufen")
    answer = input("Verkaufen oder Ablehnen?")
    if answer.lower() == "verkaufen":
        for villager in game.villagers:
            if villager.name == kind.name:
                game.villagers.remove(villager)
        game.village.resources += 20
        print("Die Schreie von Kind und seiner Eltern klingen noch lange in deinen Ohren nach. Doch das Dorf kann die neuen Ressourcen gut gebrauchen.")
        doom8 = 1
    else:
        print("Das Kind und seine Familie sind erleichtert, und der Direktor verlässt genervt das Dorf.")

def event_8b(game):
    print("Plötzlich locken dich Schreie an dein Fenster. Du siehst, wie ein junger Mensch unten auf dem Dorfplatz drei Leute niedersticht,\nbevor er selber getötet wird. Als du dir den Täter aus der Nähe anschaust realisierst du, dass du ihn kennst. Offensichtlich hat", kind, "seinem Dorf nie verziehen, dass ihr es an den Zirkus verkauft habt.")
    for i in range(3):
        game.villagers.remove(random.choice(game.villagers))
    doom8 = 0


def event_9(game):
    print("Der Betreiber eines Waisenhauses klopft an euer Tor. Er kann es sich nicht mehr leisten, seinen Betrieb weiterzuführen.\nEr bittet euch darum, ihm entweder 30 Ressourcen zu geben oder 5 Babies zu adoptieren. Was machst du?")
    answer = input("Zahlen, Adoptieren, oder Ablehnen?")
    if answer.lower() == "zahlen":
        game.village.resources -= 20
        print("Der Betreiber ist begeistert und dankt dir, für deine Grosszügigkeit. Mitsamt seinen Schützlingen macht er sich auf den Heimweg.")
    elif answer == "adoptieren":
        print("Der Betreiber ist begeistert und überlässt dir alle fünf Babies.")
        for i in range (5):
            game.villagers.append(create_random_baby_villager())
    else:
        print("Der Betreiber fleht verzweifelt um Hilfe, aber du bleibst bei deiner Entscheidung.\nEr macht sich mit seinen Schützlingen auf die Weiterreise. Was wohl mit ihnen passieren wird?")

#

def event_10(game):
    print("Einer deiner Dorfbewohner hat beim Buddeln ein kleines Stückchen Gold gefunden. Möchtest du 30 Ressourcen investieren, um nach weiterem Gold zu schürfen, oder ist es dir das Risik nicht wert?")
    answer = input("Schürfen oder Verzichten?")
    if answer.lower() == "schürfen":
        chance_gold = random.randint(0, 100)
        if chance_gold > 90:
            game.village.resources += 100
            print("Unglaublich, du stösst tatsächlich auf ein riesiges Goldvorkommen! Deine Schatzkammer ist nun gut gefüllt.")
        elif chance_gold > 70:
            print("Du findest tatsächlich ein bisschen Gold. Doch nur gerade genug, um deine Ausgaben wieder reinzuholen. Gewinn machst du keinen.")
        else:
            print("Leider findest du kein bisschen Gold. Frustriert gibst du auf.")
            game.village.resources -= 30
    else:
        print("Du lässt dich nicht von potenziellen Reichtümern locken. Deine Dorfbewohner haben schliesslich einen vernünftigen Leader verdient...\nAber was, wenn da doch Gold unter der Erde liegt?")


def event_11(game):
    print("Ein merkwürdig gekleideter alter Mann klopft an dein Tor und schreit: Heute ist Tag der Alten!\nDiese Gruppe wird viel zu wenig wertgeschätzt. Deshalb schenke ich heute jedem Menschen über 60 zehn Goldtaler!")
    old_people = 0
    for villager in game.villagers:
        if villager.age > 60:
            game.village.resources += 10
            old_people += 1
    if old_people > 6:
        print("Wow, ",old_people,"alte Leute! Dein Dorf ist zwar ein halbes Altersheim, aber dieses mal lohnt sich das auch!")
    if old_people < 3:
        print("Nur",old_people," alte Leute? Es scheint, als würdest du alte Leute hassen...")



def event_12(game):
    removed = 0
    print("Ein Bote verkündet Schlimmes: Der König braucht mehr Bedienstete. Wähle eine Personengruppe, welche du dem König für immer zusendest.")
    answer = input("Kinder,Alte, Weibliche oder Männliche?")
    if answer.lower() == "kinder":
        for villager in game.villagers:
            if villager.age < 12:
                game.villagers.remove(villager)
                removed += 1
        if removed > 0:
            print(removed, "Kinder wurden dem König entsendet.")
        else:
            print("Der König ist entrüstet, dass du versuchst, ihm niemanden zu senden. Als Strafe er 60 Ressurcen von dir ein!")
            game.village.resources -= 60

    elif answer.lower() == "alte":
        for villager in game.villagers:
            if villager.age > 60:
                game.villagers.remove(villager)
                removed += 1
        if removed > 0:
            print(removed, "Alten wurden dem König entsendet.")
        else:
            print("Der König ist entrüstet, dass du versuchst, ihm niemanden zu senden. Als Strafe er 60 Ressurcen von dir ein!")
            game.village.resources -= 60

    elif answer.lower() == "weibliche" or answer.lower() == "weiblich":
        for villager in game.villagers:
            if villager.gender == "female":
                game.villagers.remove(villager)
                removed += 1
        if removed > 0:
            print(removed, "Frauen und Mädchen wurden dem König entsendet.")
        else:
            print("Der König ist entrüstet, dass du versuchst, ihm niemanden zu senden. Als Strafe treibt er 60 Ressurcen von dir ein!")
            game.village.resources -= 60

    elif answer.lower() == "männliche" or answer.lower() == "männliche":
          for villager in game.villagers:
            if villager.gender == "male":
                game.villagers.remove(villager)
                removed += 1
            if removed > 0:
                print(removed, "Männer und Knaben wurden dem König entsendet.")
            else:
                print("Der König ist entrüstet, dass du versuchst, ihm niemanden zu senden. Als Strafe er 60 Ressurcen von dir ein!")
                game.village.resources -= 60



def event_13(game):
    print("Ein edel gekleideter Mann klopft an dein Tor. Anscheinend ist er Marketingexperte.\nEr bietet an, Werbung für dein Dorf zu machen, damit neue Leute zuziehen.\nWie viel möchtest du in diese Werbung investieren?")
    answer = (input("0,10 oder 30 Ressourcen zahlen? (nur mit einer Zahl antworten)"))
    while answer != "0" and answer != "10" and answer != "30":
        answer = (input("Versuch's nochmal. Schreib nur 0,10 oder 30."))
    if answer == 0:
        print("Der Mann verabschiedet sich höflich und zieht von Dannen.")
        return
    elif answer.lower() == "10":
        anz_neue_db = 4
        game.village.resources -= 10
    elif answer.lower() == "30":
        anz_neue_db = 12
        game.village.resources -= 30
    print("Der Mann freut sich, dass du mit ihm Geschäfte machen willst. Welche Personengruppe willst du denn anwerben?")
    answer = input("Kinder,Alte, Weibliche oder Männliche?")
    while answer.lower() != "kinder" and answer.lower() != "alte" and answer.lower() != "weibliche" and answer.lower() != "weiblich" and answer.lower() != "männliche" and answer.lower() != "männlich":
        answer = (input("Versuch's nochmal. Schreib nur 0,10 oder 30."))
    if answer.lower() == "kinder":
        for i in range(anz_neue_db):
            game.villagers.append(create_random_minor_villager())
            print(anz_neue_db,"neue Kinder sind zu deinem Dorf hinzugestossen.")
    elif answer.lower() == "alte":
        for i in range(anz_neue_db):
            game.villagers.append(create_random_old_villager())
        print(anz_neue_db, "neue alte Menschen sind zu deinem Dorf hinzugestossen.")
    elif answer.lower() == "weibliche" or "weiblich":
        for i in range(anz_neue_db):
            game.villagers.append(create_random_female_villager())
        print(anz_neue_db, "neue Mädchen und Frauen sind zu deinem Dorf hinzugestossen.")
    elif answer.lower() == "männlich" or "männliche":
        game.villagers.append(create_random_male_villager())
        print(anz_neue_db, "neue Jungen und Männer sind zu deinem Dorf hinzugestossen.")

def event_14(game):
    print("Einer deiner Dorfbewohner hat im Wald ein seltenes und hoch wirksames Heilkraut gefunden.")
    answer = input("Welchem deiner Dorfbewohner möchtest du dieses zu essen geben?")
    blub = False
    while blub == False:
        for villager in game.villagers:
            if villager.name.lower() == answer.lower():
                villager.health = 100
                blub = True
        answer = input("Gib den Namen nochmal ein. Achte auf deine Rechtschreibung!")
    print("Gratulation,", answer, "wirkt nun wieder deutlich gesünder!")

#
def event_15(game):
    print("Eines Morgens bemerkst du, dass in euer Lagerhaus eingebrochen wurde! An der Tür hängt ein Zettel, auf dem steht 'Robin Hood war da'")
    if game.village.ressources > 60:
        game.village.ressources -= 30
        print("Du hattest viele Ressourcen im Lagerhaus!... Mit Betonung auf 'hattest'. Vielleicht lernst du jetzt, etwas bescheidener zu leben.")
    elif game.village.ressources > 40:
        print("Nichts scheint zu fehlen. Offenbar bist du Robin Hood zu 'middle Class'!")
    else:
        game.village.ressources += 30
        print("Als du ins Lagerhaus reintrittst bemerkst du sofort, dass mehr da ist, als zuvor - Danke, Robin Hood!")


def event_16(game):
    print("Ein erschöpfter Bote klopft an die Tür. Der König wünsche sich sofort einen 'Stephen' und ist bereit, grosszügig für ihn zu zahlen.")
    for villager in game.villagers:
        if villager.name == "stephen":
            stephen_exists = True

        if stephen_exists:
            answer = input("Möchtest du Stephen verkaufen? Ja oder Nein?")
            if answer.lower() == "ja":
                for villager in game.villagers:
                    if villager.name == "stephen":
                        game.villagers.remove(villager)
                        game.village.ressources += 50
                print("Der Bote ist enorm erleichtert. Er zieht, mit einem verwirrten Stephen im Schlepptau davon.\nDu schaust ihm hinterher und streichelst den grossen Sack Gold, den du soeben erhlten hast.")
            else:
                print("'Stephen? Nein, noch gehört. Schönen Tag noch!' Der Bote macht sich verzweifelt aus dem Staub und Stephen schuldet dir jetzt einen Gefallen!")

        else:
            print("Stephen?")
            print("...")
            print("'Stephen?! Haben wir hier irgendwo einen Stephen?!\nDu klopfst an alle Türen im Dorf, doch niemand mit diesem Namen ist auffindbar. Schade. Der Bote zieht von dannen.")

def event_17():
    children = []
    for villager in game.villagers:
        if villager.age < 8:
            children.append(villager)
    kind = random.choice(children)
    if len(children) == 0:
        random_event()
    else:
        print("Ein edel gekleidetes Ehepaar klopft an dein Tor. Es kann selber keine Kinder bekommen, und möchte deshalb",kind.name,"adoptieren.\nEs ist bereit, einen guten Preis dafür zu zahlen. Bist du einverstanden?")
        answer = input("Möchtest du",kind.name,"verkaufen? Ja oder Nein?")
        if answer.lower() == "Ja":
            for villager in game.villagers:
                if villager.name == kind.name:
                    game.villagers.remove(villager)
            game.village.ressources += 50
            print("Das Ehepaae freut sich und verschwindet zusammen mit",kind.name, "im Horizont. \nDu schaust ihnen hinterher und streichelst den grossen Sack Gold, den du soeben erhlten hast.")
        else:
            print(
                "Das Ehepaar macht sich entrüstet aus dem Staub. So eine Frechheit von dir!")

def event_18(game):
    print("Ein Kaufmann ist zu Besuch. Er schlägt ein kleines Glücksspiel vor. Er denkt sich eine Zahl zwischen 1 und 10 aus, und du errätst sie! Gewinnst du, bekommst du das 5-Fache deines Einsatzes zurück.")
    answer = int(input("Wieviel möchtest du investieren? Bitte mit einer Zahl antworten."))
    while answer > game.village.ressources:
        print("So viel Geld hast du nicht! Wähle einen realistischeren Betrag.")
        answer = input("Wieviel möchtest du investieren? Bitte mit einer Zahl antworten.")
    guess = int(input("Welche Zahl rätst du?"))
    if guess == random.randint(1, 10):
        print("Bravo, du hast richtig geraten! Ich hatte tatsächlich an",guess,"gedacht. Hier hast du deine Belohnung von",int(answer)*5, "!")
        game.village.ressources += (answer*5)

def event_19(game):
    print("Du hilfst einer mysteriösen Frau, die sich verirrt hat. Als Dank schenkt sie dir eine Verjüngungskur.")
    answer = input("Welchem deiner Dorfbewohner möchtest du diese geben? Wenn niemandem, dann schreibe 'keinem'")
    if answer.lower() == "keinem":
        print("Leider profitiert keiner deiner Dorfbewohner vom Trank. Die Frau nimmt ihn wieder mit.")
    else:
        blub = False
        while blub == False:
            for villager in game.villagers:
                if villager.name == answer.lower() and villager.name == villager.age >16:
                    villager.age = 16
                    blub = True
            answer = input("Gib den Namen nochmal ein. Achte auf deine Rechtschreibung!")
        print("Gratulation,", answer,"wirkt nun wieder deutlich jünger!")


def event_20():
    print("Auf dem Dorfplatz streiten sich zwei Leute. Der eine glaubt, die Erde dreht sich um die Sonne (1.). Der andere glaubt, die Sonne dreht sich um die Erde (2.).")
    answer = input("Was stimmt? 1. oder 2.?")
    if answer.lower() == "1." or answer.lower() == "1":
        print("Das stimmt! Deine Dorfbewohner sind jetzt alle ein wenig schlauer. Der Lebensstil, der damit einhergeht, verbessert auch deren Gesundheit.")
        for villager in game.villagers:
                villager.health += 10
    else:
        print("Das stimmt nicht! Aber niemand kann's überprüfen. Tja!")


#ein zufälliges Event wählen und ausführen

events = [event_1,event_2,event_3,event_4,event_5,event_6,event_7,event_8,event_9,event_10,event_11,event_12,event_13,event_14,event_15,event_16,event_17,event_18,event_19,event_20]

doom3 = 0
doom8 = 0

def random_event(game):
    chance_event = random.randint(1, 6)
    if chance_event == 1:
        if doom3 == 1:
            event_3b(game)
        elif doom8 == 1:
            event_8b(game)
        else:
            random.choice(events)(game)

