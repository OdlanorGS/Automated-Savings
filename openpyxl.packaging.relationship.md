### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.workbook.html "openpyxl.packaging.workbook module") |
  * [previous](openpyxl.packaging.manifest.html "openpyxl.packaging.manifest module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.relationship module]()



# openpyxl.packaging.relationship module

_class _openpyxl.packaging.relationship.Relationship(_Id =None_, _Type =None_, _type =None_, _Target =None_, _TargetMode =None_)[[source]](../_modules/openpyxl/packaging/relationship.html#Relationship)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Represents many kinds of relationships.

Id
    

Values must be of type <class ‘str’>

Target
    

Values must be of type <class ‘str’>

TargetMode
    

Values must be of type <class ‘str’>

Type
    

Values must be of type <class ‘str’>

id
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'Relationship'_
    

target
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.packaging.relationship.RelationshipList(_iterable =()_, _/_)[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList)
    

Bases: [`ElementList`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList "openpyxl.descriptors.container.ElementList")

append(_value_)[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList.append)
    

Append object to the end of the list.

expected_type
    

alias of `Relationship`

find(_content_type_)[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList.find)
    

Find relationships by content-type NB. these content-types namespaced objects and different to the MIME-types in the package manifest :-(

get(_key_)[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList.get)
    

tagname _ = 'Relationships'_
    

to_dict()[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList.to_dict)
    

Return a dictionary of relations keyed by id

to_tree()[[source]](../_modules/openpyxl/packaging/relationship.html#RelationshipList.to_tree)
    

openpyxl.packaging.relationship.get_dependents(_archive_ , _filename_)[[source]](../_modules/openpyxl/packaging/relationship.html#get_dependents)
    

Normalise dependency file paths to absolute ones

Relative paths are relative to parent object

openpyxl.packaging.relationship.get_rel(_archive_ , _deps_ , _id =None_, _cls =None_)[[source]](../_modules/openpyxl/packaging/relationship.html#get_rel)
    

Get related object based on id or rel_type

openpyxl.packaging.relationship.get_rels_path(_path_)[[source]](../_modules/openpyxl/packaging/relationship.html#get_rels_path)
    

Convert relative path to absolutes that can be loaded from a zip archive. The path to be passed in is that of containing object (workbook, worksheet, etc.)

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.relationship module
    * `Relationship`
      * `Relationship.Id`
      * `Relationship.Target`
      * `Relationship.TargetMode`
      * `Relationship.Type`
      * `Relationship.id`
      * `Relationship.tagname`
      * `Relationship.target`
    * `RelationshipList`
      * `RelationshipList.append()`
      * `RelationshipList.expected_type`
      * `RelationshipList.find()`
      * `RelationshipList.get()`
      * `RelationshipList.tagname`
      * `RelationshipList.to_dict()`
      * `RelationshipList.to_tree()`
    * `get_dependents()`
    * `get_rel()`
    * `get_rels_path()`



#### Previous topic

[openpyxl.packaging.manifest module](openpyxl.packaging.manifest.html "previous chapter")

#### Next topic

[openpyxl.packaging.workbook module](openpyxl.packaging.workbook.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.relationship.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.workbook.html "openpyxl.packaging.workbook module") |
  * [previous](openpyxl.packaging.manifest.html "openpyxl.packaging.manifest module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.relationship module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
