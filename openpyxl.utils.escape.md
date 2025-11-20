### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.exceptions.html "openpyxl.utils.exceptions module") |
  * [previous](openpyxl.utils.datetime.html "openpyxl.utils.datetime module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.escape module]()



# openpyxl.utils.escape module

OOXML has non-standard escaping for characters < 

openpyxl.utils.escape.escape(_value_)[[source]](../_modules/openpyxl/utils/escape.html#escape)
    

Convert ASCII < 31 to OOXML: n == _x + hex(ord(n)) + _

openpyxl.utils.escape.unescape(_value_)[[source]](../_modules/openpyxl/utils/escape.html#unescape)
    

Convert escaped strings to ASCIII: _x000a_ == n

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils.escape module
    * `escape()`
    * `unescape()`



#### Previous topic

[openpyxl.utils.datetime module](openpyxl.utils.datetime.html "previous chapter")

#### Next topic

[openpyxl.utils.exceptions module](openpyxl.utils.exceptions.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.escape.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.exceptions.html "openpyxl.utils.exceptions module") |
  * [previous](openpyxl.utils.datetime.html "openpyxl.utils.datetime module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.escape module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
