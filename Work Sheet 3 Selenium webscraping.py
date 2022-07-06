#!/usr/bin/env python
# coding: utf-8

# Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Analyst” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


# In[2]:


driver = webdriver.Chrome(r'C:\Users\prath\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


# In[3]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[4]:


search_job = driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_job


# In[5]:


search_job.send_keys("Data Analyst")


# In[6]:


ser_loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
ser_loc


# In[7]:


ser_loc.send_keys("Bangalore")


# In[8]:


ser_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
ser_bot


# In[9]:


ser_bot.click()


# In[10]:


t_tag = driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
t_tag


# In[13]:


job_titles=[]

for i in t_tag[0:10]:
    job_titles.append(i.text)
job_titles


# In[14]:


company = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
len(company)


# In[15]:


company_name=[]

for i in company[0:10]:
    company_name.append(i.text)
company_name


# In[16]:


xp = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(xp)


# In[17]:


EXP=[]

for i in xp[0:10]:
    EXP.append(i.text)
EXP


# In[18]:


loc = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(loc)


# In[19]:


Loc=[]

for i in loc[0:10]:
    Loc.append(i.text)
Loc


# In[20]:


df = pd.DataFrame({'Job Titles':job_titles,'company Name':company_name,'Experience':EXP, 'Location':Loc})
df


# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You 
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, Companies” field and enter “Bangalore” in “enter the
# location” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[21]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


# In[22]:


driver = webdriver.Chrome(r'C:\Users\prath\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


# In[23]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[24]:


search_job = driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_job


# In[25]:


search_job.send_keys("Data Scientist")


# In[26]:


ser_loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
ser_loc


# In[27]:


ser_loc.send_keys("Bangalore")


# In[28]:


ser_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
ser_bot


# In[29]:


ser_bot.click()


# In[30]:


t_tag = driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
len(t_tag)


# In[31]:


job_titles=[]

for i in t_tag[0:10]:
    job_titles.append(i.text)
job_titles


# In[32]:


company = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
len(company)


# In[33]:


company_name=[]

for i in company[0:10]:
    company_name.append(i.text)
company_name


# In[34]:


xp = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(xp)


# In[35]:


EXP=[]

for i in xp[0:10]:
    EXP.append(i.text)
EXP


# In[36]:


loc = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(loc)


# In[37]:


Loc=[]

for i in loc[0:10]:
    Loc.append(i.text)
Loc


# In[38]:


df = pd.DataFrame({'Job Titles':job_titles,'company Name':company_name,'Experience':EXP, 'Location':Loc})
df


# Q3: In this question you have to scrape data using the filters available on the webpage as shown below:
# You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required. 
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs

# In[39]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


# In[40]:


driver = webdriver.Chrome(r'C:\Users\prath\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


# In[42]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[43]:


search_job = driver.find_element(By.CLASS_NAME,"suggestor-input ")
search_job


# In[44]:


search_job.send_keys("Data Scientist")


# In[45]:


ser_loc = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
ser_loc


# In[46]:


ser_loc.send_keys("Delhi")


# In[47]:


ser_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
ser_bot


# In[50]:


ser_bot.click()


# In[54]:


sal = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[5]/div[2]/div[2]/label/i')
sal


# In[55]:


sal.click()


# In[56]:


loc = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[13]/div[2]/div[3]/label/i')
loc


# In[57]:


loc.click()


# In[58]:


t_tag = driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
len(t_tag)


# In[59]:


job_titles=[]

for i in t_tag[0:10]:
    job_titles.append(i.text)
job_titles


# In[60]:


company = driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
len(company)


# In[61]:


company_name=[]

for i in company[0:10]:
    company_name.append(i.text)
company_name


# In[62]:


xp = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
len(xp)


# In[63]:


EXP=[]

for i in xp[0:10]:
    EXP.append(i.text)
EXP


# In[64]:


loc = driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(loc)


# In[65]:


Loc=[]

for i in loc[0:10]:
    Loc.append(i.text)
Loc


# In[67]:


df = pd.DataFrame({'Job Titles':job_titles,'company Name':company_name,'Experience':EXP, 'Location':Loc})
df


# Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# 1. Brand
# 2. Product Description
# 3. Price

# In[69]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


# In[70]:


driver = webdriver.Chrome(r'C:\Users\prath\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


# In[71]:


url = 'https://www.flipkart.com/'
driver.get(url)


# In[73]:


search = driver.find_element(By.CLASS_NAME,"_3704LK")
search


# In[74]:


search.send_keys("sunglasses")


# In[76]:


ser_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
ser_bot


# In[77]:


ser_bot.click()


# In[79]:


product = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
len(product)


# In[80]:


Product=[]

for i in product:
    Product.append(i.text)
Product


# In[82]:


product_dis = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
len(product_dis)


# In[83]:


Product_dis=[]

for i in product_dis:
    Product_dis.append(i.text)
Product_dis


# In[84]:


price = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
len(price)


# In[86]:


Price=[]

for i in price:
    Price.append(i.text)
Price


# In[87]:


nxt_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
nxt_bot


# In[88]:


nxt_bot.click()


# In[90]:


product2 = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
len(product2)


# In[91]:


Product2=[]

for i in product2:
    Product2.append(i.text)
Product2


# In[92]:


product_dis2 = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
len(product_dis2)


# In[93]:


Product_dis2=[]

for i in product_dis2:
    Product_dis2.append(i.text)
Product_dis2


# In[94]:


price2 = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
len(price2)


# In[95]:


Price2=[]

for i in price2:
    Price2.append(i.text)
Price2


# In[96]:


nxt_bot2 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
nxt_bot2


# In[97]:


nxt_bot2.click()


# In[98]:


product3 = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
len(product3)


# In[99]:


Product3=[]

for i in product3[0:20]:
    Product3.append(i.text)
Product3


# In[100]:


product_dis3 = driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
len(product_dis3)


# In[101]:


Product_dis3=[]

for i in product_dis3[0:20]:
    Product_dis3.append(i.text)
Product_dis3


# In[102]:


price3 = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
len(price3)


# In[103]:


Price3=[]

for i in price3[0:20]:
    Price3.append(i.text)
Price3


# In[104]:


Final_price = Price + Price2 + Price3


# In[109]:


len(Final_price)


# In[106]:


total_product = Product + Product2 + Product3


# In[107]:


len(total_product)


# In[108]:


all_dis = Product_dis +Product_dis2 + Product_dis3
len(all_dis)


# In[110]:


df = pd.DataFrame({'Brand':total_product,'Product Description':all_dis,'Price':Final_price})
df


# In[ ]:





# In[111]:


import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By


# In[112]:


driver = webdriver.Chrome(r'C:\Users\prath\Downloads\Compressed\chromedriver_win32\chromedriver.exe')


# In[114]:


url = 'https://www.flipkart.com/'
driver.get(url)


# In[115]:


search = driver.find_element(By.CLASS_NAME,"_3704LK")
search


# In[116]:


search.send_keys("i phone 11")


# In[117]:


ser_bot = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
ser_bot


# In[118]:


ser_bot.click()


# In[119]:


iphone = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
iphone


# In[120]:


iphone.click()


# In[271]:


url = 'https://www.flipkart.com/apple-iphone-11-black-128-gb/product-reviews/itm8244e8d955aba?pid=MOBFWQ6BKRYBP5X8&lid=LSTMOBFWQ6BKRYBP5X8X0KYUG&marketplace=FLIPKART'
driver.get(url)


# In[272]:


Rate= driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
len(Rate)


# In[273]:


rate=[]

for i in Rate:
    rate.append(i.text)
rate


# In[274]:


Com = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
len(Com)


# In[275]:


com=[]

for i in Com:
    com.append(i.text)
com


# In[276]:


Ful_rev = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
len(Ful_rev)


# In[277]:


ful_rev=[]

for i in Ful_rev:
    ful_rev.append(i.text)
ful_rev


# In[278]:


nex = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]")
nex


# In[279]:


nex.click()


# In[280]:


Rate2= driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
len(Rate2)


# In[281]:


rate2=[]

for i in Rate2:
    rate2.append(i.text)
rate2


# In[282]:


Com2 = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
len(Com2)


# In[283]:


com2=[]

for i in Com2:
    com2.append(i.text)
len(com2)


# In[284]:


Ful_rev2 = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
len(Ful_rev2)


# In[285]:


ful_rev2=[]

for i in Ful_rev2:
    ful_rev2.append(i.text)
len(ful_rev2)


# In[286]:


nex = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]")
nex


# In[287]:


nex.click()


# In[288]:


Rate3= driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
len(Rate3)


# In[289]:


rate3=[]

for i in Rate3:
    rate3.append(i.text)
len(rate3)


# In[290]:


Com3 = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
len(Com3)


# In[291]:


com3=[]

for i in Com3:
    com3.append(i.text)
len(com3)


# In[292]:


Ful_rev3 = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
len(Ful_rev3)


# In[293]:


ful_rev3=[]

for i in Ful_rev3:
    ful_rev3.append(i.text)
len(ful_rev3)


# In[294]:


nex = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]")
nex


# In[295]:


nex.click()


# In[296]:


Rate4= driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
len(Rate4)


# In[297]:


rate4=[]

for i in Rate4:
    rate4.append(i.text)
len(rate4)


# In[298]:


Com4 = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
com4=[]

for i in Com4:
    com4.append(i.text)
len(com4)


# In[299]:


Ful_rev4 = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
ful_rev4=[]

for i in Ful_rev4:
    ful_rev4.append(i.text)
len(ful_rev4)


# In[300]:


nex = driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[12]")
nex


# In[301]:


nex.click()


# In[302]:


Rate5= driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]')
rate5 = []
for i in Rate5:
    rate5.append(i.text)
len(rate5)


# In[303]:


rate5.append(1)


# In[304]:


len(rate5)


# In[305]:


Com5 = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
com5=[]

for i in Com5:
    com5.append(i.text)
len(com5)


# In[306]:


Ful_rev5 = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
ful_rev5=[]

for i in Ful_rev5:
    ful_rev5.append(i.text)
len(ful_rev5)


# In[307]:


total_rating = rate + rate2  + rate4 + rate5 +rate3


# In[308]:


len(total_rating)


# In[309]:


total_com = com +com2 +com3 +com4 +com5 


# In[310]:


len(total_com)


# In[311]:


total_rev = ful_rev +ful_rev2 + ful_rev3 + ful_rev4 + ful_rev5 


# In[312]:


len(total_rev)


# In[313]:


df = pd.DataFrame({'Rating':total_rating,'Review summary':total_com,'Full Review':total_rev})
df


# In[ ]:




