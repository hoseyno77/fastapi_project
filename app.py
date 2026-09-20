from fastapi_offline import FastAPIOffline

app = FastAPIOffline()
mylist = [10,20,30,40]
@app.get('/')
def home():
    return {'HELLO':"WORLD"}

@app.get('/home/')
def welcome():
    return {'welcome':"Home"}

@app.get('/getall/')
def get_all_items():
    return {'mylist':mylist}

@app.post('/add/{new_item}')
def add_item(new_item:int):
    mylist.append(new_item)
    return {'mylist':mylist}
    
@app.post('/addItem/')
def add_item_by_insert(index :int , new_item: int):
    if index< len(mylist):
        mylist.insert(index,new_item)
        return {f'{new_item} added in {index} position'}
    else:
        return {f'{index} position is out of range'}


@app.delete('/delete/{item}')
def delete_by_item(item : int):
    if item in mylist:
        mylist.remove(item)
        return {f'{item} remove from mylist'}
    else:
        return {f'{item} Not Found'}    




@app.delete('/deleteIndex/')
def delete_by_index(index: int):
    if index < len(mylist):
        mylist.pop(index)
        return {f'new mylist after delete:{mylist}'}
    else:
        return {f'{index} out of range'}  

@app.put('/update/') 
def update(old_item: int ,new_item:int):
    if old_item in mylist:
        index = mylist.index(old_item)
        mylist[index] = new_item
        return {f"new mylist after update:{mylist}"} 
    else:
        return {f"{old_item} Not Found"}


@app.put('/updateIndex/') 
def update(index: int ,new_item:int):
    if index < len(mylist):
        mylist[index] = new_item
        return {f"new mylist after update:{mylist}"} 
    else:
        return {f"{old_item} Not Found"}
     