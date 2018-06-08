def add(a , b):
    print(f"Adding {a} + {b} = " , a +b ) 
    return a + b

def subtract (a , b ):
    print (f"Subtacting {a} - {b} = ", a - b)
    return a - b

def multiply( a , b ):
    print (f"Multiplying {a} * {b} = " , a * b)
    return a * b

def divide (a , b ):
    print (f"dividing {a} / {b} = " , a / b)
    return a / b

print("Let's do some math with just functions " )

age = add (30 ,5 )
height = subtract ( 78 , 4 )
weight = multiply(90 , 2 )
iq = divide(100 , 2 )

print (f"Age : {age}  \n Height : {height} \n Weight : {weight} \n IQ :{iq}")

print ( "This is the puzzlw.")

what = add(age ,subtract(height , multiply(weight , divide(iq , 2 ))))

print("that  becomes:" , what ,"can you do it by hand ?")

