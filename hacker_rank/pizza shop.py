def get_best_price(pizzas,toppings,x):
    
    pizza_price=0

    for pizza in pizzas:
       
        best_price=pizza_price
        values={}
        for index in range(len(toppings)):
            price=do_dfs(toppings,index,pizza,x,values)+pizza
            if abs(x-price)<abs(x-best_price):
                best_price=price

        if abs(x-best_price) < abs(x-pizza_price):
            pizza_price=best_price

    return pizza_price

def do_dfs(toppings,index,pizza,x,values={}):
    if index in values:
        return values[index]
    
    total= toppings[index]

    for i in range(index+1,len(toppings)):
        val= do_dfs(toppings,i,pizza,x,values)
        if  abs(total+pizza-x)> abs(toppings[index]+val+pizza-x):
            total=toppings[index]+val

    values[index]=total
    return values[index]


print(get_best_price([850, 900],[200, 250],1000))