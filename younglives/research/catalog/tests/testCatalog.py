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

class TestCatalogSetup(unittest.TestCase):
    """Test catalog is setup correctly"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testIndexesAdded(self):
        research_catalog = getToolByName(self.portal, 'research_database_catalog')
        indexes = research_catalog._catalog.indexes.keys()
        # fields from younglives.research.authors
        assert 'familyName' in indexes
        assert 'nameOrder' in indexes
        assert 'personalNames' in indexes
        assert 'country' in indexes
        assert 'id' in indexes
        assert 'meta_type' in indexes
        assert 'paper_manager' in indexes
        assert 'sortable_title' in indexes
        assert 'paperAuthor' in indexes
        assert 'coAuthors' in indexes
        assert 'theme' in indexes
        assert 'Title' in indexes
        #assert len(indexes) == 32, indexes

    def testColumnsAdded(self):
        research_catalog = getToolByName(self.portal, 'research_database_catalog')
        columns = research_catalog.schema()
        # fields from younglives.research.authors
        assert 'familyName' in columns
        assert 'nameOrder' in columns
        assert 'personalNames' in columns
        assert 'id' in columns
        assert 'paper_manager' in columns
        assert 'paperAuthor' in columns
        assert 'coAuthors' in columns
        assert 'Title' in columns
        #assert len(columns) == 27, columns

class TestCatalogReindex(unittest.TestCase):
    """Test reindex only reindexes research types"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
