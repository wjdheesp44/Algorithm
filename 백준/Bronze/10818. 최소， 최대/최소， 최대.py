cnt = int(input())

num_list = list(map(int, input().split()))
num_list.sort()
print("%d %d" % (num_list[0], num_list[cnt-1]))