### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.cell_watch.html "openpyxl.worksheet.cell_watch module") |
  * [previous](openpyxl.worksheet.html "openpyxl.worksheet package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.cell_range module]()



# openpyxl.worksheet.cell_range module

_class _openpyxl.worksheet.cell_range.CellRange(_range_string =None_, _min_col =None_, _min_row =None_, _max_col =None_, _max_row =None_, _title =None_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Represents a range in a sheet: title and coordinates.

This object is used to perform operations on ranges, like:

  * shift, expand or shrink

  * union/intersection with another sheet range,




We can check whether a range is:

  * equal or not equal to another,

  * disjoint of another,

  * contained in another.




We can get:

  * the size of a range.

  * the range bounds (vertices)

  * the coordinates,

  * the string representation,




_property _bottom
    

A list of cell coordinates that comprise the bottom of the range

_property _bounds
    

Vertices of the range as a tuple

_property _cells
    

_property _cols
    

Return cell coordinates as columns

_property _coord
    

Excel-style representation of the range

expand(_right =0_, _down =0_, _left =0_, _up =0_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.expand)
    

Expand the range by the dimensions provided.

Parameters:
    

  * **right** (_int_) – expand range to the right by this number of cells

  * **down** (_int_) – expand range down by this number of cells

  * **left** (_int_) – expand range to the left by this number of cells

  * **up** (_int_) – expand range up by this number of cells




intersection(_other_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.intersection)
    

Return a new range with cells common to this range and _other_

Parameters:
    

**other** (_openpyxl.worksheet.cell_range.CellRange_) – Other sheet range.

Returns:
    

the intersecting sheet range.

Raise:
    

`ValueError` if the _other_ range doesn’t intersect with this range.

isdisjoint(_other_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.isdisjoint)
    

Return `True` if this range has no cell in common with _other_. Ranges are disjoint if and only if their intersection is the empty range.

Parameters:
    

**other** (_openpyxl.worksheet.cell_range.CellRange_) – Other sheet range.

Returns:
    

`True` if the range has no cells in common with other.

issubset(_other_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.issubset)
    

Test whether every cell in this range is also in _other_.

Parameters:
    

**other** (_openpyxl.worksheet.cell_range.CellRange_) – Other sheet range

Returns:
    

`True` if _range_ <= _other_.

issuperset(_other_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.issuperset)
    

Test whether every cell in _other_ is in this range.

Parameters:
    

**other** (_openpyxl.worksheet.cell_range.CellRange_) – Other sheet range

Returns:
    

`True` if _range_ >= _other_ (or _other_ in _range_).

_property _left
    

A list of cell coordinates that comprise the left-side of the range

max_col
    

Values must be of type <class ‘int’>

max_row
    

Values must be of type <class ‘int’>

min_col
    

Values must be of type <class ‘int’>

min_row
    

Values must be of type <class ‘int’>

_property _right
    

A list of cell coordinates that comprise the right-side of the range

_property _rows
    

Return cell coordinates as rows

shift(_col_shift =0_, _row_shift =0_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.shift)
    

Shift the focus of the range according to the shift values (_col_shift_ , _row_shift_).

Parameters:
    

  * **col_shift** (_int_) – number of columns to be moved by, can be negative

  * **row_shift** (_int_) – number of rows to be moved by, can be negative



Raise:
    

`ValueError` if any row or column index < 1

shrink(_right =0_, _bottom =0_, _left =0_, _top =0_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.shrink)
    

Shrink the range by the dimensions provided.

Parameters:
    

  * **right** (_int_) – shrink range from the right by this number of cells

  * **down** (_int_) – shrink range from the top by this number of cells

  * **left** (_int_) – shrink range from the left by this number of cells

  * **up** (_int_) – shrink range from the bottom by this number of cells




_property _size
    

Return the size of the range as a dictionary of rows and columns.

_property _top
    

A list of cell coordinates that comprise the top of the range

union(_other_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#CellRange.union)
    

Return the minimal superset of this range and _other_. This new range will contain all cells from this range, _other_ , and any additional cells required to form a rectangular `CellRange`.

Parameters:
    

**other** (_openpyxl.worksheet.cell_range.CellRange_) – Other sheet range.

Returns:
    

a `CellRange` that is a superset of this and _other_.

_class _openpyxl.worksheet.cell_range.MultiCellRange(_ranges ={}_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#MultiCellRange)
    

Bases: [`Strict`](openpyxl.descriptors.html#openpyxl.descriptors.Strict "openpyxl.descriptors.Strict")

add(_coord_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#MultiCellRange.add)
    

Add a cell coordinate or CellRange

ranges
    

Use a set to keep values unique

remove(_coord_)[[source]](../_modules/openpyxl/worksheet/cell_range.html#MultiCellRange.remove)
    

sorted()[[source]](../_modules/openpyxl/worksheet/cell_range.html#MultiCellRange.sorted)
    

Return a sorted list of items

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.cell_range module
    * `CellRange`
      * `CellRange.bottom`
      * `CellRange.bounds`
      * `CellRange.cells`
      * `CellRange.cols`
      * `CellRange.coord`
      * `CellRange.expand()`
      * `CellRange.intersection()`
      * `CellRange.isdisjoint()`
      * `CellRange.issubset()`
      * `CellRange.issuperset()`
      * `CellRange.left`
      * `CellRange.max_col`
      * `CellRange.max_row`
      * `CellRange.min_col`
      * `CellRange.min_row`
      * `CellRange.right`
      * `CellRange.rows`
      * `CellRange.shift()`
      * `CellRange.shrink()`
      * `CellRange.size`
      * `CellRange.top`
      * `CellRange.union()`
    * `MultiCellRange`
      * `MultiCellRange.add()`
      * `MultiCellRange.ranges`
      * `MultiCellRange.remove()`
      * `MultiCellRange.sorted()`



#### Previous topic

[openpyxl.worksheet package](openpyxl.worksheet.html "previous chapter")

#### Next topic

[openpyxl.worksheet.cell_watch module](openpyxl.worksheet.cell_watch.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.cell_range.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.cell_watch.html "openpyxl.worksheet.cell_watch module") |
  * [previous](openpyxl.worksheet.html "openpyxl.worksheet package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.cell_range module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
