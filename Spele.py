import random
while True:
    q1 = input("").lower()

    if q1== 'ja' or q1== 'jā':
        break
    elif q1== "ne" or q1== "nē":
        print("Uz redzēšanos")
        raise ValueError
        break
    else:
        print("Uzraksti <Jā vai Nē> ludzu.")

all_questions = [{
        "text": "1. Kurš rakstīja 'Vecais vīrs un jūra'?",
        "answers": "A-Selindžers: B-F. Skots Ficdžeralds; C-Ernests Hemingvejs; D-Marks Tvens;",
        "right_answer": "c",
    },
                {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },
                  {
    "text": "3. ir puisēns, kurš uzauga mežā starp dzīvniekiem. Kurā valstī tas notika?",
    "answers": "A-Brazīlijā: B-Indijā; C-Madagaskarā ; D-Latvijā ;",
    "right_answer": "b",
    },,
                 {
    "text": "4. Kā sauc instrumentālu skaņdarbu operas vai baleta ievadā?",
    "answers": "A-Etīde: B-Refrēns; C-Uvertīra; D-Artjoms ;",
    "right_answer": "c",
    },,
                  {
    "text": "5. Pasaules otrā garākā upe?",
    "answers": "A-Huanhe: B-Nīla; C-Jandzi; D-Amazone ;",
    "right_answer": "b",
    },,
                 {
    "text": "6. Pie kāda dzimtes pieder lapsa?",
    "answers": "A-Suņu dzimta: B-Kaķu dzimta; C-Jenotu dzimta; D-Lapsas dzimta ;",
    "right_answer": "a",
    },,
                  {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,
                  {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,
                  {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,,
                 {
    "text": "2. Kāds ir vidējais attālums no Zemes līdz Mēnesim?'?",
    "answers": "A-148 450 km: B-384 467 km; C-149 600 000 km; D-5km ;",
    "right_answer": "b",
    },,]



for i in range(10):        
    input("Jusu uzdēvums būs atbildēt uz 10 jautajumus un jus vār uzvarēt automobilu. Uzpiest enter lai turpināt: ")
    question = random.choice(all_questions)
    ans=input(f"Jūsu jautājums ir {question['text']}\nAtbildes varianti ir\n{question['answers']}\nJūsu atbilde ir: ").lower()
    if ans==question["right_answer"]:


        