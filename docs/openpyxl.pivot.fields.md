### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.record.html "openpyxl.pivot.record module") |
  * [previous](openpyxl.pivot.cache.html "openpyxl.pivot.cache module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.fields module]()



# openpyxl.pivot.fields module

_class _openpyxl.pivot.fields.Boolean(_x =()_, _v =None_, _u =None_, _f =None_, _c =None_, _cp =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Boolean)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

tagname _ = 'b'_
    

u
    

Values must be of type <class ‘bool’>

v
    

Values must be of type <class ‘bool’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.DateTimeField(_x =()_, _v =None_, _u =None_, _f =None_, _c =None_, _cp =None_)[[source]](../_modules/openpyxl/pivot/fields.html#DateTimeField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

tagname _ = 'd'_
    

u
    

Values must be of type <class ‘bool’>

v
    

Values must be of type <class ‘datetime.datetime’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.Error(_tpls =None_, _x =()_, _v =None_, _u =None_, _f =None_, _c =None_, _cp =None_, __in =None_, _bc =None_, _fc =None_, _i =None_, _un =None_, _st =None_, _b =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Error)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘bool’>

bc
    

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

fc
    

i
    

Values must be of type <class ‘bool’>

st
    

Values must be of type <class ‘bool’>

tagname _ = 'e'_
    

tpls
    

Values must be of type <class ‘openpyxl.pivot.fields.TupleList’>

u
    

Values must be of type <class ‘bool’>

un
    

Values must be of type <class ‘bool’>

v
    

Values must be of type <class ‘str’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.Index(_v =0_)[[source]](../_modules/openpyxl/pivot/fields.html#Index)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'x'_
    

v
    

Values must be of type <class ‘int’>

_class _openpyxl.pivot.fields.Missing(_tpls =()_, _x =()_, _u =None_, _f =None_, _c =None_, _cp =None_, __in =None_, _bc =None_, _fc =None_, _i =None_, _un =None_, _st =None_, _b =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Missing)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘bool’>

bc
    

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

fc
    

i
    

Values must be of type <class ‘bool’>

st
    

Values must be of type <class ‘bool’>

tagname _ = 'm'_
    

tpls
    

A sequence (list or tuple) that may only contain objects of the declared type

u
    

Values must be of type <class ‘bool’>

un
    

Values must be of type <class ‘bool’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.Number(_tpls =()_, _x =()_, _v =None_, _u =None_, _f =None_, _c =None_, _cp =None_, __in =None_, _bc =None_, _fc =None_, _i =None_, _un =None_, _st =None_, _b =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Number)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘bool’>

bc
    

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

fc
    

i
    

Values must be of type <class ‘bool’>

st
    

Values must be of type <class ‘bool’>

tagname _ = 'n'_
    

tpls
    

A sequence (list or tuple) that may only contain objects of the declared type

u
    

Values must be of type <class ‘bool’>

un
    

Values must be of type <class ‘bool’>

v
    

Values must be of type <class ‘float’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.Text(_tpls =()_, _x =()_, _v =None_, _u =None_, _f =None_, _c =None_, _cp =None_, __in =None_, _bc =None_, _fc =None_, _i =None_, _un =None_, _st =None_, _b =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Text)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘bool’>

bc
    

c
    

Values must be of type <class ‘str’>

cp
    

Values must be of type <class ‘int’>

f
    

Values must be of type <class ‘bool’>

fc
    

i
    

Values must be of type <class ‘bool’>

st
    

Values must be of type <class ‘bool’>

tagname _ = 's'_
    

tpls
    

A sequence (list or tuple) that may only contain objects of the declared type

u
    

Values must be of type <class ‘bool’>

un
    

Values must be of type <class ‘bool’>

v
    

Values must be of type <class ‘str’>

x
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.pivot.fields.Tuple(_fld =None_, _hier =None_, _item =None_)[[source]](../_modules/openpyxl/pivot/fields.html#Tuple)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fld
    

Values must be of type <class ‘int’>

hier
    

Values must be of type <class ‘int’>

item
    

Values must be of type <class ‘int’>

tagname _ = 'tpl'_
    

_class _openpyxl.pivot.fields.TupleList(_c =None_, _tpl =None_)[[source]](../_modules/openpyxl/pivot/fields.html#TupleList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

c
    

Values must be of type <class ‘int’>

tagname _ = 'tpls'_
    

tpl
    

Values must be of type <class ‘openpyxl.pivot.fields.Tuple’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.pivot.fields module
    * `Boolean`
      * `Boolean.c`
      * `Boolean.cp`
      * `Boolean.f`
      * `Boolean.tagname`
      * `Boolean.u`
      * `Boolean.v`
      * `Boolean.x`
    * `DateTimeField`
      * `DateTimeField.c`
      * `DateTimeField.cp`
      * `DateTimeField.f`
      * `DateTimeField.tagname`
      * `DateTimeField.u`
      * `DateTimeField.v`
      * `DateTimeField.x`
    * `Error`
      * `Error.b`
      * `Error.bc`
      * `Error.c`
      * `Error.cp`
      * `Error.f`
      * `Error.fc`
      * `Error.i`
      * `Error.st`
      * `Error.tagname`
      * `Error.tpls`
      * `Error.u`
      * `Error.un`
      * `Error.v`
      * `Error.x`
    * `Index`
      * `Index.tagname`
      * `Index.v`
    * `Missing`
      * `Missing.b`
      * `Missing.bc`
      * `Missing.c`
      * `Missing.cp`
      * `Missing.f`
      * `Missing.fc`
      * `Missing.i`
      * `Missing.st`
      * `Missing.tagname`
      * `Missing.tpls`
      * `Missing.u`
      * `Missing.un`
      * `Missing.x`
    * `Number`
      * `Number.b`
      * `Number.bc`
      * `Number.c`
      * `Number.cp`
      * `Number.f`
      * `Number.fc`
      * `Number.i`
      * `Number.st`
      * `Number.tagname`
      * `Number.tpls`
      * `Number.u`
      * `Number.un`
      * `Number.v`
      * `Number.x`
    * `Text`
      * `Text.b`
      * `Text.bc`
      * `Text.c`
      * `Text.cp`
      * `Text.f`
      * `Text.fc`
      * `Text.i`
      * `Text.st`
      * `Text.tagname`
      * `Text.tpls`
      * `Text.u`
      * `Text.un`
      * `Text.v`
      * `Text.x`
    * `Tuple`
      * `Tuple.fld`
      * `Tuple.hier`
      * `Tuple.item`
      * `Tuple.tagname`
    * `TupleList`
      * `TupleList.c`
      * `TupleList.tagname`
      * `TupleList.tpl`



#### Previous topic

[openpyxl.pivot.cache module](openpyxl.pivot.cache.html "previous chapter")

#### Next topic

[openpyxl.pivot.record module](openpyxl.pivot.record.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.pivot.fields.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.pivot.record.html "openpyxl.pivot.record module") |
  * [previous](openpyxl.pivot.cache.html "openpyxl.pivot.cache module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.pivot package](openpyxl.pivot.html) »
  * [openpyxl.pivot.fields module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
