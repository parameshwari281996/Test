import pandas as pd



import glob
txt_files=glob.glob('C:/Co/txtfile/*.txt')

def scrape():
    Username=[]
    Industry=[]
    heading=[]
    Date=[]
    Description=[]
    pros=[]
    Cons=[]
    rating=[]
    for r in range(len(txt_files)):
        print( txt_files[r])
        filne = txt_files[r]
        with open(filne,encoding="utf-8") as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 



        # Extract Heading ,Date & Description
       # heading=[]
       # Date=[]

        for i,x in enumerate(content) :
            if x =="Share this review:":
                heading.append(content[i+1])
                Date.append(content[i+2])

                #Remove Heading 
                content.remove(content[i+1])

        #Remove Date        
        for i,x in enumerate(content) :
            if x =="Share this review:":        
                content.remove(content[i+1])
        #Description=[]

        for i,x in enumerate(content) :
            if "Share this review:" in x:  
                if "Pros" not in content[i+1]: 
                    if "Read less" not in content[i+1]: 
                        Description.append(content[i+1])
                        #content.remove(content[i+1])
                       # print(content[i+1])

                else:
                    Description.append(" ")
                
                
        #Extract Pros
       # pros=[]
        for i,x in enumerate(content) :
            if x =="Pros":        
                pros.append(content[i+1])
                #print(content[i+1])
                content.remove(content[i+1])  


        #Extract Cons
       # Cons=[]
        for i,x in enumerate(content) :
            if x =="Cons":        
                Cons.append(content[i+1])
                content.remove(content[i+1])     


        #Extract & remove Rating

        #rating = []
        for i,x in enumerate(content) :
            if "Share this review:" in x:  
                if "Customer support" not in content[i-1]: 
                    if "Features" not in content[i-1]: 
                       # print(content[i-1])
                        rating.append(content[i-1])
                        #content.remove(content[i+1]) 
                else:
                     rating.append(" ")

        #Remove description
        content=[word for word in content if word not in Description]
        stopwords = stopwords = ['Verified reviewer','Overall Rating', 'Value for money','Ease of use','Customer support','Likelihood to recommend','Share this review:',
                'Pros','Cons','Features','1', '2', '3','4','5','6','7','â€¦','54','page 1 of 54','1349 reviews','Sort by','Recommended','Read less','Overall Rating',
                'Most Recent',' reviews']

        new_content=[word for word in content if word not in stopwords]
        new_content = [i for i in new_content if len(i) > 2]
        new_content=[word for word in new_content if word not in rating]

    #extraction of username


        test_list=["employees",'Computer Software'," self-employed","Marketing and Advertising","Internet",
                   'Management Consulting','Financial Services']


        for i,x in enumerate(new_content) :
                if "Review source:" in x:  

                    if "Used " in new_content[i-1]:

                        res = [ele for ele in test_list if(ele  in new_content[i-2])] 
                        result=bool(res)
                        if result==True:
                            print("<<<",new_content[i-3])
                            Username.append(new_content[i-3])
                            new_content.remove(new_content[i-3]) 
                        else:
                            print("___",new_content[i-3])
                            Username.append(new_content[i-2]) 

                    else:
                        res = [ele for ele in test_list if(ele  in new_content[i-1])] 
                        result=bool(res)
                        if result==True:
                            Username.append(new_content[i-2])
                            new_content.remove(new_content[i-2]) 

                        else:

                            print(new_content[i-1])  
                            Username.append(new_content[i-1])
                            new_content.remove(new_content[i-1]) 

                   

        #extract industry

        for i,x in enumerate(new_content) :
            if "Review source:" in x:  

                if "Used " in new_content[i-1]:
                    if "employees" in new_content[i-2]:

                        Industry.append(new_content[i-2])

                    elif " self-employed" in new_content[i-2]:   
                        Industry.append(new_content[i-2])     
                    else:
                       
                        Industry.append(" ") 
                else:

                    Industry.append(" ")
                    
                    
    rating=[i.split("/")[0] for i in rating]
    df= pd.DataFrame(list(zip(Username, Industry,heading,Date,Description,pros,Cons,rating)), 
                   columns =[ "Username" , "Industry" , "Heading" , "Date" , "Review_description" , "Pros" , "Cons" , "likelihood_to_recommend"]) 
    df['likelihood_to_recommend'] = df['likelihood_to_recommend'].replace({'Overall Rating':' ','Ease of use':''}, regex=True)
    print(len(Username))
    print(len(Industry))
    print(len(heading))
    print(len(Date))
    print(len(Description))
    print(len(pros))
    print(len(Cons))
    print(len(rating))
    df.to_csv("Pack_Test.csv")
    
if __name__ == "__main__": 
    txt_files=glob.glob('C:/Co/txtfile/*.txt')

    scrape()


