import sys
import datetime

def parseInput(arg):
    if str.lower(arg[1]) == "help":
        help()
        return
    elif str.lower(arg[1]) == "all":
        all()
        return
    elif str.lower(arg[1]) == "today":
        today()
        return
    else: #build string
        text = ' '.join(sys.argv[1:])
        text = "{} : TODO : {} \n".format(datetime.datetime.now(),text)
        writeToFILE(text)
        print(text)


def today():
    print("On date "+str(datetime.date.today())+ " your todo list looks like  ---> ")
    with open('bazaPodataka') as fp:
        for lines in fp:
            if str(datetime.date.today()) in lines:
                print(lines)

def all():
    with open('bazaPodataka') as fp:
        for lines in fp:
            print(lines)

def onDates():
    pass

def help():
    print("# Ako pokrenem sa  to do Nekakav tekst ona ce to spremiti u fajl sa trenutacnim datumom kada je pokrenuto , tj appendat cellipsis ## implementirano " \
                                                   "# AKo  pokrenem  today onda ce procitati natrag sve kaj je na taj datum trebam napraviti " \
                                                   "# AKo  pokrenem  today onda ce procitati natrag sve kaj je na taj datum trebam napraviti " \
                                                   "# Ako  pokrenem  all onda ce mi isprintati sve moje zadatke" \
                                                   "# Ako pokrenem  today/all send onda ce mi na moj mail poslati danaxnje ili sve zadatke")

def writeToFILE(text):
    with open('bazaPodataka','a') as fp:
        fp.write(text)

if __name__ == "__main__":


    if len(sys.argv)>1:
        print(sys.argv[1])
        parseInput(sys.argv)
    else:
        print("Pozvano je sa default vrijednostima tj. samo todo ")





