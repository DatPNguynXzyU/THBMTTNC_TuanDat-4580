def dem_so_Lan_luot_XH(lst):
    count_dict={}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict
input_string = input("Nhập danh sách các từ ,cách nhau bằng dấu cách: ")
word_list = input_string.split()
so_lan_ht= dem_so_Lan_luot_XH(word_list)
print("Số lần xuất hiện các phần tử: ",so_lan_ht)
