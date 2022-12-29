"""EXAMPLE 1:
The proposed program stores two integers as two constants defined inside the code,
and then display:
i. Their sum
ii. Their difference
iii. Their product
iv. Their average value
v. Their distance (i.e. the absolute value of the difference)
vi. The maximum value (i.e. the greater of the two)
vii. The minimum value (i.e. the lesser of the two)
Try to execute the follow code and understand as it work. Use the debug during the
analysis."""
"""
# Define constants
FIRST_INTEGER = 10
SECOND_INTEGER = 20

# Calculate and print sum
sum = FIRST_INTEGER + SECOND_INTEGER
print("The sum is:", sum)

# Calculate and print difference
difference = FIRST_INTEGER - SECOND_INTEGER
print("The difference is:", difference)

# Calculate and print product
product = FIRST_INTEGER * SECOND_INTEGER
print("The product is:", product)

# Calculate and print average
average = (FIRST_INTEGER + SECOND_INTEGER) / 2
print("The average is:", average)

# Calculate and print distance (absolute value of the difference)
distance = abs(FIRST_INTEGER - SECOND_INTEGER)
print("The distance is:", distance)

# Calculate and print maximum value
maximum = max(FIRST_INTEGER, SECOND_INTEGER)
print("The maximum value is:", maximum)

# Calculate and print minimum value
minimum = min(FIRST_INTEGER, SECOND_INTEGER)
print("The minimum value is:", minimum)
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 2:
You want to find out which fraction of your car’s use is for going to work, and which 
is for personal use. You know the one-way distance from your home to work. For a 
particular period, you recorded the beginning and ending kilometers on the odometer 
and the number of working days. Try to execute the follow code able of computing the 
fraction of car’s use for work and personal. Use the debug during the analysis."""
""""
km_start = int(input("insert beginning kilometers: "))
km_stop = int(input("insert ending kilometers: "))
working_days = int(input("insert the number of working days: "))
km_home_work = int(input("insert the home-work discance: "))
km_total = km_stop - km_start
km_work = working_days * (km_home_work *2)
km_not_work = km_total - km_work
km_work = 100 * (km_work/km_total)
km_not_work = 100 * (km_not_work/km_total)
print(10*"-")
print(f"car used for work activities: {km_work:3.2f} %")
print(f"car used for not work activities: {km_not_work:3.2f} %")
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 3:
. Imagine that you and a number (M) of friends go to a luxury restaurant, and when you ask for the bill, 
you want to split the total amount and the tip (15 percent) between all. Your program should print the amount 
of the bill, the tip, the total cost, and the amount each person has to pay. It should also print how much of 
what each person pays is for the bill and for the tip. Try to execute the follow code and understand as it work. 
Use the debug during the analysis."""

"""
friend_number = int(input("insert the number of friends: "))
total_amount = int(input("insert the total amount [€]: "))
total_tip = total_amount * 0.15
tip = total_tip / friend_number
amount = total_amount / friend_number
amount_per_friend = tip + amount
final_amount = total_amount + total_tip
print(15*'-')
print("GLOBAL INFORMATION")
print(f"The total tip is {total_tip} €")
print(f"The final amount is {final_amount} €")
print(15*'-')
print("INFORMATION PER FRIEND")
print(f"The final amount per friend is {amount_per_friend} €")
print(f"The tip for each friend is {tip} €")
print(f"The amount without the tip is {amount} €")
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 4: Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10"""
"""
toplam = 0
# 1 ile 10 arasındaki tam sayılar
for i in range(1, 11):
  toplam += i
print(toplam)
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 5: Write a program on python that prints the balance of an account after the first, second, and third year. 
The account has an initial balance of $1,000 and earns 5 percent interest per year."""
""""
balance = 100 # başlangıç bakiyesi
interest_rate = 0.05 # yıllık faiz oranı
interest = balance * interest_rate # ilk yıl için faiz
balance += interest # bakiye artışı
print("$" + str(balance)) # ilk yıl bakiyesi
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 6: In a scheduling program, we want to check whether two appointments overlap. For 
simplicity, appointments start at a full hour, and we use hours in the format 0-23h. The 
following pseudocode describes an algorithm that determines whether the appointment 
with start time start1 and end time end1 overlaps with the appointment with start time 
start2 and end time end2."""
"""
start1 = 8 # randevu 1 başlangıç saati
end1 = 10 # randevu 1 bitiş saati
start2 = 9 # randevu 2 başlangıç saati
end2 = 11 # randevu 2 bitiş saati

# iki randevunun çakışıp çakışmadığını kontrol edelim
if (start1 < end2) and (end1 > start2):
    print("Randevular çakışmaz.")
else:
    print("Randevular çakışır.")
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 7: The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a
given month and day."""
"""
def season(month, day):
    # mevsimi belirle
    if month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    elif month in [9, 10, 11]:
        season = "Fall"
    else:
        season = "Winter"

    # güne göre mevsimi düzelt
    if month == 3 and day >= 20:
        season = "Winter"
    elif month == 6 and day >= 21:
        season = "Summer"
    # diğer mevsimler için benzer kontroller yapılabilir

    return season


# örnek kullanımlar
print(season(3, 15))  # Spring
print(season(6, 22))  # Summer
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 9: The ability to speak more than one language is a valuable skill in today’s labor market. One of the 
basic skills is learning to greet people. Write a program that prints a twocolumn list with the greeting phrases 
shown in the following table; in the first column, print the phrase in English. In the second column, print the phrase 
in Italian. Please, find a way to align both columns."""
"""
def print_greetings():
    # karşılama ifadeleri
    greetings = [("Hello", "Ciao"),
                 ("Hi", "Salve"),
                 ("Good morning", "Buongiorno"),
                 ("Good afternoon", "Buon pomeriggio"),
                 ("Good evening", "Buonasera"),
                 ("Goodbye", "Arrivederci")]

    # sütunların uzunluklarını bul
    english_length = max([len(g[0]) for g in greetings])
    italian_length = max([len(g[1]) for g in greetings])

    # sütunları yazdır
    for g in greetings:
        print(f"{g[0]:{english_length}} | {g[1]:{italian_length}}")


# karşılama ifadelerini yazdır
print_greetings()
------------------------------------------------------------------------------------------------------------------------
"""
"""EXAMPLE 10: Write a programs that displays your name inside a box on the screen, like:
 +---------+ +-------+
 ¦ WILLIAM ¦ ¦ W ¦
 +---------+ ¦ I ¦
 ¦ L ¦
 ¦ L ¦
 ¦ I ¦
 ¦ A ¦
 ¦ M ¦
 +-------+
Do your best to approximate lines with characters such as “ | ” ,“ - ”, “ + ”, “ . ”, “ ¦ ”"""
"""
def print_name_box(name):
    # isim uzunluğunu bul
    name_length = len(name)

    # üst ve alt çizgi üret
    top_bottom_line = "+" + "-" * (name_length + 2) + "+"

    # ilk satırı yazdır
    print(top_bottom_line)
    print(f"¦ {name} ¦")

    # orta satırları yazdır
    for c in name:
        print(f"¦ {c} ¦")

    # alt çizgi yazdır
    print(top_bottom_line)


# ismi kutu içinde yazdır
print_name_box("FETHI")
------------------------------------------------------------------------------------------------------------------------
"""


