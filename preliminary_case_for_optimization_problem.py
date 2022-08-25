# -*- coding: utf-8 -*-
"""preliminary_case_for_optimization_problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hdSpXuUvUm1LKhYPHjPJy-asaQ9NWBUp
"""

import matplotlib.pyplot as plt
import numpy as np
import decimal
import random
import math
list_for_colour=['b','g','r','c','w','m','y','k']

x1, y1 = input("Enter a point: ").split()
print("x for initial point: ", x1)
print("y for initial point: ", y1)
x1=float(x1)
y1=float(y1)
x2, y2 = input("Enter a point: ").split()
print("x for final point: ", x2)
print("y for final point: ", y2)
x2=float(x2)
y2=float(y2)

#main line
x_values = [x1,x2]
y_values = [y1,y2]

#get line equation
slope_of_the_bough= float((y2-y1)/(x2-x1))
constant = float(y1 - slope_of_the_bough*x1)

#print(round(m,2))

#lists for coordinates
list_for_all_points=[]
list_for_symmetric_ones=[]
list_for_rand_x_from_main_line=[]

max_length_of_leaf=0
max_length_of_leaf = float(max_length_of_leaf)
j=1
while j<4:
  mydict_for_points={}
  mydict_for_symmetric_points={}

  #genearating of unique points on main line
  rand_x = random.randint(int(x1),int(x2))#rand_x = random.uniform(int(x1)+1,int(x2)-1)
  counter=0
  while rand_x in list_for_rand_x_from_main_line:
    rand_x = random.randint(int(x1),int(x2))
  
  list_for_rand_x_from_main_line.append(rand_x)

  print("Random x-coordinate on main line: ", rand_x)
  rand_x=float(rand_x)
  rand_y = slope_of_the_bough*float(rand_x) + constant;
  rand_y=float(rand_y)
  print("Random y-coordinate on main line: ", rand_y)


  #assign first pair of dict as point from main-line (:=head of the list)
  mydict_for_points[rand_x] = rand_y
  mydict_for_symmetric_points[rand_x] = rand_y

  #start to create coordinates around the main point to obtain leaf
  angle = input("Enter an angle(C): ")
  length_of_little_leaf = input("Enter a length(m): ")
  length_of_little_leaf=float(length_of_little_leaf)
  if max_length_of_leaf<length_of_little_leaf:
    max_length_of_leaf=length_of_little_leaf
  angle=float(angle)
  angle_converted_radian= (math.pi*angle)/180
  length_of_little_leaf=float(length_of_little_leaf)

  i=1
  while i * angle_converted_radian < math.pi:
    x_new = rand_x + length_of_little_leaf* math.cos(angle_converted_radian*i + np.arctan(slope_of_the_bough))
    y_new = rand_y + length_of_little_leaf* math.sin(angle_converted_radian*i + np.arctan(slope_of_the_bough))
    mydict_for_points[x_new]=y_new
   
    #symmetric process
    k=(2*length_of_little_leaf* math.sin(angle_converted_radian*i))/ math.sqrt(1+slope_of_the_bough**2)
    x_new_symmetric= x_new + (k*slope_of_the_bough)
    y_new_symmetric= y_new - k
    mydict_for_symmetric_points[x_new_symmetric]=y_new_symmetric
    
    i=i+1

  list_for_all_points.append(mydict_for_points)
  list_for_symmetric_ones.append(mydict_for_symmetric_points)


    #f=random.randint(0,len(list_for_colour)-1)
    #plt.plot(x_values_for_leaf_symmetric,y_values_for_leaf_symmetric,list_for_colour[f],x_values_for_leaf,y_values_for_leaf,list_for_colour[f])
  j=j+1


#put sun as a node
x_for_sun=2
y_for_sun=7
xpoints = np.array([x_for_sun])
ypoints = np.array([y_for_sun])

#print(list_for_all_points)
#print(list_for_symmetric_ones)
#print(list_for_rand_x_from_main_line)

#skecth some combinations
list_of_string_shapes =[]
j=0
while j<5:
  k=0
  string_for_shape=""
  while k<len(list_for_rand_x_from_main_line):
    main_point_x=list_for_rand_x_from_main_line[k]
    main_point_y=list_for_all_points[k].get(main_point_x)
    random_x=random.choice(list(list_for_all_points[k].keys()))
    random_y=list_for_all_points[k].get(random_x)
    while random_x==main_point_x:
      random_x=random.choice(list(list_for_all_points[k].keys()))
      random_y=list_for_all_points[k].get(random_x)
      if random_x!=main_point_x:
        break
    print("coordinates of leaf: ",random_x,"--",random_y)
    random_x_for_symmetric=random.choice(list(list_for_symmetric_ones[k].keys()))
    random_y_for_symmetric=list_for_symmetric_ones[k].get(random_x_for_symmetric)
    while random_x_for_symmetric==main_point_x:
      random_x_for_symmetric=random.choice(list(list_for_symmetric_ones[k].keys()))
      random_y=list_for_symmetric_ones[k].get(random_x)
      if random_x_for_symmetric!=main_point_x:
        break
    
    #to avoid error
    try:
      random_x = float(random_x)
    except TypeError:
      random_x = 0 
    try:
      random_y= float(random_y)
    except TypeError:
      random_y = 0 
    try:
      random_x_for_symmetric = float(random_x_for_symmetric)
    except TypeError:
      random_x_for_symmetric = 0 
    try:
      random_y_for_symmetric= float(random_y_for_symmetric)
    except TypeError:
      random_y_for_symmetric = 0 
    #to avoid error

    print("coordinates of leaf: ",random_x_for_symmetric,"--",random_y_for_symmetric)
    print("main: ", main_point_x,"-",main_point_y)
    string_for_shape = string_for_shape + chr(math.floor(47+main_point_x+max_length_of_leaf-random_x))+ chr(math.floor(47+main_point_y+max_length_of_leaf-random_y))
    x_values_for_leaf_1 = [main_point_x,random_x]
    y_values_for_leaf_1 = [main_point_y,random_y]
    x_values_for_leaf_2 = [main_point_x,random_x_for_symmetric]
    y_values_for_leaf_2 = [main_point_y,random_y_for_symmetric]
    string_for_shape = string_for_shape + chr(math.ceil(47-main_point_x-max_length_of_leaf+random_x_for_symmetric))+ chr(math.ceil(47-main_point_y-max_length_of_leaf+random_y_for_symmetric))
    plt.plot(x_values_for_leaf_1,y_values_for_leaf_1, 'c')
    plt.plot(x_values_for_leaf_2,y_values_for_leaf_2,'g')
    k=k+1
  list_of_string_shapes.append(string_for_shape)
  plt.plot(xpoints, ypoints, 'o')
  plt.plot(x_values,y_values)
  plt.show()
  plt.clf()
  plt.cla()
  plt.close()
  j=j+1

print(list_of_string_shapes)


#find the ideal one

list_for_ideal_shape=[]
counter_to_identify_process=0
print((y_for_sun*slope_of_the_bough + x_for_sun - slope_of_the_bough*constant) / (slope_of_the_bough**2 +1))
if x1 <= (y_for_sun*slope_of_the_bough + x_for_sun - slope_of_the_bough*constant) / (slope_of_the_bough**2 +1) <= x2: #it have to be revised
  counter=0
  if y_for_sun > (slope_of_the_bough)*x_for_sun + constant:
    for i in list_for_all_points :
      mydict={}
      mydict[next(iter(i))] = i.get(next(iter(i)))
      if next(iter(i)) > x_for_sun:
        #get second key-value from dict of symmetric ones
        x_for_ideal_shape=list(i.keys())[len(i)-1]
        y_for_ideal_shape=i.get(x_for_ideal_shape)
        mydict[x_for_ideal_shape] = y_for_ideal_shape
        x2_for_ideal_shape=list(list_for_symmetric_ones[counter].keys())[len(list_for_symmetric_ones[counter])-1]
        y2_for_ideal_shape=list_for_symmetric_ones[counter].get(x2_for_ideal_shape)
        mydict[x2_for_ideal_shape] = y2_for_ideal_shape
      else:
        x_for_ideal_shape=list(i.keys())[1]
        y_for_ideal_shape=i.get(x_for_ideal_shape)
        mydict[x_for_ideal_shape] = y_for_ideal_shape
        x2_for_ideal_shape=list(list_for_symmetric_ones[counter].keys())[1]
        y2_for_ideal_shape=list_for_symmetric_ones[counter].get(x2_for_ideal_shape)
        mydict[x2_for_ideal_shape] = y2_for_ideal_shape
  
      list_for_ideal_shape.append(mydict)
      counter=counter+1
      counter_to_identify_process =1

  if y_for_sun < (slope_of_the_bough)*x_for_sun + constant:
    #same process like above
    for i in list_for_symmetric_ones :
      mydict={}
      mydict[next(iter(i))] = i.get(next(iter(i)))
      if next(iter(i)) > x_for_sun:
        x_for_ideal_shape=list(i.keys())[len(i)-1]
        y_for_ideal_shape=i.get(x_for_ideal_shape)
        mydict[x_for_ideal_shape] = y_for_ideal_shape
        x2_for_ideal_shape=list(list_for_all_points[counter].keys())[len(list_for_symmetric_ones[counter])-1]
        y2_for_ideal_shape=list_for_all_points[counter].get(x2_for_ideal_shape)
        mydict[x2_for_ideal_shape] = y2_for_ideal_shape
      else:
        x_for_ideal_shape=list(i.keys())[1]
        y_for_ideal_shape=i.get(x_for_ideal_shape)
        mydict[x_for_ideal_shape] = y_for_ideal_shape
        x2_for_ideal_shape=list(list_for_all_points[counter].keys())[1]
        y2_for_ideal_shape=list_for_all_points[counter].get(x2_for_ideal_shape)
        mydict[x2_for_ideal_shape] = y2_for_ideal_shape
  
      list_for_ideal_shape.append(mydict)
      counter=counter+1
      counter_to_identify_process =2
      #get last key-value from dict of symmetric ones

else:
  counter=0
  counter_to_identify_process =3
  for i in list_for_symmetric_ones :
      mydict={}
      mydict[next(iter(i))] = i.get(next(iter(i)))
      x_for_ideal_shape=list(i.keys())[1]
      y_for_ideal_shape=i.get(x_for_ideal_shape)
      mydict[x_for_ideal_shape] = y_for_ideal_shape
      x2_for_ideal_shape=list(list_for_all_points[counter].keys())[1]
      y2_for_ideal_shape=list_for_all_points[counter].get(x2_for_ideal_shape)
      mydict[x2_for_ideal_shape] = y2_for_ideal_shape
      counter=counter+1
      list_for_ideal_shape.append(mydict)

plt.plot(xpoints, ypoints, 'o')
plt.plot(x_values,y_values)

string_for_ideal_shape=""

for i in list_for_ideal_shape:
  x_values_for_leaf_1 = [next(iter(i)),list(i.keys())[1]]
  y_values_for_leaf_1 = [i.get(next(iter(i))),i.get(list(i.keys())[1])]
  x_values_for_leaf_2 = [next(iter(i)),list(i.keys())[2]]
  y_values_for_leaf_2 = [i.get(next(iter(i))),i.get(list(i.keys())[2])]
  plt.plot(x_values_for_leaf_1,y_values_for_leaf_1)
  plt.plot(x_values_for_leaf_2,y_values_for_leaf_2)
  if counter_to_identify_process == 1:
    string_for_ideal_shape = string_for_ideal_shape + chr(math.floor(47+float(next(iter(i)))+max_length_of_leaf-float(list(i.keys())[1])))+ chr(math.floor(47+float(i.get(next(iter(i))))+max_length_of_leaf-float(i.get(list(i.keys())[1]))))
    string_for_ideal_shape = string_for_ideal_shape + chr(math.floor(47-float(next(iter(i)))-max_length_of_leaf+float(list(i.keys())[2])))+ chr(math.floor(47-float(i.get(next(iter(i))))-max_length_of_leaf+float(i.get(list(i.keys())[2]))))
  if counter_to_identify_process == 2 or counter_to_identify_process == 3:
    string_for_ideal_shape = string_for_ideal_shape + chr(math.floor(47+float(next(iter(i)))+max_length_of_leaf-float(list(i.keys())[2])))+ chr(math.floor(47+float(i.get(next(iter(i))))+max_length_of_leaf-float(i.get(list(i.keys())[2]))))
    string_for_ideal_shape = string_for_ideal_shape + chr(math.floor(47-float(next(iter(i)))-max_length_of_leaf+float(list(i.keys())[1])))+ chr(math.floor(47-float(i.get(next(iter(i))))-max_length_of_leaf+float(i.get(list(i.keys())[1]))))

for i in list_for_rand_x_from_main_line:
  string_for_ideal_shape = string_for_ideal_shape + chr(math.floor(47+i))

print(string_for_ideal_shape)
plt.show()
plt.clf()
plt.cla()
plt.close()

max_matching=0
optimal_shape=""
for i in list_of_string_shapes:
  j=0
  counter=0
  while j < len(i):
    if i[j] == string_for_ideal_shape[j]:
      counter=counter+1
    j=j+1
  if max_matching < counter:
    max_matching=counter
    optimal_shape=i

print(optimal_shape)