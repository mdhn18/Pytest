
from my_project import project_modules

def test_rolling_average():

    results1 = [1, 2, 3, 4, 5]
    expeted_results1 = [2.0, 3.0, 4.0]

    results = project_modules.rolling_average([1, 2, 3, 4, 5], 3)
    assert results == [2.0, 3.0, 4.0]