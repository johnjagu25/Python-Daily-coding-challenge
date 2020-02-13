def diamon_star(nums):
        final = ""
        nums = nums // 2 + 1
        for i in range(1,nums+1):
                for j in range(2*(nums-i)):
                        final+=" "
                for j in range(0,2*i-1):
                        final += "X "
                final += "\n"
        for i in range(nums - 1,-1,-1):
                for j in range(2*(nums-i),0,-1):
                        final+=" "
                for j in range(0,2*i-1):
                        final += "X "
                final += "\n"
        print(final)

diamon_star(5)