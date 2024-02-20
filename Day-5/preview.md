## * Table of Contents

[Table of Contents](#table-of-contents)\
[Chapter_1](#1--heading) Headings\
[Chapter_2](#2--block-of-words) Block Of Words\
[Chapter_3](#3--line-breaks) Line Breaks\
[Chapter_4](#4--combine-two-things) Combine-two-things\
[Chapter_5](#5--face-of-text) Face Of Text\
[Chapter_6](#6--bullet-points--lists) Bullet Points / Lists\
[Chapter_7](#7--line-breaks-or-page-breaks) Line breaks or Page breaks\
[Chapter_8](#8--links-and-hyperlinks) Links and Hyperlinks\
[Chapter_9](#9--images-and-figures-with-link) Images and Figures with link\
[Chapter_10](#10--adding-code-or-code-block) Adding code or code block\
[Chapter_11](#11--adding-tables) Adding Tables\
[Chapter_12](#12--install-extensions) Install Extensions for markdown language.

***

## 1- Heading

These are different type of headings. For headings we use # and space after #, and write our heading.

```markdown
# Headings: heading 1
## Headings: heading 2
### Headings: heading 3
#### Headings: heading 4
Code is executed below:
```

## Headings: heading 1

## Headings: heading 2

### Headings: heading 3

#### Headings: heading 4

and so on

## 2- Block of Words

This is normal text in markdown.

```markdown
>This is block of Speacial Text. For text like below we use > sign before text.
```

>This is second line by double clicking the enter.

## 3- Line Breaks

This is 40 Days long course on Data Science with python.

>This is second line.(Double enter)\
>This is third line with back slash.

Example:

```md
(Previous Line) one enter
(Next line) second enter
this is secondline.(Double enter)\
this is third line due to slash in the end of previous line

```

## 4- Combine Two Things

Block of words and headings.

`>## Heading 2`

Example:

>## Heading 2

## 5- Face of text

```md
*Italic*
**Bold**
***Bold And Italic***
```

Executed Form:

*Italic*\
**Bold**\
***Bold And Italic***

Or I can also you these symbols

```md
_Italic_    (One Underscore)
__Bold__    (Two Underscores)
___Bold And Italic___ (three underscores)
```

**Executed Form:**

*Italic*    (One Underscore)\
**Bold**    (Two Underscores)\
***Bold And Italic*** (three underscores)\

## 6- Bullet Points / Lists

>Bullet Points:

```md
- Day 1
- Day 2
- Day 3
- Day 4
- Day 5
  - Day 5 (sub-lists)
    - hi
- Day 6

```  

**Executed Form:**

- Day 1
- Day 2
- Day 3
- Day 4
- Day 5
  - Day 5 (sub-lists)
    - hi
- Day 6

>Numbering of lists:

```md
1. Day 1
2. Day 2
3. Day 3
   1. Day 5a
   2. Day 5b
4. Day 4
5. Day 5

```

**Executed Form:**

1. Day 1
2. Day 2
3. Day 3
4. Day 2
5. Day 3
   1. Day 5a
   2. Day 5b
6. Day 4
8. Day 5

>(automatically detect numbers mistakes)

## 7- Line breaks or Page breaks

```md
line after this block is made by ---
```

---

```md
Line after this block is made by ***
```

***

## 8- Links and Hyperlinks
>
>**Only Link:**

```md
<https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/>
< is used in this code for make the link in the notes
```

<https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/>

> **Hyperlink :**

```md
Hi for 40 days python chilla course
 [ClickHere](https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/)

```

Hi for 40 days python chilla course
 [ClickHere](https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/)

>**When using the hyper link again and again**

```md
[Codanics]: https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/

```

[Codanics]: https://codanics.com/courses/python-ka-chilla-for-data-science-40-days-of-python-for-data-science/lesson/who-is-a-data-scientist/

[Codanics] is used here as a hyper link due to the (colon after the Codanics) in the previous code.

>**But if I want to give the link to another name:**

```md
[Shaheer][Codanics] is the student of codanics.com.
He learns now Day 5 lecture of python ka chilla.

```



[Shaheer][Codanics] is the student of codanics.com.
He learns now Day 5 lecture of python ka chilla.


## 9- Images and Figures with link
>
>1. **For opening picture in the markdown loanguage we use the following method:**

```md
![picture.name](image_name_stored_in_the_folder||image_path_directly)
```

![picture.name](p1.jpeg)


>2. **For opening the picture direct from internet link:**

```md
![picture.name](image_link)
```


>3. **But if you want to give link to a picture then use the following syntax:**

```md
[![Imagename](image_link)](link_to_hyperlink)
>example is as follows:
```

<p align="center">
Click this image to open my website<bold>


>>>>>>>>>>>[![hacker](https://cdn0.iconfinder.com/data/icons/kameleon-free-pack/110/Hacker-128.png)](https://kukerytech.wordpress.com/)


>Assignment : *How to comment out a markdown line? and its shortcut.*
## 10- Adding code or code block
>
>For adding a line of code we use ``

For example:

```
`print("Shaheer Ali")`
```

For adding a block of code we use three ` like ``` one both ends of code.

```python
#I have used ``` block of code ```language_name here for showing the syntax colour of representative language.

x="Shaheer Ali"
print(x)
#or directly we can write here name to print
print("Shaheer Ali")
```

>We must show bock of code like above.

## 11- Adding Tables

```md

Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3
```

**Executed Above Code:**
Column A | Column B | Column C
---------|----------|---------
 A1 | B1 | C1
 A2 | B2 | C2
 A3 | B3 | C3

## 12- Install Extensions

   1. Markdown All in One
   2. Markdown pdf
   3. Markdownlint
   4. Markdown Shortcuts
