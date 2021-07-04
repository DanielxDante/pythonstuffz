#Formats
##file1=open("INPUT.txt","r")
##file2=open("OUTPUT.txt","w")
##for line in file1:
##    line=line.strip("\n")
##    name,nric=line.split("|")
##    if nric[0]!="T":
##        file2.write(name+"\n")
##file1.close()
##file2.close()

###Q1
#########################################################
##def sortRainfall():
##    counter=0
##    file=open("RAINFALL.txt","r")
##    array=[0]*1000
##
##    for line in file:
##        array[counter]=float(line)
##        counter+=1
##       
##    for key_index in range(1,len(array)):
##        key=array[key_index]
##        prev_index=key_index-1
##        compare=array[prev_index]
##
##        while prev_index>=0 and key<compare:
##            array[key_index]=compare
##            array[prev_index]=key
##            key_index=prev_index
##            prev_index-=1
##            compare=array[prev_index]
##            
##    return array
##
##def minRainfall(array):
##   length=len(array)
##   for i in range(length):
##      while array[i]!=0.0:
##          return array[i]
##        
##def maxRainfall(array):
##    return array[-1]
##
##def medianRainfall(array):
##    lst=[]
##    for i in range(1000):
##        if array[i]!=0.0:
##            lst.append(array[i])
##    length=len(lst)
##    if (length%2)==1:
##        return lst[(length//2)+1]
##    else:
##        return 0.5*(lst[(length//2)] + lst[(length//2)+1])
###DO NOT DELETE THE LINES BELOW
###=============================
##sortedarray = sortRainfall()
####print(sortedarray)
####minRain = minRainfall(sortedarray)
####print(minRain)
####maxRain = maxRainfall(sortedarray)
####print(maxRain)
####print(medianRainfall(sortedarray))
##############################################################
###Q2
################################################################
##def bubbleSortScores():
##    counter=0
##    file=open("UNSORTEDSCORES.txt","r")
##    array=[0]*605
##
##    for line in file:
##        array[counter]=float(line)
##        counter+=1
##
##    swapped=False
##    for i in range(len(array)-1):
##        for j in range(len(array)-i-1):
##            if array[j]>array[j+1]:
##                array[j],array[j+1]=array[j+1],array[j]
##                swapped=True
##        if not swapped:
##            break
##        
##    length=len(array)
##    if (length%2)==1:
##        return array[(length//2)+1]
##    else:
##        return 0.5*(array[(length//2)] + array[(length//2)+1])

# Menu
##option_1_done = False
##while True:
##    print("1. Read menu data")
##    print("2. Take order")
##    print("3. Quit")
##
##    try:
##        selection = int(input("\nPlease select an option: "))
##        if selection < 1 or selection > 3:
##            raise ValueError
##        elif selection == 1:
##            if option_1_done==True:
##                print("\nFile already read.\n")
##            else:
##                f = open("MENU.TXT")
##                for line in f:
##                    line = line.strip().split("$")
##                    # line[0][:3] -> menu item number
##                    # line[0][4:-1] -> menu item name
##                    # line[1] -> menu item price
##                    current_index = int(line[0][:3])
##                    current_name = line[0][4:-1]
##                    current_price = float(line[1])
##                    
##                    new_index = find_index(menu_item_indices, current_index)
##
##                    menu_item_indices = menu_item_indices[:new_index] + [current_index] + menu_item_indices[new_index:]
##                    menu_item_names = menu_item_names[:new_index] + [current_name] + menu_item_names[new_index:]
##                    menu_item_prices = menu_item_prices[:new_index] + [current_price] + menu_item_prices[new_index:]
##                f.close()
##                option_1_done = True
##                print("\nMENU.TXT read.\n")
##                #print(menu_item_indices)
##                #print(menu_item_names)
##        elif selection == 2:
##            if option_1_done==False:
##                print("\nYou must perform Option 1 before executing Option 2.\n")
##            else:
##                #print("\nStub for order taking.\n")
##                # take a new order
##                get_another_order_item = True
##                items_ordered = []
##                while get_another_order_item:
##                    order_item_input = input("\nPlease enter a menu item index (or -1 to complete the order): ")
##                    try:
##                        order_item_input = int(order_item_input)
##                    except:
##                        print("\nPlease enter a menu item NUMBER or -1.")
##                    if order_item_input == -1:
##                        get_another_order_item = False
##                    else:
##                        menu_item_index = find_item(menu_item_indices, 0, len(menu_item_indices) - 1, order_item_input)
##                        if menu_item_index == None:
##                            print("\nInvalid menu index; that index does not exist.")
##                        else:
##                            print("\nOrder taken: " + menu_item_names[menu_item_index])
##                            items_ordered.append(menu_item_index)
##                # print all ordered items
##                total_cost = 0
##                print("\n{0:<7}{1}".format("Index", "Item"))
##                for i in range(len(items_ordered)):
##                    total_cost += menu_item_prices[items_ordered[i]]
##                    print("{0:<7}{1}".format(menu_item_indices[items_ordered[i]], menu_item_names[items_ordered[i]]))
##                print("\nTotal price: $" + str(round(total_cost, 1)) + "\n")
##
##        else:
##            break
##    except FileNotFoundError:
##        print("\nMENU.TXT does not exist!\n")
##    except ValueError:
##        print("\nInvalid selection. Please input 1-3.\n")

#Writing and altering wordpad created
global summary
summary=[]
def readLog():
    file=open("WEBLOG.txt","r")
    for line in file:
        line=line.strip("\n")
        address,date_time=line.split("|")
        date=date_time[0:11]
        time=date_time[12:20]
        summary.append([address,date,time])
    file.close()

readLog()

def processLog():
    summary_report=open("SUMMARYREPORT.txt","w")

    servers=[]
    for x in summary:
        if x[0] not in servers:
            servers.append(x[0])

    report=[["empty",[]]]*len(servers)
    for i in range(len(servers)):
        report[i]=["empty",[]]
        report[i][0]=servers[i]

    for x in summary:
        for y in report:
            if x[0]==y[0]:
                y[1].append(x[1])

    for z in report:
        length=len(z[1])
        line = str(z[0]) + "     "
        for i in range(length):
            line+=(str(z[1][i])+",")
        line=line.strip(",")
        summary_report.write(line+"\n")

    summary_report.close()

    freq=0
    accessed_freq=[]
    for a in report:
        length=len(a[1])
        if length>freq:
            freq=length
        else:
            pass
    for b in report:
        if len(b[1])==freq:
            accessed_freq.append(b[0])
    print("===========================================")
    print("Highest frequency (days) : " + str(freq))
    print("Accessed by:")
    for c in accessed_freq:
        print(c)
    return("==========================================")
        

print(processLog())
    
































