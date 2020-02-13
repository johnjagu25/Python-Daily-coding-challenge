def diamon_star(nums):
        final = ""
        for i in range(nums):
                for j in range(nums-i-1):
                        final+=" "
                for j in range(0,i+1):
                        final += "X "
                final += "\n"
        for i in range(nums - 2,-1,-1):
                for j in range(nums-i-1,0,-1):
                        final+=" "
                for j in range(0,i+1):
                        final += "X "
                final += "\n"
        print(final)

diamon_star(3)