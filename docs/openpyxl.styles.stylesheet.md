### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.table.html "openpyxl.styles.table module") |
  * [previous](openpyxl.styles.styleable.html "openpyxl.styles.styleable module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.stylesheet module]()



# openpyxl.styles.stylesheet module

_class _openpyxl.styles.stylesheet.Stylesheet(_numFmts =None_, _fonts =()_, _fills =()_, _borders =()_, _cellStyleXfs =None_, _cellXfs =None_, _cellStyles =None_, _dxfs =()_, _tableStyles =None_, _colors =None_, _extLst =None_)[[source]](../_modules/openpyxl/styles/stylesheet.html#Stylesheet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

borders
    

Wrap a sequence in an containing object

cellStyleXfs
    

Values must be of type <class ‘openpyxl.styles.cell_style.CellStyleList’>

cellStyles
    

Values must be of type <class ‘openpyxl.styles.named_styles._NamedCellStyleList’>

cellXfs
    

Values must be of type <class ‘openpyxl.styles.cell_style.CellStyleList’>

colors
    

Values must be of type <class ‘openpyxl.styles.colors.ColorList’>

_property _custom_formats
    

dxfs
    

Wrap a sequence in an containing object

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fills
    

Wrap a sequence in an containing object

fonts
    

Wrap a sequence in an containing object

_classmethod _from_tree(_node_)[[source]](../_modules/openpyxl/styles/stylesheet.html#Stylesheet.from_tree)
    

Create object from XML

numFmts
    

Values must be of type <class ‘openpyxl.styles.numbers.NumberFormatList’>

tableStyles
    

Values must be of type <class ‘openpyxl.styles.table.TableStyleList’>

tagname _ = 'styleSheet'_
    

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/styles/stylesheet.html#Stylesheet.to_tree)
    

openpyxl.styles.stylesheet.apply_stylesheet(_archive_ , _wb_)[[source]](../_modules/openpyxl/styles/stylesheet.html#apply_stylesheet)
    

Add styles to workbook if present

openpyxl.styles.stylesheet.write_stylesheet(_wb_)[[source]](../_modules/openpyxl/styles/stylesheet.html#write_stylesheet)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.styles.stylesheet module
    * `Stylesheet`
      * `Stylesheet.borders`
      * `Stylesheet.cellStyleXfs`
      * `Stylesheet.cellStyles`
      * `Stylesheet.cellXfs`
      * `Stylesheet.colors`
      * `Stylesheet.custom_formats`
      * `Stylesheet.dxfs`
      * `Stylesheet.extLst`
      * `Stylesheet.fills`
      * `Stylesheet.fonts`
      * `Stylesheet.from_tree()`
      * `Stylesheet.numFmts`
      * `Stylesheet.tableStyles`
      * `Stylesheet.tagname`
      * `Stylesheet.to_tree()`
    * `apply_stylesheet()`
    * `write_stylesheet()`



#### Previous topic

[openpyxl.styles.styleable module](openpyxl.styles.styleable.html "previous chapter")

#### Next topic

[openpyxl.styles.table module](openpyxl.styles.table.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.styles.stylesheet.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.styles.table.html "openpyxl.styles.table module") |
  * [previous](openpyxl.styles.styleable.html "openpyxl.styles.styleable module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.styles package](openpyxl.styles.html) »
  * [openpyxl.styles.stylesheet module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
