### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.ole.html "openpyxl.worksheet.ole module") |
  * [previous](openpyxl.worksheet.hyperlink.html "openpyxl.worksheet.hyperlink module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.merge module]()



# openpyxl.worksheet.merge module

_class _openpyxl.worksheet.merge.MergeCell(_ref =None_)[[source]](../_modules/openpyxl/worksheet/merge.html#MergeCell)
    

Bases: [`CellRange`](openpyxl.worksheet.cell_range.html#openpyxl.worksheet.cell_range.CellRange "openpyxl.worksheet.cell_range.CellRange")

_property _ref
    

Excel-style representation of the range

tagname _ = 'mergeCell'_
    

_class _openpyxl.worksheet.merge.MergeCells(_count =None_, _mergeCell =()_)[[source]](../_modules/openpyxl/worksheet/merge.html#MergeCells)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _count
    

mergeCell
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'mergeCells'_
    

_class _openpyxl.worksheet.merge.MergedCellRange(_worksheet_ , _coord_)[[source]](../_modules/openpyxl/worksheet/merge.html#MergedCellRange)
    

Bases: [`CellRange`](openpyxl.worksheet.cell_range.html#openpyxl.worksheet.cell_range.CellRange "openpyxl.worksheet.cell_range.CellRange")

MergedCellRange stores the border information of a merged cell in the top left cell of the merged cell. The remaining cells in the merged cell are stored as MergedCell objects and get their border information from the upper left cell.

format()[[source]](../_modules/openpyxl/worksheet/merge.html#MergedCellRange.format)
    

Each cell of the merged cell is created as MergedCell if it does not already exist.

The MergedCells at the edge of the merged cell gets its borders from the upper left cell.

>   * The top MergedCells get the top border from the top left cell.
> 
>   * The bottom MergedCells get the bottom border from the top left cell.
> 
>   * The left MergedCells get the left border from the top left cell.
> 
>   * The right MergedCells get the right border from the top left cell.
> 
> 


[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.merge module
    * `MergeCell`
      * `MergeCell.ref`
      * `MergeCell.tagname`
    * `MergeCells`
      * `MergeCells.count`
      * `MergeCells.mergeCell`
      * `MergeCells.tagname`
    * `MergedCellRange`
      * `MergedCellRange.format()`



#### Previous topic

[openpyxl.worksheet.hyperlink module](openpyxl.worksheet.hyperlink.html "previous chapter")

#### Next topic

[openpyxl.worksheet.ole module](openpyxl.worksheet.ole.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.merge.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.ole.html "openpyxl.worksheet.ole module") |
  * [previous](openpyxl.worksheet.hyperlink.html "openpyxl.worksheet.hyperlink module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.merge module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
