def division(a:int, b:int):
    try:    
        c= a / b
    
    except TypeError as e :
        print(f"mauvais type : {e}")
    

division(10,0)
