from base import *


# SAML2IDP metadata settings
SAML2IDP_CONFIG = {
    'autosubmit': False,
    'issuer': 'http://idp.mentorcloud.com',
    'signing': True,
    'certificate_file': PROJECT_ROOT + '/keys/sample/sp.pem',
    'private_key_file': PROJECT_ROOT + '/keys/sample/saml.key',
}

attrSpConfig = {
    'acs_url': 'http://alpha.mentorcloud.com/sso/saml/acs/',
    'processor': 'saml2idp.compress_processor.Processor',
}

SAML2IDP_REMOTES = {
    # Group of SP CONFIGs.
    # friendlyname: SP config
    u'http://alpha.mentorcloud.com/sso/metadata/': attrSpConfig,
}

DEBUG = False
TEMPLATE_DEBUG = DEBUG
