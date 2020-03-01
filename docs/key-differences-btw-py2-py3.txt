# Key differences in Python 2 and Python 3 while migrating this project.

## Intra package import notation

- Identifying package remains the same here but, notation is different.
```python
# Python 2
from adstxtparser.parsers import adstxtcrawler

# Python 3
from .adstxtparser.parsers import adstxtcrawler
```
## Return response of request in scrapy is a class object in Python 3

- The request method in scrapy in Python 3 returns a class object which has string in binary.
- To operate on them we can use decode() method to convert them into a <class str> object.
```python
# Python 2
line.lower()

# Python 3
# Decode before using
line = line.decode()
line.lower()
```
