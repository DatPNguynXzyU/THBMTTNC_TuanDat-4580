def truy_cap_phan_Tu(tuple_data):
    first_element = tuple_data[0]
    last_elemnet = tuple_data[-1]
    return first_element,last_elemnet
input_tuple = eval(input("Nhập Tuple, ví dụ(1,2,3): "))
first,last = truy_cap_phan_Tu(input_tuple)
print("Phần tử đầu tiên: ",first)
print("Phần tử cuối cùng: ",last)
