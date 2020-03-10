# pandas and openpyxl packages should be installed
import pandas

Cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [32000,35000,37000,45000]
        }

df = pandas.DataFrame(Cars, columns= ['Brand', 'Price'])

a=df.to_excel (r'd:\\Cars.xlsx', index = None, header=True)
print (df)


#---------- Use xlwt Package -------- Just .xls-------
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

supersecretdata = [34,123,4,1234,12,34,12,41,234,123,4,123,1,45123,5,43,61,3,56]
sheet1.write(0,0,"Title")
for i,e in enumerate(supersecretdata):
    sheet1.write(i+1,0,e)

book.save("d:\\random.xls")

