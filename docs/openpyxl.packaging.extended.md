### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.interface.html "openpyxl.packaging.interface module") |
  * [previous](openpyxl.packaging.custom.html "openpyxl.packaging.custom module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.extended module]()



# openpyxl.packaging.extended module

_class _openpyxl.packaging.extended.DigSigBlob[[source]](../_modules/openpyxl/packaging/extended.html#DigSigBlob)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.packaging.extended.ExtendedProperties(_Template =None_, _Manager =None_, _Company =None_, _Pages =None_, _Words =None_, _Characters =None_, _PresentationFormat =None_, _Lines =None_, _Paragraphs =None_, _Slides =None_, _Notes =None_, _TotalTime =None_, _HiddenSlides =None_, _MMClips =None_, _ScaleCrop =None_, _HeadingPairs =None_, _TitlesOfParts =None_, _LinksUpToDate =None_, _CharactersWithSpaces =None_, _SharedDoc =None_, _HyperlinkBase =None_, _HLinks =None_, _HyperlinksChanged =None_, _DigSig =None_, _Application ='Microsoft Excel'_, _AppVersion =None_, _DocSecurity =None_)[[source]](../_modules/openpyxl/packaging/extended.html#ExtendedProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

See 22.2

Most of this is irrelevant

AppVersion
    

Values must be of type <class ‘str’>

Application
    

Values must be of type <class ‘str’>

Characters
    

Values must be of type <class ‘int’>

CharactersWithSpaces
    

Values must be of type <class ‘int’>

Company
    

Values must be of type <class ‘str’>

DigSig
    

Values must be of type <class ‘openpyxl.packaging.extended.DigSigBlob’>

DocSecurity
    

Values must be of type <class ‘int’>

HLinks
    

Values must be of type <class ‘openpyxl.packaging.extended.VectorVariant’>

HeadingPairs
    

Values must be of type <class ‘openpyxl.packaging.extended.VectorVariant’>

HiddenSlides
    

Values must be of type <class ‘int’>

HyperlinkBase
    

Values must be of type <class ‘str’>

HyperlinksChanged
    

Values must be of type <class ‘bool’>

Lines
    

Values must be of type <class ‘int’>

LinksUpToDate
    

Values must be of type <class ‘bool’>

MMClips
    

Values must be of type <class ‘int’>

Manager
    

Values must be of type <class ‘str’>

Notes
    

Values must be of type <class ‘int’>

Pages
    

Values must be of type <class ‘int’>

Paragraphs
    

Values must be of type <class ‘int’>

PresentationFormat
    

Values must be of type <class ‘str’>

ScaleCrop
    

Values must be of type <class ‘bool’>

SharedDoc
    

Values must be of type <class ‘bool’>

Slides
    

Values must be of type <class ‘int’>

Template
    

Values must be of type <class ‘str’>

TitlesOfParts
    

Values must be of type <class ‘openpyxl.packaging.extended.VectorLpstr’>

TotalTime
    

Values must be of type <class ‘int’>

Words
    

Values must be of type <class ‘int’>

tagname _ = 'Properties'_
    

to_tree()[[source]](../_modules/openpyxl/packaging/extended.html#ExtendedProperties.to_tree)
    

_class _openpyxl.packaging.extended.VectorLpstr[[source]](../_modules/openpyxl/packaging/extended.html#VectorLpstr)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.packaging.extended.VectorVariant[[source]](../_modules/openpyxl/packaging/extended.html#VectorVariant)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

openpyxl.packaging.extended.get_version()[[source]](../_modules/openpyxl/packaging/extended.html#get_version)
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging.extended module
    * `DigSigBlob`
    * `ExtendedProperties`
      * `ExtendedProperties.AppVersion`
      * `ExtendedProperties.Application`
      * `ExtendedProperties.Characters`
      * `ExtendedProperties.CharactersWithSpaces`
      * `ExtendedProperties.Company`
      * `ExtendedProperties.DigSig`
      * `ExtendedProperties.DocSecurity`
      * `ExtendedProperties.HLinks`
      * `ExtendedProperties.HeadingPairs`
      * `ExtendedProperties.HiddenSlides`
      * `ExtendedProperties.HyperlinkBase`
      * `ExtendedProperties.HyperlinksChanged`
      * `ExtendedProperties.Lines`
      * `ExtendedProperties.LinksUpToDate`
      * `ExtendedProperties.MMClips`
      * `ExtendedProperties.Manager`
      * `ExtendedProperties.Notes`
      * `ExtendedProperties.Pages`
      * `ExtendedProperties.Paragraphs`
      * `ExtendedProperties.PresentationFormat`
      * `ExtendedProperties.ScaleCrop`
      * `ExtendedProperties.SharedDoc`
      * `ExtendedProperties.Slides`
      * `ExtendedProperties.Template`
      * `ExtendedProperties.TitlesOfParts`
      * `ExtendedProperties.TotalTime`
      * `ExtendedProperties.Words`
      * `ExtendedProperties.tagname`
      * `ExtendedProperties.to_tree()`
    * `VectorLpstr`
    * `VectorVariant`
    * `get_version()`



#### Previous topic

[openpyxl.packaging.custom module](openpyxl.packaging.custom.html "previous chapter")

#### Next topic

[openpyxl.packaging.interface module](openpyxl.packaging.interface.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.extended.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.interface.html "openpyxl.packaging.interface module") |
  * [previous](openpyxl.packaging.custom.html "openpyxl.packaging.custom module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package](openpyxl.packaging.html) »
  * [openpyxl.packaging.extended module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
