def twoSum(nums,target):
    my_list =[int(x) for x in nums]
    x =int(len(nums))
    total = 1
    for i in range(len(nums)):
        for m in range(i+1,len(nums)):
            if nums[i] + nums[m] == (target):
                return[i,m]
    print("Not Found")
my_list = [1,5,6]
r= 7
print(twoSum(my_list,r))