import sys

simpleList = [['bow','arrow',[25, 30]], 'box1', 'box2', 'box3']

#Single result
print(simpleList[0][2][1])
print(simpleList[3])

#Multiple with slice
print(simpleList[0:4])
# ^ The last result is not included therefore we give one more index. ^
print(simpleList[:]) # < Another method to print all positions.

#Last position in table
print(simpleList[-1])

#From beggining to index 2 (Because last one is not included):
print(simpleList[:3])


def removeUser(whichList):
    try:
        whoRemove = input('Who do you want to remove: ')
        whichList.remove(whoRemove)
    except:
        print('Brak użytkownika.')


def workerList():
    workers = []
    while True:
        option = input('t - input new workers | e - exit from program: ')
        if option == 't':
            break
        elif option == 'e':
            sys.exit()
        else:
            print('Wrong option, try again (t for type worker, e for exit)')
            continue

    while True:
        worker_name = input(f"Worker number{len(workers) + 1} name: ")
        worker_lastname = input(f"Worker number {len(workers) + 1} lastname: ")
        if worker_name == '' and worker_lastname == '':
            for i in range(len(workers)):
                print(workers[i])
            break
        # Add element using by concatenation
        # workers = workers + [worker_name, worker_lastname]
        workers.append(worker_name + " " + worker_lastname)
        print(workers)

    #Add element at the end of list
    workers.append('Example User')
    #Add element inside of particular index number
    workers.insert(1, 'Added_by_insert')
    print(workers)
    #Using workers.remove('Name')
    removeUser(workers)
    print(workers)
    #If we know exact index of item which we want to delete - best option is del
    del workers[0]
    print(workers)

workerList()