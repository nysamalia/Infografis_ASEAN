import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt

conn = sqlalchemy.create_engine(
    'mysql+pymysql://root:12345678@localhost:3306/world'
)


q = '''select o.name as negara_asean, o.population as populasi_negara, o.gnp, i.name as ibukota, i.population as populasi, o.SurfaceArea
    from country o, city i
    where o.capital=i.id
    and o.region = 'Southeast Asia'
    order by negara_asean;
'''

df = pd.read_sql_query(sqlalchemy.text(q), conn) 
# print(df)

# No. 1
# plt.style.use('seaborn')
# plt.bar(df['negara_asean'], df['populasi_negara'], width=0.6,
#     color=['b','orange','green','r','purple','brown','pink', 'grey', 'gold', 'olive', 'lightblue']
# )
# plt.subplots_adjust(bottom=.16)
# plt.xlabel('Negara')
# plt.ylabel('Populasi (x100jt jiwa)')
# plt.xticks(rotation=20)
# plt.grid(True)
# for i, j in enumerate(df['populasi_negara']):
#     plt.text(i-.35, j, str(j), color='black', fontsize=8)
# plt.title('Populasi Negara Asean')
# plt.savefig('soal1.png')
# plt.show()

# No. 2
# negara =df['negara_asean']
# warna = ['b','orange','green','r','purple','brown','pink', 'grey', 'gold', 'olive', 'lightblue']

# plt.pie(df['populasi_negara'], labels=negara, colors=warna,
#     counterclock=True, autopct='%1.1f%%', 
#     textprops={'fontsize': 8}
# )
# plt.title('Persentase Penduduk Asean')
# plt.savefig('soal2.png')
# plt.show()

# No. 3
# plt.style.use('seaborn')
# plt.bar(df['negara_asean'], df['gnp'], 
#     color=['b','orange','green','r','purple','brown','pink', 'grey', 'gold', 'olive', 'lightblue']
# )
# plt.subplots_adjust(bottom=.16)
# plt.xlabel('Negara')
# plt.ylabel('Gross National Product (Us$')
# plt.xticks(rotation=45)
# for i, j in enumerate(df['gnp']):
#     plt.text(i-.35, j, str(j), color='black', fontsize=8)
# plt.grid(True)
# plt.title('Pendapatan Bruto Nasional ASEAN')
# plt.savefig('soal3.png')
# plt.show()

# No. 4

negara =df['negara_asean']
warna = ['lightgreen', 'lightpink','lightblue', 'purple','k','red','blue', 'yellow', 'pink','gold']

plt.pie(df['SurfaceArea'], labels=negara, colors=warna,
    counterclock=True, autopct='%1.1f%%', 
    textprops={'fontsize': 5, 'color': 'grey'}
)

plt.title('Persentase Luas Daratan Asean')
plt.savefig('soal2.png')
plt.show()



