from suds import strategy


def test_load_strategies():
    strategies = strategy.load_strategies()

    assert len(strategies) >= 1
    assert len(strategies) == len([s for s in strategies if isinstance(s, strategy.Strategy)])
