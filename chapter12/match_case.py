def http_status(status):
    match status:
        case 200 :
            return "OK"
        case 404 :
            return " Not Found"
        case 500 :
            return "International Server Error"
        case _:
            return " Unknown Status "
        
print(http_status(100))        