def SI(principal, interest, time):
    return (principal*rate*time)/100

if __name__ == "__main__":
    p = int(sys.argv[1])
    r = int(sys.argv[2])
    t = int(sys.argv[3])

    
    print("simple_interest :", simple_interest(p,r,t)) 

