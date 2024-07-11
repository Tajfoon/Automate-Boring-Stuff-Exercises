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


workers = []

while True:
    howManyWorkers = len(workers)
    worker_name = input(f"Worker number{len(workers) + 1} name: ")
    worker_lastname = input(f"Worker number {len(workers) + 1} lastname: ")
    if worker_name == '' and worker_lastname == '':
        print(workers_name[:])
        break
    workers_name = workers + [worker_name, worker_lastname]
    print(workers_name)