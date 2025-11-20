### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.core.html "openpyxl.packaging.core module") |
  * [previous](openpyxl.formatting.rule.html "openpyxl.formatting.rule module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package]()



# openpyxl.packaging package

Stuff related to Office OpenXML packaging: relationships, archive, content types.

## Submodules

  * [openpyxl.packaging.core module](openpyxl.packaging.core.html)
    * [`DocumentProperties`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties)
      * [`DocumentProperties.category`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.category)
      * [`DocumentProperties.contentStatus`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.contentStatus)
      * [`DocumentProperties.created`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.created)
      * [`DocumentProperties.creator`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.creator)
      * [`DocumentProperties.description`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.description)
      * [`DocumentProperties.identifier`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.identifier)
      * [`DocumentProperties.keywords`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.keywords)
      * [`DocumentProperties.language`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.language)
      * [`DocumentProperties.lastModifiedBy`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.lastModifiedBy)
      * [`DocumentProperties.lastPrinted`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.lastPrinted)
      * [`DocumentProperties.last_modified_by`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.last_modified_by)
      * [`DocumentProperties.modified`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.modified)
      * [`DocumentProperties.namespace`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.namespace)
      * [`DocumentProperties.revision`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.revision)
      * [`DocumentProperties.subject`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.subject)
      * [`DocumentProperties.tagname`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.tagname)
      * [`DocumentProperties.title`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.title)
      * [`DocumentProperties.version`](openpyxl.packaging.core.html#openpyxl.packaging.core.DocumentProperties.version)
    * [`NestedDateTime`](openpyxl.packaging.core.html#openpyxl.packaging.core.NestedDateTime)
      * [`NestedDateTime.expected_type`](openpyxl.packaging.core.html#openpyxl.packaging.core.NestedDateTime.expected_type)
      * [`NestedDateTime.to_tree()`](openpyxl.packaging.core.html#openpyxl.packaging.core.NestedDateTime.to_tree)
    * [`QualifiedDateTime`](openpyxl.packaging.core.html#openpyxl.packaging.core.QualifiedDateTime)
      * [`QualifiedDateTime.to_tree()`](openpyxl.packaging.core.html#openpyxl.packaging.core.QualifiedDateTime.to_tree)
  * [openpyxl.packaging.custom module](openpyxl.packaging.custom.html)
    * [`BoolProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.BoolProperty)
      * [`BoolProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.BoolProperty.value)
    * [`CustomPropertyList`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList)
      * [`CustomPropertyList.append()`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList.append)
      * [`CustomPropertyList.from_tree()`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList.from_tree)
      * [`CustomPropertyList.names`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList.names)
      * [`CustomPropertyList.props`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList.props)
      * [`CustomPropertyList.to_tree()`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.CustomPropertyList.to_tree)
    * [`DateTimeProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.DateTimeProperty)
      * [`DateTimeProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.DateTimeProperty.value)
    * [`FloatProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.FloatProperty)
      * [`FloatProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.FloatProperty.value)
    * [`IntProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.IntProperty)
      * [`IntProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.IntProperty.value)
    * [`LinkProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.LinkProperty)
      * [`LinkProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.LinkProperty.value)
    * [`NestedBoolText`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.NestedBoolText)
    * [`StringProperty`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.StringProperty)
      * [`StringProperty.value`](openpyxl.packaging.custom.html#openpyxl.packaging.custom.StringProperty.value)
  * [openpyxl.packaging.extended module](openpyxl.packaging.extended.html)
    * [`DigSigBlob`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.DigSigBlob)
    * [`ExtendedProperties`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties)
      * [`ExtendedProperties.AppVersion`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.AppVersion)
      * [`ExtendedProperties.Application`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Application)
      * [`ExtendedProperties.Characters`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Characters)
      * [`ExtendedProperties.CharactersWithSpaces`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.CharactersWithSpaces)
      * [`ExtendedProperties.Company`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Company)
      * [`ExtendedProperties.DigSig`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.DigSig)
      * [`ExtendedProperties.DocSecurity`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.DocSecurity)
      * [`ExtendedProperties.HLinks`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.HLinks)
      * [`ExtendedProperties.HeadingPairs`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.HeadingPairs)
      * [`ExtendedProperties.HiddenSlides`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.HiddenSlides)
      * [`ExtendedProperties.HyperlinkBase`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.HyperlinkBase)
      * [`ExtendedProperties.HyperlinksChanged`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.HyperlinksChanged)
      * [`ExtendedProperties.Lines`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Lines)
      * [`ExtendedProperties.LinksUpToDate`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.LinksUpToDate)
      * [`ExtendedProperties.MMClips`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.MMClips)
      * [`ExtendedProperties.Manager`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Manager)
      * [`ExtendedProperties.Notes`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Notes)
      * [`ExtendedProperties.Pages`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Pages)
      * [`ExtendedProperties.Paragraphs`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Paragraphs)
      * [`ExtendedProperties.PresentationFormat`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.PresentationFormat)
      * [`ExtendedProperties.ScaleCrop`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.ScaleCrop)
      * [`ExtendedProperties.SharedDoc`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.SharedDoc)
      * [`ExtendedProperties.Slides`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Slides)
      * [`ExtendedProperties.Template`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Template)
      * [`ExtendedProperties.TitlesOfParts`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.TitlesOfParts)
      * [`ExtendedProperties.TotalTime`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.TotalTime)
      * [`ExtendedProperties.Words`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.Words)
      * [`ExtendedProperties.tagname`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.tagname)
      * [`ExtendedProperties.to_tree()`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.ExtendedProperties.to_tree)
    * [`VectorLpstr`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.VectorLpstr)
    * [`VectorVariant`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.VectorVariant)
    * [`get_version()`](openpyxl.packaging.extended.html#openpyxl.packaging.extended.get_version)
  * [openpyxl.packaging.interface module](openpyxl.packaging.interface.html)
    * [`ISerialisableFile`](openpyxl.packaging.interface.html#openpyxl.packaging.interface.ISerialisableFile)
      * [`ISerialisableFile.id`](openpyxl.packaging.interface.html#openpyxl.packaging.interface.ISerialisableFile.id)
  * [openpyxl.packaging.manifest module](openpyxl.packaging.manifest.html)
    * [`FileExtension`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.FileExtension)
      * [`FileExtension.ContentType`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.FileExtension.ContentType)
      * [`FileExtension.Extension`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.FileExtension.Extension)
      * [`FileExtension.tagname`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.FileExtension.tagname)
    * [`Manifest`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest)
      * [`Manifest.Default`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.Default)
      * [`Manifest.Override`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.Override)
      * [`Manifest.append()`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.append)
      * [`Manifest.extensions`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.extensions)
      * [`Manifest.filenames`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.filenames)
      * [`Manifest.find()`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.find)
      * [`Manifest.findall()`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.findall)
      * [`Manifest.path`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.path)
      * [`Manifest.tagname`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.tagname)
      * [`Manifest.to_tree()`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Manifest.to_tree)
    * [`Override`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Override)
      * [`Override.ContentType`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Override.ContentType)
      * [`Override.PartName`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Override.PartName)
      * [`Override.tagname`](openpyxl.packaging.manifest.html#openpyxl.packaging.manifest.Override.tagname)
  * [openpyxl.packaging.relationship module](openpyxl.packaging.relationship.html)
    * [`Relationship`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship)
      * [`Relationship.Id`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.Id)
      * [`Relationship.Target`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.Target)
      * [`Relationship.TargetMode`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.TargetMode)
      * [`Relationship.Type`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.Type)
      * [`Relationship.id`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.id)
      * [`Relationship.tagname`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.tagname)
      * [`Relationship.target`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.Relationship.target)
    * [`RelationshipList`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList)
      * [`RelationshipList.append()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.append)
      * [`RelationshipList.expected_type`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.expected_type)
      * [`RelationshipList.find()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.find)
      * [`RelationshipList.get()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.get)
      * [`RelationshipList.tagname`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.tagname)
      * [`RelationshipList.to_dict()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.to_dict)
      * [`RelationshipList.to_tree()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.RelationshipList.to_tree)
    * [`get_dependents()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.get_dependents)
    * [`get_rel()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.get_rel)
    * [`get_rels_path()`](openpyxl.packaging.relationship.html#openpyxl.packaging.relationship.get_rels_path)
  * [openpyxl.packaging.workbook module](openpyxl.packaging.workbook.html)
    * [`ChildSheet`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet)
      * [`ChildSheet.id`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet.id)
      * [`ChildSheet.name`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet.name)
      * [`ChildSheet.sheetId`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet.sheetId)
      * [`ChildSheet.state`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet.state)
      * [`ChildSheet.tagname`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.ChildSheet.tagname)
    * [`FileRecoveryProperties`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties)
      * [`FileRecoveryProperties.autoRecover`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties.autoRecover)
      * [`FileRecoveryProperties.crashSave`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties.crashSave)
      * [`FileRecoveryProperties.dataExtractLoad`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties.dataExtractLoad)
      * [`FileRecoveryProperties.repairLoad`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties.repairLoad)
      * [`FileRecoveryProperties.tagname`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.FileRecoveryProperties.tagname)
    * [`PivotCache`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.PivotCache)
      * [`PivotCache.cacheId`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.PivotCache.cacheId)
      * [`PivotCache.id`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.PivotCache.id)
      * [`PivotCache.tagname`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.PivotCache.tagname)
    * [`WorkbookPackage`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage)
      * [`WorkbookPackage.Ignorable`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.Ignorable)
      * [`WorkbookPackage.active`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.active)
      * [`WorkbookPackage.bookViews`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.bookViews)
      * [`WorkbookPackage.calcPr`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.calcPr)
      * [`WorkbookPackage.conformance`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.conformance)
      * [`WorkbookPackage.customWorkbookViews`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.customWorkbookViews)
      * [`WorkbookPackage.definedNames`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.definedNames)
      * [`WorkbookPackage.extLst`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.extLst)
      * [`WorkbookPackage.externalReferences`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.externalReferences)
      * [`WorkbookPackage.fileRecoveryPr`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.fileRecoveryPr)
      * [`WorkbookPackage.fileSharing`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.fileSharing)
      * [`WorkbookPackage.fileVersion`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.fileVersion)
      * [`WorkbookPackage.functionGroups`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.functionGroups)
      * [`WorkbookPackage.oleSize`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.oleSize)
      * [`WorkbookPackage.pivotCaches`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.pivotCaches)
      * [`WorkbookPackage.properties`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.properties)
      * [`WorkbookPackage.sheets`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.sheets)
      * [`WorkbookPackage.smartTagPr`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.smartTagPr)
      * [`WorkbookPackage.smartTagTypes`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.smartTagTypes)
      * [`WorkbookPackage.tagname`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.tagname)
      * [`WorkbookPackage.to_tree()`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.to_tree)
      * [`WorkbookPackage.webPublishObjects`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.webPublishObjects)
      * [`WorkbookPackage.webPublishing`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.webPublishing)
      * [`WorkbookPackage.workbookPr`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.workbookPr)
      * [`WorkbookPackage.workbookProtection`](openpyxl.packaging.workbook.html#openpyxl.packaging.workbook.WorkbookPackage.workbookProtection)



[ ![Logo](../_static/logo.png) ](../index.html)

### [Table of Contents](../index.html)

  * openpyxl.packaging package
    * Submodules



#### Previous topic

[openpyxl.formatting.rule module](openpyxl.formatting.rule.html "previous chapter")

#### Next topic

[openpyxl.packaging.core module](openpyxl.packaging.core.html "next chapter")

### This Page

  * [Show Source](../_sources/api/openpyxl.packaging.rst.txt)



### Quick search

### Navigation

  * [index](../genindex.html "General Index")
  * [modules](../py-modindex.html "Python Module Index") |
  * [next](openpyxl.packaging.core.html "openpyxl.packaging.core module") |
  * [previous](openpyxl.formatting.rule.html "openpyxl.formatting.rule module") |
  * [openpyxl 3.1.3 documentation](../index.html) »
  * [openpyxl package](openpyxl.html) »
  * [openpyxl.packaging package]()



© Copyright 2010 - 2024, See AUTHORS. Created using [Sphinx](https://www.sphinx-doc.org/) 7.3.7. 
