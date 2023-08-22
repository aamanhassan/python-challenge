#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
import os

#files to upload and output
file_to_load = os.path.join(".","Resources","budget_data.csv")
file_to_output = os.path.join(".","budget_analysis.txt")

total_months = 0
total_net = 0
net_change_list = []
dates = []


#open csv file 
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    
    #read and ignore the header
    header = next(reader)
    
    first_row = next(reader)
    
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1]) 
    
    total_months = total_months + 1
    
    #loop through the remaining rows
    for row in reader:
        
        total_months = total_months + 1
        #print(total_months)
        total_net = total_net + int(row[1])
        
        
        #calculate the net change

        net_change = int(row[1])- previous_net  
        previous_net = int(row[1])
        
        net_change_list.append(net_change)
        dates.append(row[0])
     
    
        average_change = sum(net_change_list)/len(net_change_list)
    
        #calculate greatest increase in profits
        greatest_profits_increase = max(net_change_list)
        increase_date = dates[net_change_list.index(greatest_profits_increase)]

        
        #calculate greatest decrease in profits
        greatest_profits_decrease = min(net_change_list)
        decrease_date = dates[net_change_list.index(greatest_profits_decrease)]
        #print(decrease_date)
         

        
output = (
    f"Financial Analysis\n"
    f"------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase In Profits: {increase_date} (${greatest_profits_increase})\n"
    f"Greatest Decrease In Profits: {decrease_date} (${greatest_profits_decrease})\n" 
)
    
print(output)

        
with open(file_to_output,"w") as text_file:
    text_file.write(output)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




