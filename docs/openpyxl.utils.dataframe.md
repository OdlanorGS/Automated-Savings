### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.datetime.html "openpyxl.utils.datetime module") |
  * [previous](openpyxl.utils.cell.html "openpyxl.utils.cell module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.dataframe module]()



# openpyxl.utils.dataframe module

openpyxl.utils.dataframe.dataframe_to_rows(_df_ , _index =True_, _header =True_)[[source]](../_modules/openpyxl/utils/dataframe.html#dataframe_to_rows)
    

Convert a Pandas dataframe into something suitable for passing into a worksheet. If index is True then the index will be included, starting one row below the header. If header is True then column headers will be included starting one column to the right. Formatting should be done by client code.

openpyxl.utils.dataframe.expand_index(_index_ , _header =False_)[[source]](../_modules/openpyxl/utils/dataframe.html#expand_index)
    

Expand axis or column Multiindex For columns use header = True For axes use header = False (default)

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils.dataframe module
    * `dataframe_to_rows()`
    * `expand_index()`



#### Previous topic

[openpyxl.utils.cell module](openpyxl.utils.cell.html "previous chapter")

#### Next topic

[openpyxl.utils.datetime module](openpyxl.utils.datetime.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.dataframe.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.datetime.html "openpyxl.utils.datetime module") |
  * [previous](openpyxl.utils.cell.html "openpyxl.utils.cell module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.dataframe module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
