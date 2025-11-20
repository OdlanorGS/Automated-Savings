### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.comments.comments.html "openpyxl.comments.comments module") |
  * [previous](openpyxl.comments.author.html "openpyxl.comments.author module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.comments package](openpyxl.comments.html) »
  * [openpyxl.comments.comment_sheet module]()



# openpyxl.comments.comment_sheet module

_class _openpyxl.comments.comment_sheet.CommentRecord(_ref =''_, _authorId =0_, _guid =None_, _shapeId =0_, _text =None_, _commentPr =None_, _author =None_, _height =79_, _width =144_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentRecord)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

author
    

Values must be of type <class ‘str’>

authorId
    

Values must be of type <class ‘int’>

commentPr
    

Values must be of type <class ‘openpyxl.comments.comment_sheet.Properties’>

_property _content
    

Remove all inline formatting and stuff

_classmethod _from_cell(_cell_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentRecord.from_cell)
    

Class method to convert cell comment

guid
    

ref
    

Values must be of type <class ‘str’>

shapeId
    

Values must be of type <class ‘int’>

tagname _ = 'comment'_
    

text
    

Values must be of type <class ‘openpyxl.cell.text.Text’>

_class _openpyxl.comments.comment_sheet.CommentSheet(_authors =None_, _commentList =None_, _extLst =None_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentSheet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

authors
    

Values must be of type <class ‘openpyxl.comments.author.AuthorList’>

commentList
    

Wrap a sequence in an containing object

_property _comments
    

Return a dictionary of comments keyed by coord

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

_classmethod _from_comments(_comments_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentSheet.from_comments)
    

Create a comment sheet from a list of comments for a particular worksheet

mime_type _ = 'application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml'_
    

_property _path
    

Return path within the archive

tagname _ = 'comments'_
    

to_tree()[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentSheet.to_tree)
    

write_shapes(_vml =None_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#CommentSheet.write_shapes)
    

Create the VML for comments

_class _openpyxl.comments.comment_sheet.Properties(_locked =None_, _defaultSize =None_, __print =None_, _disabled =None_, _uiObject =None_, _autoFill =None_, _autoLine =None_, _altText =None_, _textHAlign =None_, _textVAlign =None_, _lockText =None_, _justLastX =None_, _autoScale =None_, _rowHidden =None_, _colHidden =None_, _anchor =None_)[[source]](../_modules/openpyxl/comments/comment_sheet.html#Properties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

altText
    

Values must be of type <class ‘str’>

autoFill
    

Values must be of type <class ‘bool’>

autoLine
    

Values must be of type <class ‘bool’>

autoScale
    

Values must be of type <class ‘bool’>

colHidden
    

Values must be of type <class ‘bool’>

defaultSize
    

Values must be of type <class ‘bool’>

disabled
    

Values must be of type <class ‘bool’>

justLastX
    

Values must be of type <class ‘bool’>

lockText
    

Values must be of type <class ‘bool’>

locked
    

Values must be of type <class ‘bool’>

rowHidden
    

Values must be of type <class ‘bool’>

textHAlign
    

Value must be one of {‘distributed’, ‘justify’, ‘center’, ‘left’, ‘right’}

textVAlign
    

Value must be one of {‘top’, ‘distributed’, ‘justify’, ‘center’, ‘bottom’}

uiObject
    

Values must be of type <class ‘bool’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.comments.comment_sheet module
    * `CommentRecord`
      * `CommentRecord.author`
      * `CommentRecord.authorId`
      * `CommentRecord.commentPr`
      * `CommentRecord.content`
      * `CommentRecord.from_cell()`
      * `CommentRecord.guid`
      * `CommentRecord.ref`
      * `CommentRecord.shapeId`
      * `CommentRecord.tagname`
      * `CommentRecord.text`
    * `CommentSheet`
      * `CommentSheet.authors`
      * `CommentSheet.commentList`
      * `CommentSheet.comments`
      * `CommentSheet.extLst`
      * `CommentSheet.from_comments()`
      * `CommentSheet.mime_type`
      * `CommentSheet.path`
      * `CommentSheet.tagname`
      * `CommentSheet.to_tree()`
      * `CommentSheet.write_shapes()`
    * `Properties`
      * `Properties.altText`
      * `Properties.autoFill`
      * `Properties.autoLine`
      * `Properties.autoScale`
      * `Properties.colHidden`
      * `Properties.defaultSize`
      * `Properties.disabled`
      * `Properties.justLastX`
      * `Properties.lockText`
      * `Properties.locked`
      * `Properties.rowHidden`
      * `Properties.textHAlign`
      * `Properties.textVAlign`
      * `Properties.uiObject`



#### Previous topic

[openpyxl.comments.author module](openpyxl.comments.author.html "previous chapter")

#### Next topic

[openpyxl.comments.comments module](openpyxl.comments.comments.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.comments.comment_sheet.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.comments.comments.html "openpyxl.comments.comments module") |
  * [previous](openpyxl.comments.author.html "openpyxl.comments.author module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.comments package](openpyxl.comments.html) »
  * [openpyxl.comments.comment_sheet module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
