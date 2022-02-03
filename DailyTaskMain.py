from MenuCommands import read_input

# Tulevaisuudessa ohjelmaan voisi lisätä:
# 1. Kyvyn hakea huomisen päivämäärän ja lisätä sen tiedostoon
# 2. Keino merkitä tehtäviä tehdyiksi
# 3. Ehkä tilastoida, miten hyvin saan päivän tehtävät tehtyä?
# 4. Tee tästä nettiappi eli se heittäisi minut nettisivulle tai sitä voisi käyttää sitä kautta

GREETING_TEXT = "Hello, master.\n 1. Do you want to open task list?\n 2. Do you want to write into task list\n " \
                "3. Remove existing list\n 4. Exit Task List Manager 2000"
Active = True

while Active:
    print(GREETING_TEXT)
    userinput = input()
    read_input(userinput)
    if userinput == "4":
        Active = False
