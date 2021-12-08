"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    obs = 'test obs'
    p = Patient(name=name)
    p.add_observation(obs)

    assert p.name == name
    assert p.observations == obs

def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Dr Smith'
    patients = ['Alice', 'Beth', 'Chloe']
    d = Doctor(name=name)
    for patient in patients:
        d.add_patient(patient)

    assert d.name == name
    assert d.patients == patients