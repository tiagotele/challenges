from basket import Basket
from dirty_farmer import DirtyFarmer
from cleaner_farmer import CleanFarmer
import concurrent.futures

import time



tree=Basket("Tree",50)
dirty_basket=Basket("Dirty Basket", 0)
clean_basket=Basket("Clean Basket", 0)

dirty_farmer=[]
for index in range(3):
    dirty_farmer.append(DirtyFarmer(index, tree, dirty_basket))

clean_farmer=[]
for index in range(3):
    clean_farmer.append(CleanFarmer(id=index, dirty_farmer=dirty_farmer, source_basket=dirty_basket, destiny_basket=clean_basket))

def print_status():
    basket_status=f"{tree.status()} - {dirty_basket.status()} - {clean_basket.status()} - "
    farmers_status=""
    for d in dirty_farmer:
        farmers_status+=d.status()
        farmers_status+=" "
    for c in clean_farmer:
        farmers_status+=c.status()
        farmers_status+=" "
    print( basket_status + farmers_status)

def status_loop():
    while True:
        print_status()
        time.sleep(1)
        if tree.is_empty() == True:
            break

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as status:
    status_future = [status.submit(status_loop)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as clean_executors:
        clean_future = [ clean_executors.submit(c.get_fruit) for c in clean_farmer ]
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as dirty_executors:
            dirty_future = [ dirty_executors.submit(c.get_fruit) for c in dirty_farmer ]


print("end all")
print_status()
