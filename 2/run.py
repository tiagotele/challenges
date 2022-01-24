from tree import Tree
from farmer import Farmer
import concurrent.futures


if __name__ == "__main__":
    t=Tree()

    farmers=[]
    for index in range(30):
        farmers.append(Farmer(index,t))

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        farmers_future = [ executor.submit(f.get_fruit) for f in farmers ]


    print("end all")