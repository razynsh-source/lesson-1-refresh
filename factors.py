def factors(x):
    f_list = []
    for i in range(1, x + 1):
        if x % i == 0:
            f_list.append(i)
    return f_list

# לא לגעת מפה ומטה. קטע הקוד הזה חיוני לצורך הבדיקה האוטומטית #
if __name__ == "__main__":
    try:
        # קריאת הקלט מהבודק האוטומטי #
        user_input = int(input())
        
        # חישוב התוצאה #
        result = factors(user_input)
        
        # הדפסת התוצאה כפי שהבודק מצפה לראות (רשימה) #
        print(result)
