"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    obs = 'test obs'
    p = Patient(name=name)
    p.add_observation(obs)

    assert p.name == name
    assert p.observations[0].value == obs
    assert len(p.observations) == 1

def test_create_doctor():
    from inflammation.models import Doctor, Patient

    patient_name = 'Alice'
    p = Patient(name=patient_name)

    name = 'Dr Smith'
    d = Doctor(name=name)
    d.add_patient(p)

    assert d.name == name
    assert d.patients[0] == p
    assert len(d.patients) == 1