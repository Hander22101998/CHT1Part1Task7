def biggest_guy(one, two ,three):
    if one > two and one > three :
        return(one)
    elif two > three and two > one: 
        return(two)
    else :
        return (three)    
result = biggest_guy(10 ,40, 50)    
print(result)
