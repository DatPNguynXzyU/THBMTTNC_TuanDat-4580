def xoa_phan_tu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_list ={'a':1,'b':2,'c':3,'d': 4}
key_to_delete ='b'
result = xoa_phan_tu(my_list,key_to_delete)
if result:
    print("phần tử đã đc xoá Dictionary: ",my_list)
else:
    print("Ko tìm thấy phần tử xoá trong Dictionary.")
