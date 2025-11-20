### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.hyperlink.html "openpyxl.worksheet.hyperlink module") |
  * [previous](openpyxl.worksheet.formula.html "openpyxl.worksheet.formula module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.header_footer module]()



# openpyxl.worksheet.header_footer module

_class _openpyxl.worksheet.header_footer.HeaderFooter(_differentOddEven =None_, _differentFirst =None_, _scaleWithDoc =None_, _alignWithMargins =None_, _oddHeader =None_, _oddFooter =None_, _evenHeader =None_, _evenFooter =None_, _firstHeader =None_, _firstFooter =None_)[[source]](../_modules/openpyxl/worksheet/header_footer.html#HeaderFooter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alignWithMargins
    

Values must be of type <class ‘bool’>

differentFirst
    

Values must be of type <class ‘bool’>

differentOddEven
    

Values must be of type <class ‘bool’>

evenFooter
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

evenHeader
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

firstFooter
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

firstHeader
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

oddFooter
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

oddHeader
    

Values must be of type <class ‘openpyxl.worksheet.header_footer.HeaderFooterItem’>

scaleWithDoc
    

Values must be of type <class ‘bool’>

tagname _ = 'headerFooter'_
    

_class _openpyxl.worksheet.header_footer.HeaderFooterItem(_left =None_, _right =None_, _center =None_)[[source]](../_modules/openpyxl/worksheet/header_footer.html#HeaderFooterItem)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

Header or footer item

center
    

Values must be of type <class ‘openpyxl.worksheet.header_footer._HeaderFooterPart’>

centre
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/worksheet/header_footer.html#HeaderFooterItem.from_tree)
    

left
    

Values must be of type <class ‘openpyxl.worksheet.header_footer._HeaderFooterPart’>

right
    

Values must be of type <class ‘openpyxl.worksheet.header_footer._HeaderFooterPart’>

to_tree(_tagname_)[[source]](../_modules/openpyxl/worksheet/header_footer.html#HeaderFooterItem.to_tree)
    

Return as XML node

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.header_footer module
    * `HeaderFooter`
      * `HeaderFooter.alignWithMargins`
      * `HeaderFooter.differentFirst`
      * `HeaderFooter.differentOddEven`
      * `HeaderFooter.evenFooter`
      * `HeaderFooter.evenHeader`
      * `HeaderFooter.firstFooter`
      * `HeaderFooter.firstHeader`
      * `HeaderFooter.oddFooter`
      * `HeaderFooter.oddHeader`
      * `HeaderFooter.scaleWithDoc`
      * `HeaderFooter.tagname`
    * `HeaderFooterItem`
      * `HeaderFooterItem.center`
      * `HeaderFooterItem.centre`
      * `HeaderFooterItem.from_tree()`
      * `HeaderFooterItem.left`
      * `HeaderFooterItem.right`
      * `HeaderFooterItem.to_tree()`



#### Previous topic

[openpyxl.worksheet.formula module](openpyxl.worksheet.formula.html "previous chapter")

#### Next topic

[openpyxl.worksheet.hyperlink module](openpyxl.worksheet.hyperlink.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.header_footer.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.hyperlink.html "openpyxl.worksheet.hyperlink module") |
  * [previous](openpyxl.worksheet.formula.html "openpyxl.worksheet.formula module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.header_footer module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
