import sys
from tasepy.examples import tasepy_main_indices
from os import getenv
from os.path import realpath, dirname

def test_tasepy_main_indices(monkeypatch,request):
    root_dir = str(request.config.rootpath) + '/'
    with monkeypatch.context() as m:
        test_path = dirname(realpath(root_dir + getenv('PYTEST_CURRENT_TEST').split(':')[0])) + "/"
        m.setattr(sys, 'argv', ['tasepy_main_indices'])
        assert tasepy_main_indices.main(test_path + '/../../tasepy/examples') == 0
