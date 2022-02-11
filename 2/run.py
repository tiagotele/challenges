from basket import Basket
from dirty_farmer import DirtyFarmer
from cleaner_farmer import CleanFarmer
import concurrent.futures

if __name__ == "__main__":
    tree=Basket("Tree",10)
    dirty_basket=Basket("Dirty Basket", 0)
    clean_basket=Basket("Clean Basket", 0)

    dirty_farmer=[]
    for index in range(3):
        dirty_farmer.append(DirtyFarmer(index, tree, dirty_basket))

    print(f"type = {type(dirty_farmer[0])}")
    

    clean_farmer=[]
    for index in range(3):
        clean_farmer.append(CleanFarmer(id=index, dirty_farmer=dirty_farmer, source_basket=dirty_basket, destiny_basket=clean_basket))
    

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as clean_executors:
        clean_future = [ clean_executors.submit(c.get_fruit) for c in clean_farmer ]
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as dirty_executors:
            dirty_future = [ dirty_executors.submit(c.get_fruit) for c in dirty_farmer ]
    
    print("end all")
    print(tree.status())
    print(dirty_basket.status())
    print(clean_basket.status())