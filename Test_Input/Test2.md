# Mauris eget bibendum neque.

- Fusce ut molestie massa, eu commodo eros. Suspendisse convallis, eros non sollicitudin posuere, orci augue tincidunt velit, nec sodales metus urna eu nibh. 
 
- Vestibulum nec ex id arcu aliquam varius quis nec nisl. Nullam massa turpis, porttitor vitae pretium nec, feugiat non turpis. 
   
   - Quisque faucibus ipsum non convallis aliquam. 

   - Fusce iaculis urna justo, a elementum enim volutpat tempor. 
   
   - Maecenas eget sollicitudin dolor, id dapibus mi. 
   
   - Cras non purus ac ex varius convallis ut at nisi.
 
## Phasellus vitae bibendum dui. Suspendisse potenti. 

- Mauris accumsan eleifend nisl ac vestibulum. 

- In quis sapien augue. Nullam vel elit ante. 

- Integer imperdiet faucibus facilisis. 

- Aenean condimentum eros et dui iaculis, non luctus ligula rhoncus.
 
 - Phasellus facilisis vulputate erat, in mattis lorem rutrum id. 
 
 - Morbi accumsan volutpat metus, eu condimentum ante venenatis at. 
 
 - Donec sodales sapien quam, et venenatis nunc facilisis ac. Nulla semper, tortor non efficitur ultrices, libero sem pulvinar orci, et gravida ex metus at felis. 
 
 - Morbi cursus velit neque, pulvinar rhoncus sapien efficitur eget. Curabitur tempor, purus id tempus sodales, nulla lorem semper erat, non placerat mauris arcu sit amet elit. Etiam mollis vitae nisi eu lobortis.

1. Vivamus justo nisl, consectetur id felis sit amet, mollis lacinia ligula. 

2. Duis ac urna ut est egestas malesuada. Sed placerat lectus ut quam sodales ultricies. 

3. Quisque imperdiet turpis id urna placerat, in laoreet nisl tristique. 

4. Vestibulum vehicula ligula sed nibh aliquet aliquam. Pellentesque eget pulvinar turpis, quis ultricies turpis. 

5. Cras sagittis odio vitae ex commodo, in pellentesque dolor venenatis. 

6. Morbi ut augue feugiat, pretium mauris sed, aliquam metus.

7. Aliquam elementum hendrerit bibendum. Integer nec euismod metus. 

8. Nulla commodo convallis euismod. Donec tempor neque nec consectetur fringilla. 

9. Sed pharetra risus sit amet vestibulum tristique. Pellentesque lacus tellus, vestibulum sed purus et, pellentesque vestibulum lacus. 

10. Donec ut dictum diam. Aliquam feugiat sem lacus, nec porta mauris aliquam ac. 

11. Etiam dignissim ullamcorper felis, sit amet blandit augue.

## Donec suscipit, nunc a lobortis laoreet, magna ex ullamcorper lorem, at sagittis neque libero scelerisque felis. 

   - Donec suscipit congue lorem.

  - Aliquam et scelerisque lacus. 
  
  - Phasellus porttitor eleifend dui, ac tristique quam feugiat vel. Quisque eget sagittis nulla. 
 
 - Curabitur pulvinar quam non enim hendrerit tempus. Integer condimentum nibh eget mollis semper. Nam aliquam molestie odio eget mollis.
 
  - Quisque in euismod ligula, sed tempor justo. 
 
 - Suspendisse fringilla eu orci quis hendrerit. Cras elit mauris, eleifend in nisi id, pharetra tincidunt metus. Sed at dui mi. Nam vitae feugiat augue.

## Codes :

```java

public class Main {

  public static void main(String[] args) {

    // positive number
    int number = 60;

    System.out.print("Factors of " + number + " are: ");

    // loop runs from 1 to 60
    for (int i = 1; i <= number; ++i) {

      // if number is divided by i
      // i is the factor
      if (number % i == 0) {
        System.out.print(i + " ");
      }
    }
  }
}

```
```c

#include <stdio.h>

int main() {

    double num;
    printf("Enter a number: ");
    scanf("%lf", &num);
    if (num <= 0.0) {
        if (num == 0.0)
            printf("You entered 0.");
        else
            printf("You entered a negative number.");
    } 
    else
        printf("You entered a positive number.");

    return 0;
}

```

```python

# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)



```

```xml

<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>

```