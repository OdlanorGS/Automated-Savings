### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.cell.text.html "openpyxl.cell.text module") |
  * [previous](openpyxl.cell.read_only.html "openpyxl.cell.read_only module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.rich_text module]()



# openpyxl.cell.rich_text module

RichText definition

_class _openpyxl.cell.rich_text.CellRichText(_* args_)[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText)
    

Bases: `list`

Represents a rich text string.

Initialize with a list made of pure strings or `TextBlock` elements Can index object to access or modify individual rich text elements it also supports the + and += operators between rich text strings There are no user methods for this class

operations which modify the string will generally call an optimization pass afterwards, that merges text blocks with identical formats, consecutive pure text strings, and remove empty strings and empty text blocks

append(_arg_)[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText.append)
    

Append object to the end of the list.

as_list()[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText.as_list)
    

Returns a list of the strings contained. The main reason for this is to make editing easier.

extend(_arg_)[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText.extend)
    

Extend list by appending elements from the iterable.

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText.from_tree)
    

to_tree()[[source]](../_modules/openpyxl/cell/rich_text.html#CellRichText.to_tree)
    

Return the full XML representation

_class _openpyxl.cell.rich_text.TextBlock(_font_ , _text_)[[source]](../_modules/openpyxl/cell/rich_text.html#TextBlock)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

Represents text string in a specific format

This class is used as part of constructing a rich text strings.

font
    

Values must be of type <class ‘openpyxl.cell.text.InlineFont’>

text
    

Values must be of type <class ‘str’>

to_tree()[[source]](../_modules/openpyxl/cell/rich_text.html#TextBlock.to_tree)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.cell.rich_text module
    * `CellRichText`
      * `CellRichText.append()`
      * `CellRichText.as_list()`
      * `CellRichText.extend()`
      * `CellRichText.from_tree()`
      * `CellRichText.to_tree()`
    * `TextBlock`
      * `TextBlock.font`
      * `TextBlock.text`
      * `TextBlock.to_tree()`



#### Previous topic

[openpyxl.cell.read_only module](openpyxl.cell.read_only.html "previous chapter")

#### Next topic

[openpyxl.cell.text module](openpyxl.cell.text.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.cell.rich_text.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.cell.text.html "openpyxl.cell.text module") |
  * [previous](openpyxl.cell.read_only.html "openpyxl.cell.read_only module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.cell package](openpyxl.cell.html) »
  * [openpyxl.cell.rich_text module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
