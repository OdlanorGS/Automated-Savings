### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.base.html "openpyxl.descriptors.base module") |
  * [previous](openpyxl.comments.shape_writer.html "openpyxl.comments.shape_writer module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package]()



# openpyxl.descriptors package

_class _openpyxl.descriptors.MetaSerialisable(_clsname_ , _bases_ , _methods_)[[source]](../_modules/openpyxl/descriptors.html#MetaSerialisable)
    

Bases: `type`

_class _openpyxl.descriptors.MetaStrict(_clsname_ , _bases_ , _methods_)[[source]](../_modules/openpyxl/descriptors.html#MetaStrict)
    

Bases: `type`

_class _openpyxl.descriptors.Strict[[source]](../_modules/openpyxl/descriptors.html#Strict)
    

Bases: `object`

## Submodules

  * [openpyxl.descriptors.base module](openpyxl.descriptors.base.html)
    * [`ASCII`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.ASCII)
      * [`ASCII.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.ASCII.expected_type)
    * [`Alias`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Alias)
    * [`Bool`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Bool)
      * [`Bool.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Bool.expected_type)
    * [`Convertible`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Convertible)
    * [`DateTime`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.DateTime)
      * [`DateTime.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.DateTime.expected_type)
    * [`Default`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Default)
    * [`Descriptor`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Descriptor)
    * [`Float`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Float)
      * [`Float.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Float.expected_type)
    * [`Integer`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Integer)
      * [`Integer.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Integer.expected_type)
    * [`Length`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Length)
    * [`MatchPattern`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern)
      * [`MatchPattern.allow_none`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MatchPattern.allow_none)
    * [`Max`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Max)
      * [`Max.allow_none`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Max.allow_none)
      * [`Max.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Max.expected_type)
    * [`Min`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Min)
      * [`Min.allow_none`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Min.allow_none)
      * [`Min.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Min.expected_type)
    * [`MinMax`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.MinMax)
    * [`NoneSet`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.NoneSet)
    * [`Set`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Set)
    * [`String`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String)
      * [`String.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.String.expected_type)
    * [`Text`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Text)
    * [`Tuple`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Tuple)
      * [`Tuple.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Tuple.expected_type)
    * [`Typed`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed)
      * [`Typed.allow_none`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed.allow_none)
      * [`Typed.expected_type`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed.expected_type)
      * [`Typed.nested`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed.nested)
  * [openpyxl.descriptors.container module](openpyxl.descriptors.container.html)
    * [`ElementList`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList)
      * [`ElementList.append()`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList.append)
      * [`ElementList.expected_type`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList.expected_type)
      * [`ElementList.from_tree()`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList.from_tree)
      * [`ElementList.tagname`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList.tagname)
      * [`ElementList.to_tree()`](openpyxl.descriptors.container.html#openpyxl.descriptors.container.ElementList.to_tree)
  * [openpyxl.descriptors.excel module](openpyxl.descriptors.excel.html)
    * [`Base64Binary`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Base64Binary)
      * [`Base64Binary.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Base64Binary.pattern)
    * [`CellRange`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.CellRange)
      * [`CellRange.allow_none`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.CellRange.allow_none)
      * [`CellRange.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.CellRange.pattern)
    * [`Extension`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Extension)
      * [`Extension.uri`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Extension.uri)
    * [`ExtensionList`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.ExtensionList)
      * [`ExtensionList.ext`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.ExtensionList.ext)
    * [`Guid`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Guid)
      * [`Guid.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Guid.pattern)
    * [`HexBinary`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.HexBinary)
      * [`HexBinary.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.HexBinary.pattern)
    * [`Percentage`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Percentage)
      * [`Percentage.max`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Percentage.max)
      * [`Percentage.min`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Percentage.min)
      * [`Percentage.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Percentage.pattern)
    * [`Relation`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Relation)
      * [`Relation.allow_none`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Relation.allow_none)
      * [`Relation.namespace`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.Relation.namespace)
    * [`TextPoint`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.TextPoint)
      * [`TextPoint.expected_type`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.TextPoint.expected_type)
      * [`TextPoint.max`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.TextPoint.max)
      * [`TextPoint.min`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.TextPoint.min)
    * [`UniversalMeasure`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.UniversalMeasure)
      * [`UniversalMeasure.pattern`](openpyxl.descriptors.excel.html#openpyxl.descriptors.excel.UniversalMeasure.pattern)
  * [openpyxl.descriptors.namespace module](openpyxl.descriptors.namespace.html)
    * [`namespaced()`](openpyxl.descriptors.namespace.html#openpyxl.descriptors.namespace.namespaced)
  * [openpyxl.descriptors.nested module](openpyxl.descriptors.nested.html)
    * [`EmptyTag`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.EmptyTag)
      * [`EmptyTag.from_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.EmptyTag.from_tree)
      * [`EmptyTag.to_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.EmptyTag.to_tree)
    * [`Nested`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.Nested)
      * [`Nested.attribute`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.Nested.attribute)
      * [`Nested.from_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.Nested.from_tree)
      * [`Nested.nested`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.Nested.nested)
      * [`Nested.to_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.Nested.to_tree)
    * [`NestedBool`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedBool)
      * [`NestedBool.from_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedBool.from_tree)
    * [`NestedFloat`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedFloat)
    * [`NestedInteger`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedInteger)
    * [`NestedMinMax`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedMinMax)
    * [`NestedNoneSet`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedNoneSet)
    * [`NestedSet`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedSet)
    * [`NestedString`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedString)
    * [`NestedText`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText)
      * [`NestedText.from_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText.from_tree)
      * [`NestedText.to_tree()`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedText.to_tree)
    * [`NestedValue`](openpyxl.descriptors.nested.html#openpyxl.descriptors.nested.NestedValue)
  * [openpyxl.descriptors.sequence module](openpyxl.descriptors.sequence.html)
    * [`MultiSequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.MultiSequence)
      * [`MultiSequence.to_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.MultiSequence.to_tree)
    * [`MultiSequencePart`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.MultiSequencePart)
    * [`NestedSequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.NestedSequence)
      * [`NestedSequence.count`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.NestedSequence.count)
      * [`NestedSequence.from_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.NestedSequence.from_tree)
      * [`NestedSequence.to_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.NestedSequence.to_tree)
    * [`Sequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence)
      * [`Sequence.container`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.container)
      * [`Sequence.expected_type`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.expected_type)
      * [`Sequence.idx_base`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.idx_base)
      * [`Sequence.seq_types`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.seq_types)
      * [`Sequence.to_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.to_tree)
      * [`Sequence.unique`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.Sequence.unique)
    * [`UniqueSequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.UniqueSequence)
      * [`UniqueSequence.container`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.UniqueSequence.container)
      * [`UniqueSequence.seq_types`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.UniqueSequence.seq_types)
    * [`ValueSequence`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.ValueSequence)
      * [`ValueSequence.attribute`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.ValueSequence.attribute)
      * [`ValueSequence.from_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.ValueSequence.from_tree)
      * [`ValueSequence.to_tree()`](openpyxl.descriptors.sequence.html#openpyxl.descriptors.sequence.ValueSequence.to_tree)
  * [openpyxl.descriptors.serialisable module](openpyxl.descriptors.serialisable.html)
    * [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable)
      * [`Serialisable.from_tree()`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable.from_tree)
      * [`Serialisable.idx_base`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable.idx_base)
      * [`Serialisable.namespace`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable.namespace)
      * [`Serialisable.tagname`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable.tagname)
      * [`Serialisable.to_tree()`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable.to_tree)



[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.descriptors package
    * `MetaSerialisable`
    * `MetaStrict`
    * `Strict`
    * Submodules



#### Previous topic

[openpyxl.comments.shape_writer module](openpyxl.comments.shape_writer.html "previous chapter")

#### Next topic

[openpyxl.descriptors.base module](openpyxl.descriptors.base.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.descriptors.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.descriptors.base.html "openpyxl.descriptors.base module") |
  * [previous](openpyxl.comments.shape_writer.html "openpyxl.comments.shape_writer module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.descriptors package]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
