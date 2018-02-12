import  math
import pypyodbc
import re
#pattern = re.compile(r"[\w']+|[\b \b.,!?;]")
class DataModel:
    def __init__(self,title,subtitle,publisher,publicationDate,author,edition,volNumber,location,URL,network,pageRange):
        self.title=title
        self.subtitle=subtitle
        self.publisher=publisher
        self.publicationDate=publicationDate
        self.author=author
        self.edition=edition
        self.volNumber=volNumber
        self.location=location
        self.URL=URL
        self.video=network
        self.pageRange=pageRange

    def weigh_datamodel(self):
        weight=float(0.0)
        #spliting in author start
        auth=self.author.replace(',','').replace(' and ',' ').replace('.','')
        #pattern = re.compile(r"[\w']+|[\b \b.,!?;]")
        lst = auth.split(' ')#re.findall(pattern,auth)
        #print(lst)
        #spliting in author end
        if len(lst)>2:
            if lst[0]!="" and lst[1]!="" and lst[2]!="" and lst[3]!="" and lst[2]!='et' and lst[3]!='al':
                weight+=2
            elif lst[2]=='et' and lst[3]=='al':
                weight+=3
        elif lst[0]!="" and lst[1]!="":
            weight+=1
        else:
            weight+=0
        if self.title!="":#need to change if given article title and book/journal(sub) title
            weight+=10
        if self.subtitle!="":
            weight+=10
        if self.edition!="":
            weight+=0.1
        if self.publisher!="":
            weight+=0.01
        if self.publicationDate!="":
            weight+=0.001
        #if self.author!="":# need to change for 2 or more authors
         #   weight+=1
        if self.volNumber!="":
            weight+=0.0001
        if self.location!="":
            weight+=100
        if self.URL!="":
            weight+=1000
        if self.video!="":
            weight+=10000
        if self.pageRange!="":
            weight+=0.00001

        return round(weight,5), lst

def main():
    connection=pypyodbc.connect(Driver='{SQL Server}',Server='LPW7-5CG65056DZ\SQLEXPRESS',Database='Citation',uid='sa',pwd='infy@123')
    cursor=connection.cursor()
    cursor.execute("Select Weigh,Rules from Cite_Rules")
    result=cursor.fetchall()
    weigh={}# consists of all the key value pairs with key as the weight and value as the rules
    for r in result:
            weigh[r[0]]=r[1]
    dm=[]
    with open("C:\\Users\\agarg\\Documents\\Citation\\datamodel.txt") as f:
        for line in f:
            dm=line.replace('\n','').split(';')
            #print(dm)
#Lname<comma><space>FI<dot><space>PublicationYear<dot><space>title(ITALICS)<dot><space>A_F2<dot><space>A_L2<space>(Ed.)<dot><space>location<colon><space>Publisher
            d1=DataModel(dm[0],dm[1],dm[2],dm[3],dm[4],dm[5],dm[6],dm[7],dm[8],dm[9],dm[10])
            weight, auth =d1.weigh_datamodel()
            print(weight)
            rule=""
            citation=""
            if weight in weigh:
                rule=(weigh[weight])
                #print(rule)
                '''
                rule=weight[r[w]].value
                pattern = re.compile(r"[\w']+|[\b \b.,!?;]")
                re.findall(pattern,rule)
                '''
                citation=rule.replace('<comma>',',').replace('<space>',' ').replace('<dot>','.').replace('<colon>',':')
                   #as pur abt this any function.
                if any(i in 'Lname' for i in citation):
                    citation=citation.replace('Lname',auth[0])
                if any(i in 'Fname' for i in citation):
                    citation=citation.replace('Fname',auth[1]) 
                    #need to do for FI(fistname initial)
                if any(i in 'FI' for i in citation):
                    auth1=auth[1]
                    citation=citation.replace('FI',auth1[0])
                if len(auth)>2:
                    if any(i in 'et' for i in citation):
                        citation=citation.replace('et',auth[2])
                    if any(i in 'al' for i in citation):
                        citation=citation.replace('al',auth[3])
                    if any(i in 'Fname2' for i in citation):
                        citation=citation.replace('Fname2',auth[2])
                    if any(i in 'A_F2' for i in citation):
                        auth2=auth[2]
                        citation=citation.replace('A_F2',auth2[0])
                    if any(i in 'A_L2' for i in citation):
                        citation=citation.replace('A_L2',auth[3])
        #title,subtitle,publisher,publicationDate,author,edition,volNumber,location,URL,network,pageRange
                if any(i in 'title' for i in citation) :
                    citation=citation.replace('title',d1.title)
                if any(i in 'VideoTitle' for i in citation) :
                    citation=citation.replace('VideoTitle',d1.title)
                if any(i in 'ArticleTitle' for i in citation) :
                    citation=citation.replace('ArticleTitle',d1.title)
                if any(i in 'PodcastName' for i in citation):
                    citation=citation.replace('PodcastName',d1.subtitle)
                if any(i in 'JournalTitle' for i in citation):
                    citation=citation.replace('JournalTitle',d1.subtitle)
                if any(i in 'Publisher' for i in citation):
                    citation=citation.replace('Publisher',d1.publisher)
                if any(i in 'PublicationYear' for i in citation):
                    year=d1.publicationDate
                    citation=citation.replace('PublicationYear',year[0:4])
                if any(i in 'PublicationDate' for i in citation):
                    citation=citation.replace('PublicationDate',d1.publicationDate)
                if any(i in '(Ed.)' for i in citation):
                    citation=citation.replace('(Ed.)',d1.edition)
                if any(i in 'number' for i in citation):
                    citation=citation.replace('number',d1.volNumber)
                if any(i in 'location' for i in citation):
                    citation=citation.replace('location',d1.location)
                if any(i in 'URL' for i in citation):
                    citation=citation.replace('URL',d1.URL)
                if any(i in 'network' for i in citation):
                    citation=citation.replace('network',d1.video)
                if any(i in 'Podcast' for i in citation):
                    citation=citation.replace('Podcast',d1.video)
                if any(i in 'pageRange' for i in citation):
                    citation=citation.replace('pageRange',d1.pageRange)
            print(citation)
#Lname<comma><space>FI<dot><space>PublicationYear<dot><space>title(italics)<dot><space>location<colon><space>Publisher

'''
sample data model input for the above rule

title :            "jungle book"
publisher:         "Disney"
publication:       "2016, July"
author:            "TOM, JILL and ROSE MARY"   
edition:           "3rd"
location:          "Miami"
'''
main()             
