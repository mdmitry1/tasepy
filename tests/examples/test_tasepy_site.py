import sys
from tasepy.examples import site_checker

def test_tase_api_site(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['tase_site_checker','-url','https://market.tase.co.il'])
        assert site_checker.main() == 200
