def factors(x):
    # יצירת רשימה ריקה לאחסון הגורמים
    result = []
    
    # מעבר על כל המספרים מ-1 ועד x (כולל)
    # range(1, x + 1) מבטיח שנתחיל ב-1 ונסיים בדיוק ב-x
    for i in range(1, x + 1):
        # בדיקה האם x מתחלק ב-i ללא שארית
        if x % i == 0:
            # הוספת המספר לרשימה
            result.append(i)
            
    return result
