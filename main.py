import json # لإضافة ميزة حفظ البيانات لاحقاً

expenses = []

while True:
    print("\n--- قائمة المصاريف ---")
    print("1. إضافة مصروف")
    print("2. عرض الكل")
    print("3. إجمالي المصاريف")
    print("4. خروج")

    choice = input("اختيارك: ")

    if choice == '1':
        try:
            amount = float(input("المبلغ (Dh): "))
            category = input("الفئة (مثلاً: أكل، نقل): ")
            date = input("التاريخ (YYYY-MM-DD): ")

            expense = {
                "id": len(expenses) + 1,
                "amount": amount,
                "category": category,
                "date": date
            }
            expenses.append(expense)
            print("✔ تمت الإضافة بنجاح")
        except ValueError:
            print("❌ خطأ: يرجى إدخال رقم صحيح للمبلغ")

    elif choice == '2':
        if not expenses:
            print("القائمة فارغة حالياً.")
        else:
            print("\nID | المبلغ | الفئة | التاريخ")
            for exp in expenses:
                print(f"{exp['id']} | {exp['amount']} Dh | {exp['category']} | {exp['date']}")

    elif choice == '3':
        total = sum(exp['amount'] for exp in expenses) # طريقة مختصرة واحترافية لحساب المجموع
        print(f"\n💰 إجمالي المصاريف هو: {total} درهم")

    elif choice == '4':
        print("إلى اللقاء!")
        break
