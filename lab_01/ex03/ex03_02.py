def Dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các số, cách nhau bầng dấu phẩy: ")
numbers = list(map(int,input_list.split(',')))
list_dao_nguoc = Dao_nguoc_list(numbers)
print("Tổng các số chẵn trong list là: ",list_dao_nguoc)
