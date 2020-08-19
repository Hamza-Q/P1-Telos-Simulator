import telos

# Test that we get the correct freedom cooldown from a given enrage.
def test_freedom_cooldown():
    # (enrage, expected_freedom_cooldown)
    test_cases = [
        (0, -1),
        (150, telos.FREEDOM_CD_150),
        (151, telos.FREEDOM_CD_150),
        (250, telos.FREEDOM_CD_250),
        (500, telos.FREEDOM_CD_250),
        (999, telos.FREEDOM_CD_250),
        (1000, telos.FREEDOM_CD_1000),
        (2500, telos.FREEDOM_CD_1000),
    ]
    for enrage, expected_freedom_cooldown in test_cases:
        assert telos.Telos.freedom_cooldown(enrage) == expected_freedom_cooldown

def test_should_freedom():
    t = telos.Telos(0)
    assert not t.should_freedom()

    t.stunned_length_ticks = 10
    assert t.should_freedom()

    for enrage in [150, 250, 1000]:
        t.enrage = enrage
        assert t.should_freedom()
    
    t.bound_length_ticks = 1
    assert t.should_freedom()

    t.bound_length_ticks = 0
    t.stunned_length_ticks = 0
    assert not t.should_freedom()

    t.freedom_cd_ticks = 10
    assert not t.should_freedom()

    t.bound_length_ticks = 1
    assert t.should_freedom()

def test_can_freedom():
    telos0 = telos.Telos(0)
    assert not telos0.can_freedom()

    telos150 = telos.Telos(150)
    assert telos150.can_freedom()
    telos150.use_freedom()
    assert not telos150.can_freedom()

    telos250 = telos.Telos(250)
    assert telos250.can_freedom()
    telos250.use_freedom()
    assert not telos250.can_freedom()

    telos1000 = telos.Telos(1000)
    assert telos1000.can_freedom()
    telos1000.use_freedom()
    assert not telos1000.can_freedom()
