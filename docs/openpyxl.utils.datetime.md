### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.escape.html "openpyxl.utils.escape module") |
  * [previous](openpyxl.utils.dataframe.html "openpyxl.utils.dataframe module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.datetime module]()



# openpyxl.utils.datetime module

Manage Excel date weirdness.

openpyxl.utils.datetime.days_to_time(_value_)[[source]](../_modules/openpyxl/utils/datetime.html#days_to_time)
    

openpyxl.utils.datetime.from_ISO8601(_formatted_string_)[[source]](../_modules/openpyxl/utils/datetime.html#from_ISO8601)
    

Convert from a timestamp string to a datetime object. According to 18.17.4 in the specification the following ISO 8601 formats are supported.

Dates B.1.1 and B.2.1 Times B.1.2 and B.2.2 Datetimes B.1.3 and B.2.3

There is no concept of timedeltas in the specification, but Excel writes them (in strict OOXML mode), so these are also understood.

openpyxl.utils.datetime.from_excel(_value_ , _epoch =datetime.datetime(1899, 12, 30, 0, 0)_, _timedelta =False_)[[source]](../_modules/openpyxl/utils/datetime.html#from_excel)
    

Convert Excel serial to Python datetime

openpyxl.utils.datetime.time_to_days(_value_)[[source]](../_modules/openpyxl/utils/datetime.html#time_to_days)
    

Convert a time value to fractions of day

openpyxl.utils.datetime.timedelta_to_days(_value_)[[source]](../_modules/openpyxl/utils/datetime.html#timedelta_to_days)
    

Convert a timedelta value to fractions of a day

openpyxl.utils.datetime.to_ISO8601(_dt_)[[source]](../_modules/openpyxl/utils/datetime.html#to_ISO8601)
    

Convert from a datetime to a timestamp string.

openpyxl.utils.datetime.to_excel(_dt_ , _epoch =datetime.datetime(1899, 12, 30, 0, 0)_)[[source]](../_modules/openpyxl/utils/datetime.html#to_excel)
    

Convert Python datetime to Excel serial

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils.datetime module
    * `days_to_time()`
    * `from_ISO8601()`
    * `from_excel()`
    * `time_to_days()`
    * `timedelta_to_days()`
    * `to_ISO8601()`
    * `to_excel()`



#### Previous topic

[openpyxl.utils.dataframe module](openpyxl.utils.dataframe.html "previous chapter")

#### Next topic

[openpyxl.utils.escape module](openpyxl.utils.escape.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.datetime.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.escape.html "openpyxl.utils.escape module") |
  * [previous](openpyxl.utils.dataframe.html "openpyxl.utils.dataframe module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.datetime module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
