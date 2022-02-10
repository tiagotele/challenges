from basket import Basket
from dirty_farmer import DirtyFarmer
import concurrent.futures

if __name__ == "__main__":
    tree=Basket("Tree",50)
    dirty_basket=Basket(50)

    dirty_farmer=[]
    for index in range(3):
        dirty_farmer.append(DirtyFarmer(index, tree, dirty_basket))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as clean_executors:
        cleaners_future = [ clean_executors.submit(c.get_fruit) for c in dirty_farmer ]
    
    print("end all")
    print(tree.status())