#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
```py
a)  
        a = 0 
        while (a < n * n * n):
            a = a + n * n
```
    The runtime complexity is O(n) because the loop only runs as many times as n because the (*n*n) in the while loop is canceled out by the (n*n) in (a = a + n * n)


```py
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
``` 
    The runtime complexity is O(n log n). Because it is nesting two loops, the outer loop is linear to the value of (n) while for the inner while loop the (j) value approaches the (n) at an exponential rate so that makes it's O(log n) for the inner loop
    


```py
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
    The runtime complexity is O(n) because the function resolves once the value of (bunnies) reaches zero and it approaches zero linearly because (bunnies) is subtracted by (1) for every recursion


## Exercise II

    The algorithm will start dropping eggs at floor 0 and the floor value will increase linearly O(n) until the first egg breaks, giving us the value f with the least amount of broken eggs (1)
