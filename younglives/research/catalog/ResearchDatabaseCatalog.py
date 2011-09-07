from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Acquisition import aq_inner
from Acquisition import aq_parent
from zope.interface import implements 

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import SimpleRecord
from Products.CMFPlone.CatalogTool import CatalogTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool
from Products.CMFPlone.utils import base_hasattr
from Products.CMFPlone.utils import safe_callable

from younglives.research.catalog.interfaces import IResearchDatabaseCatalog

import permissions

class ResearchDatabaseCatalog(BaseTool):
    """The catalog for the research database"""
    id = 'research_database_catalog'
    meta_type= 'Research Database Catalog'

    security = ClassSecurityInfo()
    implements(IResearchDatabaseCatalog)

    security.declareProtected(permissions.ManageZCatalogEntries, 'clearFindAndRebuild')
    def clearFindAndRebuild(self):
        """Copied from CMFPlone.CatalogTool.py to override what is indexed
        """
        def indexObject(obj, path):
            if (base_hasattr(obj, 'indexObject') and
                safe_callable(obj.indexObject)):
                try:
                    obj.indexObject()
                except TypeError:
                    # Catalogs have 'indexObject' as well, but they
                    # take different args, and will fail
                    pass
        self.manage_catalogClear()
        portal = aq_parent(aq_inner(self))
        at_tool = getToolByName(self, 'archetype_tool')
        catalog_map = at_tool.listCatalogs()
        portal_types = catalog_map.keys()
        obj_metatypes = []
        for portal_type in portal_types:
            obj_metatypes.append(portal_type.replace(' ', ''))
        portal.ZopeFindAndApply(portal, obj_metatypes=obj_metatypes, search_sub=True, apply_func=indexObject)

InitializeClass(ResearchDatabaseCatalog)
