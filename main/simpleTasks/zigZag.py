import time, sys

indent = 0
indentIncrasing = False

try:
    while True:
        print(' ' * indent, end='')
        print('*********')
        time.sleep(0.1)

        if indentIncrasing:
            indent = indent + 1
            if indent == 20:
                indentIncrasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncrasing = True

except KeyboardInterrupt:
    sys.exit()