from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

class TestCase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import younglives.research.catalog
        self.loadZCML(package=younglives.research.catalog)

        # Install product and call its initialize() function
        z2.installProduct(app, 'younglives.research.catalog')

        # Note: you can skip this if my.product is not a Zope 2-style
        # product, i.e. it is not in the Products.* namespace and it
        # does not have a <five:registerPackage /> directive in its
        # configure.zcml.

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'younglives.research.catalog:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'younglives.research.catalog')

        # Note: Again, you can skip this if my.product is not a Zope 2-
        # style product

FIXTURE = TestCase()
INTEGRATION_TESTING = IntegrationTesting(bases=(FIXTURE,), name="Integration")
