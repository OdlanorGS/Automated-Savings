### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.reader.html "openpyxl.reader package") |
  * [previous](openpyxl.pivot.record.html "openpyxl.pivot.record module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.table module]()



# openpyxl.pivot.table module

_class _openpyxl.pivot.table.AutoSortScope(_pivotArea =None_)[[source]](../_modules/openpyxl/pivot/table.html#AutoSortScope)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

pivotArea
    

Values must be of type <class ‘openpyxl.pivot.table.PivotArea’>

_class _openpyxl.pivot.table.ChartFormat(_chart =None_, _format =None_, _series =None_, _pivotArea =None_)[[source]](../_modules/openpyxl/pivot/table.html#ChartFormat)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chart
    

Values must be of type <class ‘int’>

format
    

Values must be of type <class ‘int’>

pivotArea
    

Values must be of type <class ‘openpyxl.pivot.table.PivotArea’>

series
    

Values must be of type <class ‘bool’>

tagname _ = 'chartFormat'_
    

_class _openpyxl.pivot.table.ColHierarchiesUsage(_count =None_, _colHierarchyUsage =()_)[[source]](../_modules/openpyxl/pivot/table.html#ColHierarchiesUsage)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

colHierarchyUsage
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

tagname _ = 'colHierarchiesUsage'_
    

_class _openpyxl.pivot.table.ConditionalFormat(_scope ='selection'_, _type =None_, _priority =None_, _pivotAreas =()_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#ConditionalFormat)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

pivotAreas
    

Wrap a sequence in an containing object

priority
    

Values must be of type <class ‘int’>

scope
    

Value must be one of {‘data’, ‘selection’, ‘field’}

tagname _ = 'conditionalFormat'_
    

type
    

Value must be one of {‘all’, ‘row’, ‘column’}

_class _openpyxl.pivot.table.ConditionalFormatList(_conditionalFormat =()_, _count =None_)[[source]](../_modules/openpyxl/pivot/table.html#ConditionalFormatList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

by_priority()[[source]](../_modules/openpyxl/pivot/table.html#ConditionalFormatList.by_priority)
    

Return a dictionary of format objects keyed by (field id and format property). This can be used to map the formats to field but also to dedupe to match worksheet definitions which are grouped by cell range

conditionalFormat
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

tagname _ = 'conditionalFormats'_
    

to_tree(_tagname =None_)[[source]](../_modules/openpyxl/pivot/table.html#ConditionalFormatList.to_tree)
    

_class _openpyxl.pivot.table.DataField(_name =None_, _fld =None_, _subtotal ='sum'_, _showDataAs ='normal'_, _baseField =-1_, _baseItem =1048832_, _numFmtId =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#DataField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

baseField
    

Values must be of type <class ‘int’>

baseItem
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fld
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

numFmtId
    

Values must be of type <class ‘int’>

showDataAs
    

Value must be one of {‘runTotal’, ‘index’, ‘percentOfRow’, ‘percentOfCol’, ‘percentOfTotal’, ‘percent’, ‘difference’, ‘normal’, ‘percentDiff’}

subtotal
    

Value must be one of {‘count’, ‘countNums’, ‘min’, ‘var’, ‘varp’, ‘average’, ‘max’, ‘sum’, ‘product’, ‘stdDevp’, ‘stdDev’}

tagname _ = 'dataField'_
    

_class _openpyxl.pivot.table.FieldItem(_n =None_, _t ='data'_, _h =None_, _s =None_, _sd =True_, _f =None_, _m =None_, _c =None_, _x =None_, _d =None_, _e =None_)[[source]](../_modules/openpyxl/pivot/table.html#FieldItem)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

c
    

Values must be of type <class ‘bool’>

d
    

Values must be of type <class ‘bool’>

e
    

Values must be of type <class ‘bool’>

f
    

Values must be of type <class ‘bool’>

h
    

Values must be of type <class ‘bool’>

m
    

Values must be of type <class ‘bool’>

n
    

Values must be of type <class ‘str’>

s
    

Values must be of type <class ‘bool’>

sd
    

Values must be of type <class ‘bool’>

t
    

Value must be one of {‘data’, ‘min’, ‘count’, ‘var’, ‘blank’, ‘varP’, ‘max’, ‘default’, ‘sum’, ‘stdDevP’, ‘avg’, ‘product’, ‘grand’, ‘countA’, ‘stdDev’}

tagname _ = 'item'_
    

x
    

Values must be of type <class ‘int’>

_class _openpyxl.pivot.table.Format(_action ='formatting'_, _dxfId =None_, _pivotArea =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#Format)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

action
    

Value must be one of {‘formatting’, ‘formula’, ‘blank’, ‘drill’}

dxfId
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

pivotArea
    

Values must be of type <class ‘openpyxl.pivot.table.PivotArea’>

tagname _ = 'format'_
    

_class _openpyxl.pivot.table.HierarchyUsage(_hierarchyUsage =None_)[[source]](../_modules/openpyxl/pivot/table.html#HierarchyUsage)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

hierarchyUsage
    

Values must be of type <class ‘int’>

tagname _ = 'hierarchyUsage'_
    

_class _openpyxl.pivot.table.Location(_ref =None_, _firstHeaderRow =None_, _firstDataRow =None_, _firstDataCol =None_, _rowPageCount =None_, _colPageCount =None_)[[source]](../_modules/openpyxl/pivot/table.html#Location)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

colPageCount
    

Values must be of type <class ‘int’>

firstDataCol
    

Values must be of type <class ‘int’>

firstDataRow
    

Values must be of type <class ‘int’>

firstHeaderRow
    

Values must be of type <class ‘int’>

ref
    

Values must be of type <class ‘str’>

rowPageCount
    

Values must be of type <class ‘int’>

tagname _ = 'location'_
    

_class _openpyxl.pivot.table.MemberList(_count =None_, _level =None_, _member =()_)[[source]](../_modules/openpyxl/pivot/table.html#MemberList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _count
    

level
    

Values must be of type <class ‘int’>

member
    

Wrap a sequence in an containing object

tagname _ = 'members'_
    

_class _openpyxl.pivot.table.MemberProperty(_name =None_, _showCell =None_, _showTip =None_, _showAsCaption =None_, _nameLen =None_, _pPos =None_, _pLen =None_, _level =None_, _field =None_)[[source]](../_modules/openpyxl/pivot/table.html#MemberProperty)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

field
    

Values must be of type <class ‘int’>

level
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

nameLen
    

Values must be of type <class ‘int’>

pLen
    

Values must be of type <class ‘int’>

pPos
    

Values must be of type <class ‘int’>

showAsCaption
    

Values must be of type <class ‘bool’>

showCell
    

Values must be of type <class ‘bool’>

showTip
    

Values must be of type <class ‘bool’>

tagname _ = 'mps'_
    

_class _openpyxl.pivot.table.PageField(_fld =None_, _item =None_, _hier =None_, _name =None_, _cap =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#PageField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cap
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fld
    

Values must be of type <class ‘int’>

hier
    

Values must be of type <class ‘int’>

item
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'pageField'_
    

_class _openpyxl.pivot.table.PivotArea(_references =()_, _extLst =None_, _field =None_, _type ='normal'_, _dataOnly =True_, _labelOnly =None_, _grandRow =None_, _grandCol =None_, _cacheIndex =None_, _outline =True_, _offset =None_, _collapsedLevelsAreSubtotals =None_, _axis =None_, _fieldPosition =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotArea)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

axis
    

Value must be one of {‘axisValues’, ‘axisRow’, ‘axisPage’, ‘axisCol’}

cacheIndex
    

Values must be of type <class ‘bool’>

collapsedLevelsAreSubtotals
    

Values must be of type <class ‘bool’>

dataOnly
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

field
    

Values must be of type <class ‘int’>

fieldPosition
    

Values must be of type <class ‘int’>

grandCol
    

Values must be of type <class ‘bool’>

grandRow
    

Values must be of type <class ‘bool’>

labelOnly
    

Values must be of type <class ‘bool’>

offset
    

Values must be of type <class ‘str’>

outline
    

Values must be of type <class ‘bool’>

references
    

Wrap a sequence in an containing object

tagname _ = 'pivotArea'_
    

type
    

Value must be one of {‘data’, ‘topRight’, ‘button’, ‘topEnd’, ‘all’, ‘normal’, ‘origin’}

_class _openpyxl.pivot.table.PivotField(_items =()_, _autoSortScope =None_, _name =None_, _axis =None_, _dataField =None_, _subtotalCaption =None_, _showDropDowns =True_, _hiddenLevel =None_, _uniqueMemberProperty =None_, _compact =True_, _allDrilled =None_, _numFmtId =None_, _outline =True_, _subtotalTop =True_, _dragToRow =True_, _dragToCol =True_, _multipleItemSelectionAllowed =None_, _dragToPage =True_, _dragToData =True_, _dragOff =True_, _showAll =True_, _insertBlankRow =None_, _serverField =None_, _insertPageBreak =None_, _autoShow =None_, _topAutoShow =True_, _hideNewItems =None_, _measureFilter =None_, _includeNewItemsInFilter =None_, _itemPageCount =10_, _sortType ='manual'_, _dataSourceSort =None_, _nonAutoSortDefault =None_, _rankBy =None_, _defaultSubtotal =True_, _sumSubtotal =None_, _countASubtotal =None_, _avgSubtotal =None_, _maxSubtotal =None_, _minSubtotal =None_, _productSubtotal =None_, _countSubtotal =None_, _stdDevSubtotal =None_, _stdDevPSubtotal =None_, _varSubtotal =None_, _varPSubtotal =None_, _showPropCell =None_, _showPropTip =None_, _showPropAsCaption =None_, _defaultAttributeDrillState =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

allDrilled
    

Values must be of type <class ‘bool’>

autoShow
    

Values must be of type <class ‘bool’>

autoSortScope
    

Values must be of type <class ‘openpyxl.pivot.table.AutoSortScope’>

avgSubtotal
    

Values must be of type <class ‘bool’>

axis
    

Value must be one of {‘axisValues’, ‘axisRow’, ‘axisPage’, ‘axisCol’}

compact
    

Values must be of type <class ‘bool’>

countASubtotal
    

Values must be of type <class ‘bool’>

countSubtotal
    

Values must be of type <class ‘bool’>

dataField
    

Values must be of type <class ‘bool’>

dataSourceSort
    

Values must be of type <class ‘bool’>

defaultAttributeDrillState
    

Values must be of type <class ‘bool’>

defaultSubtotal
    

Values must be of type <class ‘bool’>

dragOff
    

Values must be of type <class ‘bool’>

dragToCol
    

Values must be of type <class ‘bool’>

dragToData
    

Values must be of type <class ‘bool’>

dragToPage
    

Values must be of type <class ‘bool’>

dragToRow
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

hiddenLevel
    

Values must be of type <class ‘bool’>

hideNewItems
    

Values must be of type <class ‘bool’>

includeNewItemsInFilter
    

Values must be of type <class ‘bool’>

insertBlankRow
    

Values must be of type <class ‘bool’>

insertPageBreak
    

Values must be of type <class ‘bool’>

itemPageCount
    

Values must be of type <class ‘int’>

items
    

Wrap a sequence in an containing object

maxSubtotal
    

Values must be of type <class ‘bool’>

measureFilter
    

Values must be of type <class ‘bool’>

minSubtotal
    

Values must be of type <class ‘bool’>

multipleItemSelectionAllowed
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

nonAutoSortDefault
    

Values must be of type <class ‘bool’>

numFmtId
    

Values must be of type <class ‘int’>

outline
    

Values must be of type <class ‘bool’>

productSubtotal
    

Values must be of type <class ‘bool’>

rankBy
    

Values must be of type <class ‘int’>

serverField
    

Values must be of type <class ‘bool’>

showAll
    

Values must be of type <class ‘bool’>

showDropDowns
    

Values must be of type <class ‘bool’>

showPropAsCaption
    

Values must be of type <class ‘bool’>

showPropCell
    

Values must be of type <class ‘bool’>

showPropTip
    

Values must be of type <class ‘bool’>

sortType
    

Value must be one of {‘descending’, ‘manual’, ‘ascending’}

stdDevPSubtotal
    

Values must be of type <class ‘bool’>

stdDevSubtotal
    

Values must be of type <class ‘bool’>

subtotalCaption
    

Values must be of type <class ‘str’>

subtotalTop
    

Values must be of type <class ‘bool’>

sumSubtotal
    

Values must be of type <class ‘bool’>

tagname _ = 'pivotField'_
    

topAutoShow
    

Values must be of type <class ‘bool’>

uniqueMemberProperty
    

Values must be of type <class ‘str’>

varPSubtotal
    

Values must be of type <class ‘bool’>

varSubtotal
    

Values must be of type <class ‘bool’>

_class _openpyxl.pivot.table.PivotFilter(_fld =None_, _mpFld =None_, _type =None_, _evalOrder =None_, _id =None_, _iMeasureHier =None_, _iMeasureFld =None_, _name =None_, _description =None_, _stringValue1 =None_, _stringValue2 =None_, _autoFilter =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotFilter)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoFilter
    

Values must be of type <class ‘openpyxl.worksheet.filters.AutoFilter’>

description
    

Values must be of type <class ‘str’>

evalOrder
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fld
    

Values must be of type <class ‘int’>

iMeasureFld
    

Values must be of type <class ‘int’>

iMeasureHier
    

Values must be of type <class ‘int’>

id
    

Values must be of type <class ‘int’>

mpFld
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

stringValue1
    

Values must be of type <class ‘str’>

stringValue2
    

Values must be of type <class ‘str’>

tagname _ = 'filter'_
    

type
    

Value must be one of {‘tomorrow’, ‘M4’, ‘dateEqual’, ‘captionNotEqual’, ‘M3’, ‘M11’, ‘captionNotBeginsWith’, ‘dateNewerThan’, ‘captionLessThan’, ‘Q4’, ‘today’, ‘percent’, ‘captionBeginsWith’, ‘yesterday’, ‘M7’, ‘Q2’, ‘valueGreaterThan’, ‘captionEqual’, ‘M1’, ‘valueEqual’, ‘unknown’, ‘lastMonth’, ‘M6’, ‘captionGreaterThan’, ‘M5’, ‘M10’, ‘lastWeek’, ‘dateOlderThan’, ‘sum’, ‘lastYear’, ‘M12’, ‘captionLessThanOrEqual’, ‘captionNotContains’, ‘captionGreaterThanOrEqual’, ‘dateNotEqual’, ‘dateNotBetween’, ‘nextWeek’, ‘valueBetween’, ‘dateNewerThanOrEqual’, ‘captionNotEndsWith’, ‘nextQuarter’, ‘captionEndsWith’, ‘count’, ‘thisYear’, ‘dateBetween’, ‘valueGreaterThanOrEqual’, ‘Q1’, ‘M9’, ‘captionBetween’, ‘valueNotEqual’, ‘nextMonth’, ‘Q3’, ‘valueNotBetween’, ‘captionContains’, ‘dateOlderThanOrEqual’, ‘M2’, ‘valueLessThanOrEqual’, ‘thisMonth’, ‘yearToDate’, ‘thisWeek’, ‘nextYear’, ‘M8’, ‘thisQuarter’, ‘valueLessThan’, ‘captionNotBetween’, ‘lastQuarter’}

_class _openpyxl.pivot.table.PivotFilters(_count =None_, _filter =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotFilters)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

count
    

Values must be of type <class ‘int’>

filter
    

Values must be of type <class ‘openpyxl.pivot.table.PivotFilter’>

_class _openpyxl.pivot.table.PivotHierarchy(_outline =None_, _multipleItemSelectionAllowed =None_, _subtotalTop =None_, _showInFieldList =None_, _dragToRow =None_, _dragToCol =None_, _dragToPage =None_, _dragToData =None_, _dragOff =None_, _includeNewItemsInFilter =None_, _caption =None_, _mps =()_, _members =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotHierarchy)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

dragOff
    

Values must be of type <class ‘bool’>

dragToCol
    

Values must be of type <class ‘bool’>

dragToData
    

Values must be of type <class ‘bool’>

dragToPage
    

Values must be of type <class ‘bool’>

dragToRow
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

includeNewItemsInFilter
    

Values must be of type <class ‘bool’>

members
    

Values must be of type <class ‘openpyxl.pivot.table.MemberList’>

mps
    

Wrap a sequence in an containing object

multipleItemSelectionAllowed
    

Values must be of type <class ‘bool’>

outline
    

Values must be of type <class ‘bool’>

showInFieldList
    

Values must be of type <class ‘bool’>

subtotalTop
    

Values must be of type <class ‘bool’>

tagname _ = 'pivotHierarchy'_
    

_class _openpyxl.pivot.table.PivotTableStyle(_name =None_, _showRowHeaders =None_, _showColHeaders =None_, _showRowStripes =None_, _showColStripes =None_, _showLastColumn =None_)[[source]](../_modules/openpyxl/pivot/table.html#PivotTableStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

showColHeaders
    

Values must be of type <class ‘bool’>

showColStripes
    

Values must be of type <class ‘bool’>

showLastColumn
    

Values must be of type <class ‘bool’>

showRowHeaders
    

Values must be of type <class ‘bool’>

showRowStripes
    

Values must be of type <class ‘bool’>

tagname _ = 'pivotTableStyleInfo'_
    

_class _openpyxl.pivot.table.Reference(_field =None_, _count =None_, _selected =None_, _byPosition =None_, _relative =None_, _defaultSubtotal =None_, _sumSubtotal =None_, _countASubtotal =None_, _avgSubtotal =None_, _maxSubtotal =None_, _minSubtotal =None_, _productSubtotal =None_, _countSubtotal =None_, _stdDevSubtotal =None_, _stdDevPSubtotal =None_, _varSubtotal =None_, _varPSubtotal =None_, _x =()_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/table.html#Reference)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

avgSubtotal
    

Values must be of type <class ‘bool’>

byPosition
    

Values must be of type <class ‘bool’>

_property _count
    

countASubtotal
    

Values must be of type <class ‘bool’>

countSubtotal
    

Values must be of type <class ‘bool’>

defaultSubtotal
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

field
    

Values must be of type <class ‘int’>

maxSubtotal
    

Values must be of type <class ‘bool’>

minSubtotal
    

Values must be of type <class ‘bool’>

productSubtotal
    

Values must be of type <class ‘bool’>

relative
    

Values must be of type <class ‘bool’>

selected
    

Values must be of type <class ‘bool’>

stdDevPSubtotal
    

Values must be of type <class ‘bool’>

stdDevSubtotal
    

Values must be of type <class ‘bool’>

sumSubtotal
    

Values must be of type <class ‘bool’>

tagname _ = 'reference'_
    

varPSubtotal
    

Values must be of type <class ‘bool’>

varSubtotal
    

Values must be of type <class ‘bool’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.table.RowColField(_x =None_)[[source]](../_modules/openpyxl/pivot/table.html#RowColField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'field'_
    

x
    

Values must be of type <class ‘int’>

_class _openpyxl.pivot.table.RowColItem(_t ='data'_, _r =0_, _i =0_, _x =()_)[[source]](../_modules/openpyxl/pivot/table.html#RowColItem)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

i
    

Values must be of type <class ‘int’>

r
    

Values must be of type <class ‘int’>

t
    

Value must be one of {‘data’, ‘min’, ‘count’, ‘var’, ‘blank’, ‘varP’, ‘max’, ‘default’, ‘sum’, ‘stdDevP’, ‘avg’, ‘product’, ‘grand’, ‘countA’, ‘stdDev’}

tagname _ = 'i'_
    

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.table.RowHierarchiesUsage(_count =None_, _rowHierarchyUsage =()_)[[source]](../_modules/openpyxl/pivot/table.html#RowHierarchiesUsage)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_property _count
    

rowHierarchyUsage
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'rowHierarchiesUsage'_
    

_class _openpyxl.pivot.table.TableDefinition(_name =None_, _cacheId =None_, _dataOnRows =False_, _dataPosition =None_, _dataCaption =None_, _grandTotalCaption =None_, _errorCaption =None_, _showError =False_, _missingCaption =None_, _showMissing =True_, _pageStyle =None_, _pivotTableStyle =None_, _vacatedStyle =None_, _tag =None_, _updatedVersion =0_, _minRefreshableVersion =0_, _asteriskTotals =False_, _showItems =True_, _editData =False_, _disableFieldList =False_, _showCalcMbrs =True_, _visualTotals =True_, _showMultipleLabel =True_, _showDataDropDown =True_, _showDrill =True_, _printDrill =False_, _showMemberPropertyTips =True_, _showDataTips =True_, _enableWizard =True_, _enableDrill =True_, _enableFieldProperties =True_, _preserveFormatting =True_, _useAutoFormatting =False_, _pageWrap =0_, _pageOverThenDown =False_, _subtotalHiddenItems =False_, _rowGrandTotals =True_, _colGrandTotals =True_, _fieldPrintTitles =False_, _itemPrintTitles =False_, _mergeItem =False_, _showDropZones =True_, _createdVersion =0_, _indent =1_, _showEmptyRow =False_, _showEmptyCol =False_, _showHeaders =True_, _compact =True_, _outline =False_, _outlineData =False_, _compactData =True_, _published =False_, _gridDropZones =False_, _immersive =True_, _multipleFieldFilters =None_, _chartFormat =0_, _rowHeaderCaption =None_, _colHeaderCaption =None_, _fieldListSortAscending =None_, _mdxSubqueries =None_, _customListSort =None_, _autoFormatId =None_, _applyNumberFormats =False_, _applyBorderFormats =False_, _applyFontFormats =False_, _applyPatternFormats =False_, _applyAlignmentFormats =False_, _applyWidthHeightFormats =False_, _location =None_, _pivotFields =()_, _rowFields =()_, _rowItems =()_, _colFields =()_, _colItems =()_, _pageFields =()_, _dataFields =()_, _formats =()_, _conditionalFormats =None_, _chartFormats =()_, _pivotHierarchies =()_, _pivotTableStyleInfo =None_, _filters =()_, _rowHierarchiesUsage =None_, _colHierarchiesUsage =None_, _extLst =None_, _id =None_)[[source]](../_modules/openpyxl/pivot/table.html#TableDefinition)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

applyAlignmentFormats
    

Values must be of type <class ‘bool’>

applyBorderFormats
    

Values must be of type <class ‘bool’>

applyFontFormats
    

Values must be of type <class ‘bool’>

applyNumberFormats
    

Values must be of type <class ‘bool’>

applyPatternFormats
    

Values must be of type <class ‘bool’>

applyWidthHeightFormats
    

Values must be of type <class ‘bool’>

asteriskTotals
    

Values must be of type <class ‘bool’>

autoFormatId
    

Values must be of type <class ‘int’>

cache _ = None_
    

cacheId
    

Values must be of type <class ‘int’>

chartFormat
    

Values must be of type <class ‘int’>

chartFormats
    

Wrap a sequence in an containing object

colFields
    

Wrap a sequence in an containing object

colGrandTotals
    

Values must be of type <class ‘bool’>

colHeaderCaption
    

Values must be of type <class ‘str’>

colHierarchiesUsage
    

Values must be of type <class ‘openpyxl.pivot.table.ColHierarchiesUsage’>

colItems
    

Wrap a sequence in an containing object

compact
    

Values must be of type <class ‘bool’>

compactData
    

Values must be of type <class ‘bool’>

conditionalFormats
    

Values must be of type <class ‘openpyxl.pivot.table.ConditionalFormatList’>

createdVersion
    

Values must be of type <class ‘int’>

customListSort
    

Values must be of type <class ‘bool’>

dataCaption
    

Values must be of type <class ‘str’>

dataFields
    

Wrap a sequence in an containing object

dataOnRows
    

Values must be of type <class ‘bool’>

dataPosition
    

Values must be of type <class ‘int’>

disableFieldList
    

Values must be of type <class ‘bool’>

editData
    

Values must be of type <class ‘bool’>

enableDrill
    

Values must be of type <class ‘bool’>

enableFieldProperties
    

Values must be of type <class ‘bool’>

enableWizard
    

Values must be of type <class ‘bool’>

errorCaption
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fieldListSortAscending
    

Values must be of type <class ‘bool’>

fieldPrintTitles
    

Values must be of type <class ‘bool’>

filters
    

Wrap a sequence in an containing object

formats
    

Wrap a sequence in an containing object

formatted_fields()[[source]](../_modules/openpyxl/pivot/table.html#TableDefinition.formatted_fields)
    

Map fields to associated conditional formats by priority

grandTotalCaption
    

Values must be of type <class ‘str’>

gridDropZones
    

Values must be of type <class ‘bool’>

id
    

Values must be of type <class ‘str’>

immersive
    

Values must be of type <class ‘bool’>

indent
    

Values must be of type <class ‘int’>

itemPrintTitles
    

Values must be of type <class ‘bool’>

location
    

Values must be of type <class ‘openpyxl.pivot.table.Location’>

mdxSubqueries
    

Values must be of type <class ‘bool’>

mergeItem
    

Values must be of type <class ‘bool’>

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml'_
    

minRefreshableVersion
    

Values must be of type <class ‘int’>

missingCaption
    

Values must be of type <class ‘str’>

multipleFieldFilters
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

outline
    

Values must be of type <class ‘bool’>

outlineData
    

Values must be of type <class ‘bool’>

pageFields
    

Wrap a sequence in an containing object

pageOverThenDown
    

Values must be of type <class ‘bool’>

pageStyle
    

Values must be of type <class ‘str’>

pageWrap
    

Values must be of type <class ‘int’>

_property _path
    

pivotFields
    

Wrap a sequence in an containing object

pivotHierarchies
    

Wrap a sequence in an containing object

pivotTableStyle
    

Values must be of type <class ‘str’>

pivotTableStyleInfo
    

Values must be of type <class ‘openpyxl.pivot.table.PivotTableStyle’>

preserveFormatting
    

Values must be of type <class ‘bool’>

printDrill
    

Values must be of type <class ‘bool’>

published
    

Values must be of type <class ‘bool’>

rel_type _ = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotTable'_
    

rowFields
    

Wrap a sequence in an containing object

rowGrandTotals
    

Values must be of type <class ‘bool’>

rowHeaderCaption
    

Values must be of type <class ‘str’>

rowHierarchiesUsage
    

Values must be of type <class ‘openpyxl.pivot.table.RowHierarchiesUsage’>

rowItems
    

Wrap a sequence in an containing object

showCalcMbrs
    

Values must be of type <class ‘bool’>

showDataDropDown
    

Values must be of type <class ‘bool’>

showDataTips
    

Values must be of type <class ‘bool’>

showDrill
    

Values must be of type <class ‘bool’>

showDropZones
    

Values must be of type <class ‘bool’>

showEmptyCol
    

Values must be of type <class ‘bool’>

showEmptyRow
    

Values must be of type <class ‘bool’>

showError
    

Values must be of type <class ‘bool’>

showHeaders
    

Values must be of type <class ‘bool’>

showItems
    

Values must be of type <class ‘bool’>

showMemberPropertyTips
    

Values must be of type <class ‘bool’>

showMissing
    

Values must be of type <class ‘bool’>

showMultipleLabel
    

Values must be of type <class ‘bool’>

subtotalHiddenItems
    

Values must be of type <class ‘bool’>

_property _summary
    

Provide a simplified summary of the table

tag
    

Values must be of type <class ‘str’>

tagname _ = 'pivotTableDefinition'_
    

to_tree()[[source]](../_modules/openpyxl/pivot/table.html#TableDefinition.to_tree)
    

updatedVersion
    

Values must be of type <class ‘int’>

useAutoFormatting
    

Values must be of type <class ‘bool’>

vacatedStyle
    

Values must be of type <class ‘str’>

visualTotals
    

Values must be of type <class ‘bool’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.pivot.table module
    * `AutoSortScope`
      * `AutoSortScope.pivotArea`
    * `ChartFormat`
      * `ChartFormat.chart`
      * `ChartFormat.format`
      * `ChartFormat.pivotArea`
      * `ChartFormat.series`
      * `ChartFormat.tagname`
    * `ColHierarchiesUsage`
      * `ColHierarchiesUsage.colHierarchyUsage`
      * `ColHierarchiesUsage.count`
      * `ColHierarchiesUsage.tagname`
    * `ConditionalFormat`
      * `ConditionalFormat.extLst`
      * `ConditionalFormat.pivotAreas`
      * `ConditionalFormat.priority`
      * `ConditionalFormat.scope`
      * `ConditionalFormat.tagname`
      * `ConditionalFormat.type`
    * `ConditionalFormatList`
      * `ConditionalFormatList.by_priority()`
      * `ConditionalFormatList.conditionalFormat`
      * `ConditionalFormatList.count`
      * `ConditionalFormatList.tagname`
      * `ConditionalFormatList.to_tree()`
    * `DataField`
      * `DataField.baseField`
      * `DataField.baseItem`
      * `DataField.extLst`
      * `DataField.fld`
      * `DataField.name`
      * `DataField.numFmtId`
      * `DataField.showDataAs`
      * `DataField.subtotal`
      * `DataField.tagname`
    * `FieldItem`
      * `FieldItem.c`
      * `FieldItem.d`
      * `FieldItem.e`
      * `FieldItem.f`
      * `FieldItem.h`
      * `FieldItem.m`
      * `FieldItem.n`
      * `FieldItem.s`
      * `FieldItem.sd`
      * `FieldItem.t`
      * `FieldItem.tagname`
      * `FieldItem.x`
    * `Format`
      * `Format.action`
      * `Format.dxfId`
      * `Format.extLst`
      * `Format.pivotArea`
      * `Format.tagname`
    * `HierarchyUsage`
      * `HierarchyUsage.hierarchyUsage`
      * `HierarchyUsage.tagname`
    * `Location`
      * `Location.colPageCount`
      * `Location.firstDataCol`
      * `Location.firstDataRow`
      * `Location.firstHeaderRow`
      * `Location.ref`
      * `Location.rowPageCount`
      * `Location.tagname`
    * `MemberList`
      * `MemberList.count`
      * `MemberList.level`
      * `MemberList.member`
      * `MemberList.tagname`
    * `MemberProperty`
      * `MemberProperty.field`
      * `MemberProperty.level`
      * `MemberProperty.name`
      * `MemberProperty.nameLen`
      * `MemberProperty.pLen`
      * `MemberProperty.pPos`
      * `MemberProperty.showAsCaption`
      * `MemberProperty.showCell`
      * `MemberProperty.showTip`
      * `MemberProperty.tagname`
    * `PageField`
      * `PageField.cap`
      * `PageField.extLst`
      * `PageField.fld`
      * `PageField.hier`
      * `PageField.item`
      * `PageField.name`
      * `PageField.tagname`
    * `PivotArea`
      * `PivotArea.axis`
      * `PivotArea.cacheIndex`
      * `PivotArea.collapsedLevelsAreSubtotals`
      * `PivotArea.dataOnly`
      * `PivotArea.extLst`
      * `PivotArea.field`
      * `PivotArea.fieldPosition`
      * `PivotArea.grandCol`
      * `PivotArea.grandRow`
      * `PivotArea.labelOnly`
      * `PivotArea.offset`
      * `PivotArea.outline`
      * `PivotArea.references`
      * `PivotArea.tagname`
      * `PivotArea.type`
    * `PivotField`
      * `PivotField.allDrilled`
      * `PivotField.autoShow`
      * `PivotField.autoSortScope`
      * `PivotField.avgSubtotal`
      * `PivotField.axis`
      * `PivotField.compact`
      * `PivotField.countASubtotal`
      * `PivotField.countSubtotal`
      * `PivotField.dataField`
      * `PivotField.dataSourceSort`
      * `PivotField.defaultAttributeDrillState`
      * `PivotField.defaultSubtotal`
      * `PivotField.dragOff`
      * `PivotField.dragToCol`
      * `PivotField.dragToData`
      * `PivotField.dragToPage`
      * `PivotField.dragToRow`
      * `PivotField.extLst`
      * `PivotField.hiddenLevel`
      * `PivotField.hideNewItems`
      * `PivotField.includeNewItemsInFilter`
      * `PivotField.insertBlankRow`
      * `PivotField.insertPageBreak`
      * `PivotField.itemPageCount`
      * `PivotField.items`
      * `PivotField.maxSubtotal`
      * `PivotField.measureFilter`
      * `PivotField.minSubtotal`
      * `PivotField.multipleItemSelectionAllowed`
      * `PivotField.name`
      * `PivotField.nonAutoSortDefault`
      * `PivotField.numFmtId`
      * `PivotField.outline`
      * `PivotField.productSubtotal`
      * `PivotField.rankBy`
      * `PivotField.serverField`
      * `PivotField.showAll`
      * `PivotField.showDropDowns`
      * `PivotField.showPropAsCaption`
      * `PivotField.showPropCell`
      * `PivotField.showPropTip`
      * `PivotField.sortType`
      * `PivotField.stdDevPSubtotal`
      * `PivotField.stdDevSubtotal`
      * `PivotField.subtotalCaption`
      * `PivotField.subtotalTop`
      * `PivotField.sumSubtotal`
      * `PivotField.tagname`
      * `PivotField.topAutoShow`
      * `PivotField.uniqueMemberProperty`
      * `PivotField.varPSubtotal`
      * `PivotField.varSubtotal`
    * `PivotFilter`
      * `PivotFilter.autoFilter`
      * `PivotFilter.description`
      * `PivotFilter.evalOrder`
      * `PivotFilter.extLst`
      * `PivotFilter.fld`
      * `PivotFilter.iMeasureFld`
      * `PivotFilter.iMeasureHier`
      * `PivotFilter.id`
      * `PivotFilter.mpFld`
      * `PivotFilter.name`
      * `PivotFilter.stringValue1`
      * `PivotFilter.stringValue2`
      * `PivotFilter.tagname`
      * `PivotFilter.type`
    * `PivotFilters`
      * `PivotFilters.count`
      * `PivotFilters.filter`
    * `PivotHierarchy`
      * `PivotHierarchy.caption`
      * `PivotHierarchy.dragOff`
      * `PivotHierarchy.dragToCol`
      * `PivotHierarchy.dragToData`
      * `PivotHierarchy.dragToPage`
      * `PivotHierarchy.dragToRow`
      * `PivotHierarchy.extLst`
      * `PivotHierarchy.includeNewItemsInFilter`
      * `PivotHierarchy.members`
      * `PivotHierarchy.mps`
      * `PivotHierarchy.multipleItemSelectionAllowed`
      * `PivotHierarchy.outline`
      * `PivotHierarchy.showInFieldList`
      * `PivotHierarchy.subtotalTop`
      * `PivotHierarchy.tagname`
    * `PivotTableStyle`
      * `PivotTableStyle.name`
      * `PivotTableStyle.showColHeaders`
      * `PivotTableStyle.showColStripes`
      * `PivotTableStyle.showLastColumn`
      * `PivotTableStyle.showRowHeaders`
      * `PivotTableStyle.showRowStripes`
      * `PivotTableStyle.tagname`
    * `Reference`
      * `Reference.avgSubtotal`
      * `Reference.byPosition`
      * `Reference.count`
      * `Reference.countASubtotal`
      * `Reference.countSubtotal`
      * `Reference.defaultSubtotal`
      * `Reference.extLst`
      * `Reference.field`
      * `Reference.maxSubtotal`
      * `Reference.minSubtotal`
      * `Reference.productSubtotal`
      * `Reference.relative`
      * `Reference.selected`
      * `Reference.stdDevPSubtotal`
      * `Reference.stdDevSubtotal`
      * `Reference.sumSubtotal`
      * `Reference.tagname`
      * `Reference.varPSubtotal`
      * `Reference.varSubtotal`
      * `Reference.x`
    * `RowColField`
      * `RowColField.tagname`
      * `RowColField.x`
    * `RowColItem`
      * `RowColItem.i`
      * `RowColItem.r`
      * `RowColItem.t`
      * `RowColItem.tagname`
      * `RowColItem.x`
    * `RowHierarchiesUsage`
      * `RowHierarchiesUsage.count`
      * `RowHierarchiesUsage.rowHierarchyUsage`
      * `RowHierarchiesUsage.tagname`
    * `TableDefinition`
      * `TableDefinition.applyAlignmentFormats`
      * `TableDefinition.applyBorderFormats`
      * `TableDefinition.applyFontFormats`
      * `TableDefinition.applyNumberFormats`
      * `TableDefinition.applyPatternFormats`
      * `TableDefinition.applyWidthHeightFormats`
      * `TableDefinition.asteriskTotals`
      * `TableDefinition.autoFormatId`
      * `TableDefinition.cache`
      * `TableDefinition.cacheId`
      * `TableDefinition.chartFormat`
      * `TableDefinition.chartFormats`
      * `TableDefinition.colFields`
      * `TableDefinition.colGrandTotals`
      * `TableDefinition.colHeaderCaption`
      * `TableDefinition.colHierarchiesUsage`
      * `TableDefinition.colItems`
      * `TableDefinition.compact`
      * `TableDefinition.compactData`
      * `TableDefinition.conditionalFormats`
      * `TableDefinition.createdVersion`
      * `TableDefinition.customListSort`
      * `TableDefinition.dataCaption`
      * `TableDefinition.dataFields`
      * `TableDefinition.dataOnRows`
      * `TableDefinition.dataPosition`
      * `TableDefinition.disableFieldList`
      * `TableDefinition.editData`
      * `TableDefinition.enableDrill`
      * `TableDefinition.enableFieldProperties`
      * `TableDefinition.enableWizard`
      * `TableDefinition.errorCaption`
      * `TableDefinition.extLst`
      * `TableDefinition.fieldListSortAscending`
      * `TableDefinition.fieldPrintTitles`
      * `TableDefinition.filters`
      * `TableDefinition.formats`
      * `TableDefinition.formatted_fields()`
      * `TableDefinition.grandTotalCaption`
      * `TableDefinition.gridDropZones`
      * `TableDefinition.id`
      * `TableDefinition.immersive`
      * `TableDefinition.indent`
      * `TableDefinition.itemPrintTitles`
      * `TableDefinition.location`
      * `TableDefinition.mdxSubqueries`
      * `TableDefinition.mergeItem`
      * `TableDefinition.mime_type`
      * `TableDefinition.minRefreshableVersion`
      * `TableDefinition.missingCaption`
      * `TableDefinition.multipleFieldFilters`
      * `TableDefinition.name`
      * `TableDefinition.outline`
      * `TableDefinition.outlineData`
      * `TableDefinition.pageFields`
      * `TableDefinition.pageOverThenDown`
      * `TableDefinition.pageStyle`
      * `TableDefinition.pageWrap`
      * `TableDefinition.path`
      * `TableDefinition.pivotFields`
      * `TableDefinition.pivotHierarchies`
      * `TableDefinition.pivotTableStyle`
      * `TableDefinition.pivotTableStyleInfo`
      * `TableDefinition.preserveFormatting`
      * `TableDefinition.printDrill`
      * `TableDefinition.published`
      * `TableDefinition.rel_type`
      * `TableDefinition.rowFields`
      * `TableDefinition.rowGrandTotals`
      * `TableDefinition.rowHeaderCaption`
      * `TableDefinition.rowHierarchiesUsage`
      * `TableDefinition.rowItems`
      * `TableDefinition.showCalcMbrs`
      * `TableDefinition.showDataDropDown`
      * `TableDefinition.showDataTips`
      * `TableDefinition.showDrill`
      * `TableDefinition.showDropZones`
      * `TableDefinition.showEmptyCol`
      * `TableDefinition.showEmptyRow`
      * `TableDefinition.showError`
      * `TableDefinition.showHeaders`
      * `TableDefinition.showItems`
      * `TableDefinition.showMemberPropertyTips`
      * `TableDefinition.showMissing`
      * `TableDefinition.showMultipleLabel`
      * `TableDefinition.subtotalHiddenItems`
      * `TableDefinition.summary`
      * `TableDefinition.tag`
      * `TableDefinition.tagname`
      * `TableDefinition.to_tree()`
      * `TableDefinition.updatedVersion`
      * `TableDefinition.useAutoFormatting`
      * `TableDefinition.vacatedStyle`
      * `TableDefinition.visualTotals`



#### Previous topic

[openpyxl.pivot.record module](openpyxl.pivot.record.html "previous chapter")

#### Next topic

[openpyxl.reader package](openpyxl.reader.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.pivot.table.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.reader.html "openpyxl.reader package") |
  * [previous](openpyxl.pivot.record.html "openpyxl.pivot.record module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.table module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
