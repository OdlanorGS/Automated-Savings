### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.fill.html "openpyxl.drawing.fill module") |
  * [previous](openpyxl.drawing.drawing.html "openpyxl.drawing.drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.effect module]()



# openpyxl.drawing.effect module

_class _openpyxl.drawing.effect.AlphaBiLevelEffect(_thresh =None_)[[source]](../_modules/openpyxl/drawing/effect.html#AlphaBiLevelEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

thresh
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.AlphaCeilingEffect[[source]](../_modules/openpyxl/drawing/effect.html#AlphaCeilingEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.AlphaFloorEffect[[source]](../_modules/openpyxl/drawing/effect.html#AlphaFloorEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.AlphaInverseEffect[[source]](../_modules/openpyxl/drawing/effect.html#AlphaInverseEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.AlphaModulateEffect(_cont =None_)[[source]](../_modules/openpyxl/drawing/effect.html#AlphaModulateEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cont
    

Values must be of type <class ‘openpyxl.drawing.effect.EffectContainer’>

_class _openpyxl.drawing.effect.AlphaModulateFixedEffect(_amt =None_)[[source]](../_modules/openpyxl/drawing/effect.html#AlphaModulateFixedEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

amt
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.AlphaReplaceEffect(_a =None_)[[source]](../_modules/openpyxl/drawing/effect.html#AlphaReplaceEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

a
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.BiLevelEffect(_thresh =None_)[[source]](../_modules/openpyxl/drawing/effect.html#BiLevelEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

thresh
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.BlurEffect(_rad =None_, _grow =None_)[[source]](../_modules/openpyxl/drawing/effect.html#BlurEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

grow
    

Values must be of type <class ‘bool’>

rad
    

Values must be of type <class ‘float’>

_class _openpyxl.drawing.effect.Color[[source]](../_modules/openpyxl/drawing/effect.html#Color)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.ColorChangeEffect(_useA =None_, _clrFrom =None_, _clrTo =None_)[[source]](../_modules/openpyxl/drawing/effect.html#ColorChangeEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

clrFrom
    

Values must be of type <class ‘openpyxl.drawing.effect.Color’>

clrTo
    

Values must be of type <class ‘openpyxl.drawing.effect.Color’>

useA
    

Values must be of type <class ‘bool’>

_class _openpyxl.drawing.effect.ColorReplaceEffect[[source]](../_modules/openpyxl/drawing/effect.html#ColorReplaceEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.DuotoneEffect[[source]](../_modules/openpyxl/drawing/effect.html#DuotoneEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.effect.EffectContainer(_type =None_, _name =None_)[[source]](../_modules/openpyxl/drawing/effect.html#EffectContainer)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

type
    

Value must be one of {‘sib’, ‘tree’}

_class _openpyxl.drawing.effect.EffectList(_blur =None_, _fillOverlay =None_, _glow =None_, _innerShdw =None_, _outerShdw =None_, _prstShdw =None_, _reflection =None_, _softEdge =None_)[[source]](../_modules/openpyxl/drawing/effect.html#EffectList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

blur
    

Values must be of type <class ‘openpyxl.drawing.effect.BlurEffect’>

fillOverlay
    

Values must be of type <class ‘openpyxl.drawing.effect.FillOverlayEffect’>

glow
    

Values must be of type <class ‘openpyxl.drawing.effect.GlowEffect’>

innerShdw
    

Values must be of type <class ‘openpyxl.drawing.effect.InnerShadowEffect’>

outerShdw
    

Values must be of type <class ‘openpyxl.drawing.effect.OuterShadow’>

prstShdw
    

Values must be of type <class ‘openpyxl.drawing.effect.PresetShadowEffect’>

reflection
    

Values must be of type <class ‘openpyxl.drawing.effect.ReflectionEffect’>

softEdge
    

Values must be of type <class ‘openpyxl.drawing.effect.SoftEdgesEffect’>

_class _openpyxl.drawing.effect.FillOverlayEffect(_blend =None_)[[source]](../_modules/openpyxl/drawing/effect.html#FillOverlayEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

blend
    

Value must be one of {‘mult’, ‘screen’, ‘over’, ‘darken’, ‘lighten’}

_class _openpyxl.drawing.effect.GlowEffect(_rad =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/effect.html#GlowEffect)
    

Bases: [`ColorChoice`](openpyxl.drawing.colors.html#openpyxl.drawing.colors.ColorChoice "openpyxl.drawing.colors.ColorChoice")

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

prstClr
    

Value must be one of {‘ltGoldenrodYellow’, ‘darkSlateBlue’, ‘fuchsia’, ‘ltGrey’, ‘medTurquoise’, ‘moccasin’, ‘lavenderBlush’, ‘mediumSlateBlue’, ‘gold’, ‘paleVioletRed’, ‘darkGoldenrod’, ‘darkSlateGray’, ‘lightGrey’, ‘mediumBlue’, ‘chocolate’, ‘yellow’, ‘lightSkyBlue’, ‘darkGrey’, ‘lightSlateGrey’, ‘tomato’, ‘turquoise’, ‘darkSalmon’, ‘mediumTurquoise’, ‘mediumSpringGreen’, ‘paleGreen’, ‘lightGreen’, ‘darkGreen’, ‘bisque’, ‘green’, ‘maroon’, ‘hotPink’, ‘ltSeaGreen’, ‘darkBlue’, ‘mediumVioletRed’, ‘dkGreen’, ‘plum’, ‘darkGray’, ‘medSpringGreen’, ‘wheat’, ‘red’, ‘aquamarine’, ‘dkGrey’, ‘whiteSmoke’, ‘yellowGreen’, ‘ltSlateGray’, ‘medSlateBlue’, ‘dkSlateGrey’, ‘ltBlue’, ‘lightCoral’, ‘steelBlue’, ‘paleTurquoise’, ‘pink’, ‘greenYellow’, ‘darkSlateGrey’, ‘mistyRose’, ‘crimson’, ‘darkKhaki’, ‘ltGreen’, ‘ltSlateGrey’, ‘blanchedAlmond’, ‘magenta’, ‘orange’, ‘lightGoldenrodYellow’, ‘dkKhaki’, ‘cornflowerBlue’, ‘coral’, ‘limeGreen’, ‘mediumPurple’, ‘firebrick’, ‘ltCoral’, ‘ltSkyBlue’, ‘mintCream’, ‘chartreuse’, ‘medBlue’, ‘ltPink’, ‘snow’, ‘dkSlateGray’, ‘ltCyan’, ‘deepSkyBlue’, ‘thistle’, ‘darkSeaGreen’, ‘tan’, ‘lightPink’, ‘paleGoldenrod’, ‘rosyBrown’, ‘lightSalmon’, ‘lightGray’, ‘dkCyan’, ‘dkOrange’, ‘mediumSeaGreen’, ‘lightCyan’, ‘orangeRed’, ‘mediumAquamarine’, ‘aqua’, ‘darkMagenta’, ‘ghostWhite’, ‘cyan’, ‘dkSalmon’, ‘lightSeaGreen’, ‘brown’, ‘skyBlue’, ‘ltYellow’, ‘dkSeaGreen’, ‘darkRed’, ‘midnightBlue’, ‘orchid’, ‘oldLace’, ‘violet’, ‘dkOrchid’, ‘dkBlue’, ‘darkCyan’, ‘salmon’, ‘navajoWhite’, ‘medOrchid’, ‘oliveDrab’, ‘dimGrey’, ‘darkOliveGreen’, ‘mediumOrchid’, ‘honeydew’, ‘linen’, ‘peachPuff’, ‘springGreen’, ‘medVioletRed’, ‘cornsilk’, ‘papayaWhip’, ‘forestGreen’, ‘dkSlateBlue’, ‘lightYellow’, ‘purple’, ‘teal’, ‘white’, ‘dkRed’, ‘medSeaGreen’, ‘seaGreen’, ‘seaShell’, ‘gray’, ‘dkViolet’, ‘navy’, ‘lawnGreen’, ‘slateBlue’, ‘dimGray’, ‘dodgerBlue’, ‘lightBlue’, ‘dkMagenta’, ‘royalBlue’, ‘floralWhite’, ‘powderBlue’, ‘grey’, ‘aliceBlue’, ‘silver’, ‘gainsboro’, ‘dkOliveGreen’, ‘indigo’, ‘lightSteelBlue’, ‘khaki’, ‘ltSteelBlue’, ‘cadetBlue’, ‘black’, ‘ltSalmon’, ‘darkOrchid’, ‘saddleBrown’, ‘goldenrod’, ‘darkViolet’, ‘lightSlateGray’, ‘darkTurquoise’, ‘peru’, ‘beige’, ‘ivory’, ‘medPurple’, ‘slateGrey’, ‘olive’, ‘antiqueWhite’, ‘blueViolet’, ‘blue’, ‘medAquamarine’, ‘ltGray’, ‘azure’, ‘dkGoldenrod’, ‘darkOrange’, ‘indianRed’, ‘dkGray’, ‘sienna’, ‘slateGray’, ‘lime’, ‘dkTurquoise’, ‘sandyBrown’, ‘lemonChiffon’, ‘deepPink’, ‘burlyWood’, ‘lavender’}

rad
    

Values must be of type <class ‘float’>

schemeClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SchemeColor’>

scrgbClr
    

Values must be of type <class ‘openpyxl.drawing.colors.RGBPercent’>

srgbClr
    

Values must be of type <class ‘str’>

sysClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SystemColor’>

_class _openpyxl.drawing.effect.GrayscaleEffect[[source]](../_modules/openpyxl/drawing/effect.html#GrayscaleEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'grayscl'_
    

_class _openpyxl.drawing.effect.HSLEffect(_hue =None_, _sat =None_, _lum =None_)[[source]](../_modules/openpyxl/drawing/effect.html#HSLEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

hue
    

Values must be of type <class ‘int’>

lum
    

Values must be of type <class ‘int’>

sat
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.InnerShadowEffect(_blurRad =None_, _dist =None_, _dir =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/effect.html#InnerShadowEffect)
    

Bases: [`ColorChoice`](openpyxl.drawing.colors.html#openpyxl.drawing.colors.ColorChoice "openpyxl.drawing.colors.ColorChoice")

blurRad
    

Values must be of type <class ‘float’>

dir
    

Values must be of type <class ‘int’>

dist
    

Values must be of type <class ‘float’>

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

_class _openpyxl.drawing.effect.LuminanceEffect(_bright =0_, _contrast =0_)[[source]](../_modules/openpyxl/drawing/effect.html#LuminanceEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

bright
    

Values must be of type <class ‘int’>

contrast
    

Values must be of type <class ‘int’>

tagname _ = 'lum'_
    

_class _openpyxl.drawing.effect.OuterShadow(_blurRad =None_, _dist =None_, _dir =None_, _sx =None_, _sy =None_, _kx =None_, _ky =None_, _algn =None_, _rotWithShape =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/effect.html#OuterShadow)
    

Bases: [`ColorChoice`](openpyxl.drawing.colors.html#openpyxl.drawing.colors.ColorChoice "openpyxl.drawing.colors.ColorChoice")

algn
    

Value must be one of {‘l’, ‘t’, ‘r’, ‘b’, ‘br’, ‘bl’, ‘tl’, ‘ctr’, ‘tr’}

blurRad
    

Values must be of type <class ‘float’>

dir
    

Values must be of type <class ‘int’>

dist
    

Values must be of type <class ‘float’>

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

kx
    

Values must be of type <class ‘int’>

ky
    

Values must be of type <class ‘int’>

prstClr
    

Value must be one of {‘ltGoldenrodYellow’, ‘darkSlateBlue’, ‘fuchsia’, ‘ltGrey’, ‘medTurquoise’, ‘moccasin’, ‘lavenderBlush’, ‘mediumSlateBlue’, ‘gold’, ‘paleVioletRed’, ‘darkGoldenrod’, ‘darkSlateGray’, ‘lightGrey’, ‘mediumBlue’, ‘chocolate’, ‘yellow’, ‘lightSkyBlue’, ‘darkGrey’, ‘lightSlateGrey’, ‘tomato’, ‘turquoise’, ‘darkSalmon’, ‘mediumTurquoise’, ‘mediumSpringGreen’, ‘paleGreen’, ‘lightGreen’, ‘darkGreen’, ‘bisque’, ‘green’, ‘maroon’, ‘hotPink’, ‘ltSeaGreen’, ‘darkBlue’, ‘mediumVioletRed’, ‘dkGreen’, ‘plum’, ‘darkGray’, ‘medSpringGreen’, ‘wheat’, ‘red’, ‘aquamarine’, ‘dkGrey’, ‘whiteSmoke’, ‘yellowGreen’, ‘ltSlateGray’, ‘medSlateBlue’, ‘dkSlateGrey’, ‘ltBlue’, ‘lightCoral’, ‘steelBlue’, ‘paleTurquoise’, ‘pink’, ‘greenYellow’, ‘darkSlateGrey’, ‘mistyRose’, ‘crimson’, ‘darkKhaki’, ‘ltGreen’, ‘ltSlateGrey’, ‘blanchedAlmond’, ‘magenta’, ‘orange’, ‘lightGoldenrodYellow’, ‘dkKhaki’, ‘cornflowerBlue’, ‘coral’, ‘limeGreen’, ‘mediumPurple’, ‘firebrick’, ‘ltCoral’, ‘ltSkyBlue’, ‘mintCream’, ‘chartreuse’, ‘medBlue’, ‘ltPink’, ‘snow’, ‘dkSlateGray’, ‘ltCyan’, ‘deepSkyBlue’, ‘thistle’, ‘darkSeaGreen’, ‘tan’, ‘lightPink’, ‘paleGoldenrod’, ‘rosyBrown’, ‘lightSalmon’, ‘lightGray’, ‘dkCyan’, ‘dkOrange’, ‘mediumSeaGreen’, ‘lightCyan’, ‘orangeRed’, ‘mediumAquamarine’, ‘aqua’, ‘darkMagenta’, ‘ghostWhite’, ‘cyan’, ‘dkSalmon’, ‘lightSeaGreen’, ‘brown’, ‘skyBlue’, ‘ltYellow’, ‘dkSeaGreen’, ‘darkRed’, ‘midnightBlue’, ‘orchid’, ‘oldLace’, ‘violet’, ‘dkOrchid’, ‘dkBlue’, ‘darkCyan’, ‘salmon’, ‘navajoWhite’, ‘medOrchid’, ‘oliveDrab’, ‘dimGrey’, ‘darkOliveGreen’, ‘mediumOrchid’, ‘honeydew’, ‘linen’, ‘peachPuff’, ‘springGreen’, ‘medVioletRed’, ‘cornsilk’, ‘papayaWhip’, ‘forestGreen’, ‘dkSlateBlue’, ‘lightYellow’, ‘purple’, ‘teal’, ‘white’, ‘dkRed’, ‘medSeaGreen’, ‘seaGreen’, ‘seaShell’, ‘gray’, ‘dkViolet’, ‘navy’, ‘lawnGreen’, ‘slateBlue’, ‘dimGray’, ‘dodgerBlue’, ‘lightBlue’, ‘dkMagenta’, ‘royalBlue’, ‘floralWhite’, ‘powderBlue’, ‘grey’, ‘aliceBlue’, ‘silver’, ‘gainsboro’, ‘dkOliveGreen’, ‘indigo’, ‘lightSteelBlue’, ‘khaki’, ‘ltSteelBlue’, ‘cadetBlue’, ‘black’, ‘ltSalmon’, ‘darkOrchid’, ‘saddleBrown’, ‘goldenrod’, ‘darkViolet’, ‘lightSlateGray’, ‘darkTurquoise’, ‘peru’, ‘beige’, ‘ivory’, ‘medPurple’, ‘slateGrey’, ‘olive’, ‘antiqueWhite’, ‘blueViolet’, ‘blue’, ‘medAquamarine’, ‘ltGray’, ‘azure’, ‘dkGoldenrod’, ‘darkOrange’, ‘indianRed’, ‘dkGray’, ‘sienna’, ‘slateGray’, ‘lime’, ‘dkTurquoise’, ‘sandyBrown’, ‘lemonChiffon’, ‘deepPink’, ‘burlyWood’, ‘lavender’}

rotWithShape
    

Values must be of type <class ‘bool’>

schemeClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SchemeColor’>

scrgbClr
    

Values must be of type <class ‘openpyxl.drawing.colors.RGBPercent’>

srgbClr
    

Values must be of type <class ‘str’>

sx
    

Values must be of type <class ‘int’>

sy
    

Values must be of type <class ‘int’>

sysClr
    

Values must be of type <class ‘openpyxl.drawing.colors.SystemColor’>

tagname _ = 'outerShdw'_
    

_class _openpyxl.drawing.effect.PresetShadowEffect(_prst =None_, _dist =None_, _dir =None_, _** kw_)[[source]](../_modules/openpyxl/drawing/effect.html#PresetShadowEffect)
    

Bases: [`ColorChoice`](openpyxl.drawing.colors.html#openpyxl.drawing.colors.ColorChoice "openpyxl.drawing.colors.ColorChoice")

dir
    

Values must be of type <class ‘int’>

dist
    

Values must be of type <class ‘float’>

hslClr
    

Values must be of type <class ‘openpyxl.drawing.colors.HSLColor’>

prst
    

Value must be one of {‘shdw12’, ‘shdw5’, ‘shdw10’, ‘shdw15’, ‘shdw18’, ‘shdw8’, ‘shdw11’, ‘shdw2’, ‘shdw7’, ‘shdw14’, ‘shdw3’, ‘shdw16’, ‘shdw20’, ‘shdw4’, ‘shdw9’, ‘shdw1’, ‘shdw13’, ‘shdw17’, ‘shdw6’, ‘shdw19’}

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

_class _openpyxl.drawing.effect.ReflectionEffect(_blurRad =None_, _stA =None_, _stPos =None_, _endA =None_, _endPos =None_, _dist =None_, _dir =None_, _fadeDir =None_, _sx =None_, _sy =None_, _kx =None_, _ky =None_, _algn =None_, _rotWithShape =None_)[[source]](../_modules/openpyxl/drawing/effect.html#ReflectionEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algn
    

Value must be one of {‘l’, ‘t’, ‘r’, ‘b’, ‘br’, ‘bl’, ‘tl’, ‘ctr’, ‘tr’}

blurRad
    

Values must be of type <class ‘float’>

dir
    

Values must be of type <class ‘int’>

dist
    

Values must be of type <class ‘float’>

endA
    

Values must be of type <class ‘int’>

endPos
    

Values must be of type <class ‘int’>

fadeDir
    

Values must be of type <class ‘int’>

kx
    

Values must be of type <class ‘int’>

ky
    

Values must be of type <class ‘int’>

rotWithShape
    

Values must be of type <class ‘bool’>

stA
    

Values must be of type <class ‘int’>

stPos
    

Values must be of type <class ‘int’>

sx
    

Values must be of type <class ‘int’>

sy
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.effect.SoftEdgesEffect(_rad =None_)[[source]](../_modules/openpyxl/drawing/effect.html#SoftEdgesEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

rad
    

Values must be of type <class ‘float’>

_class _openpyxl.drawing.effect.TintEffect(_hue =0_, _amt =0_)[[source]](../_modules/openpyxl/drawing/effect.html#TintEffect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

amt
    

Values must be of type <class ‘int’>

hue
    

Values must be of type <class ‘int’>

tagname _ = 'tint'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.effect module
    * `AlphaBiLevelEffect`
      * `AlphaBiLevelEffect.thresh`
    * `AlphaCeilingEffect`
    * `AlphaFloorEffect`
    * `AlphaInverseEffect`
    * `AlphaModulateEffect`
      * `AlphaModulateEffect.cont`
    * `AlphaModulateFixedEffect`
      * `AlphaModulateFixedEffect.amt`
    * `AlphaReplaceEffect`
      * `AlphaReplaceEffect.a`
    * `BiLevelEffect`
      * `BiLevelEffect.thresh`
    * `BlurEffect`
      * `BlurEffect.grow`
      * `BlurEffect.rad`
    * `Color`
    * `ColorChangeEffect`
      * `ColorChangeEffect.clrFrom`
      * `ColorChangeEffect.clrTo`
      * `ColorChangeEffect.useA`
    * `ColorReplaceEffect`
    * `DuotoneEffect`
    * `EffectContainer`
      * `EffectContainer.name`
      * `EffectContainer.type`
    * `EffectList`
      * `EffectList.blur`
      * `EffectList.fillOverlay`
      * `EffectList.glow`
      * `EffectList.innerShdw`
      * `EffectList.outerShdw`
      * `EffectList.prstShdw`
      * `EffectList.reflection`
      * `EffectList.softEdge`
    * `FillOverlayEffect`
      * `FillOverlayEffect.blend`
    * `GlowEffect`
      * `GlowEffect.hslClr`
      * `GlowEffect.prstClr`
      * `GlowEffect.rad`
      * `GlowEffect.schemeClr`
      * `GlowEffect.scrgbClr`
      * `GlowEffect.srgbClr`
      * `GlowEffect.sysClr`
    * `GrayscaleEffect`
      * `GrayscaleEffect.tagname`
    * `HSLEffect`
      * `HSLEffect.hue`
      * `HSLEffect.lum`
      * `HSLEffect.sat`
    * `InnerShadowEffect`
      * `InnerShadowEffect.blurRad`
      * `InnerShadowEffect.dir`
      * `InnerShadowEffect.dist`
      * `InnerShadowEffect.hslClr`
      * `InnerShadowEffect.prstClr`
      * `InnerShadowEffect.schemeClr`
      * `InnerShadowEffect.scrgbClr`
      * `InnerShadowEffect.srgbClr`
      * `InnerShadowEffect.sysClr`
    * `LuminanceEffect`
      * `LuminanceEffect.bright`
      * `LuminanceEffect.contrast`
      * `LuminanceEffect.tagname`
    * `OuterShadow`
      * `OuterShadow.algn`
      * `OuterShadow.blurRad`
      * `OuterShadow.dir`
      * `OuterShadow.dist`
      * `OuterShadow.hslClr`
      * `OuterShadow.kx`
      * `OuterShadow.ky`
      * `OuterShadow.prstClr`
      * `OuterShadow.rotWithShape`
      * `OuterShadow.schemeClr`
      * `OuterShadow.scrgbClr`
      * `OuterShadow.srgbClr`
      * `OuterShadow.sx`
      * `OuterShadow.sy`
      * `OuterShadow.sysClr`
      * `OuterShadow.tagname`
    * `PresetShadowEffect`
      * `PresetShadowEffect.dir`
      * `PresetShadowEffect.dist`
      * `PresetShadowEffect.hslClr`
      * `PresetShadowEffect.prst`
      * `PresetShadowEffect.prstClr`
      * `PresetShadowEffect.schemeClr`
      * `PresetShadowEffect.scrgbClr`
      * `PresetShadowEffect.srgbClr`
      * `PresetShadowEffect.sysClr`
    * `ReflectionEffect`
      * `ReflectionEffect.algn`
      * `ReflectionEffect.blurRad`
      * `ReflectionEffect.dir`
      * `ReflectionEffect.dist`
      * `ReflectionEffect.endA`
      * `ReflectionEffect.endPos`
      * `ReflectionEffect.fadeDir`
      * `ReflectionEffect.kx`
      * `ReflectionEffect.ky`
      * `ReflectionEffect.rotWithShape`
      * `ReflectionEffect.stA`
      * `ReflectionEffect.stPos`
      * `ReflectionEffect.sx`
      * `ReflectionEffect.sy`
    * `SoftEdgesEffect`
      * `SoftEdgesEffect.rad`
    * `TintEffect`
      * `TintEffect.amt`
      * `TintEffect.hue`
      * `TintEffect.tagname`



#### Previous topic

[openpyxl.drawing.drawing module](openpyxl.drawing.drawing.html "previous chapter")

#### Next topic

[openpyxl.drawing.fill module](openpyxl.drawing.fill.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.effect.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.fill.html "openpyxl.drawing.fill module") |
  * [previous](openpyxl.drawing.drawing.html "openpyxl.drawing.drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.effect module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
