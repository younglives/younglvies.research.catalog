from Products.GenericSetup.utils import exportObjects
from Products.GenericSetup.utils import importObjects
from Products.GenericSetup.ZCatalog.exportimport import ZCatalogXMLAdapter

from Products.CMFCore.utils import getToolByName

def importCatalogTool(context):
    """Import catalog tool.
    """
    site = context.getSite()
    tool = getToolByName(site, 'research_database_catalog', None)
    if tool is not None:
        importObjects(tool, '', context)

def exportCatalogTool(context):
    """Export catalog tool.
    """
    site = context.getSite()
    tool = getToolByName(site, 'research_database_catalog', None)
    if tool is None:
        logger = context.getLogger('research_database_catalog')
        logger.info('Nothing to export.')
        return
    exportObjects(tool, '', context)

class ResearchDatabaseCatalogXMLAdapter(ZCatalogXMLAdapter):

    """Override Catalog importer to change the name.
    """

    name = 'research_database_catalog'
