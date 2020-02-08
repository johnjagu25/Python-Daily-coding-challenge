
def spreadsheet_column(value):
    columns =  ""
    while value > 0:
        remainder = value % 26
        if remainder == 0:
            columns += "Z"
            value = ( value // 26 ) - 1
        else :
            columns += chr( (remainder - 1) + ord("A"))
            value = value // 26
    
    return columns[::-1]
        
print(spreadsheet_column(703))
print(spreadsheet_column(2058))
print(spreadsheet_column(457003))