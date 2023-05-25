#28、列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=[1,2,3,4,5,6,7,8,9,10]
def fn(a):
    return a%2==1
newlist=filter(fn,a)
newlist=[i for i in newlist]
print(newlist)
res=[i for i in a  if i%2==1]
print(res)