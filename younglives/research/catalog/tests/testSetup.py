import time
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from zExceptions import BadRequest

from zope.component import getSiteManager

from Products.CMFCore.utils import getToolByName

from base import INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testToolInstalled(self):
        tool = getToolByName(self.portal, 'research_database_catalog')
        assert tool.id == 'research_database_catalog', tool.id
        assert tool.meta_type == 'Research Database Catalog', tool.meta_type

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        try:
            portal_setup.runAllImportStepsFromProfile('profile-younglives.research.catalog:default')
        except BadRequest:
            # if tests run too fast, duplicate profile import id makes test fail
            time.sleep(0.5)
            portal_setup.runAllImportStepsFromProfile('profile-younglives.research.catalog:default')
