### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.formula.html "openpyxl.worksheet.formula module") |
  * [previous](openpyxl.worksheet.errors.html "openpyxl.worksheet.errors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.filters module]()



# openpyxl.worksheet.filters module

_class _openpyxl.worksheet.filters.AutoFilter(_ref =None_, _filterColumn =()_, _sortState =None_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#AutoFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

add_filter_column(_col_id_ , _vals_ , _blank =False_)[[source]](../_modules/openpyxl/worksheet/filters.html#AutoFilter.add_filter_column)
    

Add row filter for specified column.

Parameters:
    

  * **col_id** (_int_) – Zero-origin column id. 0 means first column.

  * **vals** (_str_ _[__]_) – Value list to show.

  * **blank** (_bool_) – Show rows that have blank cell if True (default=``False``)




add_sort_condition(_ref_ , _descending =False_)[[source]](../_modules/openpyxl/worksheet/filters.html#AutoFilter.add_sort_condition)
    

Add sort condition for cpecified range of cells.

Parameters:
    

  * **ref** (_string_ _,__is the same as that_ _of_ _the filter_) – range of the cells (e.g. ‘A2:A150’)

  * **descending** (_bool_) – Descending sort order (default=``False``)




extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

filterColumn
    

A sequence (list or tuple) that may only contain objects of the declared type

ref
    

sortState
    

Values must be of type <class ‘openpyxl.worksheet.filters.SortState’>

tagname _ = 'autoFilter'_
    

_class _openpyxl.worksheet.filters.BlankFilter(_** kw_)[[source]](../_modules/openpyxl/worksheet/filters.html#BlankFilter)
    

Bases: `CustomFilter`

Exclude blanks

_property _operator
    

Value must be one of {‘lessThanOrEqual’, ‘lessThan’, ‘equal’, ‘greaterThanOrEqual’, ‘notEqual’, ‘greaterThan’}

_property _val
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.filters.ColorFilter(_dxfId =None_, _cellColor =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#ColorFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cellColor
    

Values must be of type <class ‘bool’>

dxfId
    

Values must be of type <class ‘int’>

tagname _ = 'colorFilter'_
    

_class _openpyxl.worksheet.filters.CustomFilter(_operator ='equal'_, _val =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#CustomFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

convert()[[source]](../_modules/openpyxl/worksheet/filters.html#CustomFilter.convert)
    

Convert to more specific filter

operator
    

Value must be one of {‘lessThanOrEqual’, ‘lessThan’, ‘equal’, ‘greaterThanOrEqual’, ‘notEqual’, ‘greaterThan’}

tagname _ = 'customFilter'_
    

val
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.filters.CustomFilters(__and =None_, _customFilter =()_)[[source]](../_modules/openpyxl/worksheet/filters.html#CustomFilters)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

customFilter
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'customFilters'_
    

_class _openpyxl.worksheet.filters.DateGroupItem(_year =None_, _month =None_, _day =None_, _hour =None_, _minute =None_, _second =None_, _dateTimeGrouping =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#DateGroupItem)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

dateTimeGrouping
    

Value must be one of {‘second’, ‘day’, ‘hour’, ‘month’, ‘minute’, ‘year’}

day
    

Values must be of type <class ‘float’>

hour
    

Values must be of type <class ‘float’>

minute
    

Values must be of type <class ‘float’>

month
    

Values must be of type <class ‘float’>

second
    

Values must be of type <class ‘int’>

tagname _ = 'dateGroupItem'_
    

year
    

Values must be of type <class ‘int’>

_class _openpyxl.worksheet.filters.DynamicFilter(_type =None_, _val =None_, _valIso =None_, _maxVal =None_, _maxValIso =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#DynamicFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

maxVal
    

Values must be of type <class ‘float’>

maxValIso
    

Values must be of type <class ‘datetime.datetime’>

tagname _ = 'dynamicFilter'_
    

type
    

Value must be one of {‘tomorrow’, ‘M4’, ‘M3’, ‘M11’, ‘Q4’, ‘today’, ‘yesterday’, ‘Q2’, ‘M1’, ‘lastMonth’, ‘M6’, ‘M5’, ‘lastWeek’, ‘lastYear’, ‘M12’, ‘nextWeek’, ‘thisQuarter’, ‘Q1’, ‘M7’, ‘nextQuarter’, ‘thisYear’, ‘M10’, ‘M9’, ‘belowAverage’, ‘Q3’, ‘aboveAverage’, ‘nextMonth’, ‘M2’, ‘thisMonth’, ‘yearToDate’, ‘thisWeek’, ‘nextYear’, ‘null’, ‘M8’, ‘lastQuarter’}

val
    

Values must be of type <class ‘float’>

valIso
    

Values must be of type <class ‘datetime.datetime’>

_class _openpyxl.worksheet.filters.FilterColumn(_colId =None_, _hiddenButton =False_, _showButton =True_, _filters =None_, _top10 =None_, _customFilters =None_, _dynamicFilter =None_, _colorFilter =None_, _iconFilter =None_, _extLst =None_, _blank =None_, _vals =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#FilterColumn)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

colId
    

Values must be of type <class ‘int’>

col_id
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

colorFilter
    

Values must be of type <class ‘openpyxl.worksheet.filters.ColorFilter’>

customFilters
    

Values must be of type <class ‘openpyxl.worksheet.filters.CustomFilters’>

dynamicFilter
    

Values must be of type <class ‘openpyxl.worksheet.filters.DynamicFilter’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

filters
    

Values must be of type <class ‘openpyxl.worksheet.filters.Filters’>

hiddenButton
    

Values must be of type <class ‘bool’>

iconFilter
    

Values must be of type <class ‘openpyxl.worksheet.filters.IconFilter’>

showButton
    

Values must be of type <class ‘bool’>

tagname _ = 'filterColumn'_
    

top10
    

Values must be of type <class ‘openpyxl.worksheet.filters.Top10’>

_class _openpyxl.worksheet.filters.Filters(_blank =None_, _calendarType =None_, _filter =()_, _dateGroupItem =()_)[[source]](../_modules/openpyxl/worksheet/filters.html#Filters)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

blank
    

Values must be of type <class ‘bool’>

calendarType
    

Value must be one of {‘korea’, ‘saka’, ‘hebrew’, ‘japan’, ‘thai’, ‘gregorianArabic’, ‘gregorianUs’, ‘taiwan’, ‘gregorian’, ‘hijri’, ‘gregorianXlitFrench’, ‘gregorianXlitEnglish’, ‘gregorianMeFrench’}

dateGroupItem
    

A sequence (list or tuple) that may only contain objects of the declared type

filter
    

A sequence of primitive types that are stored as a single attribute. “val” is the default attribute

tagname _ = 'filters'_
    

_class _openpyxl.worksheet.filters.IconFilter(_iconSet =None_, _iconId =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#IconFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

iconId
    

Values must be of type <class ‘int’>

iconSet
    

Value must be one of {‘3Symbols’, ‘5Arrows’, ‘3Arrows’, ‘3Flags’, ‘3TrafficLights1’, ‘3Signs’, ‘3Symbols2’, ‘4ArrowsGray’, ‘4RedToBlack’, ‘4TrafficLights’, ‘5ArrowsGray’, ‘5Rating’, ‘3TrafficLights2’, ‘4Arrows’, ‘4Rating’, ‘5Quarters’, ‘3ArrowsGray’}

tagname _ = 'iconFilter'_
    

_class _openpyxl.worksheet.filters.NumberFilter(_operator ='equal'_, _val =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#NumberFilter)
    

Bases: `CustomFilter`

operator
    

Value must be one of {‘lessThanOrEqual’, ‘lessThan’, ‘equal’, ‘greaterThanOrEqual’, ‘notEqual’, ‘greaterThan’}

val
    

Values must be of type <class ‘float’>

_class _openpyxl.worksheet.filters.SortCondition(_ref =None_, _descending =None_, _sortBy =None_, _customList =None_, _dxfId =None_, _iconSet =None_, _iconId =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#SortCondition)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

customList
    

Values must be of type <class ‘str’>

descending
    

Values must be of type <class ‘bool’>

dxfId
    

Values must be of type <class ‘int’>

iconId
    

Values must be of type <class ‘int’>

iconSet
    

Value must be one of {‘3Symbols’, ‘5Arrows’, ‘3Arrows’, ‘3Flags’, ‘3TrafficLights1’, ‘3Signs’, ‘3Symbols2’, ‘4ArrowsGray’, ‘4RedToBlack’, ‘4TrafficLights’, ‘5ArrowsGray’, ‘5Rating’, ‘3TrafficLights2’, ‘4Arrows’, ‘4Rating’, ‘5Quarters’, ‘3ArrowsGray’}

ref
    

sortBy
    

Value must be one of {‘fontColor’, ‘value’, ‘cellColor’, ‘icon’}

tagname _ = 'sortCondition'_
    

_class _openpyxl.worksheet.filters.SortState(_columnSort =None_, _caseSensitive =None_, _sortMethod =None_, _ref =None_, _sortCondition =()_, _extLst =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#SortState)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caseSensitive
    

Values must be of type <class ‘bool’>

columnSort
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

ref
    

sortCondition
    

A sequence (list or tuple) that may only contain objects of the declared type

sortMethod
    

Value must be one of {‘pinYin’, ‘stroke’}

tagname _ = 'sortState'_
    

_class _openpyxl.worksheet.filters.StringFilter(_operator ='contains'_, _val =None_, _exclude =False_)[[source]](../_modules/openpyxl/worksheet/filters.html#StringFilter)
    

Bases: `CustomFilter`

exclude
    

Values must be of type <class ‘bool’>

operator
    

Value must be one of {‘wildcard’, ‘endswith’, ‘contains’, ‘startswith’}

to_tree(_tagname =None_, _idx =None_, _namespace =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#StringFilter.to_tree)
    

val
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.filters.Top10(_top =None_, _percent =None_, _val =None_, _filterVal =None_)[[source]](../_modules/openpyxl/worksheet/filters.html#Top10)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

filterVal
    

Values must be of type <class ‘float’>

percent
    

Values must be of type <class ‘bool’>

tagname _ = 'top10'_
    

top
    

Values must be of type <class ‘bool’>

val
    

Values must be of type <class ‘float’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.filters module
    * `AutoFilter`
      * `AutoFilter.add_filter_column()`
      * `AutoFilter.add_sort_condition()`
      * `AutoFilter.extLst`
      * `AutoFilter.filterColumn`
      * `AutoFilter.ref`
      * `AutoFilter.sortState`
      * `AutoFilter.tagname`
    * `BlankFilter`
      * `BlankFilter.operator`
      * `BlankFilter.val`
    * `ColorFilter`
      * `ColorFilter.cellColor`
      * `ColorFilter.dxfId`
      * `ColorFilter.tagname`
    * `CustomFilter`
      * `CustomFilter.convert()`
      * `CustomFilter.operator`
      * `CustomFilter.tagname`
      * `CustomFilter.val`
    * `CustomFilters`
      * `CustomFilters.customFilter`
      * `CustomFilters.tagname`
    * `DateGroupItem`
      * `DateGroupItem.dateTimeGrouping`
      * `DateGroupItem.day`
      * `DateGroupItem.hour`
      * `DateGroupItem.minute`
      * `DateGroupItem.month`
      * `DateGroupItem.second`
      * `DateGroupItem.tagname`
      * `DateGroupItem.year`
    * `DynamicFilter`
      * `DynamicFilter.maxVal`
      * `DynamicFilter.maxValIso`
      * `DynamicFilter.tagname`
      * `DynamicFilter.type`
      * `DynamicFilter.val`
      * `DynamicFilter.valIso`
    * `FilterColumn`
      * `FilterColumn.colId`
      * `FilterColumn.col_id`
      * `FilterColumn.colorFilter`
      * `FilterColumn.customFilters`
      * `FilterColumn.dynamicFilter`
      * `FilterColumn.extLst`
      * `FilterColumn.filters`
      * `FilterColumn.hiddenButton`
      * `FilterColumn.iconFilter`
      * `FilterColumn.showButton`
      * `FilterColumn.tagname`
      * `FilterColumn.top10`
    * `Filters`
      * `Filters.blank`
      * `Filters.calendarType`
      * `Filters.dateGroupItem`
      * `Filters.filter`
      * `Filters.tagname`
    * `IconFilter`
      * `IconFilter.iconId`
      * `IconFilter.iconSet`
      * `IconFilter.tagname`
    * `NumberFilter`
      * `NumberFilter.operator`
      * `NumberFilter.val`
    * `SortCondition`
      * `SortCondition.customList`
      * `SortCondition.descending`
      * `SortCondition.dxfId`
      * `SortCondition.iconId`
      * `SortCondition.iconSet`
      * `SortCondition.ref`
      * `SortCondition.sortBy`
      * `SortCondition.tagname`
    * `SortState`
      * `SortState.caseSensitive`
      * `SortState.columnSort`
      * `SortState.extLst`
      * `SortState.ref`
      * `SortState.sortCondition`
      * `SortState.sortMethod`
      * `SortState.tagname`
    * `StringFilter`
      * `StringFilter.exclude`
      * `StringFilter.operator`
      * `StringFilter.to_tree()`
      * `StringFilter.val`
    * `Top10`
      * `Top10.filterVal`
      * `Top10.percent`
      * `Top10.tagname`
      * `Top10.top`
      * `Top10.val`



#### Previous topic

[openpyxl.worksheet.errors module](openpyxl.worksheet.errors.html "previous chapter")

#### Next topic

[openpyxl.worksheet.formula module](openpyxl.worksheet.formula.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.filters.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.formula.html "openpyxl.worksheet.formula module") |
  * [previous](openpyxl.worksheet.errors.html "openpyxl.worksheet.errors module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.filters module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
