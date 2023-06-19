# Réalisé par : Tidjet Ghilas 
X = {'a', 'b' , 'c'}
Q = {'q0', 'q1', 'q2','q3','q4','q5','q6','q7'}
I = 'q0'
F = {'q0', 'q1','q2','q3'}
transitions = {
    'q0': {
        'a': 'q0',
        'b' : 'q1',
        'c' : 'q4'
    },
    'q1': {
        'a': 'q0' ,
        'b' : 'q2',
        'c' : 'q5'

    },
    'q2': {
        'a' : 'q3',
        'b' : 'q2',
        'c' : 'q6'

    },
    
    'q3': {
        'a' : 'q0',
        'c' : 'q7'
        
    },
    'q4': {
        'c' : 'q1'
    },
    'q5': {
        'c' : 'q2'
    },
    'q6': {
        'c' : 'q3'
    },
    'q7': {
        'c' : 'q0'
    }
}

pos = 1
actuel = I

mot_saisi = input("Vueillez saisir un mot : ")

for lettre in mot_saisi:
    if lettre not in X:
        print(f"Le mot n'appartient pas au langage, car {lettre} n'est pas dans l'alphabet")
        exit()
    try:
        actuel = transitions[actuel][lettre]
    except KeyError:
        print(f"Le mot n'appartient pas au langage car il contient la chaine interdite 'bbab' ou bien une chaine de 'c' imapire, La lettre {lettre} à la position {pos} est inattendu. ")
        exit()
    pos+=1

if actuel in F:
    print("Le mot appartient au langage")
else:
    print("Le mot n'appartient pas au langage, car le nombre de lettres 'c' est impair ")