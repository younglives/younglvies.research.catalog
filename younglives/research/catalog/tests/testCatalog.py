import unittest2 as unittest

from zope.interface.verify import verifyClass

from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFCore.utils import getToolByName

from younglives.research.catalog.ResearchDatabaseCatalog import ResearchDatabaseCatalog
from younglives.research.catalog.interfaces import IResearchDatabaseCatalog

from base import INTEGRATION_TESTING

class TestCatalogImplements(unittest.TestCase):
    """Test catalog implements correct interfaces"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAdapterImplements(self):
        verifyClass(ICatalogTool, ResearchDatabaseCatalog)

    def testInterfaceIsAdapted(self):
        ICatalogTool.providedBy(ResearchDatabaseCatalog)

    def testAdapterImplementsCatalog(self):
        verifyClass(IResearchDatabaseCatalog, ResearchDatabaseCatalog)

    def testCatalogInterfaceIsAdapted(self):
        IResearchDatabaseCatalog.providedBy(ResearchDatabaseCatalog)

class TestArchetypesConfig(unittest.TestCase):
    """Test catalog configured correctly on Archetypes tool"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.at_tool = getToolByName(self.portal, 'archetype_tool')

    def testCatalogRegistered(self):
        """Test catalog registered with archetypes tool"""
        at_tool = self.at_tool
        available_catalogs = at_tool.getCatalogsInSite()
        assert 'research_database_catalog' in available_catalogs

    def testTypesRegistered(self):
        """Test enquiry types registered with library enquiry catalog"""
        at_tool = self.at_tool
        catalog_map = at_tool.listCatalogs()
        portal_types = catalog_map.keys()
        assert 'Author' in portal_types
        assert 'Research' in portal_types
