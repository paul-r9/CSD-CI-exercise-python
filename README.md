# ISBN - International Standard Book Number


[![Build Status](https://dev.azure.com/paul0287/CSD-CI-exercise-python/_apis/build/status/paul-r9.CSD-CI-exercise-python?branchName=trunk)](https://dev.azure.com/paul0287/CSD-CI-exercise-python/_build/latest?definitionId=5&branchName=trunk)

[Azure DevOps Project page](https://dev.azure.com/paul0287/CSD-CI-exercise-python)


There are two ISBN standards: ISBN-10 and ISBN-13. Support for ISBN-13 is essential, whereas support for ISBN-10 is optional.

Here are some valid examples of each:

### ISBN-10
- 0 0201485672
- 0 201 48567 2
- 0-201-48567-2
- 0-439-42089-X
- 0-321-14653-0

### ISBN-13
- 9780201485677
- 978 0 131 49505 0
- 978-0596809485
- 978-0-13-595705-9
- 978-0-262-13472-9


ISBN-10 is made up of 9 digits plus a check digit (which may be 'X') and ISBN-13 is made up of 12 digits plus a check digit. Spaces and hyphens may be included in a code, but are not significant. This means that 9780471486480 is equivalent to 978-0-471-48648-0 and 978 0 471 48648 0.

The check digit for ISBN-10 is calculated by multiplying each digit by its position (i.e., 1 x 1st digit, 2 x 2nd digit, etc.), summing these products together and taking modulo 11 of the result (with 'X' being used if the result is 10).

The check digit for ISBN-13 is calculated by multiplying each digit alternately by 1 or 3 (i.e., 1 x 1st digit, 3 x 2nd digit, 1 x 3rd digit, 3 x 4th digit, etc.), summing these products together, taking modulo 10 of the result and subtracting this value from 10, and then taking the modulo 10 of the result again to produce a single digit.


Basic task:

- [ ] Create a function that takes a string and returns true if that is a valid ISBN-13 and false otherwise.
- [ ] Handle ISBN-13 strings with dashes
- [ ] Handle ISBN-13 strings with spaces

Advanced task:

- [ ] Also validate ISBN-10 strings.
- [ ] ISBN-10 checksum digit can sometimes be "X"
- [ ] Add ability to lookup BookInfo by ISBN. ISBN should be validated before doing the Service lookup. Create a Fake that is passed into the ISBN class via constructor injection. The fake will act as an ISBNService that returns BookInfo for a valid ISBN.


Here is some valid BookInfo to use with the Fake. 

| Title                                     | Author         | ISBN-10    | ISBN-13       |
|-------------------------------------------|----------------|------------|---------------|
| 97 Things Every Programmer Should Know    | Kevlin Henney  | 0596809484 | 9780596809485 |
| Accelerate | Forsgren, Humble, Kim | 1942788339 | 9781942788331 |
| Pattern-Oriented SW Architecture Vol 1 |Frank Buschmann |0471958697 | 9780471958697 |
| Pattern-Oriented SW Architecture Vol 2 | Douglas Schmidt | 0471606952 | 9780471606956 |
| Pattern-Oriented SW Architecture Vol 3 | Michael Kircher | 0478084525 | 9780470845257 |
| Pattern-Oriented SW Architecture Vol 4 | Frank Buschmann | 0470059028 | 9780470059029 |
| Pattern-Oriented SW Architecture Vol 5 | Frank Buschmann | 0471486485 | 9780471486480 |
| Refactoring | Martin Fowler | 0201485672 | 9780201485677 |
| Refactoring 2nd Edition | Martin Fowler | 0134757599 | 9780134757599 |
| Test Driven Development by Example | Kent Beck | 0321146530 | 9780321146533 |
| The Laws of Simplicity | John Maeda | 0262134721 | 9780262134729 |
| The Thief Lord | Cornelia Funke | 043942089X  | 9780439420891 |
| Working Effectively with Legacy Code | Michael Feathers | 0131177052 | 9780131177055 |
| xUnit Test Patterns | Gerard Meszaros | 0131495054 | 9780131495050 |

