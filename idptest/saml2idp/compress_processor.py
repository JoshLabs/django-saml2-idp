import xml_render
import demo
import codex


class Processor(demo.Processor):
    """
    Mcloud SAML 2.0 AuthnRequest to Response Handler Processor.
    """

    def _decode_request(self):
        """
        Decodes request using both Base64 and Zipping.
        """
        self._request_xml = codex.decode_base64_and_inflate(self._saml_request)

    def _format_assertion(self):
        # NOTE: This uses the SalesForce assertion for the demo.
        self._assertion_params['ATTRIBUTES'] = {
            'allowMentorcloud': True,
        }
        self._assertion_xml = xml_render.get_assertion_salesforce_xml(self._assertion_params, signed=True)
