import pandas as pd
import numpy as np



df=pd.read_table("species/bos_taurus/manually_annotated_breeds.tsv")
df=df.sort_values(by=['species','breed','subspecies'])
df=df.sort_values(by=['subspecies','breed'])


origins_df



origins={'Italy':['Reggiana','Modenese','Romagnola','Chianina','Piemontese','Podolica','Maremmana'],
         'Austria':['Tyrolean Grey'],
         'Switzerland':['Simmental','Brown Swiss','Original Braunvieh'],
         'France':['Charolais',"Blonde D'Aquitaine",'Limousin','Maine Anjou','Salers'],
         'Scotland':['Angus','Red angus'],
         'Germany':['Gelbvieh'],
         'England':['Hereford','Jersey','Shorthorn'],
         'Brazil':['Nelore'],
         'International':['Holstein'],
         'Africa':['Arsi','Barka','Butana','Boran','Goffa','Kenana','Mursi','Afar','Ndama','Sheko','Fogera','Horro'],
         'Tibet':['Yak'],
         'Asia':['Banteng','Zebu'],
         'USA':['Brahman']}


origins_df=[]

for k,v in origins.items():
    for i in v:
        origins_df.append([k,i])
origins_df=pd.DataFrame(origins_df)
origins_df.columns=['Origin','Breed']
origins_df=origins_df.sort_values(by='Origin')

codes=pd.read_table("species/bos_taurus/subspecies_codes.tsv")

df=pd.read_table("species/bos_taurus/manually_annotated_breeds.tsv")
df=df.rename(columns={'breed_type':'subspecies'})

codes_subspecies={'AFT':'taurus','AFI':'indicus','AFS':'indicusXtaurus','AFZ':'indicusXtaurus','EUT':'taurus',
                  'AST':'taurus','AMI':'indicusXtaurus','ASI':'indicus','AFB':np.nan}

df['species']='Bos taurus'
df['species']=df['species'].where(df['subspecies']!='AFB','Syncerus caffer')
df=df.replace("-","AFT")

df['subspecies']=df['subspecies'].apply(lambda x:codes_subspecies[x])



subspecies={'indicus':['Arsi','Barka','Butana','Ethiopian Boran','Goffa','Kenana','Mursi','Ogaden',''],
            'taurus':['Muturu','Sheko','Ndama','Sheko'],
            'indicusXtaurus':['Afar','Ankole','Fogera','Horro'],

            #'africanusXindicus':['Fogera','Horro','']


            }

df=df.drop(columns=['study'])
df=df[['breed','species','subspecies','origin']]
df.to_csv("species/bos_taurus/manually_annotated_breeds.tsv", index=False, sep='\t')
