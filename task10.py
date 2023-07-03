lst = ['robot'] * 10
lst += ['human'] *10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)
data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)