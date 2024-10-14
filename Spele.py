import random
while True:
    q1 = input("Vai jus vēleties spēlet?: \n").lower()

    if q1== 'ja' or q1== 'jā':
        break
    elif q1== "ne" or q1== "nē":
        print("Uz redzēšanos")
        quit()
        break
    else:
        print("Uzraksti <Jā vai Nē> ludzu.")

all_questions = [{
        "text": "Kurš rakstīja 'Vecais vīrs un jūra'?",
        "answers": "A-Selindžers: B-F. Skots Ficdžeralds; C-Ernests Hemingvejs; D-Marks Tvens;",
        "right_answer": "c",
    },
                {
    "text": "Kāds ir vidējais attālums no Zemes līdz Mēnesim?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },
                  {
    "text": "Puisēns, kurš uzauga mežā starp dzīvniekiem. Kurā valstī tas notika?",
    "answers": "A-Brazīlijā: B-Indijā; C-Madagaskarā ; D-Latvijā ;",
    "right_answer": "b",
    },
                 {
    "text": "Kā sauc instrumentālu skaņdarbu operas vai baleta ievadā?",
    "answers": "A-Etīde: B-Refrēns; C-Uvertīra; D-Artjoms ;",
    "right_answer": "c",
    },
                  {
    "text": "Pasaules otrā garākā upe?",
    "answers": "A-Huanhe: B-Nīla; C-Jandzi; D-Amazone ;",
    "right_answer": "b",
    },
                 {
    "text": "Pie kāda dzimtes pieder lapsa?",
    "answers": "A-Suņu dzimta: B-Kaķu dzimta; C-Jenotu dzimta; D-Lapsas dzimta ;",
    "right_answer": "a",
    },
                  {
    "text": "Cik kaulu ir pieaugušam cilvēkam?'?",
    "answers": "A-206: B-223; C-201; D-202;",
    "right_answer": "a",
    },
                  {
    "text": "Cik ilga 'Simtgadu karš'?",
    "answers": "A-99: B-143; C-121; D-116 ;",
    "right_answer": "d",
    },
                  {
    "text": "Kuru kontinentu klāj ledus?",
    "answers": "A-Āzija: B-Āfrika; C-Antarktīda; D-Ziemeļamerika;",
    "right_answer": "c",
    },
                 {
    "text": "Kurā gadā tika dibināta Izraēla?",
    "answers": "A-1325. gadā: B-1991. gadā; C-1948. gadā; D-1899. gadā ;",
    "right_answer": "c",
    },
             {
    "text": "Nosauc Turcijas galvaspilsētu!",
    "answers": "A-Ankara: B-Stambula; C-Antalja; D-Latvija ;",
    "right_answer": "a",
    },
                 {
    "text": "Kas ir pasaules dziļākais ezers?",
    "answers": "A-Baikāls: B-Kaspijas jūra; C-Tanganjikas ezers; D-Isikuls ;",
    "right_answer": "a",
    },
                 {
    "text": "Piena ceļš ir... ",
    "answers": "A- Galaktika: B-Zvaigžņu kopa ; C-Saules sistēma; D- Planētu parāde ;",
    "right_answer": "a",
    },
                 {
    "text": "Čības ciliāts ir... ",
    "answers": "A-Baktērijas : B-Vīruss; C-Vienkāršākais vienšūnas organisms.; D-Modes apavi ;",
    "right_answer": "c",
    },
                 {
    "text": "Kurš izgudroja datoru?",
    "answers": "A-Bils Geitss: B-Stīvs Džobss ; C- Čārlzs Beidžs; D-Alans Tjūrings ;",
    "right_answer": "c",
    }]

balvas=['Šokolādes konfekšu kārba',' Abonementa sportu zālē','Gludeklis','Tosteris','Biļete uz Dubaiju','Veļas mašīna',' TV','Telefons','1000 eiro','Automašīna',]

for i in range(10):        
    input("Jusu uzdēvums būs atbildēt uz 10 jautajumus un jus vār uzvarēt automobilu. Uzpiest enter lai turpināt: \n")
    question = random.choice(all_questions)
    all_questions.remove(question)
    ans=input(f"Jūsu jautājums ir {question['text']}\nAtbildes varianti ir\n{question['answers']}\nJūsu atbilde ir: \n").lower()
    if ans==question["right_answer"]:
        player_choice=input(f"Vai jūs gribāt turpināt vai ņemt balvu({balvas[i]}). Ievadiet ja, ja gribi ņemt balvu: \n").lower()
        if player_choice=='ja':
            print(f"Jūsu balva ir {balvas[i]}. Uz redzēšanos.")
            break
    else:
        print("Jūs zaudējāt")
        break
        



        