import random
when=['a few years ago', 'yesterday', 'last night', 'a long time ago', 'On 20th Jan']
who =['a rabbit', 'a big big jerry', 'a mouse', 'a turtle', 'a cat']
name =['Ali', 'Miriam', 'daniel', 'hauck', 'starwalker']
residence =['Varcelona', 'India', 'Germany', 'Cenice', 'England']
went =['cinemy', 'university', 'seminar', 'school', 'laundry']
happened =['made a lot of friends', 'eats a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

print(random.choice(when)+', '+random.choice(who)+ ' that lived in '+ random.choice(residence)+', '+'went to the '+random.choice(went)+'and'+random.choice(happened))
