def kiem_tra_so_NT(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0: 
            return False
    return True
number = int (input("Nhập số cần kiểm tra: "))
if kiem_tra_so_NT(number):
    print(number,"Là Số nguyên tố")
else: 
    print(number,"Không phải là số nguyên tố")
