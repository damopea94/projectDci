#!/usr/bin/env python
# coding: utf-8

# # APPS THAT ARE PROFFITABLE IN THE MARKET BETWEEN GOOGLEPLAY APP AND IOS APPS.
# The aim of this project is to use the data to analze our data and use it to check trends about apps that are free and more popular amoung the users. 

# In[59]:


from csv import reader


opened_file = open("AppleStore.csv")
read_file = reader(opened_file)
apps_data = list(read_file)
print(len(apps_data))


opened_file_android = open("googleplaystore.csv")
read_file_android = reader(opened_file_android)
apps_data_google = list(read_file_android)
print(len(apps_data_google))


# In[4]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
print(googleplay_header)
print('\n')
explore_data(googleplay, 0,4, True)


# In[17]:


print(ios_header)
print('\n')
element_data(ios, 0,5, True)



# In[18]:


print(googleplay[10472])  # incorrect row
print('\n')
print(googleplay_header)  # header
print('\n')
print(googleplay[0])  


# # Deleting of Data 

# In[19]:


for element in googleplay:  # i looped the data information to erase a line if the length of line dosen't approach the length of the header  
    if len(element) !=13: 
        del(element)
del googleplay[10472] #reading from the discusion 10472 is the incorrect line in the row and NB the code can't be run twice becasue it is going to keep delete our data each time we run it.
print(len(googleplay))


# In[63]:


print('\n')
explore_data(apps_data,0,1, True)


# # Data that keeps appearing 

# In[33]:


duplicate_apps = []
unique_apps = []

for app in googleplay: # i looped through the googleplay data set.
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')


# # There was 1181 duplicted data when we ran our code. we careated two lists duplicated apps and unique apps.  

# In[34]:


reviews_apps={} # created empty dicitionary with the name reviews apps.

for apps in googleplay: # looped through the googleplay set so when i run my data it dosent include the header.
    name=apps[0]
    n_reviews=float(apps[3]) 
    
    if name in reviews_apps and reviews_apps[name] < n_reviews: # we looped through the review apps 
        reviews_apps[name] = n_reviews
        
    elif name not in reviews_apps:
        reviews_apps[name] = n_reviews
print('initial length:', len(googleplay))
print('Actual length:', len(reviews_apps))


# # To expel the duplicated entries  above,we will create an empty dictionary where each key is a unique app name and value is the most elevated number of reviews. number of audits.

# # Removing row by creating empty lists
# (a) the geogleplay clean store new cleaned data 
# (b) already added  store app names in the data
# we use this to confirm the number of rows in our data

# In[35]:


googleplay_clean = [] # create googleplay empty list to store new data 
already_added = []     # used to store the apps name 

for apps in googleplay: 
    name=apps[0]
    n_reviews=float(apps[3]) # extracting data converting it to float
    
    if (reviews_apps[name] == n_reviews) and (name not in already_added):
        googleplay_clean.append(apps)  
        already_added.append(name) # we append already added to name
    
print(len(googleplay_clean))


# # Removing Non-English Appps 
# * some of the apps are intended for non english clients. our company being a company that create just english apps. we need to sort the english app out of the data.
# * there is a coresponding number with each alpahbet in python therefore we use the function "ord"."ord" return an integer representing the Unicode code point of the character when the argument is a unicode object
# * the number are from 0-127

# In[37]:


def check_english (string): # we define our variable 
    for alphabet in string:
        if ord(alphabet)>127: # we use the function ord when the alaphabet is greater than 127 it return false but if it is less than return True
            return False 
    return True


# # Examples of the code above that return True and False After using the Function 

# In[38]:


check_english('boy')


# In[39]:


check_english('欢乐')


# In[40]:


check_english('Instachat 😜')


# In[64]:


check_english('Docs To Go™ Free Office Suite')


# # create Apps with Emojis and other symbols 
# * looking at the examples above some of the examples with emoji returns false and also Docs To Go™ Free Office Suite
# * this alpahbet falls outside of our range 0-127 which made it return false and it could cost us data loss.

# In[41]:


def check1_english(string): # define function
    in_english = 0
    for alphabet in string:
        if ord(alphabet)>127: 
            in_english +=1 # add 1 to in_english 
    if in_english > 3: # if the addition is greater than 3 (+1 above) the output false but if less than 3 True 
            return False
    else:
            return True


# # Examples are shown below 

# In[42]:


check1_english('Instachat 😜😜😜')


# In[43]:


check1_english("Docs To Go™ Free Office Suite")


# # Sorting our Googleplay English app From Non English Apps 
# * we have 9614 english apps and 45 non englis apps

# In[44]:


googleplay_english = []
googleplay_not_english = []

for app in googleplay_clean:
    string_name = app[0]
    if (check1_english(string_name)) is True:
        googleplay_english.append(app)
        
    else:
        googleplay_not_english.append(app)
print(len(googleplay_english))
print(len(googleplay_not_english))


# # Sorting our Ios English app From Non English Apps 
# * we have 6183 english apps and 1014 non englis apps

# In[45]:


ios_english = []
ios_not_english = []

for app in ios:
    ios_name = app[1]
    if (check1_english(ios_name)) is True:
        ios_english.append(app)
        
    else:
        ios_not_english.append(app)
print(len(ios_english))
print(len(ios_not_english))


# # Isolating free Apps together to get our analysis 
# * we run the data for free apps 
# * We get just english apps only 
# 

# In[47]:


googleplay_final = []
ios_final = []

for app in googleplay_english:
    price = app[7]
    if price == '0': # we use this(==) to make sure the app price is zero dollars
        googleplay_final.append(app)
        
for app in ios_english:
    price = app[4]
    if price == '0.0':
        ios_final.append(app)
        
print(len(googleplay_final))
print(len(ios_final))


# # most popular apps by genre 
# * Construct frequency table for each genre
# * start analsysis by finding the most common genre

# In[48]:


ios_genres={}
googleplay_genres={}

for app in ios_english:
    category =app[11] #category are on row 11
    if category not in ios_genres:
        ios_genres[category] = 1
    else:
        ios_genres[category]+=1
print(ios_genres)
print('\n')

for app in googleplay_english:
    category =app[9] #category are on row 9
    if category not in googleplay_genres:
        googleplay_genres[category] = 1
    else:
        googleplay_genres[category]+=1

print(googleplay_genres)
print('\n')


# # Create frequency table 
# * we create 2 frequency table ios and googleplay 
# * we change the frequency to precentage for better analysis
# * the sorted out data only return as dictionary, so we convert them to tuple where by the dictionary comes first and seprated by : 

# In[49]:


def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
display_table(ios_final, 11) #apple data to analyze


# # The above output can be alayze by
# * The most common genre amoung the ios users is Games.followed by Entertaiment which is 8% whuich photo and vido at 5%
# * I see that most education and social networking are almost the same % which someone indicate people are mostly try to look for apps to educate themselves and at the same time markeeting on social media.
# * The weather and drinks shows almost the same % also which indicate the weather condition plays a role in the app people tends to use to get food and drinks.
# * most apps are such as designed for recreational and relaxing activities such as games and entertainmnet
# * We need to look at the number of download for each genre before reconcomending apps to build.

# In[50]:


display_table(googleplay_final, 9) #analyze


# # The googleplay apps show significant difference form the ios app. The most apps used are Tools and more pritical purposes 
# * The two tables uncover that Entertainment, Games, and Education applications are the most mainstream sorts with the expectation of complimentary English applications. in the two stores
# * The recurrence tables uncover the most continuous application sorts not what types have the most clients.
# 

# # We will presently take a gander at what classifications have been introduced the most. Google Play doesn't have the information from the introduces classification so we will take a gander at the quantity of client evaluations. 
# 
# We will utilize a settled circle to figure the averages¶

# In[51]:


genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)


# # Navigation and social Networking applications are the most famous with audits for the Apple App store.

# In[52]:


display_table(googleplay_final, 5) # the Installs columns how many times they were downloaded 


# # We have to secretiveWe have to covert the install numbers from strings to floats. To evacuate the characters we can utilize str supplant to dispose of commas and in addition to characters. the introduce numbers from strings to glides. To evacuate the characters we can utilize str supplant to dispose of commas and in addition to characters.

# In[53]:


categories_googleplay = freq_table(googleplay_final, 1)
popular_installs=[]

for category in categories_googleplay:
    total = 0
    len_category = 0
    for app in googleplay_final:
        category_app = app[1]
        if category_app == category:            
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    if avg_n_installs > 9000:
        popular_installs.append(category)

print(category, ':', avg_n_installs) #most popular app insalled 


# # * Apps in the googleplay are more toward maps and navigation 

# In[58]:


for app in ios_final:
    if app[-5] == 'Games':
        print(app[1], ':', app[5])


# # The three genres in the App Store with the most downloads are Games, Entertainment, and Photo/Video apps.

# In[60]:


for app in ios_final:
    if app[-5] == 'Games' and int(app[5]) > 700000:
            print(app[1])


# # conclusion 
# We analsye data that could be more profitable for both markets and which apps ia more common amoung the consumers. we see that most popular gneres amoung the googleplay store are more of tools than entertainmnet, i will remcomned ios to build more apps that has do with tools and googleplay For those famous games in the App Store, I would check on the off chance that they are accessible in the Google Play Store. In the event that they are not accessible, my next reccomedation is to make android renditions of those apps.¶

# In[ ]:




