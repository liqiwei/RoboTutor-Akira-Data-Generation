from random import *

def main():
    nameFile=open("data_source_names.txt","w")
    csvFile = open("diffLevels.csv", "r")
    csvFile.readline()

    for i in range(15): #change this to 30 at end
        cArray = csvFile.readline().split(",")
        fileName=naming(i,cArray)
        nameFile.write(fileName)
        nameFile.write("\n")

        f = open(fileName, "w")
        f.write("{\n")
        f0="""  "datasource"  """+" : "+"[ \n"
        f.write(f0)
        f.write("\n")
        f.write("       {\n")

        for j in range(11):
            choiceVar = choices(cArray)
            targetVar = target(choiceVar)
            answerVar = answer(targetVar, choiceVar)

            f1=""" "type":"""+type()+",\n"
            f2=""" "choices":"""+str(choiceVar)+",\n"
            f3=""" "item_counter":"""+str(j+1)+",\n"
            f4=""" "answer":"""+str(answerVar)+",\n"
            f5=""" "target":"""+str(choiceVar[targetVar])+",\n"
            f6=""" "belowString":"""+str(belowString(cArray))+ ",\n"
            f7=""" "audio":"true" \n"""
            f.write(f1)
            f.write(f2)
            f.write(f3)
            f.write(f4)
            f.write(f5)
            f.write(f6)
            f.write(f7)

            if j==10:
                f.write("       } \n")
            else:
                f.write("       } ,\n")
            f.write("\n")

        f.write("   ]\n")
        f.write("}\n")


def naming(i,cArray):
    #belowString
    if belowString(cArray)=="0":
        belowStringVar="_show" #visual
    else:
        belowStringVar=""

    lanes="_"+cArray[9].rstrip()+"L"   #number of lanes
    KC="_"+cArray[5]  #SDID
    level="_"+cArray[4]  #level
    order="_"+cArray[7]  #order

    off=cArray[3]    #offset
    minValue=cArray[1]
    if off=="within": offVar="_OFFW"+minValue
    else: offVar="_OFF"+off

    name="akira.num_say"+belowStringVar+lanes+KC+order+offVar+level+".json"
    return name


def type():
    return "CAk_Data"


def choices(cArray):
    ch = []
    lanes = cArray[len(cArray) - 1]
    order = cArray[len(cArray) - 3]

    for i in range(int(lanes)):
        offset=cArray[3]
        m=0

        if offset=="within":
            m=randint(0,int(cArray[1]))
        else:
            m=int(offset)

        ch.append(str(randint(int(cArray[1]), int(cArray[2])) * m))

    if order == "asc":
        ch = sorted(ch)
    if order == "des":
        ch = sorted(ch, key=int, reverse=True)
    return ch


def target(choiceVar):
    rand = randint(0, (len(choiceVar) - 1))
    return rand


def answer(targetVar, choiceVar):
    if targetVar == 0:
        return "LEFT"
    if len(choiceVar) == 2:
        return "RIGHT"
    if targetVar == 1:
        return "CENTER"
    return "RIGHT"


def belowString(cArray):
    if cArray[6] == 'Audio + Visual':
        return "0"
    else:
        return "null"


main()
