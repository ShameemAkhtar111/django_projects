num = int(input())
val_list = input().split()
# max_count=0
# pre_max_count=0
# fav_singer=[]
# for x in val_list:
#     if val_list.count(x)>= max_count:
#         max_count = val_list.count(x)
#         if x not in fav_singer:
#             fav_singer.append(x)
#             if max_count > pre_max_count:
#                 fav_singer = []
#                 fav_singer.append(x)
#     pre_max_count = max_count

# print(len(fav_singer))

singer_count = {}
max_count = 0
fav_singer = set()

for singer in val_list:
    singer_count[singer] = singer_count.get(singer,0) + 1
    if  singer_count[singer] > max_count:
        max_count = singer_count[singer]
        fav_singer = {singer}
    elif singer_count[singer] == max_count:
        fav_singer.add(singer)

print(len(fav_singer))