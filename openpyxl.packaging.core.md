### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.custom.html "openpyxl.packaging.custom module") |
  * [previous](openpyxl.packaging.html "openpyxl.packaging package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.core module]()



# openpyxl.packaging.core module

_class _openpyxl.packaging.core.DocumentProperties(_category =None_, _contentStatus =None_, _keywords =None_, _lastModifiedBy =None_, _lastPrinted =None_, _revision =None_, _version =None_, _created =None_, _creator ='openpyxl'_, _description =None_, _identifier =None_, _language =None_, _modified =None_, _subject =None_, _title =None_)[[source]](../_modules/openpyxl/packaging/core.html#DocumentProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

High-level properties of the document. Defined in ECMA-376 Par2 Annex D

category
    

Values must be of type <class ‘str’>

contentStatus
    

Values must be of type <class ‘str’>

created
    

Values must be of type <class ‘datetime.datetime’>

creator
    

Values must be of type <class ‘str’>

description
    

Values must be of type <class ‘str’>

identifier
    

Values must be of type <class ‘str’>

keywords
    

Values must be of type <class ‘str’>

language
    

Values must be of type <class ‘str’>

lastModifiedBy
    

Values must be of type <class ‘str’>

lastPrinted
    

Values must be of type <class ‘datetime.datetime’>

last_modified_by
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

modified
    

Values must be of type <class ‘datetime.datetime’>

namespace _ = 'http://schemas.openxmlformats.org/package/2006/metadata/core-properties'_
    

revision
    

Values must be of type <class ‘str’>

subject
    

Values must be of type <class ‘str’>

tagname _ = 'coreProperties'_
    

title
    

Values must be of type <class ‘str’>

version
    

Values must be of type <class ‘str’>

_class _openpyxl.packaging.core.NestedDateTime(_* args_, _** kw_)[[source]](../_modules/openpyxl/packaging/core.html#NestedDateTime)
    

Bases: [`DateTime`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.DateTime "openpyxl.descriptors.base.DateTime"), [`NestedText`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText "openpyxl.descriptors.nested.NestedText")

expected_type
    

alias of `datetime`

to_tree(_tagname =None_, _value =None_, _namespace =None_)[[source]](../_modules/openpyxl/packaging/core.html#NestedDateTime.to_tree)
    

_class _openpyxl.packaging.core.QualifiedDateTime(_* args_, _** kw_)[[source]](../_modules/openpyxl/packaging/core.html#QualifiedDateTime)
    

Bases: `NestedDateTime`

In certain situations Excel will complain if the additional type attribute isn’t set

to_tree(_tagname =None_, _value =None_, _namespace =None_)[[source]](../_modules/openpyxl/packaging/core.html#QualifiedDateTime.to_tree)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.core module
    * `DocumentProperties`
      * `DocumentProperties.category`
      * `DocumentProperties.contentStatus`
      * `DocumentProperties.created`
      * `DocumentProperties.creator`
      * `DocumentProperties.description`
      * `DocumentProperties.identifier`
      * `DocumentProperties.keywords`
      * `DocumentProperties.language`
      * `DocumentProperties.lastModifiedBy`
      * `DocumentProperties.lastPrinted`
      * `DocumentProperties.last_modified_by`
      * `DocumentProperties.modified`
      * `DocumentProperties.namespace`
      * `DocumentProperties.revision`
      * `DocumentProperties.subject`
      * `DocumentProperties.tagname`
      * `DocumentProperties.title`
      * `DocumentProperties.version`
    * `NestedDateTime`
      * `NestedDateTime.expected_type`
      * `NestedDateTime.to_tree()`
    * `QualifiedDateTime`
      * `QualifiedDateTime.to_tree()`



#### Previous topic

[openpyxl.packaging package](openpyxl.packaging.html "previous chapter")

#### Next topic

[openpyxl.packaging.custom module](openpyxl.packaging.custom.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.core.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.custom.html "openpyxl.packaging.custom module") |
  * [previous](openpyxl.packaging.html "openpyxl.packaging package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.core module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
