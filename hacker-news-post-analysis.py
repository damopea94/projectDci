#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 1. We import our data 
# 2. Remove our headers from list
# Hacker News is where clients can submit posts that are decided on and remarked upon by different clients. I will concentrate on two sorts of posts from Hacker News: Ask HN and Show HN. Ask HN are posts that ask the Hacker News people group explicit inquiries while Show HN entries show client tasks to the network. The top Hacker News posts which have the most remarks can get a huge number of guests to their locales. In this undertaking, I will break down an informational collection (https://www.kaggle.com/programmer news/programmer news-posts) from Kaggle to decide if Ask HN or Show HN posts get more remarks overall. The informational collection has been diminished from ~3000,000 lines to ~20,000 pushes by expelling all entries which didn't get any remarks.

# In[32]:


from csv import reader
open_file = open('hacker_news.csv')
read_file = reader(open_file)
hn = list(read_file)
hn_header= hn[0]
hn = hn[1:]
print(hn_header)
print(hn[:5])


# # Removing Ask HN and Show HN Posts
# 1.Since we're just worried about post titles starting with Ask HN or Show HN, we'll make new arrangements of records containing only the information for those titles.So we sepertae our data for better analysis.
# 

# In[47]:


ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    
    title = post[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(post)
       
    elif title.lower().startswith("show hn"):
        show_posts.append(post)
        
    else:
        other_posts.append(post)
        
print('ask posts:',         len(ask_posts))
print('show posts:',       len(show_posts))
print('other posts:',     len(other_posts))


# # Calculating the average number of posts for ask posts and show posts.
# Let's find the average number of comments existing in ask_posts and show_posts and see which of the two type of posts have the largest average number of comments.

# In[54]:


total_ask_comments = 0
# Finding average number of comments in ask_posts

for item in ask_posts:
    total_ask_comments += int(item[4])
    
avg_ask_comments = total_ask_comments/len(ask_posts)
print('ask comments:',  avg_ask_comments)
print('\n')

# Finding average number of comments in show_posts
total_show_comments = 0
for item in show_posts:
    total_show_comments += int(item[4])
    
avg_show_comments = total_show_comments/len(show_posts)
print('show comments:',   avg_show_comments)


# From the above results we can see that show posts receive less comments on average than ask posts.Posts whose title starts with 'Ask comments' have more normal remarks than posts whose title starts with  'Show comments'.This end bodes well since posts who are provoking a talk would be bound to get remarks than presents whose objective is in plain view client work.
# 
# 

# # Calculating the amount of ask posts and total number of comments created per hour
# 

# In[56]:


import datetime as dt

result_list = []
counts_by_hour = {}
comments_by_hour = {}

# Created_at column is in elemdent of index 6
# and number of comments is in column with index 4
for posts in ask_posts:
    result_list.append([posts[6], int(posts[4])])
                        
for row in result_list:
    row[0] = dt.datetime.strptime(row[0], "%m/%d/%Y %H:%M")
    if row[0].hour not in counts_by_hour:
        counts_by_hour[row[0].hour] = 1
        comments_by_hour[row[0].hour] = row[1]
    else:
        counts_by_hour[row[0].hour] += 1
        comments_by_hour[row[0].hour] += row[1]
print("Number of ask HN posts created by hour ->", counts_by_hour)
print("\n")
print("Number of ask HN comments created by hour ->", comments_by_hour)


# # Calculating the average number of comments for posts created during each hour of the day
# 

# In[66]:


swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)


# In[67]:


sorted_swap = sorted(swap_avg_by_hour, reverse = True)

print(sorted_swap)


# # Printing the five highest average number of comments for posts created during each hour of the day

# In[74]:


# Sort the values and print the the 5 hours with the highest average comments.

print("5 highest average numbers of comments")

for avg, hr in sorted_swap[:5]:
    print( "{}: {:.2f} average comments per post".format(dt.datetime.strptime(str(hr), "%H").strftime("%H:%M"),avg ))


# # Conclusion

# Prior to this undertaking, it was built up that Hacker News posts with the Ask HN posts have increasingly normal remarks than the Post Hn posts. In this manner, a client is bound to get their post to the highest point of the Hacker News posting on the off chance that they make Ask HN post types. In the wake of examining the hour of each posting and averaging the number of remarks every hour, the information proposes that the main 5 hours for Ask Posts to get remarks are: 15, 2, 20, 16, and 21 UTC.
# From the results above we see that ask HN posts created at 3PM ET/10:00 PM UTC+3 have a higher chance of receiving comments.

# In[ ]:




