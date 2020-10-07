import wrds

db = wrds.Connection()

# libraries = db.list_libraries()
# CRSP成分股数据
tables = db.list_tables(library='crsp')
# des = db.describe_table(library='crsp', table=)

print(tables)