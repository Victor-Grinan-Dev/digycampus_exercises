#ex.1
def lue_tiedosto(tiedostopolku):
    try:
        file = open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    file.close()

#ex.2
def lue_tiedosto(tiedostopolku):
    try:
        file = open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print(f"The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    file.close()
#ex.3
def lue_tiedosto(tiedostopolku):
    try:
        file=open(tiedostopolku, 'r')
        for line in file:
            print(line.strip())
        file.close()
    except  FileNotFoundError:
        print(f"Tiedostoa {tiedostopolku} ei löydy!")
    except Exception as e:
        print(f"An error occurred: {e}")