I am so grateful, first of all, to Allah, that I encountered a slugify problem with crillic letters and Django admin was saying 
'Enter a valid slug that contains letters, numbers and etc'  although I included allow_unicode=True in slugify function. So then this 
github repository gave me the best solution so far, which is using django-uuslug, it handles both unicoding and uniqueness together.
So it is a great idea to use django-uuslug even the letters are in Chinese.  Link to the educational source I am grateful for: https://github.com/un33k/django-uuslug
