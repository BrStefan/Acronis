from pytest_bdd import scenarios
from pathlib import Path

from steps.basic_search_steps import *

current_file = Path(__file__)
feature_file = current_file.parent.parent / 'features' / 'basic_search.feature'

scenarios(str(feature_file))