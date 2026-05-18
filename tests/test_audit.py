import unittest

from citelocal.audit import audit_local_html, extract_page


class AuditExtractionTests(unittest.TestCase):
    def test_extracts_json_ld_types_from_graph(self):
        html = '''
        <html><head><title>Graph Test</title>
        <script type="application/ld+json">
        {"@context":"https://schema.org","@graph":[{"@type":"WebSite"},{"@type":"LocalBusiness","name":"Acme HVAC"}]}
        </script></head><body><h1>Acme HVAC in Dayton</h1></body></html>
        '''
        page = extract_page(html, "https://example.com")
        self.assertIn("LocalBusiness", page["json_ld_types"])
        self.assertIn("WebSite", page["json_ld_types"])

    def test_local_sample_scores_without_network(self):
        html = '''
        <title>River City HVAC | Cincinnati Heating & Cooling</title>
        <meta name="description" content="River City HVAC provides emergency furnace repair in Cincinnati, OH.">
        <script type="application/ld+json">{"@type":"LocalBusiness","name":"River City HVAC"}</script>
        <h1>River City HVAC in Cincinnati, OH</h1>
        <p>Call 513-555-0110 for HVAC repair, service area details, hours, pricing, FAQ, reviews, licensed and insured.</p>
        <a href="/services/ac-installation">AC installation</a><a href="/faq">FAQ</a>
        '''
        result = audit_local_html("River City HVAC", "HVAC", "Cincinnati, OH", "https://example.com", html)
        self.assertGreaterEqual(result.overall_score, 70)
        self.assertEqual(result.grade, "B")


if __name__ == "__main__":
    unittest.main()
