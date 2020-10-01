def qs(MyList, left, right):
  if left < right:
    pivot = partition(MyList, left, right)
    qs(MyList, left, pivot-1)
    qs(MyList, pivot+1, right)   

def partition(MyList, left, right):
  i = left
  pivot = MyList[right]
  for j in range(left, right):
    if(MyList[j] < pivot):
      MyList[i], MyList[j] = MyList[j], MyList[i]
      i = i + 1
  MyList[i], MyList[right] = MyList[right], MyList[i]
  return i

# function to print list
def PrintList(MyList):
  for i in MyList:
    print(i, end=" ")
  print("\n")
  
# test the code                 
MyList = [-20, 8, 22, 40, 2, 6, 28]
n = len(MyList)
print("Original List")
PrintList(MyList)

qs(MyList, 0, n-1)
print("Sorted List")
PrintList(MyList)
