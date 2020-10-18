#Your code
#def letterCombinations(digits): 
#    return List[str]
#Задание 1
alphabet = {'2' : list('abc'),
            '3' : list("def"),
            '4' : list('ghi'),
            '5' : list('jkl'),
            '6' : list('mno')}

def func(answer, digit):
  if len(digit)<1:
    return answer
  elif len(answer)<1:
    res = alphabet[digit[0]]
  else:
    list2 = alphabet[digit[0]]
    print(list2)
    res = []
    for li1 in answer:
      for li2 in list2:
        res.append(li1+li2)
        #print(res)
  print(res)
  #print(digit)
  func(res,digit[1:])

#func([],'234')
#Задание 2
#Your code


def subsets1(nums):  
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                print("in if",curr)
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
            print(output)
        return output

#print(subsets1([1,2,3,4]))

def subsets(nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
            print(result)
        return result 
l=['1','2','3','4']        
#print(subsets(l))
#print(['1']+['3'])

#Задание 3

def restoreIpAddresses(str_input): 

     def check(strr):
        if len(strr)==0:
          return False
        elif strr[0] == 0:
          return False
        elif 0 <= int(strr) < 256:
          return True
        else:
          return False

     def func(strin, level, first_symb, res):
        
        if (level == 4 and check(strin[first_symb:])):
          res+=strin[first_symb:]
          output.append(res)
          res = ''
          print(output)
          return
        elif level<4:
          for i in range(1,4):
            if check(strin[first_symb:first_symb+i]):
              res+=strin[first_symb:first_symb+i]+"."
              print(level+1, first_symb+i, res)
              func(strin, level+1, first_symb+i, res)
              res = res[:first_symb+level-1]

     
     output = []
     func(str_input,1,0,"")      
     
     return output

#print(restoreIpAddresses("2262251115"))
#Задание 4
import sys
def sumTarget(nums,target):
    nums.sort()
    listToReturn={}
    if 3<=len(nums)<=10**3:
        nums.sort()
        for i in range(len(nums)):
            index=0
            if -10**3<=nums[i]<=10**3:
                if -10**4<=target<=10**4:
                    k=i+1
                    if k>len(nums)-1:
                        continue
                    for j in range(len(nums)-1):
                        result=nums[i]+nums[k]+nums[j]
                        if abs(result-target)<=target:
                            listToReturn.update({index:str(nums[i])+' '+str(nums[k])+' '+str(nums[j])})
                        index+=1
        return listToReturn

    else:
        return

        
print(sumTarget([-1,1,2,-4,3,1000,5,-3],1))


