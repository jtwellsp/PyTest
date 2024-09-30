

# **How to Run**
To run this project, use the following command:
```bash
python -m puzzle_solver.main
 ```

# **Write Up**

I started writing this code orginally in C++, I quickly ran into some memory leaking issues and switched over to python. Although python seemed to be better for the overall finished product, I ran into a few issues. One of the issues was slowness, because of testing, I began with a small tree to just see if it was working first, I had used a 2x2 square. When switching to a 3x3 this seemed to slow things down quite a bit, although this very well could've been the machine I was running it on it overall just took me longer to get to the finished product. When I finally got my code working, I at first thought we need to include cost for both BFS and A*, this turned out to be false and I had to later go in and change this. One thing I did differently then the project spec sheet, I didn't allowed the algorithm to fail if the soluntion was not possible, to fix this I created a class to run a checker to make sure it would work before testing. The importance of this is to ensure that there is no infinte loops being created, I could have used error-handling here bud decided against it for a clean appearance and a way to compare BFS and A* easier. <br><br>


The good, my code is running and functioning well, there is a few concerns though, when running both BFS and A* I get very similiar results if not exactly identical. Although this is something that worried me at first as if my program wasn't functioning properly, after a little research and going back through class notes I realized that the results might end up the same for both because the paths aren't deep enough for BFS to be truly affected yet. My worry though is the cost seems to be also the same, and this seems to be a worrying factor considering A* might take more steps but ultimatly it will find the shortest path at the end, but I feel as this should also affect the cost because of it having to predict. A* is known for being the best to find the shortest path but ultimatly after implementing a method to run both of these I feel for the case of this programming assignment BFS and A* are very similar because the puzzle isn't big enough to truly affect the outcome of finding shortest path. <br><br>


What went well for me, after switching to python I was able to get the code knocked out quickly, my results and everything seems to be working atleast. I decided to use tuple's because they seem to be better at handling and keeping track of things. I also used the following librarys:

```python
from heapq import heappush, heappop
from collections import deque
```
These librarys allowed me to use heappop, and heappush to keep track and store values to use later. This seemed to be very useful and led me to better be able get to the solutions in testing.<br> <br>


The bad, I am unsure currently if what I stated above is entierly factual and am having a little bit of a hard time finding proper documentation or explanations to support my theory. With limited time left and the project being due tonight I am faced with the problem of having to submit without knowing if what I am saying it true or not. I plan on researching and maybe trying to implement DFS as well into this and see if I can gain any other infomation. If there is any suggestions for issues please let me know, I am always open to feedback on how to improve this code. <br>

### Author

[Author: JT Wellspring](https://github.com/jtwellsp)

[Instructor: Dr. Snehasis Mukhopadhyay](https://science.indianapolis.iu.edu/people-directory/people/mukhopadhyay-snehasis.html)


### Useful Resources Used

[BFS Understanding](https://dev.to/lukegarrigan/what-is-bfs-breadth-first-search-nad)

[A* Understanding](https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288)

Professor Resources and Class Material