def check(slope,xb,yb,xr,yr):
    z=yb-yr-slope*(xb-xr)
    if slope>=10000 or slope<-99999:
        z=xb-xr
    if z>0:#red
        return 1
    elif z==0:
        return 2
    else:
        return 0
t=input()
while t>0:
    t-=1
    n,m=map(int,raw_input().split())
    red=[]#n red
    blue=[]
    for i in range(n):
        x,y=map(int,raw_input().split())
        red.append([x,y])
    for i in range(m):
        x,y=map(int,raw_input().split())
        blue.append([x,y])
    red.sort(key=lambda x:x[0])
    slopes=[]
    for i in range(n):
        flag=0
        mi=100000
        ma=-999999999
        x1,y1=red[i]
        for j in range(i,n):#changes
            x2,y2=red[j]
            if x2==x1:
                slopes.append([100000,100000])
                flag=1
                break
            slope=((y2-y1)*1.0)/(x2-x1)
            mi=min(mi,slope)
            ma=max(ma,slope)
        if flag==0:
            slopes.append([mi,ma])
    maxim=-1
   # print red
    #print slopes
    for i in range(n):
        xr,yr=red[i]
        mi=slopes[i][0]
        ma=slopes[i][1]
        mi1=m
        red_points1=0
        blue_points1=0
        red_points2=0
        blue_points2=0
        red_points3=0
        blue_points3=0
        red_points4=0
        blue_points4=0
        
        red_points11=0
        blue_points11=0
        red_points22=0
        blue_points22=0
        red_points33=0
        blue_points33=0
        red_points44=0
        blue_points44=0
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points1+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)>=1:
                red_points1+=1
            #else:
             #   blue_points1+=1

                
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points11+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points11+=1
            #else:
             #   blue_points1+=1
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points2+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points2+=1
            #else:
             #   blue_points2+=1
        
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points22+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points22+=1
            #else:
             #   blue_points2+=1

                
                
                
                
        mi=ma
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points3+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                red_points3+=1
            #else:
             #   blue_points1+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points33+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points33+=1
                
                
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points4+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points4+=1
            #else:
             #   blue_points2+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points44+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points44+=1
            #else:
             #   blue_points2+=1
                
                
                
                

        #print red_points1,blue_points1,red_points11,blue_points11
        #print red_points2,blue_points2,red_points22,blue_points22
        #print red_points3,blue_points3,red_points33,blue_points33
        #print red_points4,blue_points4,red_points44,blue_points44
       # print red_points3,blue_points3,red_points4,blue_points4
        #print red_points1,blue_points1,red_points2,blue_points2
        #print red_points3,blue_points3,red_points4,blue_points4
        maxim=max(maxim,red_points1+blue_points1,red_points2+blue_points2)
        maxim=max(maxim,red_points3+blue_points3,red_points4+blue_points4)
        maxim=max(maxim,red_points11+blue_points11,red_points22+blue_points22)
        maxim=max(maxim,red_points33+blue_points33,red_points44+blue_points44)
    
    
    
    
    
    
    
    ###########################
    ################
    
    temp1=[]
    temp2=[]
    for i in range(n):
        temp1.append(red[i])
    for i in range(m):
        temp2.append(blue[i])
    red=[]
    blue=[]
    for i in range(m):
       red.append(temp2[i])
    for i in range(n):
        blue.append(temp1[i])
    #print maxim
    temp=n
    n=m
    m=temp
    
    ##
	#print maxim
    red.sort(key=lambda x:x[0])
    slopes=[]
    for i in range(n):
        flag=0
        mi=100000
        ma=-999999999
        x1,y1=red[i]
        for j in range(i,n):
            x2,y2=red[j]
            if x2==x1:
                slopes.append([100000,100000])
                flag=1
                break
            slope=((y2-y1)*1.0)/(x2-x1)
            mi=min(mi,slope)
            ma=max(ma,slope)
        if flag==0:
            slopes.append([mi,ma])
    for i in range(n):
        xr,yr=red[i]
        mi=slopes[i][0]
        ma=slopes[i][1]
        red_points1=0
        blue_points1=0
        red_points2=0
        blue_points2=0
        red_points3=0
        blue_points3=0
        red_points4=0
        blue_points4=0
        
        red_points11=0
        blue_points11=0
        red_points22=0
        blue_points22=0
        red_points33=0
        blue_points33=0
        red_points44=0
        blue_points44=0
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points1+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)>=1:
                red_points1+=1
            #else:
             #   blue_points1+=1

                
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points11+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points11+=1
            #else:
             #   blue_points1+=1
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points2+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points2+=1
            #else:
             #   blue_points2+=1
        
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points22+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points22+=1
            #else:
             #   blue_points2+=1

                
                
                
                
        mi=ma
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points3+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                red_points3+=1
            #else:
             #   blue_points1+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points33+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points33+=1
                
                
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points4+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points4+=1
            #else:
             #   blue_points2+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points44+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points44+=1
            #else:
             #   blue_points2+=1
                
                
                
                

     #   print red_points1,blue_points1,red_points2,blue_points2
      #  print red_points3,blue_points3,red_points4,blue_points4
        #print red_points1,blue_points1,red_points2,blue_points2
        #print red_points3,blue_points3,red_points4,blue_points4
        maxim=max(maxim,red_points1+blue_points1,red_points2+blue_points2)
        maxim=max(maxim,red_points3+blue_points3,red_points4+blue_points4)
        maxim=max(maxim,red_points11+blue_points11,red_points22+blue_points22)
        maxim=max(maxim,red_points33+blue_points33,red_points44+blue_points44)
    
    
    
    
    


































	temp1=[]
    temp2=[]
    for i in range(n):
        temp1.append(red[i])
    for i in range(m):
        temp2.append(blue[i])
    red=[]
    blue=[]
    for i in range(m):
       red.append(temp2[i])
    for i in range(n):
        blue.append(temp1[i])
    #print maxim
    temp=n
    n=m
    m=temp
    
    ##
	#print maxim
    red.sort(key=lambda x:x[0])

	

    for i in range(n):
        flag=0
        mi=100000
        ma=-999999999
        x1,y1=red[i]
        for j in range(m):#changes
            x2,y2=blue[j]
            if x2==x1:
                slopes.append([100000,100000])
                flag=1
                break
            slope=((y2-y1)*1.0)/(x2-x1)
            mi=min(mi,slope)
            ma=max(ma,slope)
        if flag==0:
            slopes.append([mi,ma])
    #maxim=-1
   # print red
    #print slopes
    for i in range(n):
        xr,yr=red[i]
        mi=slopes[i][0]
        ma=slopes[i][1]
        mi1=m
        red_points1=0
        blue_points1=0
        red_points2=0
        blue_points2=0
        red_points3=0
        blue_points3=0
        red_points4=0
        blue_points4=0
        
        red_points11=0
        blue_points11=0
        red_points22=0
        blue_points22=0
        red_points33=0
        blue_points33=0
        red_points44=0
        blue_points44=0
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points1+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)>=1:
                red_points1+=1
            #else:
             #   blue_points1+=1

                
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points11+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points11+=1
            #else:
             #   blue_points1+=1
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points2+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points2+=1
            #else:
             #   blue_points2+=1
        
        
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points22+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points22+=1
            #else:
             #   blue_points2+=1

                
                
                
                
        mi=ma
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0:
                blue_points3+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                red_points3+=1
            #else:
             #   blue_points1+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                blue_points33+=1
            #else:
                #blue_points1+=1
      #  print 
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==1:
                red_points33+=1
                
                
                
                
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1:
                blue_points4+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0 or check(mi,xb,yb,xr,yr)==2:
                red_points4+=1
            #else:
             #   blue_points2+=1
                
        for j in range(m):
            xb,yb=blue[j]
            if check(mi,xb,yb,xr,yr)==1 or check(mi,xb,yb,xr,yr)==2:
                blue_points44+=1
            #else:
             #   blue_points2+=1
        for j in range(n):
            xb,yb=red[j]
            if check(mi,xb,yb,xr,yr)==0:
                red_points44+=1
            #else:
             #   blue_points2+=1
                
                
                
                

        #print red_points1,blue_points1,red_points11,blue_points11
        #print red_points2,blue_points2,red_points22,blue_points22
        #print red_points3,blue_points3,red_points33,blue_points33
        #print red_points4,blue_points4,red_points44,blue_points44
       # print red_points3,blue_points3,red_points4,blue_points4
        #print red_points1,blue_points1,red_points2,blue_points2
        #print red_points3,blue_points3,red_points4,blue_points4
        maxim=max(maxim,red_points1+blue_points1,red_points2+blue_points2)
        maxim=max(maxim,red_points3+blue_points3,red_points4+blue_points4)
        maxim=max(maxim,red_points11+blue_points11,red_points22+blue_points22)
        maxim=max(maxim,red_points33+blue_points33,red_points44+blue_points44)

    print n+m-maxim
