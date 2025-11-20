### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.geometry.html "openpyxl.drawing.geometry module") |
  * [previous](openpyxl.drawing.effect.html "openpyxl.drawing.effect module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.fill module]()



# openpyxl.drawing.fill module

_class _openpyxl.drawing.fill.Blip(_cstate =None_, _embed =None_, _link =None_, _noGrp =None_, _noSelect =None_, _noRot =None_, _noChangeAspect =None_, _noMove =None_, _noResize =None_, _noEditPoints =None_, _noAdjustHandles =None_, _noChangeArrowheads =None_, _noChangeShapeType =None_, _extLst =None_, _alphaBiLevel =None_, _alphaCeiling =None_, _alphaFloor =None_, _alphaInv =None_, _alphaMod =None_, _alphaModFix =None_, _alphaRepl =None_, _biLevel =None_, _blur =None_, _clrChange =None_, _clrRepl =None_, _duotone =None_, _fillOverlay =None_, _grayscl =None_, _hsl =None_, _lum =None_, _tint =None_)[[source]](../_modules/openpyxl/drawing/fill.html#Blip)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

alphaBiLevel
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaBiLevelEffect’>

alphaCeiling
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaCeilingEffect’>

alphaFloor
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaFloorEffect’>

alphaInv
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaInverseEffect’>

alphaMod
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaModulateEffect’>

alphaModFix
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaModulateFixedEffect’>

alphaRepl
    

Values must be of type <class ‘openpyxl.drawing.effect.AlphaReplaceEffect’>

biLevel
    

Values must be of type <class ‘openpyxl.drawing.effect.BiLevelEffect’>

blur
    

Values must be of type <class ‘openpyxl.drawing.effect.BlurEffect’>

clrChange
    

Values must be of type <class ‘openpyxl.drawing.effect.ColorChangeEffect’>

clrRepl
    

Values must be of type <class ‘openpyxl.drawing.effect.ColorReplaceEffect’>

cstate
    

Value must be one of {‘hqprint’, ‘screen’, ‘print’, ‘email’}

duotone
    

Values must be of type <class ‘openpyxl.drawing.effect.DuotoneEffect’>

embed
    

Values must be of type <class ‘str’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fillOverlay
    

Values must be of type <class ‘openpyxl.drawing.effect.FillOverlayEffect’>

grayscl
    

Values must be of type <class ‘openpyxl.drawing.effect.GrayscaleEffect’>

hsl
    

Values must be of type <class ‘openpyxl.drawing.effect.HSLEffect’>

link
    

Values must be of type <class ‘str’>

lum
    

Values must be of type <class ‘openpyxl.drawing.effect.LuminanceEffect’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

noAdjustHandles
    

Values must be of type <class ‘bool’>

noChangeArrowheads
    

Values must be of type <class ‘bool’>

noChangeAspect
    

Values must be of type <class ‘bool’>

noChangeShapeType
    

Values must be of type <class ‘bool’>

noEditPoints
    

Values must be of type <class ‘bool’>

noGrp
    

Values must be of type <class ‘bool’>

noMove
    

Values must be of type <class ‘bool’>

noResize
    

Values must be of type <class ‘bool’>

noRot
    

Values must be of type <class ‘bool’>

noSelect
    

Values must be of type <class ‘bool’>

tagname _ = 'blip'_
    

tint
    

Values must be of type <class ‘openpyxl.drawing.effect.TintEffect’>

_class _openpyxl.drawing.fill.BlipFillProperties(_dpi=None_ , _rotWithShape=None_ , _blip=None_ , _tile=None_ , _stretch= <openpyxl.drawing.fill.StretchInfoProperties object> Parameters: fillRect=<openpyxl.drawing.fill.RelativeRect object> Parameters: l=None_, _t=None_ , _r=None_ , _b=None_ , _srcRect=None_)[[source]](../_modules/openpyxl/drawing/fill.html#BlipFillProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

blip
    

Values must be of type <class ‘openpyxl.drawing.fill.Blip’>

dpi
    

Values must be of type <class ‘int’>

rotWithShape
    

Values must be of type <class ‘bool’>

srcRect
    

Values must be of type <class ‘openpyxl.drawing.fill.RelativeRect’>

stretch
    

Values must be of type <class ‘openpyxl.drawing.fill.StretchInfoProperties’>

tagname _ = 'blipFill'_
    

tile
    

Values must be of type <class ‘openpyxl.drawing.fill.TileInfoProperties’>

_class _openpyxl.drawing.fill.GradientFillProperties(_flip =None_, _rotWithShape =None_, _gsLst =()_, _lin =None_, _path =None_, _tileRect =None_)[[source]](../_modules/openpyxl/drawing/fill.html#GradientFillProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

flip
    

Value must be one of {‘xy’, ‘y’, ‘x’}

gsLst
    

Wrap a sequence in an containing object

lin
    

Values must be of type <class ‘openpyxl.drawing.fill.LinearShadeProperties’>

linear
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

path
    

Values must be of type <class ‘openpyxl.drawing.fill.PathShadeProperties’>

rotWithShape
    

Values must be of type <class ‘bool’>

stop_list
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

tagname _ = 'gradFill'_
    

tileRect
    

Values must be of type <class ‘openpyxl.drawing.fill.RelativeRect’>

_class _openpyxl.drawing.fill.GradientStop(_pos =None_, _scrgbClr =None_, _srgbClr =None_, _hslClr =None_, _sysClr =None_, _schemeClr =None_, _prstClr =None_)[[source]](../_modules/openpyxl/drawing/fill.html#GradientStop)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

RGB
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

RGBPercent
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

pos
    

Values must be of type <class ‘float’>

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

tagname _ = 'gs'_
    

_class _openpyxl.drawing.fill.LinearShadeProperties(_ang =None_, _scaled =None_)[[source]](../_modules/openpyxl/drawing/fill.html#LinearShadeProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ang
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

scaled
    

Values must be of type <class ‘bool’>

tagname _ = 'lin'_
    

_class _openpyxl.drawing.fill.PathShadeProperties(_path =None_, _fillToRect =None_)[[source]](../_modules/openpyxl/drawing/fill.html#PathShadeProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fillToRect
    

Values must be of type <class ‘openpyxl.drawing.fill.RelativeRect’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

path
    

Value must be one of {‘rect’, ‘shape’, ‘circle’}

tagname _ = 'path'_
    

_class _openpyxl.drawing.fill.PatternFillProperties(_prst =None_, _fgClr =None_, _bgClr =None_)[[source]](../_modules/openpyxl/drawing/fill.html#PatternFillProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

background
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

bgClr
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorChoice’>

fgClr
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorChoice’>

foreground
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

preset
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

prst
    

Value must be one of {‘diagBrick’, ‘pct70’, ‘narHorz’, ‘pct80’, ‘ltDnDiag’, ‘dkVert’, ‘ltVert’, ‘ltUpDiag’, ‘dashVert’, ‘lgGrid’, ‘shingle’, ‘weave’, ‘plaid’, ‘lgCheck’, ‘pct75’, ‘dkDnDiag’, ‘divot’, ‘pct25’, ‘smConfetti’, ‘dnDiag’, ‘horz’, ‘vert’, ‘pct90’, ‘smCheck’, ‘pct5’, ‘wdUpDiag’, ‘cross’, ‘upDiag’, ‘horzBrick’, ‘dkHorz’, ‘openDmnd’, ‘trellis’, ‘dashDnDiag’, ‘dotGrid’, ‘pct10’, ‘solidDmnd’, ‘sphere’, ‘dashHorz’, ‘wave’, ‘narVert’, ‘wdDnDiag’, ‘ltHorz’, ‘dotDmnd’, ‘dashUpDiag’, ‘lgConfetti’, ‘pct60’, ‘pct20’, ‘pct50’, ‘smGrid’, ‘dkUpDiag’, ‘diagCross’, ‘pct30’, ‘pct40’, ‘zigZag’}

tagname _ = 'pattFill'_
    

_class _openpyxl.drawing.fill.RelativeRect(_l =None_, _t =None_, _r =None_, _b =None_)[[source]](../_modules/openpyxl/drawing/fill.html#RelativeRect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘float’>

bottom
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

l
    

Values must be of type <class ‘float’>

left
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

r
    

Values must be of type <class ‘float’>

right
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

t
    

Values must be of type <class ‘float’>

tagname _ = 'rect'_
    

top
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.drawing.fill.SolidColorFillProperties(_scrgbClr =None_, _srgbClr =None_, _hslClr =None_, _sysClr =None_, _schemeClr =None_, _prstClr =None_)[[source]](../_modules/openpyxl/drawing/fill.html#SolidColorFillProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

RGB
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

RGBPercent
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

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

tagname _ = 'solidFill'_
    

_class _openpyxl.drawing.fill.StretchInfoProperties(_fillRect= <openpyxl.drawing.fill.RelativeRect object> Parameters: l=None_, _t=None_ , _r=None_ , _b=None_)[[source]](../_modules/openpyxl/drawing/fill.html#StretchInfoProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fillRect
    

Values must be of type <class ‘openpyxl.drawing.fill.RelativeRect’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'stretch'_
    

_class _openpyxl.drawing.fill.TileInfoProperties(_tx =None_, _ty =None_, _sx =None_, _sy =None_, _flip =None_, _algn =None_)[[source]](../_modules/openpyxl/drawing/fill.html#TileInfoProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algn
    

Value must be one of {‘l’, ‘t’, ‘r’, ‘b’, ‘br’, ‘bl’, ‘tl’, ‘ctr’, ‘tr’}

flip
    

Value must be one of {‘xy’, ‘y’, ‘x’}

sx
    

Values must be of type <class ‘int’>

sy
    

Values must be of type <class ‘int’>

tx
    

Values must be of type <class ‘int’>

ty
    

Values must be of type <class ‘int’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.fill module
    * `Blip`
      * `Blip.alphaBiLevel`
      * `Blip.alphaCeiling`
      * `Blip.alphaFloor`
      * `Blip.alphaInv`
      * `Blip.alphaMod`
      * `Blip.alphaModFix`
      * `Blip.alphaRepl`
      * `Blip.biLevel`
      * `Blip.blur`
      * `Blip.clrChange`
      * `Blip.clrRepl`
      * `Blip.cstate`
      * `Blip.duotone`
      * `Blip.embed`
      * `Blip.extLst`
      * `Blip.fillOverlay`
      * `Blip.grayscl`
      * `Blip.hsl`
      * `Blip.link`
      * `Blip.lum`
      * `Blip.namespace`
      * `Blip.noAdjustHandles`
      * `Blip.noChangeArrowheads`
      * `Blip.noChangeAspect`
      * `Blip.noChangeShapeType`
      * `Blip.noEditPoints`
      * `Blip.noGrp`
      * `Blip.noMove`
      * `Blip.noResize`
      * `Blip.noRot`
      * `Blip.noSelect`
      * `Blip.tagname`
      * `Blip.tint`
    * `BlipFillProperties`
      * `BlipFillProperties.blip`
      * `BlipFillProperties.dpi`
      * `BlipFillProperties.rotWithShape`
      * `BlipFillProperties.srcRect`
      * `BlipFillProperties.stretch`
      * `BlipFillProperties.tagname`
      * `BlipFillProperties.tile`
    * `GradientFillProperties`
      * `GradientFillProperties.flip`
      * `GradientFillProperties.gsLst`
      * `GradientFillProperties.lin`
      * `GradientFillProperties.linear`
      * `GradientFillProperties.namespace`
      * `GradientFillProperties.path`
      * `GradientFillProperties.rotWithShape`
      * `GradientFillProperties.stop_list`
      * `GradientFillProperties.tagname`
      * `GradientFillProperties.tileRect`
    * `GradientStop`
      * `GradientStop.RGB`
      * `GradientStop.RGBPercent`
      * `GradientStop.hslClr`
      * `GradientStop.namespace`
      * `GradientStop.pos`
      * `GradientStop.prstClr`
      * `GradientStop.schemeClr`
      * `GradientStop.scrgbClr`
      * `GradientStop.srgbClr`
      * `GradientStop.sysClr`
      * `GradientStop.tagname`
    * `LinearShadeProperties`
      * `LinearShadeProperties.ang`
      * `LinearShadeProperties.namespace`
      * `LinearShadeProperties.scaled`
      * `LinearShadeProperties.tagname`
    * `PathShadeProperties`
      * `PathShadeProperties.fillToRect`
      * `PathShadeProperties.namespace`
      * `PathShadeProperties.path`
      * `PathShadeProperties.tagname`
    * `PatternFillProperties`
      * `PatternFillProperties.background`
      * `PatternFillProperties.bgClr`
      * `PatternFillProperties.fgClr`
      * `PatternFillProperties.foreground`
      * `PatternFillProperties.namespace`
      * `PatternFillProperties.preset`
      * `PatternFillProperties.prst`
      * `PatternFillProperties.tagname`
    * `RelativeRect`
      * `RelativeRect.b`
      * `RelativeRect.bottom`
      * `RelativeRect.l`
      * `RelativeRect.left`
      * `RelativeRect.namespace`
      * `RelativeRect.r`
      * `RelativeRect.right`
      * `RelativeRect.t`
      * `RelativeRect.tagname`
      * `RelativeRect.top`
    * `SolidColorFillProperties`
      * `SolidColorFillProperties.RGB`
      * `SolidColorFillProperties.RGBPercent`
      * `SolidColorFillProperties.hslClr`
      * `SolidColorFillProperties.prstClr`
      * `SolidColorFillProperties.schemeClr`
      * `SolidColorFillProperties.scrgbClr`
      * `SolidColorFillProperties.srgbClr`
      * `SolidColorFillProperties.sysClr`
      * `SolidColorFillProperties.tagname`
    * `StretchInfoProperties`
      * `StretchInfoProperties.fillRect`
      * `StretchInfoProperties.namespace`
      * `StretchInfoProperties.tagname`
    * `TileInfoProperties`
      * `TileInfoProperties.algn`
      * `TileInfoProperties.flip`
      * `TileInfoProperties.sx`
      * `TileInfoProperties.sy`
      * `TileInfoProperties.tx`
      * `TileInfoProperties.ty`



#### Previous topic

[openpyxl.drawing.effect module](openpyxl.drawing.effect.html "previous chapter")

#### Next topic

[openpyxl.drawing.geometry module](openpyxl.drawing.geometry.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.fill.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.geometry.html "openpyxl.drawing.geometry module") |
  * [previous](openpyxl.drawing.effect.html "openpyxl.drawing.effect module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.fill module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
