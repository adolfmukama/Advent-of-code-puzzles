

def my_file(i):
  test_data = i
  test = 0
  emplist = []
  x = test_data.split(":")
  y = x[1].split(";")
  z = [item.split(",") for item in y]
  n = x[0].split()
  temp = n[0]
  n[0] = n[1]
  n[1] = temp
  n = [n[0] + " " + n[1]]
  z += [n]
  for i in z:
      for x in i:
          v = x.split(",")
          h = [j.split() for j in v]
          print (h)
          [d] = h
          for i in d:
            if i == "blue":
              g = d.index(i) - 1  # Get the index of the quantity corresponding to "blue"
              if int(d[g]) >= 14:
                if emplist == []:
                  emplist.append(z[-1:])  # Append the entire game to emplist if the quantity is greater than or equal to 12
                else:
                  continue
                  
                break  # Break out of the loop after finding the quantity for "blue"
            if i == "red":
              g = d.index(i) - 1  # Get the index of the quantity corresponding to "blue"
              if int(d[g]) >= 12:
                if emplist == []:
                  emplist.append(z[-1:])  # Append the entire game to emplist if the quantity is greater than or equal to 12
                else:
                  continue
                break  # Break out of the loop after finding the quantity for "blue"
            if i == "green":
              g = d.index(i) - 1  # Get the index of the quantity corresponding to "blue"
              if int(d[g]) >= 13:
                if emplist == []:
                  emplist.append(z[-1:])  # Append the entire game to emplist if the quantity is greater than or equal to 12
                else:
                  continue
                break  # Break out of the loop after finding the quantity for "blue"
  #print(emplist)
  if emplist ==[]:
    game_id = 0
    
    
  else:
    [[[true_list]]] = emplist
    vd = true_list.split()
          #print (vd)
    game_id = int(vd[0])
    test += game_id
    print("test:", test)

def sum_id():
    fhand = open("/home/kali/Documents/puzzles/puz02.txt", "r")
    fh = fhand.readlines()
    total_id = 0

    for i in fh:
        v = i.split()
        xm = int(v[1].strip(":"))
        total_id += xm
    return total_id



fhand = open("/home/kali/Documents/puzzles/puz02.txt", "r")
fh = fhand.readlines()
total_id = 0
zh = sum_id()

for i in fh:
    i = [str(i)]
    #print(i)
    game_id = my_file(i[0])
    #print (total_id)
    #total_id = total_id + game_id
#print (f"The total game_id is: {zh - total_id}")


