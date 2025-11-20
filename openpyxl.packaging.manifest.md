### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.relationship.html "openpyxl.packaging.relationship module") |
  * [previous](openpyxl.packaging.interface.html "openpyxl.packaging.interface module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.manifest module]()



# openpyxl.packaging.manifest module

File manifest

_class _openpyxl.packaging.manifest.FileExtension(_Extension_ , _ContentType_)[[source]](../_modules/openpyxl/packaging/manifest.html#FileExtension)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ContentType
    

Values must be of type <class ‘str’>

Extension
    

Values must be of type <class ‘str’>

tagname _ = 'Default'_
    

_class _openpyxl.packaging.manifest.Manifest(_Default =()_, _Override =()_)[[source]](../_modules/openpyxl/packaging/manifest.html#Manifest)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

Default
    

A sequence (list or tuple) that may only contain objects of the declared type

Override
    

A sequence (list or tuple) that may only contain objects of the declared type

append(_obj_)[[source]](../_modules/openpyxl/packaging/manifest.html#Manifest.append)
    

Add content object to the package manifest # needs a contract…

_property _extensions
    

Map content types to file extensions Skip parts without extensions

_property _filenames
    

find(_content_type_)[[source]](../_modules/openpyxl/packaging/manifest.html#Manifest.find)
    

Find specific content-type

findall(_content_type_)[[source]](../_modules/openpyxl/packaging/manifest.html#Manifest.findall)
    

Find all elements of a specific content-type

path _ = '[Content_Types].xml'_
    

tagname _ = 'Types'_
    

to_tree()[[source]](../_modules/openpyxl/packaging/manifest.html#Manifest.to_tree)
    

Custom serialisation method to allow setting a default namespace

_class _openpyxl.packaging.manifest.Override(_PartName_ , _ContentType_)[[source]](../_modules/openpyxl/packaging/manifest.html#Override)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ContentType
    

Values must be of type <class ‘str’>

PartName
    

Values must be of type <class ‘str’>

tagname _ = 'Override'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.manifest module
    * `FileExtension`
      * `FileExtension.ContentType`
      * `FileExtension.Extension`
      * `FileExtension.tagname`
    * `Manifest`
      * `Manifest.Default`
      * `Manifest.Override`
      * `Manifest.append()`
      * `Manifest.extensions`
      * `Manifest.filenames`
      * `Manifest.find()`
      * `Manifest.findall()`
      * `Manifest.path`
      * `Manifest.tagname`
      * `Manifest.to_tree()`
    * `Override`
      * `Override.ContentType`
      * `Override.PartName`
      * `Override.tagname`



#### Previous topic

[openpyxl.packaging.interface module](openpyxl.packaging.interface.html "previous chapter")

#### Next topic

[openpyxl.packaging.relationship module](openpyxl.packaging.relationship.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.manifest.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.relationship.html "openpyxl.packaging.relationship module") |
  * [previous](openpyxl.packaging.interface.html "openpyxl.packaging.interface module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.manifest module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
