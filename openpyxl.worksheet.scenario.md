### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.smart_tag.html "openpyxl.worksheet.smart_tag module") |
  * [previous](openpyxl.worksheet.related.html "openpyxl.worksheet.related module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.scenario module]()



# openpyxl.worksheet.scenario module

_class _openpyxl.worksheet.scenario.InputCells(_r =None_, _deleted =False_, _undone =False_, _val =None_, _numFmtId =None_)[[source]](../_modules/openpyxl/worksheet/scenario.html#InputCells)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

deleted
    

Values must be of type <class ‘bool’>

numFmtId
    

Values must be of type <class ‘int’>

r
    

Values must be of type <class ‘str’>

tagname _ = 'inputCells'_
    

undone
    

Values must be of type <class ‘bool’>

val
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.scenario.Scenario(_inputCells =()_, _name =None_, _locked =False_, _hidden =False_, _count =None_, _user =None_, _comment =None_)[[source]](../_modules/openpyxl/worksheet/scenario.html#Scenario)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

comment
    

Values must be of type <class ‘str’>

_property _count
    

hidden
    

Values must be of type <class ‘bool’>

inputCells
    

A sequence (list or tuple) that may only contain objects of the declared type

locked
    

Values must be of type <class ‘bool’>

name
    

Values must be of type <class ‘str’>

tagname _ = 'scenario'_
    

user
    

Values must be of type <class ‘str’>

_class _openpyxl.worksheet.scenario.ScenarioList(_scenario =()_, _current =None_, _show =None_, _sqref =None_)[[source]](../_modules/openpyxl/worksheet/scenario.html#ScenarioList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

append(_scenario_)[[source]](../_modules/openpyxl/worksheet/scenario.html#ScenarioList.append)
    

current
    

Values must be of type <class ‘int’>

scenario
    

A sequence (list or tuple) that may only contain objects of the declared type

show
    

Values must be of type <class ‘int’>

sqref
    

Values must be of type <class ‘openpyxl.worksheet.cell_range.MultiCellRange’>

tagname _ = 'scenarios'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.worksheet.scenario module
    * `InputCells`
      * `InputCells.deleted`
      * `InputCells.numFmtId`
      * `InputCells.r`
      * `InputCells.tagname`
      * `InputCells.undone`
      * `InputCells.val`
    * `Scenario`
      * `Scenario.comment`
      * `Scenario.count`
      * `Scenario.hidden`
      * `Scenario.inputCells`
      * `Scenario.locked`
      * `Scenario.name`
      * `Scenario.tagname`
      * `Scenario.user`
    * `ScenarioList`
      * `ScenarioList.append()`
      * `ScenarioList.current`
      * `ScenarioList.scenario`
      * `ScenarioList.show`
      * `ScenarioList.sqref`
      * `ScenarioList.tagname`



#### Previous topic

[openpyxl.worksheet.related module](openpyxl.worksheet.related.html "previous chapter")

#### Next topic

[openpyxl.worksheet.smart_tag module](openpyxl.worksheet.smart_tag.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.worksheet.scenario.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.worksheet.smart_tag.html "openpyxl.worksheet.smart_tag module") |
  * [previous](openpyxl.worksheet.related.html "openpyxl.worksheet.related module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.worksheet package](openpyxl.worksheet.html) »
  * [openpyxl.worksheet.scenario module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
