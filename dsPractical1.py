book ={
    "math":2,
    "english":6,
    "science":10,
    "marathi":10
}

member ={
    "m1":5,
    "m2":0,
    "m3":0,
    "m4":0
}
#1average
total_borrow=sum(member.values())
print(total_borrow)
total_member=len(member)
print(total_member)
average=total_borrow/total_member
print(f"Average number of a books borrow by all member is : {average}")

#2highest and lowest 
highest_borrow=max(book.values())
hbookname=max(book.keys())
print(f"Highest book borrow :{hbookname} - {highest_borrow}")

low_borrow=min(book.values())
lbookname=min(book , key=book.get)
print(f"lowest book borrow :{lbookname} - {low_borrow}")

#3not borrow
no_borrow=0
for m in member:
    if member[m]==0:
        no_borrow+=1
print(f"Number of Member who not borrow any book: {no_borrow}")

#4frequently borrow
max_borrow=max(book.values())
frequently_borrowed=[book for book, count in book.items() if count == max_borrow]
print(f"frequently books borrow :{frequently_borrowed}")
        