### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.graphic.html "openpyxl.drawing.graphic module") |
  * [previous](openpyxl.drawing.fill.html "openpyxl.drawing.fill module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.geometry module]()



# openpyxl.drawing.geometry module

_class _openpyxl.drawing.geometry.AdjPoint2D(_x =None_, _y =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#AdjPoint2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

x
    

Values must be of type <class ‘int’>

y
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.AdjustHandleList[[source]](../_modules/openpyxl/drawing/geometry.html#AdjustHandleList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

_class _openpyxl.drawing.geometry.Backdrop(_anchor =None_, _norm =None_, _up =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Backdrop)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

anchor
    

Values must be of type <class ‘openpyxl.drawing.geometry.Point3D’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

norm
    

Values must be of type <class ‘openpyxl.drawing.geometry.Vector3D’>

up
    

Values must be of type <class ‘openpyxl.drawing.geometry.Vector3D’>

_class _openpyxl.drawing.geometry.Bevel(_w =None_, _h =None_, _prst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Bevel)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

h
    

Values must be of type <class ‘int’>

prst
    

Value must be one of {‘divot’, ‘artDeco’, ‘relaxedInset’, ‘coolSlant’, ‘softRound’, ‘riblet’, ‘circle’, ‘cross’, ‘slope’, ‘convex’, ‘angle’, ‘hardEdge’}

tagname _ = 'bevel'_
    

w
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.Camera(_prst =None_, _fov =None_, _zoom =None_, _rot =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Camera)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fov
    

Values must be of type <class ‘int’>

prst
    

Value must be one of {‘legacyObliqueTopLeft’, ‘isometricLeftDown’, ‘legacyObliqueBottomLeft’, ‘obliqueTop’, ‘perspectiveHeroicRightFacing’, ‘legacyObliqueFront’, ‘legacyObliqueBottom’, ‘perspectiveBelow’, ‘legacyPerspectiveTopRight’, ‘isometricOffAxis3Right’, ‘perspectiveHeroicLeftFacing’, ‘legacyPerspectiveBottomLeft’, ‘perspectiveRelaxedModerately’, ‘perspectiveAboveLeftFacing’, ‘perspectiveAboveRightFacing’, ‘isometricOffAxis2Top’, ‘perspectiveRight’, ‘obliqueBottomRight’, ‘isometricOffAxis2Left’, ‘legacyPerspectiveFront’, ‘perspectiveAbove’, ‘perspectiveRelaxed’, ‘legacyObliqueBottomRight’, ‘legacyObliqueTopRight’, ‘isometricTopUp’, ‘isometricOffAxis2Right’, ‘isometricOffAxis3Left’, ‘obliqueBottomLeft’, ‘isometricRightDown’, ‘orthographicFront’, ‘isometricBottomUp’, ‘perspectiveLeft’, ‘isometricTopDown’, ‘legacyObliqueRight’, ‘isometricLeftUp’, ‘isometricOffAxis1Right’, ‘perspectiveHeroicExtremeLeftFacing’, ‘perspectiveHeroicExtremeRightFacing’, ‘isometricRightUp’, ‘isometricOffAxis1Top’, ‘isometricOffAxis1Left’, ‘legacyPerspectiveTop’, ‘obliqueTopRight’, ‘isometricOffAxis3Bottom’, ‘obliqueTopLeft’, ‘perspectiveFront’, ‘isometricOffAxis4Bottom’, ‘legacyObliqueTop’, ‘legacyPerspectiveLeft’, ‘obliqueBottom’, ‘perspectiveContrastingRightFacing’, ‘isometricOffAxis4Right’, ‘obliqueRight’, ‘isometricBottomDown’, ‘legacyPerspectiveRight’, ‘legacyPerspectiveBottomRight’, ‘obliqueLeft’, ‘perspectiveContrastingLeftFacing’, ‘legacyObliqueLeft’, ‘legacyPerspectiveTopLeft’, ‘legacyPerspectiveBottom’, ‘isometricOffAxis4Left’}

rot
    

Values must be of type <class ‘openpyxl.drawing.geometry.SphereCoords’>

tagname _ = 'camera'_
    

zoom
    

Values must be of type <class ‘openpyxl.descriptors.excel.Percentage’>

_class _openpyxl.drawing.geometry.ConnectionSite(_ang =None_, _pos =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#ConnectionSite)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ang
    

Values must be of type <class ‘float’>

pos
    

Values must be of type <class ‘openpyxl.drawing.geometry.AdjPoint2D’>

_class _openpyxl.drawing.geometry.ConnectionSiteList(_cxn =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#ConnectionSiteList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cxn
    

Values must be of type <class ‘openpyxl.drawing.geometry.ConnectionSite’>

_class _openpyxl.drawing.geometry.CustomGeometry2D(_avLst =None_, _gdLst =None_, _ahLst =None_, _cxnLst =None_, _rect =None_, _pathLst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#CustomGeometry2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

ahLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.AdjustHandleList’>

avLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.GeomGuideList’>

cxnLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.ConnectionSiteList’>

gdLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.GeomGuideList’>

pathLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.Path2DList’>

_class _openpyxl.drawing.geometry.FontReference(_idx =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#FontReference)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

idx
    

Value must be one of {‘minor’, ‘major’}

_class _openpyxl.drawing.geometry.GeomGuide(_name =None_, _fmla =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#GeomGuide)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

fmla
    

Values must be of type <class ‘str’>

name
    

Values must be of type <class ‘str’>

_class _openpyxl.drawing.geometry.GeomGuideList(_gd =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#GeomGuideList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

gd
    

Values must be of type <class ‘openpyxl.drawing.geometry.GeomGuide’>

_class _openpyxl.drawing.geometry.GeomRect(_l =None_, _t =None_, _r =None_, _b =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#GeomRect)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

b
    

Values must be of type <class ‘int’>

l
    

Values must be of type <class ‘int’>

r
    

Values must be of type <class ‘int’>

t
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.GroupTransform2D(_rot =0_, _flipH =None_, _flipV =None_, _off =None_, _ext =None_, _chOff =None_, _chExt =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#GroupTransform2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chExt
    

Values must be of type <class ‘openpyxl.drawing.geometry.PositiveSize2D’>

chOff
    

Values must be of type <class ‘openpyxl.drawing.geometry.Point2D’>

ext
    

Values must be of type <class ‘openpyxl.drawing.geometry.PositiveSize2D’>

flipH
    

Values must be of type <class ‘bool’>

flipV
    

Values must be of type <class ‘bool’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

off
    

Values must be of type <class ‘openpyxl.drawing.geometry.Point2D’>

rot
    

Values must be of type <class ‘int’>

tagname _ = 'xfrm'_
    

_class _openpyxl.drawing.geometry.LightRig(_rig =None_, _dir =None_, _rot =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#LightRig)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

dir
    

Value must be one of {‘l’, ‘t’, ‘r’, ‘b’, ‘br’, ‘bl’, ‘tl’, ‘tr’}

rig
    

Value must be one of {‘sunrise’, ‘soft’, ‘flood’, ‘legacyHarsh2’, ‘legacyFlat4’, ‘legacyFlat3’, ‘twoPt’, ‘legacyNormal3’, ‘brightRoom’, ‘legacyFlat2’, ‘balanced’, ‘threePt’, ‘chilly’, ‘sunset’, ‘glow’, ‘legacyNormal2’, ‘legacyHarsh4’, ‘legacyNormal1’, ‘harsh’, ‘contrasting’, ‘legacyFlat1’, ‘legacyNormal4’, ‘legacyHarsh1’, ‘morning’, ‘freezing’, ‘flat’, ‘legacyHarsh3’}

rot
    

Values must be of type <class ‘openpyxl.drawing.geometry.SphereCoords’>

tagname _ = 'lightRig'_
    

_class _openpyxl.drawing.geometry.Path2D(_w =None_, _h =None_, _fill =None_, _stroke =None_, _extrusionOk =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Path2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

extrusionOk
    

Values must be of type <class ‘bool’>

fill
    

Value must be one of {‘norm’, ‘darkenLess’, ‘darken’, ‘lighten’, ‘lightenLess’}

h
    

Values must be of type <class ‘float’>

stroke
    

Values must be of type <class ‘bool’>

w
    

Values must be of type <class ‘float’>

_class _openpyxl.drawing.geometry.Path2DList(_path =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Path2DList)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

path
    

Values must be of type <class ‘openpyxl.drawing.geometry.Path2D’>

_class _openpyxl.drawing.geometry.Point2D(_x =None_, _y =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Point2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

tagname _ = 'off'_
    

x
    

Values must be of type <class ‘int’>

y
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.Point3D(_x =None_, _y =None_, _z =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Point3D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

tagname _ = 'anchor'_
    

x
    

Values must be of type <class ‘int’>

y
    

Values must be of type <class ‘int’>

z
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.PositiveSize2D(_cx =None_, _cy =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#PositiveSize2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

cx
    

Values must be of type <class ‘int’>

cy
    

Values must be of type <class ‘int’>

height
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

Dimensions in EMUs

tagname _ = 'ext'_
    

width
    

Aliases can be used when either the desired attribute name is not allowed or confusing in Python (eg. “type”) or a more descriptive name is desired (eg. “underline” for “u”)

_class _openpyxl.drawing.geometry.PresetGeometry2D(_prst =None_, _avLst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#PresetGeometry2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

avLst
    

Values must be of type <class ‘openpyxl.drawing.geometry.GeomGuideList’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

prst
    

Value must be one of {‘flowChartMultidocument’, ‘corner’, ‘curvedConnector5’, ‘mathMultiply’, ‘lightningBolt’, ‘circularArrow’, ‘flowChartPunchedCard’, ‘flowChartMagneticTape’, ‘actionButtonHelp’, ‘can’, ‘hexagon’, ‘diagStripe’, ‘line’, ‘smileyFace’, ‘star32’, ‘leftBrace’, ‘flowChartOnlineStorage’, ‘bentConnector4’, ‘mathEqual’, ‘quadArrow’, ‘flowChartCollate’, ‘star4’, ‘actionButtonMovie’, ‘noSmoking’, ‘flowChartOfflineStorage’, ‘upArrow’, ‘wedgeEllipseCallout’, ‘leftRightArrowCallout’, ‘flowChartPredefinedProcess’, ‘leftArrow’, ‘pie’, ‘foldedCorner’, ‘flowChartSort’, ‘cornerTabs’, ‘rect’, ‘mathNotEqual’, ‘rightArrowCallout’, ‘round2SameRect’, ‘plaqueTabs’, ‘star12’, ‘irregularSeal2’, ‘snip2SameRect’, ‘leftArrowCallout’, ‘star5’, ‘pieWedge’, ‘snip1Rect’, ‘flowChartConnector’, ‘ellipse’, ‘gear9’, ‘bevel’, ‘straightConnector1’, ‘rightBracket’, ‘flowChartProcess’, ‘chartX’, ‘flowChartTerminator’, ‘rightBrace’, ‘curvedConnector4’, ‘accentBorderCallout2’, ‘flowChartDisplay’, ‘curvedRightArrow’, ‘flowChartManualInput’, ‘roundRect’, ‘stripedRightArrow’, ‘actionButtonHome’, ‘flowChartExtract’, ‘leftRightUpArrow’, ‘uturnArrow’, ‘actionButtonSound’, ‘chartStar’, ‘frame’, ‘verticalScroll’, ‘horizontalScroll’, ‘leftRightRibbon’, ‘heart’, ‘borderCallout2’, ‘actionButtonForwardNext’, ‘doubleWave’, ‘bentConnector3’, ‘accentCallout3’, ‘borderCallout1’, ‘trapezoid’, ‘parallelogram’, ‘heptagon’, ‘funnel’, ‘accentCallout1’, ‘nonIsoscelesTrapezoid’, ‘actionButtonBackPrevious’, ‘halfFrame’, ‘leftUpArrow’, ‘diamond’, ‘callout1’, ‘leftCircularArrow’, ‘squareTabs’, ‘swooshArrow’, ‘star8’, ‘bracketPair’, ‘accentBorderCallout1’, ‘blockArc’, ‘flowChartSummingJunction’, ‘ribbon’, ‘flowChartInputOutput’, ‘upDownArrowCallout’, ‘irregularSeal1’, ‘rtTriangle’, ‘bracePair’, ‘accentCallout2’, ‘callout2’, ‘cloud’, ‘actionButtonBlank’, ‘bentArrow’, ‘flowChartMagneticDrum’, ‘chartPlus’, ‘upArrowCallout’, ‘gear6’, ‘flowChartDecision’, ‘actionButtonEnd’, ‘chord’, ‘flowChartOr’, ‘actionButtonInformation’, ‘flowChartMagneticDisk’, ‘round1Rect’, ‘octagon’, ‘sun’, ‘homePlate’, ‘ellipseRibbon2’, ‘flowChartManualOperation’, ‘decagon’, ‘actionButtonBeginning’, ‘upDownArrow’, ‘bentConnector2’, ‘flowChartOffpageConnector’, ‘accentBorderCallout3’, ‘actionButtonDocument’, ‘quadArrowCallout’, ‘leftBracket’, ‘arc’, ‘chevron’, ‘ribbon2’, ‘flowChartAlternateProcess’, ‘flowChartInternalStorage’, ‘mathPlus’, ‘mathMinus’, ‘triangle’, ‘plaque’, ‘leftRightArrow’, ‘cube’, ‘bentUpArrow’, ‘plus’, ‘lineInv’, ‘downArrow’, ‘borderCallout3’, ‘flowChartDelay’, ‘snip2DiagRect’, ‘callout3’, ‘actionButtonReturn’, ‘flowChartMerge’, ‘dodecagon’, ‘leftRightCircularArrow’, ‘snipRoundRect’, ‘wedgeRectCallout’, ‘wedgeRoundRectCallout’, ‘pentagon’, ‘curvedConnector2’, ‘ellipseRibbon’, ‘curvedUpArrow’, ‘flowChartPreparation’, ‘star16’, ‘mathDivide’, ‘wave’, ‘flowChartDocument’, ‘downArrowCallout’, ‘round2DiagRect’, ‘flowChartPunchedTape’, ‘notchedRightArrow’, ‘star24’, ‘moon’, ‘bentConnector5’, ‘star7’, ‘curvedConnector3’, ‘cloudCallout’, ‘rightArrow’, ‘donut’, ‘curvedDownArrow’, ‘teardrop’, ‘star10’, ‘curvedLeftArrow’, ‘star6’}

_class _openpyxl.drawing.geometry.Scene3D(_camera =None_, _lightRig =None_, _backdrop =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Scene3D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

backdrop
    

Values must be of type <class ‘openpyxl.drawing.geometry.Backdrop’>

camera
    

Values must be of type <class ‘openpyxl.drawing.geometry.Camera’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

lightRig
    

Values must be of type <class ‘openpyxl.drawing.geometry.LightRig’>

_class _openpyxl.drawing.geometry.Shape3D(_z =None_, _extrusionH =None_, _contourW =None_, _prstMaterial =None_, _bevelT =None_, _bevelB =None_, _extrusionClr =None_, _contourClr =None_, _extLst =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Shape3D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

bevelB
    

Values must be of type <class ‘openpyxl.drawing.geometry.Bevel’>

bevelT
    

Values must be of type <class ‘openpyxl.drawing.geometry.Bevel’>

contourClr
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

contourW
    

Values must be of type <class ‘int’>

extLst
    

Values must be of type <class ‘openpyxl.descriptors.excel.ExtensionList’>

extrusionClr
    

Values must be of type <class ‘openpyxl.styles.colors.Color’>

extrusionH
    

Values must be of type <class ‘int’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

prstMaterial
    

Value must be one of {‘clear’, ‘powder’, ‘legacyPlastic’, ‘legacyWireframe’, ‘translucentPowder’, ‘dkEdge’, ‘softEdge’, ‘legacyMetal’, ‘softmetal’, ‘flat’, ‘metal’, ‘matte’, ‘plastic’, ‘legacyMatte’, ‘warmMatte’}

z
    

Values must be of type <class ‘openpyxl.descriptors.base.Integer’>

_class _openpyxl.drawing.geometry.ShapeStyle(_lnRef =None_, _fillRef =None_, _effectRef =None_, _fontRef =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#ShapeStyle)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

effectRef
    

Values must be of type <class ‘openpyxl.drawing.geometry.StyleMatrixReference’>

fillRef
    

Values must be of type <class ‘openpyxl.drawing.geometry.StyleMatrixReference’>

fontRef
    

Values must be of type <class ‘openpyxl.drawing.geometry.FontReference’>

lnRef
    

Values must be of type <class ‘openpyxl.drawing.geometry.StyleMatrixReference’>

_class _openpyxl.drawing.geometry.SphereCoords(_lat =None_, _lon =None_, _rev =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#SphereCoords)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

lat
    

Values must be of type <class ‘int’>

lon
    

Values must be of type <class ‘int’>

rev
    

Values must be of type <class ‘int’>

tagname _ = 'sphereCoords'_
    

_class _openpyxl.drawing.geometry.StyleMatrixReference(_idx =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#StyleMatrixReference)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

idx
    

Values must be of type <class ‘int’>

_class _openpyxl.drawing.geometry.Transform2D(_rot =None_, _flipH =None_, _flipV =None_, _off =None_, _ext =None_, _chOff =None_, _chExt =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Transform2D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

chExt
    

Values must be of type <class ‘openpyxl.drawing.geometry.PositiveSize2D’>

chOff
    

Values must be of type <class ‘openpyxl.drawing.geometry.Point2D’>

ext
    

Values must be of type <class ‘openpyxl.drawing.geometry.PositiveSize2D’>

flipH
    

Values must be of type <class ‘bool’>

flipV
    

Values must be of type <class ‘bool’>

namespace _ = 'http://schemas.openxmlformats.org/drawingml/2006/main'_
    

off
    

Values must be of type <class ‘openpyxl.drawing.geometry.Point2D’>

rot
    

Values must be of type <class ‘int’>

tagname _ = 'xfrm'_
    

_class _openpyxl.drawing.geometry.Vector3D(_dx =None_, _dy =None_, _dz =None_)[[source]](../_modules/openpyxl/drawing/geometry.html#Vector3D)
    

Bases: [`Serialisable`](openpyxl.descriptors.serialisable.html#openpyxl.descriptors.serialisable.Serialisable "openpyxl.descriptors.serialisable.Serialisable")

dx
    

Values must be of type <class ‘int’>

dy
    

Values must be of type <class ‘int’>

dz
    

Values must be of type <class ‘int’>

tagname _ = 'vector'_
    

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.drawing.geometry module
    * `AdjPoint2D`
      * `AdjPoint2D.x`
      * `AdjPoint2D.y`
    * `AdjustHandleList`
    * `Backdrop`
      * `Backdrop.anchor`
      * `Backdrop.extLst`
      * `Backdrop.norm`
      * `Backdrop.up`
    * `Bevel`
      * `Bevel.h`
      * `Bevel.prst`
      * `Bevel.tagname`
      * `Bevel.w`
    * `Camera`
      * `Camera.fov`
      * `Camera.prst`
      * `Camera.rot`
      * `Camera.tagname`
      * `Camera.zoom`
    * `ConnectionSite`
      * `ConnectionSite.ang`
      * `ConnectionSite.pos`
    * `ConnectionSiteList`
      * `ConnectionSiteList.cxn`
    * `CustomGeometry2D`
      * `CustomGeometry2D.ahLst`
      * `CustomGeometry2D.avLst`
      * `CustomGeometry2D.cxnLst`
      * `CustomGeometry2D.gdLst`
      * `CustomGeometry2D.pathLst`
    * `FontReference`
      * `FontReference.idx`
    * `GeomGuide`
      * `GeomGuide.fmla`
      * `GeomGuide.name`
    * `GeomGuideList`
      * `GeomGuideList.gd`
    * `GeomRect`
      * `GeomRect.b`
      * `GeomRect.l`
      * `GeomRect.r`
      * `GeomRect.t`
    * `GroupTransform2D`
      * `GroupTransform2D.chExt`
      * `GroupTransform2D.chOff`
      * `GroupTransform2D.ext`
      * `GroupTransform2D.flipH`
      * `GroupTransform2D.flipV`
      * `GroupTransform2D.namespace`
      * `GroupTransform2D.off`
      * `GroupTransform2D.rot`
      * `GroupTransform2D.tagname`
    * `LightRig`
      * `LightRig.dir`
      * `LightRig.rig`
      * `LightRig.rot`
      * `LightRig.tagname`
    * `Path2D`
      * `Path2D.extrusionOk`
      * `Path2D.fill`
      * `Path2D.h`
      * `Path2D.stroke`
      * `Path2D.w`
    * `Path2DList`
      * `Path2DList.path`
    * `Point2D`
      * `Point2D.namespace`
      * `Point2D.tagname`
      * `Point2D.x`
      * `Point2D.y`
    * `Point3D`
      * `Point3D.tagname`
      * `Point3D.x`
      * `Point3D.y`
      * `Point3D.z`
    * `PositiveSize2D`
      * `PositiveSize2D.cx`
      * `PositiveSize2D.cy`
      * `PositiveSize2D.height`
      * `PositiveSize2D.namespace`
      * `PositiveSize2D.tagname`
      * `PositiveSize2D.width`
    * `PresetGeometry2D`
      * `PresetGeometry2D.avLst`
      * `PresetGeometry2D.namespace`
      * `PresetGeometry2D.prst`
    * `Scene3D`
      * `Scene3D.backdrop`
      * `Scene3D.camera`
      * `Scene3D.extLst`
      * `Scene3D.lightRig`
    * `Shape3D`
      * `Shape3D.bevelB`
      * `Shape3D.bevelT`
      * `Shape3D.contourClr`
      * `Shape3D.contourW`
      * `Shape3D.extLst`
      * `Shape3D.extrusionClr`
      * `Shape3D.extrusionH`
      * `Shape3D.namespace`
      * `Shape3D.prstMaterial`
      * `Shape3D.z`
    * `ShapeStyle`
      * `ShapeStyle.effectRef`
      * `ShapeStyle.fillRef`
      * `ShapeStyle.fontRef`
      * `ShapeStyle.lnRef`
    * `SphereCoords`
      * `SphereCoords.lat`
      * `SphereCoords.lon`
      * `SphereCoords.rev`
      * `SphereCoords.tagname`
    * `StyleMatrixReference`
      * `StyleMatrixReference.idx`
    * `Transform2D`
      * `Transform2D.chExt`
      * `Transform2D.chOff`
      * `Transform2D.ext`
      * `Transform2D.flipH`
      * `Transform2D.flipV`
      * `Transform2D.namespace`
      * `Transform2D.off`
      * `Transform2D.rot`
      * `Transform2D.tagname`
    * `Vector3D`
      * `Vector3D.dx`
      * `Vector3D.dy`
      * `Vector3D.dz`
      * `Vector3D.tagname`



#### Previous topic

[openpyxl.drawing.fill module](openpyxl.drawing.fill.html "previous chapter")

#### Next topic

[openpyxl.drawing.graphic module](openpyxl.drawing.graphic.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.drawing.geometry.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.drawing.graphic.html "openpyxl.drawing.graphic module") |
  * [previous](openpyxl.drawing.fill.html "openpyxl.drawing.fill module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.drawing package](openpyxl.drawing.html) »
  * [openpyxl.drawing.geometry module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
