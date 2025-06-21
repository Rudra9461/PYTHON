# we have genrated a function which generates tables in a folder tables and generates table from 1 to 21


def generateTable(n):
    table =""
    for i in range(1,11):
        table +=f"{n} X {i} = {n*i} \n"

    with open (f"tables/table_{n}.txt" , "w") as f:
        f.write(table)


for i in range(2 ,21):
    generateTable(i)