from dirty_basket import Basket
from tree import Tree
from farmer import Farmer
import concurrent.futures


if __name__ == "__main__":
    tree=Tree(10)
    dirty_basket=Basket(name='dirty')
    clean_basket=Basket(name='clean')

    farmers=[]
    for index in range(3):
        farmers.append(Farmer(index,tree,dirty_basket=dirty_basket, clean_basket=None))
    cleaners=[]
    for index in range(3):
        cleaners.append(Farmer(index,None,dirty_basket=dirty_basket, clean_basket=clean_basket))

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as clean_executors:
        cleaners_future = [ clean_executors.submit(c.get_fruit_from_dirty_basket) for c in cleaners ]
    
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as dirty_executor:
            farmers_future = [ dirty_executor.submit(f.get_fruit_from_tree) for f in farmers ]


    print("end all")
    print(f"clean basket total={clean_basket.get_fruit()}")