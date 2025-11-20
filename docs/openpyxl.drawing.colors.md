### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.connector.html "openpyxl.drawing.connector module") |
  * [previous](openpyxl.drawing.html "openpyxl.drawing package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.colors module]()



# openpyxl.drawing.colors module

_class _openpyxl.drawing.colors.ColorChoice(_scrgbClr =None_, _srgbClr =None_, _hslClr =None_, _sysClr =None_, _schemeClr =None_, _prstClr =None_)[[source]](../_modules/openpyxl/drawing/colors.html#ColorChoice)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

RGB
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

RGBPercent
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

prstClr
    

Value must be one of {‘ltGoldenrodYellow’, ‘darkSlateBlue’, ‘fuchsia’, ‘ltGrey’, ‘medTurquoise’, ‘moccasin’, ‘lavenderBlush’, ‘mediumSlateBlue’, ‘gold’, ‘paleVioletRed’, ‘darkGoldenrod’, ‘darkSlateGray’, ‘lightGrey’, ‘mediumBlue’, ‘chocolate’, ‘yellow’, ‘lightSkyBlue’, ‘darkGrey’, ‘lightSlateGrey’, ‘tomato’, ‘turquoise’, ‘darkSalmon’, ‘mediumTurquoise’, ‘mediumSpringGreen’, ‘paleGreen’, ‘lightGreen’, ‘darkGreen’, ‘bisque’, ‘green’, ‘maroon’, ‘hotPink’, ‘ltSeaGreen’, ‘darkBlue’, ‘mediumVioletRed’, ‘dkGreen’, ‘plum’, ‘darkGray’, ‘medSpringGreen’, ‘wheat’, ‘red’, ‘aquamarine’, ‘dkGrey’, ‘whiteSmoke’, ‘yellowGreen’, ‘ltSlateGray’, ‘medSlateBlue’, ‘dkSlateGrey’, ‘ltBlue’, ‘lightCoral’, ‘steelBlue’, ‘paleTurquoise’, ‘pink’, ‘greenYellow’, ‘darkSlateGrey’, ‘mistyRose’, ‘crimson’, ‘darkKhaki’, ‘ltGreen’, ‘ltSlateGrey’, ‘blanchedAlmond’, ‘magenta’, ‘orange’, ‘lightGoldenrodYellow’, ‘dkKhaki’, ‘cornflowerBlue’, ‘coral’, ‘limeGreen’, ‘mediumPurple’, ‘firebrick’, ‘ltCoral’, ‘ltSkyBlue’, ‘mintCream’, ‘chartreuse’, ‘medBlue’, ‘ltPink’, ‘snow’, ‘dkSlateGray’, ‘ltCyan’, ‘deepSkyBlue’, ‘thistle’, ‘darkSeaGreen’, ‘tan’, ‘lightPink’, ‘paleGoldenrod’, ‘rosyBrown’, ‘lightSalmon’, ‘lightGray’, ‘dkCyan’, ‘dkOrange’, ‘mediumSeaGreen’, ‘lightCyan’, ‘orangeRed’, ‘mediumAquamarine’, ‘aqua’, ‘darkMagenta’, ‘ghostWhite’, ‘cyan’, ‘dkSalmon’, ‘lightSeaGreen’, ‘brown’, ‘skyBlue’, ‘ltYellow’, ‘dkSeaGreen’, ‘darkRed’, ‘midnightBlue’, ‘orchid’, ‘oldLace’, ‘violet’, ‘dkOrchid’, ‘dkBlue’, ‘darkCyan’, ‘salmon’, ‘navajoWhite’, ‘medOrchid’, ‘oliveDrab’, ‘dimGrey’, ‘darkOliveGreen’, ‘mediumOrchid’, ‘honeydew’, ‘linen’, ‘peachPuff’, ‘springGreen’, ‘medVioletRed’, ‘cornsilk’, ‘papayaWhip’, ‘forestGreen’, ‘dkSlateBlue’, ‘lightYellow’, ‘purple’, ‘teal’, ‘white’, ‘dkRed’, ‘medSeaGreen’, ‘seaGreen’, ‘seaShell’, ‘gray’, ‘dkViolet’, ‘navy’, ‘lawnGreen’, ‘slateBlue’, ‘dimGray’, ‘dodgerBlue’, ‘lightBlue’, ‘dkMagenta’, ‘royalBlue’, ‘floralWhite’, ‘powderBlue’, ‘grey’, ‘aliceBlue’, ‘silver’, ‘gainsboro’, ‘dkOliveGreen’, ‘indigo’, ‘lightSteelBlue’, ‘khaki’, ‘ltSteelBlue’, ‘cadetBlue’, ‘black’, ‘ltSalmon’, ‘darkOrchid’, ‘saddleBrown’, ‘goldenrod’, ‘darkViolet’, ‘lightSlateGray’, ‘darkTurquoise’, ‘peru’, ‘beige’, ‘ivory’, ‘medPurple’, ‘slateGrey’, ‘olive’, ‘antiqueWhite’, ‘blueViolet’, ‘blue’, ‘medAquamarine’, ‘ltGray’, ‘azure’, ‘dkGoldenrod’, ‘darkOrange’, ‘indianRed’, ‘dkGray’, ‘sienna’, ‘slateGray’, ‘lime’, ‘dkTurquoise’, ‘sandyBrown’, ‘lemonChiffon’, ‘deepPink’, ‘burlyWood’, ‘lavender’}

schemeClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SchemeColor’>

scrgbClr
    

Values must be of type <class ‘openpyxl.drawing.colors.RGBPercent’>

srgbClr
    

Values must be of type <class ‘str’>

sysClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SystemColor’>

tagname _ = 'colorChoice'_
    

_class _openpyxl.drawing.colors.ColorChoiceDescriptor(_* args_, _** kw_)[[source]](../_modules/openpyxl/drawing/colors.html#ColorChoiceDescriptor)
    

Bases: [`Typed`](openpyxl.descriptors.base.html#openpyxl.descriptors.base.Typed "openpyxl.descriptors.base.Typed")

Objects can choose from 7 different kinds of color system. Assume RGBHex if a string is passed in.

allow_none _ = True_
    

expected_type
    

alias of `ColorChoice`

_class _openpyxl.drawing.colors.ColorMapping(_bg1 ='lt1'_, _tx1 ='dk1'_, _bg2 ='lt2'_, _tx2 ='dk2'_, _accent1 ='accent1'_, _accent2 ='accent2'_, _accent3 ='accent3'_, _accent4 ='accent4'_, _accent5 ='accent5'_, _accent6 ='accent6'_, _hlink ='hlink'_, _folHlink ='folHlink'_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/colors.html#ColorMapping)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

accent1
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

accent2
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

accent3
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

accent4
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

accent5
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

accent6
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

bg1
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

bg2
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

folHlink
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

hlink
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

tagname _ = 'clrMapOvr'_
    

tx1
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

tx2
    

Value must be one of {‘folHlink’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘lt1’, ‘accent5’, ‘accent1’, ‘dk2’, ‘accent2’, ‘accent3’}

_class _openpyxl.drawing.colors.HSLColor(_hue =None_, _sat =None_, _lum =None_)[[source]](../_modules/openpyxl/drawing/colors.html#HSLColor)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

hue
    

Values must be of type <class ‘int’>

lum
    

Values must be of type <class ‘float’>

sat
    

Values must be of type <class ‘float’>

tagname _ = 'hslClr'_
    

_class _openpyxl.drawing.colors.RGBPercent(_r =None_, _g =None_, _b =None_)[[source]](../_modules/openpyxl/drawing/colors.html#RGBPercent)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘float’>

g
    

Values must be of type <class ‘float’>

r
    

Values must be of type <class ‘float’>

tagname _ = 'rgbClr'_
    

_class _openpyxl.drawing.colors.SchemeColor(_tint =None_, _shade =None_, _comp =None_, _inv =None_, _gray =None_, _alpha =None_, _alphaOff =None_, _alphaMod =None_, _hue =None_, _hueOff =None_, _hueMod =None_, _sat =None_, _satOff =None_, _satMod =None_, _lum =None_, _lumOff =None_, _lumMod =None_, _red =None_, _redOff =None_, _redMod =None_, _green =None_, _greenOff =None_, _greenMod =None_, _blue =None_, _blueOff =None_, _blueMod =None_, _gamma =None_, _invGamma =None_, _val =None_)[[source]](../_modules/openpyxl/drawing/colors.html#SchemeColor)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alpha
    

Values must be of type <class ‘int’>

alphaMod
    

Values must be of type <class ‘int’>

alphaOff
    

Values must be of type <class ‘int’>

blue
    

Values must be of type <class ‘int’>

blueMod
    

Values must be of type <class ‘int’>

blueOff
    

Values must be of type <class ‘int’>

comp
    

Values must be of type <class ‘bool’>

gamma
    

Values must be of type <class ‘bool’>

gray
    

Values must be of type <class ‘int’>

green
    

Values must be of type <class ‘int’>

greenMod
    

Values must be of type <class ‘int’>

greenOff
    

Values must be of type <class ‘int’>

hue
    

Values must be of type <class ‘int’>

hueMod
    

Values must be of type <class ‘int’>

hueOff
    

Values must be of type <class ‘int’>

inv
    

Values must be of type <class ‘int’>

invGamma
    

Values must be of type <class ‘bool’>

lum
    

Values must be of type <class ‘int’>

lumMod
    

Values must be of type <class ‘int’>

lumOff
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

red
    

Values must be of type <class ‘int’>

redMod
    

Values must be of type <class ‘int’>

redOff
    

Values must be of type <class ‘int’>

sat
    

Values must be of type <class ‘int’>

satMod
    

Values must be of type <class ‘int’>

satOff
    

Values must be of type <class ‘int’>

shade
    

Values must be of type <class ‘int’>

tagname _ = 'schemeClr'_
    

tint
    

Values must be of type <class ‘int’>

val
    

Value must be one of {‘bg1’, ‘folHlink’, ‘phClr’, ‘hlink’, ‘dk1’, ‘lt2’, ‘accent6’, ‘accent4’, ‘accent5’, ‘lt1’, ‘tx1’, ‘accent1’, ‘dk2’, ‘bg2’, ‘tx2’, ‘accent2’, ‘accent3’}

_class _openpyxl.drawing.colors.SystemColor(_val ='windowText'_, _lastClr =None_, _tint =None_, _shade =None_, _comp =None_, _inv =None_, _gray =None_, _alpha =None_, _alphaOff =None_, _alphaMod =None_, _hue =None_, _hueOff =None_, _hueMod =None_, _sat =None_, _satOff =None_, _satMod =None_, _lum =None_, _lumOff =None_, _lumMod =None_, _red =None_, _redOff =None_, _redMod =None_, _green =None_, _greenOff =None_, _greenMod =None_, _blue =None_, _blueOff =None_, _blueMod =None_, _gamma =None_, _invGamma =None_)[[source]](../_modules/openpyxl/drawing/colors.html#SystemColor)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alpha
    

Values must be of type <class ‘int’>

alphaMod
    

Values must be of type <class ‘int’>

alphaOff
    

Values must be of type <class ‘int’>

blue
    

Values must be of type <class ‘int’>

blueMod
    

Values must be of type <class ‘int’>

blueOff
    

Values must be of type <class ‘int’>

comp
    

Values must be of type <class ‘openpyxl.drawing.colors.Transform’>

gamma
    

Values must be of type <class ‘openpyxl.drawing.colors.Transform’>

gray
    

Values must be of type <class ‘openpyxl.drawing.colors.Transform’>

green
    

Values must be of type <class ‘int’>

greenMod
    

Values must be of type <class ‘int’>

greenOff
    

Values must be of type <class ‘int’>

hue
    

Values must be of type <class ‘int’>

hueMod
    

Values must be of type <class ‘int’>

hueOff
    

Values must be of type <class ‘int’>

inv
    

Values must be of type <class ‘openpyxl.drawing.colors.Transform’>

invGamma
    

Values must be of type <class ‘openpyxl.drawing.colors.Transform’>

lastClr
    

Values must be of type <class ‘str’>

lum
    

Values must be of type <class ‘int’>

lumMod
    

Values must be of type <class ‘int’>

lumOff
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

red
    

Values must be of type <class ‘int’>

redMod
    

Values must be of type <class ‘int’>

redOff
    

Values must be of type <class ‘int’>

sat
    

Values must be of type <class ‘int’>

satMod
    

Values must be of type <class ‘int’>

satOff
    

Values must be of type <class ‘int’>

shade
    

Values must be of type <class ‘int’>

tagname _ = 'sysClr'_
    

tint
    

Values must be of type <class ‘int’>

val
    

Value must be one of {‘3dDkShadow’, ‘gradientInactiveCaption’, ‘grayText’, ‘captionText’, ‘activeCaption’, ‘window’, ‘gradientActiveCaption’, ‘btnText’, ‘inactiveBorder’, ‘menu’, ‘btnFace’, ‘activeBorder’, ‘scrollBar’, ‘menuText’, ‘appWorkspace’, ‘3dLight’, ‘infoBk’, ‘inactiveCaption’, ‘infoText’, ‘background’, ‘btnShadow’, ‘highlight’, ‘hotLight’, ‘menuBar’, ‘highlightText’, ‘windowFrame’, ‘btnHighlight’, ‘menuHighlight’, ‘inactiveCaptionText’, ‘windowText’}

_class _openpyxl.drawing.colors.Transform[[source]](../_modules/openpyxl/drawing/colors.html#Transform)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.colors module
    * `ColorChoice`
      * `ColorChoice.RGB`
      * `ColorChoice.RGBPercent`
      * `ColorChoice.hslClr`
      * `ColorChoice.namespace`
      * `ColorChoice.prstClr`
      * `ColorChoice.schemeClr`
      * `ColorChoice.scrgbClr`
      * `ColorChoice.srgbClr`
      * `ColorChoice.sysClr`
      * `ColorChoice.tagname`
    * `ColorChoiceDescriptor`
      * `ColorChoiceDescriptor.allow_none`
      * `ColorChoiceDescriptor.expected_type`
    * `ColorMapping`
      * `ColorMapping.accent1`
      * `ColorMapping.accent2`
      * `ColorMapping.accent3`
      * `ColorMapping.accent4`
      * `ColorMapping.accent5`
      * `ColorMapping.accent6`
      * `ColorMapping.bg1`
      * `ColorMapping.bg2`
      * `ColorMapping.extLst`
      * `ColorMapping.folHlink`
      * `ColorMapping.hlink`
      * `ColorMapping.tagname`
      * `ColorMapping.tx1`
      * `ColorMapping.tx2`
    * `HSLColor`
      * `HSLColor.hue`
      * `HSLColor.lum`
      * `HSLColor.sat`
      * `HSLColor.tagname`
    * `RGBPercent`
      * `RGBPercent.b`
      * `RGBPercent.g`
      * `RGBPercent.r`
      * `RGBPercent.tagname`
    * `SchemeColor`
      * `SchemeColor.alpha`
      * `SchemeColor.alphaMod`
      * `SchemeColor.alphaOff`
      * `SchemeColor.blue`
      * `SchemeColor.blueMod`
      * `SchemeColor.blueOff`
      * `SchemeColor.comp`
      * `SchemeColor.gamma`
      * `SchemeColor.gray`
      * `SchemeColor.green`
      * `SchemeColor.greenMod`
      * `SchemeColor.greenOff`
      * `SchemeColor.hue`
      * `SchemeColor.hueMod`
      * `SchemeColor.hueOff`
      * `SchemeColor.inv`
      * `SchemeColor.invGamma`
      * `SchemeColor.lum`
      * `SchemeColor.lumMod`
      * `SchemeColor.lumOff`
      * `SchemeColor.namespace`
      * `SchemeColor.red`
      * `SchemeColor.redMod`
      * `SchemeColor.redOff`
      * `SchemeColor.sat`
      * `SchemeColor.satMod`
      * `SchemeColor.satOff`
      * `SchemeColor.shade`
      * `SchemeColor.tagname`
      * `SchemeColor.tint`
      * `SchemeColor.val`
    * `SystemColor`
      * `SystemColor.alpha`
      * `SystemColor.alphaMod`
      * `SystemColor.alphaOff`
      * `SystemColor.blue`
      * `SystemColor.blueMod`
      * `SystemColor.blueOff`
      * `SystemColor.comp`
      * `SystemColor.gamma`
      * `SystemColor.gray`
      * `SystemColor.green`
      * `SystemColor.greenMod`
      * `SystemColor.greenOff`
      * `SystemColor.hue`
      * `SystemColor.hueMod`
      * `SystemColor.hueOff`
      * `SystemColor.inv`
      * `SystemColor.invGamma`
      * `SystemColor.lastClr`
      * `SystemColor.lum`
      * `SystemColor.lumMod`
      * `SystemColor.lumOff`
      * `SystemColor.namespace`
      * `SystemColor.red`
      * `SystemColor.redMod`
      * `SystemColor.redOff`
      * `SystemColor.sat`
      * `SystemColor.satMod`
      * `SystemColor.satOff`
      * `SystemColor.shade`
      * `SystemColor.tagname`
      * `SystemColor.tint`
      * `SystemColor.val`
    * `Transform`



#### Previous topic

[openpyxl.drawing package](openpyxl.drawing.html "previous chapter")

#### Next topic

[openpyxl.drawing.connector module](openpyxl.drawing.connector.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.colors.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.connector.html "openpyxl.drawing.connector module") |
  * [previous](openpyxl.drawing.html "openpyxl.drawing package") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.colors module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
