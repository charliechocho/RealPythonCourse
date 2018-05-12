import json

j_file = open('products.json', 'r')
s = j_file.read()

j = json.loads(s)

def clean_j(x):
    cln = x.replace(',', '-')
    return cln

def clean_u(x):
    cln = x.split(',')
    for i in range(1,len(cln)):
        cln[i] = cln[i].strip(' u')

    #cln[5] = cln[5].strip(' u')
    cln = str(cln).replace('"','')
    cln = str(cln).replace('\\','')
    cln = cln.strip('[]')
    return cln



with open('productsNsku.csv', 'w') as j_file2:
    j_file2.write("SkuNo#,Product,UnitPrice,UnitShippingPrice,Manufacturer,ImageLink\n")

    for i in range(len(j)):
        try:
            if ',' in j[i]['name']:
                j[i]['name'] = clean_j(j[i]['name'])
            else:
                pass
        except TypeError:
            pass

        if 'manufacturer' in j[i]:
            try:
                if ',' in j[i]['manufacturer']:
                    j[i]['manufacturer'] = clean_j(j[i]['manufacturer'])
                else:
                    pass
            except TypeError:
                pass
        else:
            pass

        if 'manufacturer' in j[i]:
                inp_str = j[i]['sku'], j[i]['name'], j[i]['price'], j[i]['shipping'], j[i]['manufacturer'], j[i]['image']

                inp_str = str(inp_str).strip('(u)')
                inp_str = clean_u(inp_str)

                j_file2.write(str(inp_str).replace("'", ""))
                j_file2.write('\n')
        else:
             pass


j_file.close()
j_file2.close()
