# Write your solution here
def create_tuple(x: int, y: int, z: int):
    l = [x,y,z]
    l = sorted(l)
    l[1]= l[2]
    l[2] = x+y+z
    t = (l[0],l[1],l[2])
    return t
if __name__ == "__main__":
    print(create_tuple(5,3,-1))

### another method ###

def create_tuple(x: int, y: int, z: int):
    smallest = min[x,y,z]
    greatest = max[x,y,z]
    total = sum[x,y,z]
    return (smallest,greatest,total)
    