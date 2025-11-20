### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.fields.html "openpyxl.pivot.fields module") |
  * [previous](openpyxl.pivot.html "openpyxl.pivot package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.cache module]()



# openpyxl.pivot.cache module

_class _openpyxl.pivot.cache.CacheDefinition(_invalid =None_, _saveData =None_, _refreshOnLoad =None_, _optimizeMemory =None_, _enableRefresh =None_, _refreshedBy =None_, _refreshedDate =None_, _refreshedDateIso =None_, _backgroundQuery =None_, _missingItemsLimit =None_, _createdVersion =None_, _refreshedVersion =None_, _minRefreshableVersion =None_, _recordCount =None_, _upgradeOnRefresh =None_, _tupleCache =None_, _supportSubquery =None_, _supportAdvancedDrill =None_, _cacheSource =None_, _cacheFields =()_, _cacheHierarchies =()_, _kpis =()_, _calculatedItems =()_, _calculatedMembers =()_, _dimensions =()_, _measureGroups =()_, _maps =()_, _extLst =None_, _id =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CacheDefinition)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

backgroundQuery
    

Values must be of type <class ‘bool’>

cacheFields
    

Wrap a sequence in an containing object

cacheHierarchies
    

Wrap a sequence in an containing object

cacheSource
    

Values must be of type <class ‘openpyxl.pivot.cache.CacheSource’>

calculatedItems
    

Wrap a sequence in an containing object

calculatedMembers
    

Wrap a sequence in an containing object

createdVersion
    

Values must be of type <class ‘int’>

dimensions
    

Wrap a sequence in an containing object

enableRefresh
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

id
    

Values must be of type <class ‘str’>

invalid
    

Values must be of type <class ‘bool’>

kpis
    

Wrap a sequence in an containing object

maps
    

Wrap a sequence in an containing object

measureGroups
    

Wrap a sequence in an containing object

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml'_
    

minRefreshableVersion
    

Values must be of type <class ‘int’>

missingItemsLimit
    

Values must be of type <class ‘int’>

optimizeMemory
    

Values must be of type <class ‘bool’>

_property _path
    

recordCount
    

Values must be of type <class ‘int’>

records _ = None_
    

refreshOnLoad
    

Values must be of type <class ‘bool’>

refreshedBy
    

Values must be of type <class ‘str’>

refreshedDate
    

Values must be of type <class ‘float’>

refreshedDateIso
    

Values must be of type <class ‘datetime.datetime’>

refreshedVersion
    

Values must be of type <class ‘int’>

rel_type _ = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotCacheDefinition'_
    

saveData
    

Values must be of type <class ‘bool’>

supportAdvancedDrill
    

Values must be of type <class ‘bool’>

supportSubquery
    

Values must be of type <class ‘bool’>

tagname _ = 'pivotCacheDefinition'_
    

to_tree()[[source]](../_modules/openpyxl/pivot/cache.html#CacheDefinition.to_tree)
    

tupleCache
    

Values must be of type <class ‘openpyxl.pivot.cache.TupleCache’>

upgradeOnRefresh
    

Values must be of type <class ‘bool’>

_class _openpyxl.pivot.cache.CacheField(_sharedItems =None_, _fieldGroup =None_, _mpMap =None_, _extLst =None_, _name =None_, _caption =None_, _propertyName =None_, _serverField =None_, _uniqueList =True_, _numFmtId =None_, _formula =None_, _sqlType =0_, _hierarchy =0_, _level =0_, _databaseField =True_, _mappingCount =None_, _memberPropertyField =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CacheField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

databaseField
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fieldGroup
    

Values must be of type <class ‘openpyxl.pivot.cache.FieldGroup’>

formula
    

Values must be of type <class ‘str’>

hierarchy
    

Values must be of type <class ‘int’>

level
    

Values must be of type <class ‘int’>

mappingCount
    

Values must be of type <class ‘int’>

memberPropertyField
    

Values must be of type <class ‘bool’>

mpMap
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

numFmtId
    

Values must be of type <class ‘int’>

propertyName
    

Values must be of type <class ‘str’>

serverField
    

Values must be of type <class ‘bool’>

sharedItems
    

Values must be of type <class ‘openpyxl.pivot.cache.SharedItems’>

sqlType
    

Values must be of type <class ‘int’>

tagname _ = 'cacheField'_
    

uniqueList
    

Values must be of type <class ‘bool’>

_class _openpyxl.pivot.cache.CacheHierarchy(_uniqueName =''_, _caption =None_, _measure =None_, _set =None_, _parentSet =None_, _iconSet =0_, _attribute =None_, _time =None_, _keyAttribute =None_, _defaultMemberUniqueName =None_, _allUniqueName =None_, _allCaption =None_, _dimensionUniqueName =None_, _displayFolder =None_, _measureGroup =None_, _measures =None_, _count =None_, _oneField =None_, _memberValueDatatype =None_, _unbalanced =None_, _unbalancedGroup =None_, _hidden =None_, _fieldsUsage =()_, _groupLevels =()_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CacheHierarchy)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

allCaption
    

Values must be of type <class ‘str’>

allUniqueName
    

Values must be of type <class ‘str’>

attribute
    

Values must be of type <class ‘bool’>

caption
    

Values must be of type <class ‘str’>

count
    

Values must be of type <class ‘int’>

defaultMemberUniqueName
    

Values must be of type <class ‘str’>

dimensionUniqueName
    

Values must be of type <class ‘str’>

displayFolder
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fieldsUsage
    

Wrap a sequence in an containing object

groupLevels
    

Wrap a sequence in an containing object

hidden
    

Values must be of type <class ‘bool’>

iconSet
    

Values must be of type <class ‘int’>

keyAttribute
    

Values must be of type <class ‘bool’>

measure
    

Values must be of type <class ‘bool’>

measureGroup
    

Values must be of type <class ‘str’>

measures
    

Values must be of type <class ‘bool’>

memberValueDatatype
    

Values must be of type <class ‘int’>

oneField
    

Values must be of type <class ‘bool’>

parentSet
    

Values must be of type <class ‘int’>

set
    

Values must be of type <class ‘bool’>

tagname _ = 'cacheHierarchy'_
    

time
    

Values must be of type <class ‘bool’>

unbalanced
    

Values must be of type <class ‘bool’>

unbalancedGroup
    

Values must be of type <class ‘bool’>

uniqueName
    

Values must be of type <class ‘str’>

_class _openpyxl.pivot.cache.CacheSource(_type =None_, _connectionId =None_, _worksheetSource =None_, _consolidation =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CacheSource)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

connectionId
    

Values must be of type <class ‘int’>

consolidation
    

Values must be of type <class ‘openpyxl.pivot.cache.Consolidation’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

tagname _ = 'cacheSource'_
    

type
    

Value must be one of {‘external’, ‘consolidation’, ‘worksheet’, ‘scenario’}

worksheetSource
    

Values must be of type <class ‘openpyxl.pivot.cache.WorksheetSource’>

_class _openpyxl.pivot.cache.CalculatedItem(_field =None_, _formula =None_, _pivotArea =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CalculatedItem)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

field
    

Values must be of type <class ‘int’>

formula
    

Values must be of type <class ‘str’>

pivotArea
    

Values must be of type <class ‘openpyxl.pivot.table.PivotArea’>

tagname _ = 'calculatedItem'_
    

_class _openpyxl.pivot.cache.CalculatedMember(_name =None_, _mdx =None_, _memberName =None_, _hierarchy =None_, _parent =None_, _solveOrder =None_, _set =None_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#CalculatedMember)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

hierarchy
    

Values must be of type <class ‘str’>

mdx
    

Values must be of type <class ‘str’>

memberName
    

Values must be of type <class ‘str’>

name
    

Values must be of type <class ‘str’>

parent
    

Values must be of type <class ‘str’>

set
    

Values must be of type <class ‘bool’>

solveOrder
    

Values must be of type <class ‘int’>

tagname _ = 'calculatedMember'_
    

_class _openpyxl.pivot.cache.Consolidation(_autoPage =None_, _pages =()_, _rangeSets =()_)[[source]](../_modules/openpyxl/pivot/cache.html#Consolidation)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoPage
    

Values must be of type <class ‘bool’>

pages
    

Wrap a sequence in an containing object

rangeSets
    

Wrap a sequence in an containing object

tagname _ = 'consolidation'_
    

_class _openpyxl.pivot.cache.FieldGroup(_par =None_, _base =None_, _rangePr =None_, _discretePr =()_, _groupItems =None_)[[source]](../_modules/openpyxl/pivot/cache.html#FieldGroup)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

base
    

Values must be of type <class ‘int’>

discretePr
    

Wrap a sequence in an containing object

groupItems
    

Values must be of type <class ‘openpyxl.pivot.cache.GroupItems’>

par
    

Values must be of type <class ‘int’>

rangePr
    

Values must be of type <class ‘openpyxl.pivot.cache.RangePr’>

tagname _ = 'fieldGroup'_
    

_class _openpyxl.pivot.cache.FieldUsage(_x =None_)[[source]](../_modules/openpyxl/pivot/cache.html#FieldUsage)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'fieldUsage'_
    

x
    

Values must be of type <class ‘int’>

_class _openpyxl.pivot.cache.GroupItems(_count =None_, _m =()_, _n =()_, _b =()_, _e =()_, _s =()_, _d =()_)[[source]](../_modules/openpyxl/pivot/cache.html#GroupItems)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

A sequence (list or tuple) that may only contain objects of the declared type

_property _count
    

d
    

A sequence (list or tuple) that may only contain objects of the declared type

e
    

A sequence (list or tuple) that may only contain objects of the declared type

m
    

A sequence (list or tuple) that may only contain objects of the declared type

n
    

A sequence (list or tuple) that may only contain objects of the declared type

s
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'groupItems'_
    

_class _openpyxl.pivot.cache.GroupLevel(_uniqueName =None_, _caption =None_, _user =None_, _customRollUp =None_, _groups =()_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#GroupLevel)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

customRollUp
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

groups
    

Wrap a sequence in an containing object

tagname _ = 'groupLevel'_
    

uniqueName
    

Values must be of type <class ‘str’>

user
    

Values must be of type <class ‘bool’>

_class _openpyxl.pivot.cache.GroupMember(_uniqueName =None_, _group =None_)[[source]](../_modules/openpyxl/pivot/cache.html#GroupMember)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

group
    

Values must be of type <class ‘bool’>

tagname _ = 'groupMember'_
    

uniqueName
    

Values must be of type <class ‘str’>

_class _openpyxl.pivot.cache.LevelGroup(_name =None_, _uniqueName =None_, _caption =None_, _uniqueParent =None_, _id =None_, _groupMembers =()_)[[source]](../_modules/openpyxl/pivot/cache.html#LevelGroup)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

groupMembers
    

Wrap a sequence in an containing object

id
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'group'_
    

uniqueName
    

Values must be of type <class ‘str’>

uniqueParent
    

Values must be of type <class ‘str’>

_class _openpyxl.pivot.cache.MeasureDimensionMap(_measureGroup =None_, _dimension =None_)[[source]](../_modules/openpyxl/pivot/cache.html#MeasureDimensionMap)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

dimension
    

Values must be of type <class ‘int’>

measureGroup
    

Values must be of type <class ‘int’>

tagname _ = 'map'_
    

_class _openpyxl.pivot.cache.MeasureGroup(_name =None_, _caption =None_)[[source]](../_modules/openpyxl/pivot/cache.html#MeasureGroup)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'measureGroup'_
    

_class _openpyxl.pivot.cache.OLAPKPI(_uniqueName =None_, _caption =None_, _displayFolder =None_, _measureGroup =None_, _parent =None_, _value =None_, _goal =None_, _status =None_, _trend =None_, _weight =None_, _time =None_)[[source]](../_modules/openpyxl/pivot/cache.html#OLAPKPI)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

displayFolder
    

Values must be of type <class ‘str’>

goal
    

Values must be of type <class ‘str’>

measureGroup
    

Values must be of type <class ‘str’>

parent
    

Values must be of type <class ‘str’>

status
    

Values must be of type <class ‘str’>

tagname _ = 'kpi'_
    

time
    

Values must be of type <class ‘str’>

trend
    

Values must be of type <class ‘str’>

uniqueName
    

Values must be of type <class ‘str’>

value
    

Values must be of type <class ‘str’>

weight
    

Values must be of type <class ‘str’>

_class _openpyxl.pivot.cache.OLAPSet(_count =None_, _maxRank =None_, _setDefinition =None_, _sortType =None_, _queryFailed =None_, _tpls =None_, _sortByTuple =None_)[[source]](../_modules/openpyxl/pivot/cache.html#OLAPSet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

count
    

Values must be of type <class ‘int’>

maxRank
    

Values must be of type <class ‘int’>

queryFailed
    

Values must be of type <class ‘bool’>

setDefinition
    

Values must be of type <class ‘str’>

sortByTuple
    

Values must be of type <class ‘openpyxl.pivot.fields.TupleList’>

sortType
    

Value must be one of {‘ascendingNatural’, ‘descendingNatural’, ‘descending’, ‘ascendingAlpha’, ‘descendingAlpha’, ‘ascending’}

tagname _ = 'set'_
    

tpls
    

Values must be of type <class ‘openpyxl.pivot.fields.TupleList’>

_class _openpyxl.pivot.cache.PCDSDTCEntries(_count =None_, _m =None_, _n =None_, _e =None_, _s =None_)[[source]](../_modules/openpyxl/pivot/cache.html#PCDSDTCEntries)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

count
    

Values must be of type <class ‘int’>

e
    

Values must be of type <class ‘openpyxl.pivot.fields.Error’>

m
    

Values must be of type <class ‘openpyxl.pivot.fields.Missing’>

n
    

Values must be of type <class ‘openpyxl.pivot.fields.Number’>

s
    

Values must be of type <class ‘openpyxl.pivot.fields.Text’>

tagname _ = 'entries'_
    

_class _openpyxl.pivot.cache.PageItem(_name =None_)[[source]](../_modules/openpyxl/pivot/cache.html#PageItem)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

tagname _ = 'pageItem'_
    

_class _openpyxl.pivot.cache.PivotDimension(_measure =None_, _name =None_, _uniqueName =None_, _caption =None_)[[source]](../_modules/openpyxl/pivot/cache.html#PivotDimension)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

caption
    

Values must be of type <class ‘str’>

measure
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'dimension'_
    

uniqueName
    

Values must be of type <class ‘str’>

_class _openpyxl.pivot.cache.Query(_mdx =None_, _tpls =None_)[[source]](../_modules/openpyxl/pivot/cache.html#Query)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

mdx
    

Values must be of type <class ‘str’>

tagname _ = 'query'_
    

tpls
    

Values must be of type <class ‘openpyxl.pivot.fields.TupleList’>

_class _openpyxl.pivot.cache.RangePr(_autoStart =True_, _autoEnd =True_, _groupBy ='range'_, _startNum =None_, _endNum =None_, _startDate =None_, _endDate =None_, _groupInterval =1_)[[source]](../_modules/openpyxl/pivot/cache.html#RangePr)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

autoEnd
    

Values must be of type <class ‘bool’>

autoStart
    

Values must be of type <class ‘bool’>

endDate
    

Values must be of type <class ‘datetime.datetime’>

endNum
    

Values must be of type <class ‘float’>

groupBy
    

Value must be one of {‘seconds’, ‘months’, ‘range’, ‘minutes’, ‘days’, ‘years’, ‘hours’, ‘quarters’}

groupInterval
    

Values must be of type <class ‘float’>

startDate
    

Values must be of type <class ‘datetime.datetime’>

startNum
    

Values must be of type <class ‘float’>

tagname _ = 'rangePr'_
    

_class _openpyxl.pivot.cache.RangeSet(_i1 =None_, _i2 =None_, _i3 =None_, _i4 =None_, _ref =None_, _name =None_, _sheet =None_)[[source]](../_modules/openpyxl/pivot/cache.html#RangeSet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

i1
    

Values must be of type <class ‘int’>

i2
    

Values must be of type <class ‘int’>

i3
    

Values must be of type <class ‘int’>

i4
    

Values must be of type <class ‘int’>

name
    

Values must be of type <class ‘str’>

ref
    

Values must be of type <class ‘str’>

sheet
    

Values must be of type <class ‘str’>

tagname _ = 'rangeSet'_
    

_class _openpyxl.pivot.cache.ServerFormat(_culture =None_, _format =None_)[[source]](../_modules/openpyxl/pivot/cache.html#ServerFormat)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

culture
    

Values must be of type <class ‘str’>

format
    

Values must be of type <class ‘str’>

tagname _ = 'serverFormat'_
    

_class _openpyxl.pivot.cache.SharedItems(__fields =()_, _containsSemiMixedTypes =None_, _containsNonDate =None_, _containsDate =None_, _containsString =None_, _containsBlank =None_, _containsMixedTypes =None_, _containsNumber =None_, _containsInteger =None_, _minValue =None_, _maxValue =None_, _minDate =None_, _maxDate =None_, _count =None_, _longText =None_)[[source]](../_modules/openpyxl/pivot/cache.html#SharedItems)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

containsBlank
    

Values must be of type <class ‘bool’>

containsDate
    

Values must be of type <class ‘bool’>

containsInteger
    

Values must be of type <class ‘bool’>

containsMixedTypes
    

Values must be of type <class ‘bool’>

containsNonDate
    

Values must be of type <class ‘bool’>

containsNumber
    

Values must be of type <class ‘bool’>

containsSemiMixedTypes
    

Values must be of type <class ‘bool’>

containsString
    

Values must be of type <class ‘bool’>

_property _count
    

d
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

e
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

longText
    

Values must be of type <class ‘bool’>

m
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

maxDate
    

Values must be of type <class ‘datetime.datetime’>

maxValue
    

Values must be of type <class ‘float’>

minDate
    

Values must be of type <class ‘datetime.datetime’>

minValue
    

Values must be of type <class ‘float’>

n
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

s
    

Allow a multisequence to be built up from parts

Excluded from the instance __elements__ or __attrs__ as is effectively an Alias

tagname _ = 'sharedItems'_
    

_class _openpyxl.pivot.cache.TupleCache(_entries =None_, _sets =()_, _queryCache =()_, _serverFormats =()_, _extLst =None_)[[source]](../_modules/openpyxl/pivot/cache.html#TupleCache)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

entries
    

Values must be of type <class ‘openpyxl.pivot.cache.PCDSDTCEntries’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

queryCache
    

Wrap a sequence in an containing object

serverFormats
    

Wrap a sequence in an containing object

sets
    

Wrap a sequence in an containing object

tagname _ = 'tupleCache'_
    

_class _openpyxl.pivot.cache.WorksheetSource(_ref =None_, _name =None_, _sheet =None_)[[source]](../_modules/openpyxl/pivot/cache.html#WorksheetSource)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

ref
    

Values must be of type <class ‘str’>

sheet
    

Values must be of type <class ‘str’>

tagname _ = 'worksheetSource'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.pivot.cache module
    * `CacheDefinition`
      * `CacheDefinition.backgroundQuery`
      * `CacheDefinition.cacheFields`
      * `CacheDefinition.cacheHierarchies`
      * `CacheDefinition.cacheSource`
      * `CacheDefinition.calculatedItems`
      * `CacheDefinition.calculatedMembers`
      * `CacheDefinition.createdVersion`
      * `CacheDefinition.dimensions`
      * `CacheDefinition.enableRefresh`
      * `CacheDefinition.extLst`
      * `CacheDefinition.id`
      * `CacheDefinition.invalid`
      * `CacheDefinition.kpis`
      * `CacheDefinition.maps`
      * `CacheDefinition.measureGroups`
      * `CacheDefinition.mime_type`
      * `CacheDefinition.minRefreshableVersion`
      * `CacheDefinition.missingItemsLimit`
      * `CacheDefinition.optimizeMemory`
      * `CacheDefinition.path`
      * `CacheDefinition.recordCount`
      * `CacheDefinition.records`
      * `CacheDefinition.refreshOnLoad`
      * `CacheDefinition.refreshedBy`
      * `CacheDefinition.refreshedDate`
      * `CacheDefinition.refreshedDateIso`
      * `CacheDefinition.refreshedVersion`
      * `CacheDefinition.rel_type`
      * `CacheDefinition.saveData`
      * `CacheDefinition.supportAdvancedDrill`
      * `CacheDefinition.supportSubquery`
      * `CacheDefinition.tagname`
      * `CacheDefinition.to_tree()`
      * `CacheDefinition.tupleCache`
      * `CacheDefinition.upgradeOnRefresh`
    * `CacheField`
      * `CacheField.caption`
      * `CacheField.databaseField`
      * `CacheField.extLst`
      * `CacheField.fieldGroup`
      * `CacheField.formula`
      * `CacheField.hierarchy`
      * `CacheField.level`
      * `CacheField.mappingCount`
      * `CacheField.memberPropertyField`
      * `CacheField.mpMap`
      * `CacheField.name`
      * `CacheField.numFmtId`
      * `CacheField.propertyName`
      * `CacheField.serverField`
      * `CacheField.sharedItems`
      * `CacheField.sqlType`
      * `CacheField.tagname`
      * `CacheField.uniqueList`
    * `CacheHierarchy`
      * `CacheHierarchy.allCaption`
      * `CacheHierarchy.allUniqueName`
      * `CacheHierarchy.attribute`
      * `CacheHierarchy.caption`
      * `CacheHierarchy.count`
      * `CacheHierarchy.defaultMemberUniqueName`
      * `CacheHierarchy.dimensionUniqueName`
      * `CacheHierarchy.displayFolder`
      * `CacheHierarchy.extLst`
      * `CacheHierarchy.fieldsUsage`
      * `CacheHierarchy.groupLevels`
      * `CacheHierarchy.hidden`
      * `CacheHierarchy.iconSet`
      * `CacheHierarchy.keyAttribute`
      * `CacheHierarchy.measure`
      * `CacheHierarchy.measureGroup`
      * `CacheHierarchy.measures`
      * `CacheHierarchy.memberValueDatatype`
      * `CacheHierarchy.oneField`
      * `CacheHierarchy.parentSet`
      * `CacheHierarchy.set`
      * `CacheHierarchy.tagname`
      * `CacheHierarchy.time`
      * `CacheHierarchy.unbalanced`
      * `CacheHierarchy.unbalancedGroup`
      * `CacheHierarchy.uniqueName`
    * `CacheSource`
      * `CacheSource.connectionId`
      * `CacheSource.consolidation`
      * `CacheSource.extLst`
      * `CacheSource.tagname`
      * `CacheSource.type`
      * `CacheSource.worksheetSource`
    * `CalculatedItem`
      * `CalculatedItem.extLst`
      * `CalculatedItem.field`
      * `CalculatedItem.formula`
      * `CalculatedItem.pivotArea`
      * `CalculatedItem.tagname`
    * `CalculatedMember`
      * `CalculatedMember.extLst`
      * `CalculatedMember.hierarchy`
      * `CalculatedMember.mdx`
      * `CalculatedMember.memberName`
      * `CalculatedMember.name`
      * `CalculatedMember.parent`
      * `CalculatedMember.set`
      * `CalculatedMember.solveOrder`
      * `CalculatedMember.tagname`
    * `Consolidation`
      * `Consolidation.autoPage`
      * `Consolidation.pages`
      * `Consolidation.rangeSets`
      * `Consolidation.tagname`
    * `FieldGroup`
      * `FieldGroup.base`
      * `FieldGroup.discretePr`
      * `FieldGroup.groupItems`
      * `FieldGroup.par`
      * `FieldGroup.rangePr`
      * `FieldGroup.tagname`
    * `FieldUsage`
      * `FieldUsage.tagname`
      * `FieldUsage.x`
    * `GroupItems`
      * `GroupItems.b`
      * `GroupItems.count`
      * `GroupItems.d`
      * `GroupItems.e`
      * `GroupItems.m`
      * `GroupItems.n`
      * `GroupItems.s`
      * `GroupItems.tagname`
    * `GroupLevel`
      * `GroupLevel.caption`
      * `GroupLevel.customRollUp`
      * `GroupLevel.extLst`
      * `GroupLevel.groups`
      * `GroupLevel.tagname`
      * `GroupLevel.uniqueName`
      * `GroupLevel.user`
    * `GroupMember`
      * `GroupMember.group`
      * `GroupMember.tagname`
      * `GroupMember.uniqueName`
    * `LevelGroup`
      * `LevelGroup.caption`
      * `LevelGroup.groupMembers`
      * `LevelGroup.id`
      * `LevelGroup.name`
      * `LevelGroup.tagname`
      * `LevelGroup.uniqueName`
      * `LevelGroup.uniqueParent`
    * `MeasureDimensionMap`
      * `MeasureDimensionMap.dimension`
      * `MeasureDimensionMap.measureGroup`
      * `MeasureDimensionMap.tagname`
    * `MeasureGroup`
      * `MeasureGroup.caption`
      * `MeasureGroup.name`
      * `MeasureGroup.tagname`
    * `OLAPKPI`
      * `OLAPKPI.caption`
      * `OLAPKPI.displayFolder`
      * `OLAPKPI.goal`
      * `OLAPKPI.measureGroup`
      * `OLAPKPI.parent`
      * `OLAPKPI.status`
      * `OLAPKPI.tagname`
      * `OLAPKPI.time`
      * `OLAPKPI.trend`
      * `OLAPKPI.uniqueName`
      * `OLAPKPI.value`
      * `OLAPKPI.weight`
    * `OLAPSet`
      * `OLAPSet.count`
      * `OLAPSet.maxRank`
      * `OLAPSet.queryFailed`
      * `OLAPSet.setDefinition`
      * `OLAPSet.sortByTuple`
      * `OLAPSet.sortType`
      * `OLAPSet.tagname`
      * `OLAPSet.tpls`
    * `PCDSDTCEntries`
      * `PCDSDTCEntries.count`
      * `PCDSDTCEntries.e`
      * `PCDSDTCEntries.m`
      * `PCDSDTCEntries.n`
      * `PCDSDTCEntries.s`
      * `PCDSDTCEntries.tagname`
    * `PageItem`
      * `PageItem.name`
      * `PageItem.tagname`
    * `PivotDimension`
      * `PivotDimension.caption`
      * `PivotDimension.measure`
      * `PivotDimension.name`
      * `PivotDimension.tagname`
      * `PivotDimension.uniqueName`
    * `Query`
      * `Query.mdx`
      * `Query.tagname`
      * `Query.tpls`
    * `RangePr`
      * `RangePr.autoEnd`
      * `RangePr.autoStart`
      * `RangePr.endDate`
      * `RangePr.endNum`
      * `RangePr.groupBy`
      * `RangePr.groupInterval`
      * `RangePr.startDate`
      * `RangePr.startNum`
      * `RangePr.tagname`
    * `RangeSet`
      * `RangeSet.i1`
      * `RangeSet.i2`
      * `RangeSet.i3`
      * `RangeSet.i4`
      * `RangeSet.name`
      * `RangeSet.ref`
      * `RangeSet.sheet`
      * `RangeSet.tagname`
    * `ServerFormat`
      * `ServerFormat.culture`
      * `ServerFormat.format`
      * `ServerFormat.tagname`
    * `SharedItems`
      * `SharedItems.b`
      * `SharedItems.containsBlank`
      * `SharedItems.containsDate`
      * `SharedItems.containsInteger`
      * `SharedItems.containsMixedTypes`
      * `SharedItems.containsNonDate`
      * `SharedItems.containsNumber`
      * `SharedItems.containsSemiMixedTypes`
      * `SharedItems.containsString`
      * `SharedItems.count`
      * `SharedItems.d`
      * `SharedItems.e`
      * `SharedItems.longText`
      * `SharedItems.m`
      * `SharedItems.maxDate`
      * `SharedItems.maxValue`
      * `SharedItems.minDate`
      * `SharedItems.minValue`
      * `SharedItems.n`
      * `SharedItems.s`
      * `SharedItems.tagname`
    * `TupleCache`
      * `TupleCache.entries`
      * `TupleCache.extLst`
      * `TupleCache.queryCache`
      * `TupleCache.serverFormats`
      * `TupleCache.sets`
      * `TupleCache.tagname`
    * `WorksheetSource`
      * `WorksheetSource.name`
      * `WorksheetSource.ref`
      * `WorksheetSource.sheet`
      * `WorksheetSource.tagname`



#### Previous topic

[openpyxl.pivot package](openpyxl.pivot.html "previous chapter")

#### Next topic

[openpyxl.pivot.fields module](openpyxl.pivot.fields.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.pivot.cache.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.fields.html "openpyxl.pivot.fields module") |
  * [previous](openpyxl.pivot.html "openpyxl.pivot package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.cache module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
