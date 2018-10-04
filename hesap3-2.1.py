
# coding: utf-8

# In[30]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[81]:

def draw_some_vector(v,m):
    x= [v[0],m[0]]
    y= [v[1],m[1]]
    
    plt.axis([-15, 15, -15, 15])
    plt.plot(x,y)

def scaler_exp(a,b):
    return (a[0]*b[0]+a[1]*b[1])

def vektor_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]

def vektor_subs(v,w):
    return [v[0]-w[0],v[1]-w[1]]

def vektor_skalerle_carpim(c,v):
    return [c*v[0],c*v[1]]

def vektor_distance(v,w):
    return ( ((w[0]-v[0])**2) + ((w[1]-v[1])**2) ) **.5


# In[82]:

v=[5,5]
w=[3,3]
k=[1,7]
draw_some_vector(k,w)
draw_some_vector([0,0],v)

print (vektor_skalerle_carpim(5,w))
print (scaler_exp(w,v))
print (vektor_add(w,v))
print (vektor_distance(v,w))

v=[5,5]
w=[10,12]
draw_some_vector(v,w)
draw_some_vector([0,0],[-7,5])


# In[ ]:



