### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.picture.html "openpyxl.worksheet.picture module") |
  * [previous](openpyxl.worksheet.page.html "openpyxl.worksheet.page module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.pagebreak module]()



# openpyxl.worksheet.pagebreak module

_class _openpyxl.worksheet.pagebreak.Break(_id =0_, _min =0_, _max =16383_, _man =True_, _pt =None_)[[source]](../_modules/openpyxl/worksheet/pagebreak.html#Break)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

id
    

Values must be of type <class ‘int’>

man
    

Values must be of type <class ‘bool’>

max
    

Values must be of type <class ‘int’>

min
    

Values must be of type <class ‘int’>

pt
    

Values must be of type <class ‘bool’>

tagname _ = 'brk'_
    

_class _openpyxl.worksheet.pagebreak.ColBreak(_count =None_, _manualBreakCount =None_, _brk =()_)[[source]](../_modules/openpyxl/worksheet/pagebreak.html#ColBreak)
    

Bases: `RowBreak`

brk
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

_property _manualBreakCount
    

tagname _ = 'colBreaks'_
    

openpyxl.worksheet.pagebreak.PageBreak
    

alias of `RowBreak`

_class _openpyxl.worksheet.pagebreak.RowBreak(_count =None_, _manualBreakCount =None_, _brk =()_)[[source]](../_modules/openpyxl/worksheet/pagebreak.html#RowBreak)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

append(_brk =None_)[[source]](../_modules/openpyxl/worksheet/pagebreak.html#RowBreak.append)
    

Add a page break

brk
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

_property _manualBreakCount
    

tagname _ = 'rowBreaks'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.pagebreak module
    * `Break`
      * `Break.id`
      * `Break.man`
      * `Break.max`
      * `Break.min`
      * `Break.pt`
      * `Break.tagname`
    * `ColBreak`
      * `ColBreak.brk`
      * `ColBreak.count`
      * `ColBreak.manualBreakCount`
      * `ColBreak.tagname`
    * `PageBreak`
    * `RowBreak`
      * `RowBreak.append()`
      * `RowBreak.brk`
      * `RowBreak.count`
      * `RowBreak.manualBreakCount`
      * `RowBreak.tagname`



#### Previous topic

[openpyxl.worksheet.page module](openpyxl.worksheet.page.html "previous chapter")

#### Next topic

[openpyxl.worksheet.picture module](openpyxl.worksheet.picture.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.pagebreak.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.picture.html "openpyxl.worksheet.picture module") |
  * [previous](openpyxl.worksheet.page.html "openpyxl.worksheet.page module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.pagebreak module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
