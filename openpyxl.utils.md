### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.bound_dictionary.html "openpyxl.utils.bound_dictionary module") |
  * [previous](openpyxl.styles.table.html "openpyxl.styles.table module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package]()



# openpyxl.utils package

## Submodules

  * [openpyxl.utils.bound_dictionary module](openpyxl.utils.bound_dictionary.html)
    * [`BoundDictionary`](openpyxl.utils.bound_dictionary.html#openpyxl.utils.bound_dictionary.BoundDictionary)
  * [openpyxl.utils.cell module](openpyxl.utils.cell.html)
    * [`absolute_coordinate()`](openpyxl.utils.cell.html#openpyxl.utils.cell.absolute_coordinate)
    * [`cols_from_range()`](openpyxl.utils.cell.html#openpyxl.utils.cell.cols_from_range)
    * [`column_index_from_string()`](openpyxl.utils.cell.html#openpyxl.utils.cell.column_index_from_string)
    * [`coordinate_from_string()`](openpyxl.utils.cell.html#openpyxl.utils.cell.coordinate_from_string)
    * [`coordinate_to_tuple()`](openpyxl.utils.cell.html#openpyxl.utils.cell.coordinate_to_tuple)
    * [`get_column_interval()`](openpyxl.utils.cell.html#openpyxl.utils.cell.get_column_interval)
    * [`get_column_letter()`](openpyxl.utils.cell.html#openpyxl.utils.cell.get_column_letter)
    * [`quote_sheetname()`](openpyxl.utils.cell.html#openpyxl.utils.cell.quote_sheetname)
    * [`range_boundaries()`](openpyxl.utils.cell.html#openpyxl.utils.cell.range_boundaries)
    * [`range_to_tuple()`](openpyxl.utils.cell.html#openpyxl.utils.cell.range_to_tuple)
    * [`rows_from_range()`](openpyxl.utils.cell.html#openpyxl.utils.cell.rows_from_range)
  * [openpyxl.utils.dataframe module](openpyxl.utils.dataframe.html)
    * [`dataframe_to_rows()`](openpyxl.utils.dataframe.html#openpyxl.utils.dataframe.dataframe_to_rows)
    * [`expand_index()`](openpyxl.utils.dataframe.html#openpyxl.utils.dataframe.expand_index)
  * [openpyxl.utils.datetime module](openpyxl.utils.datetime.html)
    * [`days_to_time()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.days_to_time)
    * [`from_ISO8601()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.from_ISO8601)
    * [`from_excel()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.from_excel)
    * [`time_to_days()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.time_to_days)
    * [`timedelta_to_days()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.timedelta_to_days)
    * [`to_ISO8601()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.to_ISO8601)
    * [`to_excel()`](openpyxl.utils.datetime.html#openpyxl.utils.datetime.to_excel)
  * [openpyxl.utils.escape module](openpyxl.utils.escape.html)
    * [`escape()`](openpyxl.utils.escape.html#openpyxl.utils.escape.escape)
    * [`unescape()`](openpyxl.utils.escape.html#openpyxl.utils.escape.unescape)
  * [openpyxl.utils.exceptions module](openpyxl.utils.exceptions.html)
    * [`CellCoordinatesException`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.CellCoordinatesException)
    * [`IllegalCharacterError`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.IllegalCharacterError)
    * [`InvalidFileException`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.InvalidFileException)
    * [`NamedRangeException`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.NamedRangeException)
    * [`ReadOnlyWorkbookException`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.ReadOnlyWorkbookException)
    * [`SheetTitleException`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.SheetTitleException)
    * [`WorkbookAlreadySaved`](openpyxl.utils.exceptions.html#openpyxl.utils.exceptions.WorkbookAlreadySaved)
  * [openpyxl.utils.indexed_list module](openpyxl.utils.indexed_list.html)
    * [`IndexedList`](openpyxl.utils.indexed_list.html#openpyxl.utils.indexed_list.IndexedList)
      * [`IndexedList.add()`](openpyxl.utils.indexed_list.html#openpyxl.utils.indexed_list.IndexedList.add)
      * [`IndexedList.append()`](openpyxl.utils.indexed_list.html#openpyxl.utils.indexed_list.IndexedList.append)
      * [`IndexedList.index()`](openpyxl.utils.indexed_list.html#openpyxl.utils.indexed_list.IndexedList.index)
  * [openpyxl.utils.inference module](openpyxl.utils.inference.html)
    * [`cast_numeric()`](openpyxl.utils.inference.html#openpyxl.utils.inference.cast_numeric)
    * [`cast_percentage()`](openpyxl.utils.inference.html#openpyxl.utils.inference.cast_percentage)
    * [`cast_time()`](openpyxl.utils.inference.html#openpyxl.utils.inference.cast_time)
  * [openpyxl.utils.protection module](openpyxl.utils.protection.html)
    * [`hash_password()`](openpyxl.utils.protection.html#openpyxl.utils.protection.hash_password)
  * [openpyxl.utils.units module](openpyxl.utils.units.html)
    * [`DEFAULT_HEADER`](openpyxl.utils.units.html#openpyxl.utils.units.DEFAULT_HEADER)
    * [`EMU_to_cm()`](openpyxl.utils.units.html#openpyxl.utils.units.EMU_to_cm)
    * [`EMU_to_inch()`](openpyxl.utils.units.html#openpyxl.utils.units.EMU_to_inch)
    * [`EMU_to_pixels()`](openpyxl.utils.units.html#openpyxl.utils.units.EMU_to_pixels)
    * [`angle_to_degrees()`](openpyxl.utils.units.html#openpyxl.utils.units.angle_to_degrees)
    * [`cm_to_EMU()`](openpyxl.utils.units.html#openpyxl.utils.units.cm_to_EMU)
    * [`cm_to_dxa()`](openpyxl.utils.units.html#openpyxl.utils.units.cm_to_dxa)
    * [`degrees_to_angle()`](openpyxl.utils.units.html#openpyxl.utils.units.degrees_to_angle)
    * [`dxa_to_cm()`](openpyxl.utils.units.html#openpyxl.utils.units.dxa_to_cm)
    * [`dxa_to_inch()`](openpyxl.utils.units.html#openpyxl.utils.units.dxa_to_inch)
    * [`inch_to_EMU()`](openpyxl.utils.units.html#openpyxl.utils.units.inch_to_EMU)
    * [`inch_to_dxa()`](openpyxl.utils.units.html#openpyxl.utils.units.inch_to_dxa)
    * [`pixels_to_EMU()`](openpyxl.utils.units.html#openpyxl.utils.units.pixels_to_EMU)
    * [`pixels_to_points()`](openpyxl.utils.units.html#openpyxl.utils.units.pixels_to_points)
    * [`points_to_pixels()`](openpyxl.utils.units.html#openpyxl.utils.units.points_to_pixels)
    * [`short_color()`](openpyxl.utils.units.html#openpyxl.utils.units.short_color)



[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils package
    * Submodules



#### Previous topic

[openpyxl.styles.table module](openpyxl.styles.table.html "previous chapter")

#### Next topic

[openpyxl.utils.bound_dictionary module](openpyxl.utils.bound_dictionary.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.utils.bound_dictionary.html "openpyxl.utils.bound_dictionary module") |
  * [previous](openpyxl.styles.table.html "openpyxl.styles.table module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
