def dict_diff(source1,source2):
    for key,value in source1.items():
        for key,value in source2.items():
           if(source1[key] in source2[key]):


dict1 = {'Fruits':['apple','banana','carrot'],
          'Vegetable':['potato','tomato']
          }
dict2 = {'Fruits':['apple','mango','carrot'],
         'Vegetable':['potato','tomato']
         }






