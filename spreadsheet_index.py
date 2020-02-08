def spreadsheet_column(s): 
    index = 0;  
    for val in range(len(s)):  
        index *= 26;  
        index += ord(s[val]) - ord('A') + 1;  
  
    return index;  

print(spreadsheet_column('AAA'))
print(spreadsheet_column('CAD'))
print(spreadsheet_column('YZAA'))