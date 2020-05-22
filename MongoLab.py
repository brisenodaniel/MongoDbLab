import pymongo

#connect
client = pymongo.MongoClient(r'mongodb+srv://root:root@cluster0-u2atu.gcp.mongodb.net/test?retryWrites=true&w=majority')
db = client['CPSC408-MongoLab']
#populate inventory
db.inventory.insert_many([
   { 'item': "journal", 'qty': 25, 'status': "A", 'size': { 'h': 14, 'w': 21, 'uom': "cm" }, 'tags': [ "blank", "red" ] },
   { 'item': "notebook", 'qty': 50, 'status': "A", 'size': { 'h': 8.5, 'w': 11, 'uom': "in" }, 'tags': [ "red", "blank" ] },
   { 'item': "paper", 'qty': 10, 'status': "D", 'size': { 'h': 8.5, 'w': 11, 'uom': "in" }, 'tags': [ "red", "blank", "plain" ] },
   {'item': "planner", 'qty': 0, 'status': "D", 'size': { 'h': 22.85, 'w': 30, 'uom': "cm" }, 'tags': [ "blank", "red" ] },
   { 'item': "postcard", 'qty': 45,'status': "A", 'size': { 'h': 10, 'w': 15.25, 'uom': "cm" }, 'tags': [ "blue" ] }
])

#find all
print("All entries unformatted\n", db.inventory.find({}))

#find with filter applied
print('Filter: {status : "D"}\n', [ x  for x in db.inventory.find({"status":"D"})])
print("Filter: {qty : 0 }\n", [x for x in db.inventory.find({'qty':0})])
print('Filter: {qty:0, status:"D"}\n',[x for x in db.inventory.find({ 'qty': 0, 'status': "D" })])
print('Filter: { "size.uom": "in" }\n',[x for x in db.inventory.find( { "size.uom": "in" } )])
print('Filter: { size: { h: 14, w: 21, uom: "cm" } }\n',[x for x in db.inventory.find( { 'size': { 'h': 14, 'w': 21, 'uom': "cm" } } )])
print('Filter: { tags: "red" }\n',[x for x in db.inventory.find( { 'tags': "red" } )])
print('Filter: { tags: [ "red", "blank" ] }\n',[x for x in db.inventory.find( { 'tags': [ "red", "blank" ] } )])

#find with projection
print('(Filter, projection): ( { }, { item: 1, status: 1 } )\n', [x for x in db.inventory.find( {}, { 'item': 1, 'status': 1 } )])
print('(Filter, projection):( { }, { _id: 0, item: 1, status: 1 } )\n',[x for x in db.inventory.find( {}, { '_id': 0, 'item': 1, 'status': 1 } )])

#use in for-loop

for item in db.inventory.find({"item":"planner"},{"_id": 0, 'item':1}):
    print(item)


#simple insert
db.inventory.insert_one({'item':'Rene Action-figure','qty':20,'status':'D','size': { 'h': 14, 'w': 21, 'uom': "cm" }, 'tags': [ "blank", "red" ] , 'catchphrase':"It's on the syllabus"})
for item in db.inventory.find({},{'_id':0}):
    print(item)

    
