from StringIO import StringIO
from Products.CMFCore.utils import getToolByName

def configureArchetypeTool(portal, out):
    """
    Configure the archetype tool for the library enquiry catalog
    """
    at_tool = getToolByName(portal, 'archetype_tool')
    at_tool.setCatalogsByType('Author', ['portal_catalog', 'research_database_catalog'])
    at_tool.setCatalogsByType('Research', ['portal_catalog', 'research_database_catalog'])

def setupVarious(context):
    """
    Import various settings.
    """
    # Only run step if a flag file is present
    if context.readDataFile('younglives.research.catalog_various.txt') is None:
        return
    site = context.getSite()
    out = StringIO()

    configureArchetypeTool(site, out)
