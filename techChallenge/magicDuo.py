

# count
count = 0


# product is less than 1,000
# make sure numbers are increasing
product
productList = []

for i in range(len(product)):
    if(i == 0):
        if(product[i + 2] and product[i+1] < product[i+2]):     # if product has 3 digits 
            count += 1
        elif(not product[i+2] and product[i] < product[i+1]):
            count += 1
        else:
            print('not magic')


print(count)
                
