#ex.1
def lue_tiedosto1(tiedostopolku):
    try:
        file = open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
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
        print(f"An error occurred: {e}", end='')

#ex.5
def tallenna5(tiedostopolku, asiakas_nro, nimi, tilaus):
    file = open(tiedostopolku, 'a')
    file.write(f"{asiakas_nro}:{nimi}\n * {tilaus}\n\n")
    file.close()     