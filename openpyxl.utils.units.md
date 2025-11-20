### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.html "openpyxl.workbook package") |
  * [previous](openpyxl.utils.protection.html "openpyxl.utils.protection module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.units module]()



# openpyxl.utils.units module

openpyxl.utils.units.DEFAULT_HEADER _ = 0.3_
    

From the ECMA Spec (4th Edition part 1) Page setup: “Left Page Margin in inches” p. 1647

Docs from <http://startbigthinksmall.wordpress.com/2010/01/04/points-inches-and-emus-measuring-units-in-office-open-xml/>

See also <http://msdn.microsoft.com/en-us/library/dd560821(v=office.12).aspx>

dxa: The main unit in OOXML is a twentieth of a point. Also called twips. pt: point. In Excel there are 72 points to an inch hp: half-points are used to specify font sizes. A font-size of 12pt equals 24 half points pct: Half-points are used to specify font sizes. A font-size of 12pt equals 24 half points

EMU: English Metric Unit, EMUs are used for coordinates in vector-based drawings and embedded pictures. One inch equates to 914400 EMUs and a centimeter is 360000. For bitmaps the default resolution is 96 dpi (known as PixelsPerInch in Excel). Spec p. 1122

For radial geometry Excel uses integer units of 1/60000th of a degree.

openpyxl.utils.units.EMU_to_cm(_value_)[[source]](../_modules/openpyxl/utils/units.html#EMU_to_cm)
    

openpyxl.utils.units.EMU_to_inch(_value_)[[source]](../_modules/openpyxl/utils/units.html#EMU_to_inch)
    

openpyxl.utils.units.EMU_to_pixels(_value_)[[source]](../_modules/openpyxl/utils/units.html#EMU_to_pixels)
    

openpyxl.utils.units.angle_to_degrees(_value_)[[source]](../_modules/openpyxl/utils/units.html#angle_to_degrees)
    

openpyxl.utils.units.cm_to_EMU(_value_)[[source]](../_modules/openpyxl/utils/units.html#cm_to_EMU)
    

1 cm = 360000 EMUs

openpyxl.utils.units.cm_to_dxa(_value_)[[source]](../_modules/openpyxl/utils/units.html#cm_to_dxa)
    

openpyxl.utils.units.degrees_to_angle(_value_)[[source]](../_modules/openpyxl/utils/units.html#degrees_to_angle)
    

1 degree = 60000 angles

openpyxl.utils.units.dxa_to_cm(_value_)[[source]](../_modules/openpyxl/utils/units.html#dxa_to_cm)
    

openpyxl.utils.units.dxa_to_inch(_value_)[[source]](../_modules/openpyxl/utils/units.html#dxa_to_inch)
    

openpyxl.utils.units.inch_to_EMU(_value_)[[source]](../_modules/openpyxl/utils/units.html#inch_to_EMU)
    

1 inch = 914400 EMUs

openpyxl.utils.units.inch_to_dxa(_value_)[[source]](../_modules/openpyxl/utils/units.html#inch_to_dxa)
    

1 inch = 72 * 20 dxa

openpyxl.utils.units.pixels_to_EMU(_value_)[[source]](../_modules/openpyxl/utils/units.html#pixels_to_EMU)
    

1 pixel = 9525 EMUs

openpyxl.utils.units.pixels_to_points(_value_ , _dpi =96_)[[source]](../_modules/openpyxl/utils/units.html#pixels_to_points)
    

96 dpi, 72i

openpyxl.utils.units.points_to_pixels(_value_ , _dpi =96_)[[source]](../_modules/openpyxl/utils/units.html#points_to_pixels)
    

openpyxl.utils.units.short_color(_color_)[[source]](../_modules/openpyxl/utils/units.html#short_color)
    

format a color to its short size

[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.utils.units module
    * `DEFAULT_HEADER`
    * `EMU_to_cm()`
    * `EMU_to_inch()`
    * `EMU_to_pixels()`
    * `angle_to_degrees()`
    * `cm_to_EMU()`
    * `cm_to_dxa()`
    * `degrees_to_angle()`
    * `dxa_to_cm()`
    * `dxa_to_inch()`
    * `inch_to_EMU()`
    * `inch_to_dxa()`
    * `pixels_to_EMU()`
    * `pixels_to_points()`
    * `points_to_pixels()`
    * `short_color()`



#### Previous topic

[openpyxl.utils.protection module](openpyxl.utils.protection.html "previous chapter")

#### Next topic

[openpyxl.workbook package](openpyxl.workbook.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.utils.units.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.workbook.html "openpyxl.workbook package") |
  * [previous](openpyxl.utils.protection.html "openpyxl.utils.protection module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.utils package](openpyxl.utils.html) »
  * [openpyxl.utils.units module]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
