source1= {'Fruits':['apple','mango','carrot'],
          'Vegetable':['potato','tomato']
          }

source2 = {'Fruits':['apple','mango','carrot'],
         'Vegetable':['potato','tomato']
         }
source3={}

for key,value in source1.items():
    for key1,value1 in source2.items():
        if key==key1 and value==value1:
            source3[key]='Equal'
        else:
            source3[key]='not equal'

print(source3)


