### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.xdr.html "openpyxl.drawing.xdr module") |
  * [previous](openpyxl.drawing.spreadsheet_drawing.html "openpyxl.drawing.spreadsheet_drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.text module]()



# openpyxl.drawing.text module

_class _openpyxl.drawing.text.AutonumberBullet(_type =None_, _startAt =None_)[[source]](../_modules/openpyxl/drawing/text.html#AutonumberBullet)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

startAt
    

Values must be of type <class ‘int’>

type
    

Value must be one of {‘romanLcParenR’, ‘circleNumWdWhitePlain’, ‘romanUcParenR’, ‘arabicPeriod’, ‘romanLcPeriod’, ‘arabic2Minus’, ‘thaiNumPeriod’, ‘ea1ChsPeriod’, ‘hebrew2Minus’, ‘ea1ChsPlain’, ‘alphaUcPeriod’, ‘hindiAlphaPeriod’, ‘hindiAlpha1Period’, ‘thaiAlphaParenR’, ‘alphaLcParenR’, ‘alphaUcParenBoth’, ‘ea1JpnKorPlain’, ‘hindiNumPeriod’, ‘arabicParenR’, ‘arabicDbPeriod’, ‘ea1JpnKorPeriod’, ‘romanUcPeriod’, ‘alphaUcParenR’, ‘romanUcParenBoth’, ‘arabicPlain’, ‘circleNumDbPlain’, ‘alphaLcPeriod’, ‘thaiAlphaParenBoth’, ‘thaiNumParenR’, ‘hindiNumParenR’, ‘ea1JpnChsDbPeriod’, ‘ea1ChtPeriod’, ‘arabicDbPlain’, ‘thaiAlphaPeriod’, ‘thaiNumParenBoth’, ‘alphaLcParenBoth’, ‘arabicParenBoth’, ‘ea1ChtPlain’, ‘romanLcParenBoth’, ‘arabic1Minus’, ‘circleNumWdBlackPlain’}

_class _openpyxl.drawing.text.CharacterProperties(_kumimoji =None_, _lang =None_, _altLang =None_, _sz =None_, _b =None_, _i =None_, _u =None_, _strike =None_, _kern =None_, _cap =None_, _spc =None_, _normalizeH =None_, _baseline =None_, _noProof =None_, _dirty =None_, _err =None_, _smtClean =None_, _smtId =None_, _bmk =None_, _ln =None_, _highlight =None_, _latin =None_, _ea =None_, _cs =None_, _sym =None_, _hlinkClick =None_, _hlinkMouseOver =None_, _rtl =None_, _extLst =None_, _noFill =None_, _solidFill =None_, _gradFill =None_, _blipFill =None_, _pattFill =None_, _grpFill =None_, _effectLst =None_, _effectDag =None_, _uLnTx =None_, _uLn =None_, _uFillTx =None_, _uFill =None_)[[source]](../_modules/openpyxl/drawing/text.html#CharacterProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

altLang
    

Values must be of type <class ‘str’>

b
    

Values must be of type <class ‘bool’>

baseline
    

Values must be of type <class ‘int’>

blipFill
    

Values must be of type <class ‘openpyxl.drawing.fill.BlipFillProperties’>

bmk
    

Values must be of type <class ‘str’>

cap
    

Value must be one of {‘small’, ‘all’}

cs
    

Values must be of type <class ‘openpyxl.drawing.text.Font’>

dirty
    

Values must be of type <class ‘bool’>

ea
    

Values must be of type <class ‘openpyxl.drawing.text.Font’>

effectDag
    

Values must be of type <class ‘openpyxl.drawing.effect.EffectContainer’>

effectLst
    

Values must be of type <class ‘openpyxl.drawing.effect.EffectList’>

err
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

gradFill
    

Values must be of type <class ‘openpyxl.drawing.fill.GradientFillProperties’>

grpFill
    

Values must be of type <class ‘bool’>

highlight
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

hlinkClick
    

Values must be of type <class ‘openpyxl.drawing.text.Hyperlink’>

hlinkMouseOver
    

Values must be of type <class ‘openpyxl.drawing.text.Hyperlink’>

i
    

Values must be of type <class ‘bool’>

kern
    

Values must be of type <class ‘int’>

kumimoji
    

Values must be of type <class ‘bool’>

lang
    

Values must be of type <class ‘str’>

latin
    

Values must be of type <class ‘openpyxl.drawing.text.Font’>

ln
    

Values must be of type <class ‘openpyxl.drawing.line.LineProperties’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

noFill
    

Values must be of type <class ‘bool’>

noProof
    

Values must be of type <class ‘bool’>

normalizeH
    

Values must be of type <class ‘bool’>

pattFill
    

Values must be of type <class ‘openpyxl.drawing.fill.PatternFillProperties’>

rtl
    

Values must be of type <class ‘bool’>

smtClean
    

Values must be of type <class ‘bool’>

smtId
    

Values must be of type <class ‘int’>

solidFill
    

Values must be of type <class ‘openpyxl.drawing.colors.ColorChoice’>

spc
    

Values must be of type <class ‘int’>

strike
    

Value must be one of {‘sngStrike’, ‘noStrike’, ‘dblStrike’}

sym
    

Values must be of type <class ‘openpyxl.drawing.text.Font’>

sz
    

Values must be of type <class ‘float’>

tagname _ = 'defRPr'_
    

u
    

Value must be one of {‘words’, ‘sng’, ‘dbl’, ‘dotted’, ‘dashLong’, ‘wavyDbl’, ‘dashHeavy’, ‘dottedHeavy’, ‘dotDashHeavy’, ‘wavy’, ‘wavyHeavy’, ‘dotDash’, ‘dotDotDash’, ‘dash’, ‘heavy’, ‘dashLongHeavy’, ‘dotDotDashHeavy’}

uFill
    

Values must be of type <class ‘bool’>

uFillTx
    

Values must be of type <class ‘bool’>

uLn
    

Values must be of type <class ‘openpyxl.drawing.line.LineProperties’>

uLnTx
    

Values must be of type <class ‘bool’>

_class _openpyxl.drawing.text.EmbeddedWAVAudioFile(_name =None_)[[source]](../_modules/openpyxl/drawing/text.html#EmbeddedWAVAudioFile)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

name
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.text.Font(_typeface =None_, _panose =None_, _pitchFamily =None_, _charset =None_)[[source]](../_modules/openpyxl/drawing/text.html#Font)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

charset
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

panose
    

pitchFamily
    

Values must be of type <class ‘float’>

tagname _ = 'latin'_
    

typeface
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.text.GeomGuide(_name =None_, _fmla =None_)[[source]](../_modules/openpyxl/drawing/text.html#GeomGuide)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fmla
    

Values must be of type <class ‘str’>

name
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.text.GeomGuideList(_gd =None_)[[source]](../_modules/openpyxl/drawing/text.html#GeomGuideList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

gd
    

A sequence (list or tuple) that may only contain objects of the declared type

_class _openpyxl.drawing.text.Hyperlink(_invalidUrl =None_, _action =None_, _tgtFrame =None_, _tooltip =None_, _history =None_, _highlightClick =None_, _endSnd =None_, _snd =None_, _extLst =None_, _id =None_)[[source]](../_modules/openpyxl/drawing/text.html#Hyperlink)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

action
    

Values must be of type <class ‘str’>

endSnd
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

highlightClick
    

Values must be of type <class ‘bool’>

history
    

Values must be of type <class ‘bool’>

id
    

Values must be of type <class ‘str’>

invalidUrl
    

Values must be of type <class ‘str’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

snd
    

Values must be of type <class ‘openpyxl.drawing.text.EmbeddedWAVAudioFile’>

tagname _ = 'hlinkClick'_
    

tgtFrame
    

Values must be of type <class ‘str’>

tooltip
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.text.LineBreak(_rPr =None_)[[source]](../_modules/openpyxl/drawing/text.html#LineBreak)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

rPr
    

Values must be of type <class ‘openpyxl.drawing.text.CharacterProperties’>

tagname _ = 'br'_
    

_class _openpyxl.drawing.text.ListStyle(_defPPr =None_, _lvl1pPr =None_, _lvl2pPr =None_, _lvl3pPr =None_, _lvl4pPr =None_, _lvl5pPr =None_, _lvl6pPr =None_, _lvl7pPr =None_, _lvl8pPr =None_, _lvl9pPr =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/text.html#ListStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

defPPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

lvl1pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl2pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl3pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl4pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl5pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl6pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl7pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl8pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

lvl9pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'lstStyle'_
    

_class _openpyxl.drawing.text.Paragraph(_pPr =None_, _endParaRPr =None_, _r =None_, _br =None_, _fld =None_)[[source]](../_modules/openpyxl/drawing/text.html#Paragraph)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

br
    

Values must be of type <class ‘openpyxl.drawing.text.LineBreak’>

endParaRPr
    

Values must be of type <class ‘openpyxl.drawing.text.CharacterProperties’>

fld
    

Values must be of type <class ‘openpyxl.drawing.text.TextField’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

properties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

r
    

A sequence (list or tuple) that may only contain objects of the declared type

tagname _ = 'p'_
    

text
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.drawing.text.ParagraphProperties(_marL =None_, _marR =None_, _lvl =None_, _indent =None_, _algn =None_, _defTabSz =None_, _rtl =None_, _eaLnBrk =None_, _fontAlgn =None_, _latinLnBrk =None_, _hangingPunct =None_, _lnSpc =None_, _spcBef =None_, _spcAft =None_, _tabLst =None_, _defRPr =None_, _extLst =None_, _buClrTx =None_, _buClr =None_, _buSzTx =None_, _buSzPct =None_, _buSzPts =None_, _buFontTx =None_, _buFont =None_, _buNone =None_, _buAutoNum =None_, _buChar =None_, _buBlip =None_)[[source]](../_modules/openpyxl/drawing/text.html#ParagraphProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algn
    

Value must be one of {‘l’, ‘r’, ‘just’, ‘thaiDist’, ‘justLow’, ‘ctr’, ‘dist’}

buAutoNum
    

Values must be of type <class ‘bool’>

buBlip
    

Values must be of type <class ‘openpyxl.drawing.fill.Blip’>

buChar
    

Values must be of type <class ‘str’>

buClr
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

buClrTx
    

Values must be of type <class ‘bool’>

buFont
    

Values must be of type <class ‘openpyxl.drawing.text.Font’>

buFontTx
    

Values must be of type <class ‘bool’>

buNone
    

Values must be of type <class ‘bool’>

buSzPct
    

Values must be of type <class ‘int’>

buSzPts
    

Values must be of type <class ‘int’>

buSzTx
    

Values must be of type <class ‘bool’>

defRPr
    

Values must be of type <class ‘openpyxl.drawing.text.CharacterProperties’>

defTabSz
    

Values must be of type <class ‘int’>

eaLnBrk
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

fontAlgn
    

Value must be one of {‘base’, ‘t’, ‘b’, ‘ctr’, ‘auto’}

hangingPunct
    

Values must be of type <class ‘bool’>

indent
    

Values must be of type <class ‘int’>

latinLnBrk
    

Values must be of type <class ‘bool’>

lnSpc
    

Values must be of type <class ‘openpyxl.drawing.text.Spacing’>

lvl
    

Values must be of type <class ‘int’>

marL
    

Values must be of type <class ‘int’>

marR
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

rtl
    

Values must be of type <class ‘bool’>

spcAft
    

Values must be of type <class ‘openpyxl.drawing.text.Spacing’>

spcBef
    

Values must be of type <class ‘openpyxl.drawing.text.Spacing’>

tabLst
    

Values must be of type <class ‘openpyxl.drawing.text.TabStopList’>

tagname _ = 'pPr'_
    

_class _openpyxl.drawing.text.PresetTextShape(_prst =None_, _avLst =None_)[[source]](../_modules/openpyxl/drawing/text.html#PresetTextShape)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

avLst
    

Values must be of type <class ‘openpyxl.drawing.text.GeomGuideList’>

prst
    

Values must be of type <openpyxl.descriptors.base.Set object at 0x7f1b33741b50>

_class _openpyxl.drawing.text.RegularTextRun(_rPr =None_, _t =''_)[[source]](../_modules/openpyxl/drawing/text.html#RegularTextRun)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

properties
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

rPr
    

Values must be of type <class ‘openpyxl.drawing.text.CharacterProperties’>

t
    

Values must be of type <class ‘str’>

tagname _ = 'r'_
    

value
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.drawing.text.RichTextProperties(_rot =None_, _spcFirstLastPara =None_, _vertOverflow =None_, _horzOverflow =None_, _vert =None_, _wrap =None_, _lIns =None_, _tIns =None_, _rIns =None_, _bIns =None_, _numCol =None_, _spcCol =None_, _rtlCol =None_, _fromWordArt =None_, _anchor =None_, _anchorCtr =None_, _forceAA =None_, _upright =None_, _compatLnSpc =None_, _prstTxWarp =None_, _scene3d =None_, _extLst =None_, _noAutofit =None_, _normAutofit =None_, _spAutoFit =None_, _flatTx =None_)[[source]](../_modules/openpyxl/drawing/text.html#RichTextProperties)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

anchor
    

Value must be one of {‘t’, ‘just’, ‘b’, ‘ctr’, ‘dist’}

anchorCtr
    

Values must be of type <class ‘bool’>

bIns
    

Values must be of type <class ‘int’>

compatLnSpc
    

Values must be of type <class ‘bool’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

flatTx
    

Values must be of type <class ‘int’>

forceAA
    

Values must be of type <class ‘bool’>

fromWordArt
    

Values must be of type <class ‘bool’>

horzOverflow
    

Value must be one of {‘clip’, ‘overflow’}

lIns
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

noAutofit
    

Values must be of type <class ‘bool’>

normAutofit
    

Values must be of type <class ‘bool’>

numCol
    

Values must be of type <class ‘int’>

prstTxWarp
    

Values must be of type <class ‘openpyxl.drawing.text.PresetTextShape’>

rIns
    

Values must be of type <class ‘int’>

rot
    

Values must be of type <class ‘int’>

rtlCol
    

Values must be of type <class ‘bool’>

scene3d
    

Values must be of type <class ‘openpyxl.drawing.geometry.Scene3D’>

spAutoFit
    

Values must be of type <class ‘bool’>

spcCol
    

Values must be of type <class ‘int’>

spcFirstLastPara
    

Values must be of type <class ‘bool’>

tIns
    

Values must be of type <class ‘int’>

tagname _ = 'bodyPr'_
    

upright
    

Values must be of type <class ‘bool’>

vert
    

Value must be one of {‘wordArtVert’, ‘horz’, ‘vert270’, ‘vert’, ‘eaVert’, ‘mongolianVert’, ‘wordArtVertRtl’}

vertOverflow
    

Value must be one of {‘clip’, ‘overflow’, ‘ellipsis’}

wrap
    

Value must be one of {‘square’, ‘none’}

_class _openpyxl.drawing.text.Spacing(_spcPct =None_, _spcPts =None_)[[source]](../_modules/openpyxl/drawing/text.html#Spacing)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

spcPct
    

Values must be of type <class ‘int’>

spcPts
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.text.TabStop(_pos =None_, _algn =None_)[[source]](../_modules/openpyxl/drawing/text.html#TabStop)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

algn
    

Values must be of type <openpyxl.descriptors.base.Set object at 0x7f1b33740080>

pos
    

Values must be of type <class ‘openpyxl.descriptors.base.Integer’>

_class _openpyxl.drawing.text.TabStopList(_tab =None_)[[source]](../_modules/openpyxl/drawing/text.html#TabStopList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tab
    

Values must be of type <class ‘openpyxl.drawing.text.TabStop’>

_class _openpyxl.drawing.text.TextField(_id =None_, _type =None_, _rPr =None_, _pPr =None_, _t =None_)[[source]](../_modules/openpyxl/drawing/text.html#TextField)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

id
    

Values must be of type <class ‘str’>

pPr
    

Values must be of type <class ‘openpyxl.drawing.text.ParagraphProperties’>

rPr
    

Values must be of type <class ‘openpyxl.drawing.text.CharacterProperties’>

t
    

Values must be of type <class ‘str’>

type
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.text.TextNormalAutofit(_fontScale =None_, _lnSpcReduction =None_)[[source]](../_modules/openpyxl/drawing/text.html#TextNormalAutofit)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fontScale
    

Values must be of type <class ‘int’>

lnSpcReduction
    

Values must be of type <class ‘int’>

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.text module
    * `AutonumberBullet`
      * `AutonumberBullet.startAt`
      * `AutonumberBullet.type`
    * `CharacterProperties`
      * `CharacterProperties.altLang`
      * `CharacterProperties.b`
      * `CharacterProperties.baseline`
      * `CharacterProperties.blipFill`
      * `CharacterProperties.bmk`
      * `CharacterProperties.cap`
      * `CharacterProperties.cs`
      * `CharacterProperties.dirty`
      * `CharacterProperties.ea`
      * `CharacterProperties.effectDag`
      * `CharacterProperties.effectLst`
      * `CharacterProperties.err`
      * `CharacterProperties.extLst`
      * `CharacterProperties.gradFill`
      * `CharacterProperties.grpFill`
      * `CharacterProperties.highlight`
      * `CharacterProperties.hlinkClick`
      * `CharacterProperties.hlinkMouseOver`
      * `CharacterProperties.i`
      * `CharacterProperties.kern`
      * `CharacterProperties.kumimoji`
      * `CharacterProperties.lang`
      * `CharacterProperties.latin`
      * `CharacterProperties.ln`
      * `CharacterProperties.namespace`
      * `CharacterProperties.noFill`
      * `CharacterProperties.noProof`
      * `CharacterProperties.normalizeH`
      * `CharacterProperties.pattFill`
      * `CharacterProperties.rtl`
      * `CharacterProperties.smtClean`
      * `CharacterProperties.smtId`
      * `CharacterProperties.solidFill`
      * `CharacterProperties.spc`
      * `CharacterProperties.strike`
      * `CharacterProperties.sym`
      * `CharacterProperties.sz`
      * `CharacterProperties.tagname`
      * `CharacterProperties.u`
      * `CharacterProperties.uFill`
      * `CharacterProperties.uFillTx`
      * `CharacterProperties.uLn`
      * `CharacterProperties.uLnTx`
    * `EmbeddedWAVAudioFile`
      * `EmbeddedWAVAudioFile.name`
    * `Font`
      * `Font.charset`
      * `Font.namespace`
      * `Font.panose`
      * `Font.pitchFamily`
      * `Font.tagname`
      * `Font.typeface`
    * `GeomGuide`
      * `GeomGuide.fmla`
      * `GeomGuide.name`
    * `GeomGuideList`
      * `GeomGuideList.gd`
    * `Hyperlink`
      * `Hyperlink.action`
      * `Hyperlink.endSnd`
      * `Hyperlink.extLst`
      * `Hyperlink.highlightClick`
      * `Hyperlink.history`
      * `Hyperlink.id`
      * `Hyperlink.invalidUrl`
      * `Hyperlink.namespace`
      * `Hyperlink.snd`
      * `Hyperlink.tagname`
      * `Hyperlink.tgtFrame`
      * `Hyperlink.tooltip`
    * `LineBreak`
      * `LineBreak.namespace`
      * `LineBreak.rPr`
      * `LineBreak.tagname`
    * `ListStyle`
      * `ListStyle.defPPr`
      * `ListStyle.extLst`
      * `ListStyle.lvl1pPr`
      * `ListStyle.lvl2pPr`
      * `ListStyle.lvl3pPr`
      * `ListStyle.lvl4pPr`
      * `ListStyle.lvl5pPr`
      * `ListStyle.lvl6pPr`
      * `ListStyle.lvl7pPr`
      * `ListStyle.lvl8pPr`
      * `ListStyle.lvl9pPr`
      * `ListStyle.namespace`
      * `ListStyle.tagname`
    * `Paragraph`
      * `Paragraph.br`
      * `Paragraph.endParaRPr`
      * `Paragraph.fld`
      * `Paragraph.namespace`
      * `Paragraph.pPr`
      * `Paragraph.properties`
      * `Paragraph.r`
      * `Paragraph.tagname`
      * `Paragraph.text`
    * `ParagraphProperties`
      * `ParagraphProperties.algn`
      * `ParagraphProperties.buAutoNum`
      * `ParagraphProperties.buBlip`
      * `ParagraphProperties.buChar`
      * `ParagraphProperties.buClr`
      * `ParagraphProperties.buClrTx`
      * `ParagraphProperties.buFont`
      * `ParagraphProperties.buFontTx`
      * `ParagraphProperties.buNone`
      * `ParagraphProperties.buSzPct`
      * `ParagraphProperties.buSzPts`
      * `ParagraphProperties.buSzTx`
      * `ParagraphProperties.defRPr`
      * `ParagraphProperties.defTabSz`
      * `ParagraphProperties.eaLnBrk`
      * `ParagraphProperties.extLst`
      * `ParagraphProperties.fontAlgn`
      * `ParagraphProperties.hangingPunct`
      * `ParagraphProperties.indent`
      * `ParagraphProperties.latinLnBrk`
      * `ParagraphProperties.lnSpc`
      * `ParagraphProperties.lvl`
      * `ParagraphProperties.marL`
      * `ParagraphProperties.marR`
      * `ParagraphProperties.namespace`
      * `ParagraphProperties.rtl`
      * `ParagraphProperties.spcAft`
      * `ParagraphProperties.spcBef`
      * `ParagraphProperties.tabLst`
      * `ParagraphProperties.tagname`
    * `PresetTextShape`
      * `PresetTextShape.avLst`
      * `PresetTextShape.prst`
    * `RegularTextRun`
      * `RegularTextRun.namespace`
      * `RegularTextRun.properties`
      * `RegularTextRun.rPr`
      * `RegularTextRun.t`
      * `RegularTextRun.tagname`
      * `RegularTextRun.value`
    * `RichTextProperties`
      * `RichTextProperties.anchor`
      * `RichTextProperties.anchorCtr`
      * `RichTextProperties.bIns`
      * `RichTextProperties.compatLnSpc`
      * `RichTextProperties.extLst`
      * `RichTextProperties.flatTx`
      * `RichTextProperties.forceAA`
      * `RichTextProperties.fromWordArt`
      * `RichTextProperties.horzOverflow`
      * `RichTextProperties.lIns`
      * `RichTextProperties.namespace`
      * `RichTextProperties.noAutofit`
      * `RichTextProperties.normAutofit`
      * `RichTextProperties.numCol`
      * `RichTextProperties.prstTxWarp`
      * `RichTextProperties.rIns`
      * `RichTextProperties.rot`
      * `RichTextProperties.rtlCol`
      * `RichTextProperties.scene3d`
      * `RichTextProperties.spAutoFit`
      * `RichTextProperties.spcCol`
      * `RichTextProperties.spcFirstLastPara`
      * `RichTextProperties.tIns`
      * `RichTextProperties.tagname`
      * `RichTextProperties.upright`
      * `RichTextProperties.vert`
      * `RichTextProperties.vertOverflow`
      * `RichTextProperties.wrap`
    * `Spacing`
      * `Spacing.spcPct`
      * `Spacing.spcPts`
    * `TabStop`
      * `TabStop.algn`
      * `TabStop.pos`
    * `TabStopList`
      * `TabStopList.tab`
    * `TextField`
      * `TextField.id`
      * `TextField.pPr`
      * `TextField.rPr`
      * `TextField.t`
      * `TextField.type`
    * `TextNormalAutofit`
      * `TextNormalAutofit.fontScale`
      * `TextNormalAutofit.lnSpcReduction`



#### Previous topic

[openpyxl.drawing.spreadsheet_drawing module](openpyxl.drawing.spreadsheet_drawing.html "previous chapter")

#### Next topic

[openpyxl.drawing.xdr module](openpyxl.drawing.xdr.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.text.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.xdr.html "openpyxl.drawing.xdr module") |
  * [previous](openpyxl.drawing.spreadsheet_drawing.html "openpyxl.drawing.spreadsheet_drawing module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.text module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
