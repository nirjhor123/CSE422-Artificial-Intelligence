f=open('input.txt')
g={}
hurestic={}
while True:
  line=f.readline()
  if line=="":
    break
  line=line.split()
  u=line[0]
  hu=line[1]
  #print(line[1])
  hurestic[u]=int(hu)
  for i in range(2,len(line)):
    #print(i)
    if i%2==0:
      v=line[i]
    else:
      w=int(line[i])
      #print(w)
      if u not in g:
        g[u]=[]
      g[u].append((v,w))
#print(g)                    
#print(hurestic)
import math
import queue
frontier=queue.PriorityQueue()
d={}
p={}
estimated={}
def a_star_search(g,s,e):
  import queue
  frontier=queue.PriorityQueue()
  for i in g:
    d[i]=math.inf
    p[i]=None
    estimated[i]=math.inf
  d[s]=0
  #print(dh)
  #dh[s]=hs[s]
  frontier.put((estimated[s],s))
 # print(frontier.qsize())
  #print(frontier.get())
  while frontier.qsize()!=0:
      v=frontier.get()                   #item in frontier
      visited=v[1]                         #name of the place
     # print("Visited",visited)
      for i in g[v[1]]:
              #print(i)
              #print(i[0])
              #print(d[i[0]])
             
              #print(visited,d[visited])
              #print(d[visited]+i[1])
              if(d[i[0]]>d[visited]+i[1]):
                d[i[0]]=d[visited]+i[1]
                estimated[i[0]]=d[i[0]]+hurestic[i[0]]
                #print(estimated)
                p[i[0]]=v[1]
                frontier.put((estimated[i[0]],i[0]))
                #print(list(frontier.queue))
              if v==e:
                #print(p)
                #print(d[e])
                break
  #print(d)
  if(d[e]==math.inf):
     print("No path found")
  else:
      a=e
      r=""
      while(a!=s):
          if(a==e):
               r=a+r
          else:
               r=a+"->"+r
          a=p[a]
      r=s+"->"+r
      if(r==""):
          print("NO PATH FOUND")
      else:
         
         print("Path: "+r)
         print("Total Distance :"+str(d[e])+" km")
      #print(list(frontier.queue))

a_star_search(g,'Arad','Bucharest')
#print(frontier.qsize())