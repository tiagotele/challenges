from dirty_basket import Basket
from tree import Tree
from farmer import Farmer
import concurrent.futures


if __name__ == "__main__":
    tree=Tree()
    dirty_basket=Basket()

    farmers=[]
    for index in range(3):
        farmers.append(Farmer(index,tree,dirty_basket))

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        farmers_future = [ executor.submit(f.get_fruit) for f in farmers ]


    print("end all")