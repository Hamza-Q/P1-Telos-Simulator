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
