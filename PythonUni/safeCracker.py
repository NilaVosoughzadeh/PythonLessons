# تمرین پایتون گاو صندوق
# رمز گاوصندوق ۴ رقم است
# تقسیم رقم سوم بر رقم اول، ۴ است
# رقم آخر فرد است
# رقم آخر یک واحد از رقم اول خود، کوچک‌تر است
# رقم اول سه واحد از رقم دوم، کوچک‌تر است
# تقسیم رقم دوم بر رقم اول، ۲/۵ است
for i in range(1000,9999):
    x=str(i)
    digit1=int(x[0])
    digit2=int(x[1])
    digit3=int(x[2])
    digit4=int(x[3])
    if digit3/digit1 == 4:
        if digit4%2 != 0:
            if digit1-digit4 == 1:
                if digit2-digit1 == 3:
                    if digit2/digit1 == 2.5:
                        print(i)
