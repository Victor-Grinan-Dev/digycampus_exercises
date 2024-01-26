#ex.1
def lue_tiedosto1(tiedostopolku):
    try:
        file = open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except FileNotFoundError:
        print(f"The file '{tiedostopolku}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    

#ex.2
def tallenna2(oppilaat, pisteet):
    students_file = open('oppilaat.txt', 'w')
    for oppilas in oppilaat:
        students_file.write(oppilas + '\n')

    scores_file = open('pisteet.txt', 'w')
    for piste in pisteet:
        scores_file.write(str(piste) + '\n')

#ex.3
def lue_tiedosto3(tiedostopolku):
    try:
        file=open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except  FileNotFoundError:
        print(f"Tiedostoa {tiedostopolku} ei löydy!")
    except Exception as e:
        print(f"An error occurred: {e}")

#ex.4
def lue_tiedosto4(tiedostopolku):
    try:
        file=open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except  FileNotFoundError:
        print(f"Tiedostoa {tiedostopolku} ei löydy!")
    except Exception as e:
        print(f"An error occurred: {e}")

#ex.5
def tallenna5(tiedostopolku, asiakas_nro, nimi, tilaus):
    file = open(tiedostopolku, 'a')
    file.write(f"{asiakas_nro}:{nimi}\n * {tilaus}\n\n")
    file.close()     

#ex.6
def jasenna_keskustelu(polku):
    character_script:str
    try:
        file = open(polku, 'r')
        lines = file.readlines()
        mother_script = open('mother.txt', 'w')
        daughter_script = open('daughter.txt', 'w')
        for line in lines:
            if line.strip() == 'Daughter:':
                character_script = 'daughter.txt'
            elif line.strip() == 'Mother:':
                character_script = 'mother.txt'
            else:
                if character_script == 'mother.txt':
                    mother_script = open('mother.txt', 'a')
                    mother_script.write(f"{line}")
                    mother_script.close()
                if character_script == 'daughter.txt':
                    daughter_script = open('daughter.txt', 'a')
                    daughter_script.write(f"{line}")
                    daughter_script.close()
        file.close()
        mother_script.close()
        daughter_script.close()
    except FileNotFoundError:
        print(f"The file '{polku}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_exercise_6():
    texts = ['keskustelu1.txt', 'keskustelu2.txt'] 
    lue_tiedosto1('keskustelu1.txt')
    # for text in texts:    
    #     jasenna_keskustelu(text)        

"""
os.remove() 
os.rename()
datetime.date.today() 
str(datetime.date.today())
"""