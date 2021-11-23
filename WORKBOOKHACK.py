import json
from colored import fg, bg, attr
r2 = fg(255)
b = fg(75)
r3 = fg(1)
def write_data():
    checknumber=input(f"{r2}[{b}?{r2}] Check number:")
    answer=input(f"{r2}[{b}?{r2}] Answer:")
    data_dic = {f'{checknumber}': f'{answer}'}
    with open("data.json", "r+") as file:
        data = json.load(file)
        data.update(data_dic)
        file.seek(0)
        json.dump(data, file)
        file.truncate()
def read_data():
    numberasked=input(f"{r2}[{b}?{r2}] What number have you been asked:")
    with open('data.json', 'r') as myfile:
        data=myfile.read()
    obj = json.loads(data)
    print(f"{r2}[{r3}!{r2}]",str(obj[f"{numberasked}"]))
def choice():
    which=int(input(f"{r2}[{b}?{r2}] 1 to enter a digit, 2 if you got checked:"))
    if which==1:
        write_data()
    if which==2:
        read_data()
    use_again=input(f"{r2}[{b}?{r2}] Would you like to use again (y/n):")
    if use_again=="y":
        choice()
    if use_again=="n":
        exit()

print(f"""{b}

░██████╗██████╗░░█████╗░██████╗░██╗░░██╗  ██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░██████╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██████╔╝░╚███╔╝░  ██████╦╝░╚████╔╝░██████╔╝███████║╚█████╗░╚█████╗░█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██╔══██╗░██╔██╗░  ██╔══██╗░░╚██╔╝░░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗
██████╔╝██║░░░░░██║░░██║██║░░██║██╔╝╚██╗  ██████╦╝░░░██║░░░██║░░░░░██║░░██║██████╔╝██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
""")
with open('data.json', 'r') as myfile:
        data=myfile.read()
        obj = json.loads(data)
amountoftimes=len(obj)
print(f"{b}Welcome to SPARX BYPASSER, Long live hegartymaths!")
choice()
