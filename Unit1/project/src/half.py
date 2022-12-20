import sys
for i in range(len(sys.argv[1])):
        for j in range(i + 1, len(sys.argv[1])):
            print(sys.argv[1][i], sys.argv[1][j])
